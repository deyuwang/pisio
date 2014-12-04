'''
@author: wdy
'''

chinese_suits = ['coin', 'string', 'myriad']

suits = chinese_suits

print suits.pop()
print suits, chinese_suits


suits.remove('coin')

print suits

suits[0] = 'spade'

suits = [1, 3, 4]
suits[0:2] = ['heart', 'diamond']

nest = list(suits)
print nest

suits.insert(1, 'Joker')
print suits
