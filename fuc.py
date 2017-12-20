#!/usr/bin/env python3
def f(a,c,data = []):
   a.append('456')
   c = 100
   data.append(a)
   return data

a = ['11','12']
c = 1
print(f(a,c))
print(a,c)
