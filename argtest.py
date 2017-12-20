#!/usr/bin/env python3
import sys
print(len(sys.argv))
print('import')
if __name__ == '__main__':
 print('not import')
 for s in sys.argv:
    print(s)
print('finish')
