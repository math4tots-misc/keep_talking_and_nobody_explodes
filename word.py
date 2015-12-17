from sys import argv

poss = argv[1:]

words = [
  'about', 'after', 'again', 'below', 'could',
  'every', 'first', 'found', 'great', 'house',
  'large', 'learn', 'never', 'other', 'place',
  'plant', 'point', 'right', 'small', 'sound',
  'spell', 'still', 'study', 'their', 'there',
  'these', 'thing', 'think', 'three', 'water',
  'where', 'which', 'world', 'would', 'write',
]

copy = set(words)

for i, p in enumerate(poss):
  copy = set(w for w in copy if w[i] in p)

print(copy)
