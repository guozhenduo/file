#!/usr/bin/env python

import sys 
file_name = sys.argv[1]

file_obj = open(f"{file_name}","r") 
inline = 1 # Tell the program, what line is it
file = file_obj.readlines()

for i in file:
    statement = " ".join((i.split("#")[0]).split())
    
    if statement[-1] != ';':
        print(f"In {file_name}:{inline}:error: \nexpected ';' after statment.")
        print(f"    {statement}")
        
    print(f"{statement.replace(';','')}")
