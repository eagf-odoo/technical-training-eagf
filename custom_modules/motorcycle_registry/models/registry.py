from odoo import models, fields

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry Info'
    _rec_name = "registry_number"

    registry_number = fields.Char(string = "Registry Number", required = True)
    vin = fields.Char(string = "Vin", required = True)
    first_name = fields.Char(string = "First Name", required = True)
    last_name = fields.Char(string = "Last Name", required = True)
    picture = fields.Image(string = "Picture")
    current_mileage = fields.Float(string = "Current Mileage")
    license_plate = fields.Char(string = "License Plate")
    certificate_title = fields.Binary(string = "Certificate Title")
    register_date = fields.Date(index = True)
    