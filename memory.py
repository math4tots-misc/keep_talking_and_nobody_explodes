try:
  raw_input
except NameError:
  raw_input = input

d1, = list(map(int, raw_input('stage 1 [d]: ').split()))

if d1 == 1:
  p1 = 2
elif d1 == 2:
  p1 = 2
elif d1 == 3:
  p1 = 3
elif d1 == 4:
  p1 = 4

print('press button in position %s' % p1)

d2, p1, v1 = list(map(int, raw_input('stage 2 [d p v]: ').split()))

if d2 == 1:
  print('press button labeled 4')
elif d2 == 2:
  print('same position as in stage 1')
elif d2 == 3:
  print('first position')
elif d2 == 4:
  print('same position as in stage 1')

d3, p2, v2 = list(map(int, raw_input('stage 3 [d p v]: ').split()))

if d3 == 1:
  print('press button labeled 4')
elif d3 == 2:
  print('same position as in stage 1')
elif d3 == 3:
  print('first position')
elif d3 == 4:
  print('same position as in stage 1')


