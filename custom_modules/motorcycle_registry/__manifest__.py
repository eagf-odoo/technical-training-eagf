{
    'name': "Motorcycle Registry",
    'summary':"Manage Registration of Motorcycles",
    'description': """Motorcycle Registry
    ============================
    This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycle of tehe brand""",
    'license': "OPL-1",
    'author': "eagf",
    'website': "https://www.github.com/eagf-odoo",
    'category': "Kawiil/Kawiil",
    'depends': ['base'],
    'data': [
        'security/registry_groups.xml',
        'security/ir.model.access.csv',
        'security/registry_security.xml',
        'views/registry_menuitems.xml'
    ],
    'demo': [
        'demo/registry_demo.xml'
    ],
    'application': True,
}