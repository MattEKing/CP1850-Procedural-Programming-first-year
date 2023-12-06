# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:42:45 2023

@author: matthew.king
"""
import csv
def read_file(file_name):
    try: 
        file_handle = open(file_name, newline="")
        try:
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
        

# finally will run even after the error happenes so the code doesn't stop.