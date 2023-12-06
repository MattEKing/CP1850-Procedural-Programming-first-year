# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 08:09:28 2023

@author: matthew.king
"""

import pickle 

movies = [["Monty Python and the holy grail", 1975],
          ["On the Waterfront", 1954],
          ["Cat on the Hot Tin Roof", 1939]]

# writing a pickle to a file 

with open('movies_pic.bin', 'wb') as binary_file:
    pickle.dump(movies, binary_file)

# reading binary file..

with open('movies.bin', 'rb') as binary_file:
    new_movie_collection = pickle.load(binary_file)