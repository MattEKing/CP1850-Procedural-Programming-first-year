# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:26:48 2023

@author: matthew.king
"""
characters = {'Arun':{'class': ' knight',
                      'weapon':'lance',
                      'city': 'Rivendale',
                      'HPPotions': 5,
                      'MPPotions': 10,},
              'Yennifer': {'Class': 'Wizard',
                           'weapon': 'Dagger',
                           'city': 'allentown',
                           'HPPotions': 10,
                           'MPPotions': 2,
                           'skill': 'Dark Magic'}}

weapon = characters['Arun']['weapon']
characters['Arun']['skill'] = 'Rolling bash'
characters['Arun'].pop('skill')
characters['Yennifer'].get('weapon')
characters['Yennifer'].get('Armor', 'cloth')
characters['Arun']['Reg_skill'] = ['Bash','taunt', 'Stab']
characters["Arun"]['Reg_skill']
characters["Arun"]['Reg_skill'][0]
