#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import api, models


class pdf_cotizacion_report(models.AbstractModel):
    _name = 'report.custom_roatsa.pdf_cotizacion_template'

    @api.model
    def render_html(self, docids, data=None):
        cotizacion = self.env['sale.order'].browse(docids)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': cotizacion,
            'data': data,
        }
        return self.env['report'].render('custom_roatsa.pdf_cotizacion_template', docargs)
