# -*- coding: utf-8 -*-
{
    'name': 'POS Kitchen Receipt',
    'version': '17.0',
    'author': "",
    'website': "",
    "price": 10000,
    "currency": "USD",
    'license': "OPL-1",
    "images": [],
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'summary': '',
    'description': '',
    'data': [
    ],
    'depends': ['point_of_sale','pos_restaurant'],
    'installable': True,
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_kitchen_receipt//static/src/**/*',
        ],
    },
}
