#!/usr/bin/env python

import sys 
file_name = sys.argv[1]

file_obj = open(f"{file_name}","r") 
inline = 1 # Tell the program, what line is it
file = file_obj.readlines()
j = 0

for i in file:
    statement = " ".join((i.split("#")[0]).split())
    
    if statement[-1] != ';' and not(statement[-1] == "\\"):
        # report error 
        print(f"In {file_name}:{inline}:error: \nexpected ';' after statment.")
        print(f"    {statement}")
        print(" " * len(statement) + 3 * " ","^")

        exit(123)

    elif j == 1:
        continue

    elif statement[-1] == '\\':
        print(f"{statement.replace(';','')[:-1]}")
        j = 1
        continue

    else:
        print(f"{statement.replace(';','')}")
