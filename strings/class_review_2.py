# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:42:43 2023

@author: matthew.king
"""

# pickle file function

dict_fr_pickle = {'Wizard':{'Skills': ['Fireball', 'Ice Wall'],
                            'Equipment':['Hat', 'Staff'],
                            'inventory':['HP Postion',"MP Potsion"]},
                  "Rogue":{'Skills': ['steal','backstep'],
                           'Equipment': ['dagger', 'cloth'],
                           'inventory': ['HP Postion','MP postion']}}

import pickle
# this will write to the binary file with a pickle.dump()
with open('Legends_of_CNA.pkl', 'wb') as bfh:
    pickle.dump(dict_fr_pickle, bfh)
    
# this will read the pickle file with a pickle.load()
with open('Legends_of_CNA.pkl', 'rb') as rbfh:
    check_dict = pickle.load(rbfh)

# reviewing Dictinoaries
#creating a dict
example_dict = {'date':'2020-12-22',
                'quarter': 4,
                'region': 'w',
                'amount': 2500}

#Accessing the objects
example_dict['amount']

#update the objects
example_dict['amount'] = 3500

#creating new keys
region = {'w': 'West','e': 'East','n':'north','s':'south'}
example_dict['region_full_name'] = region[example_dict['region']]


# nested dict
example_dict2 = {'date':{'year': 2020,'month': 12,'day':22},
                 'quarter': 4,
                 'region': ['w', 'e'],
                 'amount': 2500}
#Accessing object is nested dicts
example_dict2['region'][0]
