#!/usr/bin/env python
# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
import odoo.addons.decimal_precision as dp
import logging

class product_product_v5(models.Model):
    _inherit = 'product.template'

    costo_promedio = fields.Float(string="Costo promedio",compute="_compute_costo_promedio")
    cantidadprueba = fields.Float(string="Cantidad",compute="_compute_costo_promedio")
    promedioprueba = fields.Float(string="Promedio:",compute="_compute_costo_promedio")
    
    def _compute_costo_promedio(self): 
        for record in self:
            costo=self.env['stock.quant'].search([('product_id.id','=',record.product_variant_id.id),('location_id.usage','=', 'internal')])
            promedio=0
            cantidad=0
            for cost in costo:
                if cost.cost!=0:
                    promedio+=cost.cost*cost.qty
                cantidad+=cost.qty
            if cantidad!=0:
                record.costo_promedio=promedio/cantidad
                record.cantidadprueba=cantidad
                record.promedioprueba=promedio
                final_precio=promedio/cantidad
                sql = "update product_supplierinfo set price=%s where product_tmpl_id=%s" % (final_precio,record.id)
                self._cr.execute(sql)
            else:
                record.costo_promedio=0
