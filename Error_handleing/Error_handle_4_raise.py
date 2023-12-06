# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:57:00 2023

@author: matthew.king
"""
import csv
def get_movies(file_name):
    if len(file_name) == 0 :
        raise ValueError ("the filename argument is required")
    try: 
        file_handle = open(file_name, newline="")
        try:
            raise ValueError ("The filename argument is required")
            movies = []
            csv_read_handle = csv.reader(file_handle)
            for row in csv_read_handle:
                movies.append(row)
            return movies 
        except Exception as e:
            print(type(e), e)
        finally:
            file_handle.close()
    except FileNotFoundError:
        print("File not found")
        
# you can raise errors to check your try statements. 