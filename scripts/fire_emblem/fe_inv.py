"""
a simple script to better understand dictionaries
"""
#pylint: disable=invalid-name
#fun dynamic web interaction? :)

import pprint

#item and durability and description
char_stuff = {
    'items' : [
    {
        "item" : "Iron Sword",
        "durability" : 46,
        "desc" : "A basic sword made of iron."
    },
    {
        "item" : "Vulnerary",
        "durability": 3,
        "desc" : "Restores small HP"
    }
    ]
}

item_used = char_stuff['items'][1]['item']

pprint.pprint('Marth used a ' + item_used + ' to restore a small amout of HP.')
