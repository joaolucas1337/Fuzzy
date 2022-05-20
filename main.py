# Imports
import os
import sys
import numpy as np
import skfuzzy as fz

# GPUs dic
gpu = {
    'GTX 1080ti': {
        'RAM': '11gb',
        'CLOCK': '1481Mhz',
        'BUS': '352 bits',
        'PRICE': 'R$ 3.000,00',
        'YEAR': 2017
    },
    'RTX 2060': {
        'RAM': '6gb',
        'CLOCK': '1365Mhz',
        'BUS': '192 bits',
        'PRICE': 'R$ 2.700,00',
        'YEAR': 2020
    }
}


# Main Class
class Main():
    def __init__(self):
        for a, b in gpu.items():
            print(f'\nPlaca: {a}')
            specs = '      -> RAM: ' + str(b['RAM']) + '\n'
            specs += '      -> BUS: ' + str(b['BUS']) + '\n'
            specs += '      -> CLOCK: ' + str(b['CLOCK']) + '\n'
            specs += '      -> PRICE: ' + str(b['PRICE']) + '\n'
            specs += '      -> YEAR: ' + str(b['YEAR']) + '\n'
            print(f'    Specs:\n{specs}')


if __name__ == '__main__':
    Main()
