from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry Info'
    _rec_name = "registry_number"
    # Add constraint to VIN
    _sql_constraints = [('vin_unique','UNIQUE(vin)', 'Another registration for this VIN number already exists!')]

    registry_number = fields.Char(string = "Registry Number", required = True, default = "MRN0001")
    vin = fields.Char(string = "VIN", required = True)
    first_name = fields.Char(string = "First Name", required = True)
    last_name = fields.Char(string = "Last Name", required = True)
    picture = fields.Image(string = "Picture")
    current_mileage = fields.Float(string = "Current Mileage")
    license_plate = fields.Char(string = "License Plate")
    certificate_title = fields.Binary(string = "Certificate Title")
    register_date = fields.Date(index = True)

    # Override create method to add the sequence
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0001')) == ('MRN0001'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)
    
    # Check if VIN is correct
    @api.constrains('vin')
    def _check_vin_pattern(self):
        pattern = '^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{6}$'
        for registry in self.filtered(lambda r:r.vin):
            match = re.match(pattern, registry.vin)
            if not match:
                raise ValidationError('Invalid VIN!')
            if not registry.vin[0:2] == 'KA':
                raise ValidationError('Only motorcycles from Kawiil are allowed')
    
    # Check license plate
    @api.constrains('license_plate')
    def _check_license_plate(self):
        pattern = '^[A-Z]{1,3}\d{1,4}[A-Z]{0,2}$'
        for registry in self.filtered(lambda r:r.license_plate):
            match = re.match(pattern, registry.license_plate)
            if not match:
                raise ValidationError('Invalid license plate!')
