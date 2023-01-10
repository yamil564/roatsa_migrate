#https://gitlab.merchise.org/merchise/odoo/-/blob/40b4584b009a979dcfbff4f464a6bdbbbebc583e/odoo/addons/base/models/res_partner.py
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Transportista(models.Model):
    _name = 'transport.transportista'
    
    name = fields.Char('Nombre')
    codigo = fields.Char('Codigo')
    descripcion = fields.Char('Descripcion')
    active = fields.Boolean(default=True, help="The active field allows you to hide the category without removing it.")
    vehiculo = fields.Many2one('transport.vehicle', string="Vehiculo")
    #middle_name = fields.Char('Segundo Nombre', size=128)
    #last_name = fields.Char('Apellidos', size=128)
    catalog_06_id=fields.Many2one('einvoice.catalog.06', 'Tipo de Documento')
    color = fields.Integer(string='Color Index', default=0)
    #child_ids = fields.One2many('res.partner', 'parent_id', string='Contacts', domain=[('active', '=', True)])  # force "active_test" domain to bypass _search() override
    child_ids = fields.One2many('transport.transportista', 'parent_id', string='Contacts')  #, domain=[('active', '=', True)] force "active_test" domain to bypass _search() override
    birth_date = fields.Date('Fecha de Nacimiento')
    company_type=fields.Selection([('person', 'Individual'), ('company', 'Compania')])
    company_name = fields.Char('Company Name')
    comment = fields.Text(string='Notes')
    default_is_company=fields.Boolean("default_is_company", default=True)
    gender = fields.Selection(
        [('m', 'Masculino'), ('f', 'Femenino'),
         ('o', 'Other')], 'Sexo')
    nationality = fields.Many2one('res.country', 'Nationalidad')
    image = fields.Binary()
    image_small = fields.Binary("Small-sized image", attachment=True,
        help="Small-sized image of this contact. It is automatically "\
             "resized as a 64x64px image, with aspect ratio preserved. "\
             "Use this field anywhere a small image is required.")

    emergency_contact = fields.Many2one(
        'res.partner', 'Contacto de Emergencia')
    id_number = fields.Char('DNI', size=64)
    is_company=fields.Boolean("Is company", default=False)#falta
    ruc = fields.Char("RUC", size=20)
    registration_name = fields.Char('Razon Social', size=128, index=True, )
    type = fields.Selection(
        [('contact', 'Contact'),
         ('invoice', 'Invoice address'),
         ('delivery', 'Shipping address'),
         ('other', 'Other address'),
         ("private", "Private Address"),
        ], string='Address Type',
        default='contact',
        help="Used by Sales and Purchase Apps to select the relevant address depending on the context.")
    
    
    email = fields.Char("Email", size=64)
    #direccion
    phone = fields.Char()
    mobile = fields.Char()
    #lang = fields.Selection(_lang_get, string='Language', default=lambda self: self.env.lang,
    #                        help="All the emails and documents sent to this contact will be translated in this language.")
    
    state_id = fields.Many2one('res.country.state', 'Departamento')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    province_id = fields.Many2one('res.country.state', 'Provincia')
    parent_id=fields.Many2one('transport.transportista', 'Compania')
    district_id = fields.Many2one('res.country.state', 'Distrito')
    street = fields.Char()
    street2 = fields.Char()
    city = fields.Char()
    visa_info = fields.Char('Visa Info', size=64)
    vat = fields.Char(string='Nro Documento')
    title = fields.Many2one('res.partner.title')
    website = fields.Char()
    zip = fields.Char(change_default=True)
    #direccion =fields.Char("Direccion", size=64)
    @api.depends('is_company')
    def _compute_company_type(self):
        for partner in self:
            partner.company_type = 'company' if partner.is_company else 'person'

    def _write_company_type(self):
        for partner in self:
            partner.is_company = partner.company_type == 'company'

    @api.onchange('company_type')
    def onchange_company_type(self):
        self.is_company = (self.company_type == 'company')

        

class VehicleSaleOrder(models.Model):
    _inherit = 'sale.order'

    transportista = fields.Many2one('transport.transportista', string="Transportista", required=True)

class stock_picking_v4(models.Model):#Picking
    _inherit = 'stock.picking'

    transportista = fields.Many2one('transport.transportista', string="Transportista")
     
    def _get_transportista(self):
        for record in self:
            transp = record.env['sale.order'].search([('name', '=',record.group_id.name )])
            record.transportista=transp.transportista.id

class VehicleCreation(models.Model):
    _name = 'transport.vehicle'

    name = fields.Char(string="Nombre del vehiculo", required=True)
    #driver_name = fields.Many2one('res.partner', string="Nombre de contacto")
    driver_name = fields.Many2one('transport.transportista', string="Nombre de contacto")
    vehicle_image = fields.Binary(string='Imagen', store=True, attachment=True)
    licence_plate = fields.Char(string="Placa", required=True)
    mob_no = fields.Char(string="Numero de telefono movil")
    vehicle_address = fields.Char(string="Direccion")
    vehicle_city = fields.Char(string='Ciudad')
    vehicle_zip = fields.Char(string='CODIGO POSTAL')
    state_id = fields.Many2one('res.country.state', string='Estado')
    country_id = fields.Many2one('res.country', string='Pais')
    active_available = fields.Boolean(string="Activo", default=True)

class PuertoAreopuertoEmbarque(models.Model):
    _name = 'puerto.aeropuerto.embarque'

    name = fields.Char(string="Codigo", required=True)
    Descripcion = fields.Char(string="Descripcion", required=True)

class PuertoAreopuertoDesembarque(models.Model):
    _name = 'puerto.aeropuerto.desembarque'

    name = fields.Char(string="Codigo", required=True)
    Descripcion = fields.Char(string="Descripcion", required=True)