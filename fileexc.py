#!/usr/bin/env python3
filename = input('Enter file path')

try :
	f = open(filename)
	print(f.read())
	
except FileNotFoundError:
	print('File not found!')

finally :
	f.close()

