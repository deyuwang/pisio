'''
@SICP 2.4.5
@author: wdy
'''

numerals = {'I': 1.0, 'V':5, 'X': 10}
print numerals['I']

numerals['I'] = 2.0

print numerals.values()
sum(numerals.values())

print dict([(3,9), (4, 16), (5, 25)])

#default

print numerals.get('A', 0)
