# -*- coding: utf-8 -*-
"""
Custom module for sending the data of the manufacturing order to the
external MES application of the EDIT (Enterprise Digital Twin) project.
"""
import json
import socket

from odoo import models, fields, api

import requests


class seamk_mfg_order(models.TransientModel):
    """Send the data of the Odoo's manufacturing order to the external MES app."""
    
    _inherit = "mrp.product.produce"


    def do_produce(self):
        """Produce the part."""
        # When Odoo admin saves the Manufacturing Order by clicking the 'Save'
        # button, the method do_produce() is called. The method is located at
        # the file ...\server\odoo\addons\mrp\wizard\mrp_product_produce.py.

        # Use the super() to extend the functionality of the original
        # do_produce() method without changing the source code of the Odoo.
        action = super(seamk_mfg_order, self).do_produce()

        for record in self:
            product_name = record.product_id.name
            display_name = record.product_id.display_name
    
            # Read the name of the manufacturing order and use the name to
            # to search the manufacturing order record.
            name = self.production_id.name
            mo_record = record.env["mrp.production"].search([("name", "=", name)])

            # Read the custom product parameters.
            custom_params = json.loads(mo_record.x_fea_params)

            # Set the product information.
            product = {"name": product_name}
            if product_name == "Cube":
                product["partno"] = 60000
                product["params"] = {}
            
            elif product_name == "Cell Phone":
                # In the case of the cell phone, the display name is
                # '[xxxx0] Cell Phone (myCover, myBoard, myFuseL, myFuseR)'.
                partno = int(display_name[1:6])
                # Change the values of missing fuses from 'None' to 'Empty'.
                params = custom_params.get(str(partno), {})
                if params["fuseL"] == "None":
                    params["fuseL"] = "Empty"
                if params["fuseR"] == "None":
                    params["fuseR"] = "Empty"
                product["partno"] = partno
                product["params"] = params

            elif product_name == "Support":
                partno = 70000
                product["partno"] = partno
                product["params"] = custom_params.get(str(partno), {})
                # The Support has an additional field for image data.
                # Type of the 'x_fea_image' field is binary -> convert to str.
                product["imgdata"] = str(mo_record.x_fea_image)[1:-1]

            # Get a current date in UCT.
            now = fields.Datetime.now()
            timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")

            # Manufacturing order data to be sent to the MES.
            manufacturing_order = {
                "date_created": timestamp,
                "name": name,
                "origin": "Odoo",
                "sales_order": mo_record.origin,
                "erp_order_id": mo_record.id,
                "product": product,
                "qty_todo": int(mo_record.product_qty)
            }

            # API configuration of the MES.
            host = "localhost"
            port = 8000
            url = f"http://{host}:{port}/api/mfg-orders"

            # Send the manufacturing order data to the external MES application.
            try:
                requests.post(url, json=manufacturing_order)
            except requests.exceptions.ConnectionError:
                # TODO: error handling
                pass

        return action
