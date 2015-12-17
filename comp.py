# r -> red
# b -> blue
# v -> violate
# w -> white

# 0 -> no led
# 1 -> yes led

# 0 -> no star
# 1 -> star

from sys import argv

d = {
  'w00': 'C',
  'w10': 'D',
  'b00': 'S',
  'r00': 'S',
  'v00': 'S',
  'r01': 'C',
  'v01': 'P',
  'w11': 'B',
  'r10': 'B',
  'b11': 'P',
  'b01': 'D',
  'r01': 'C',
  'r11': 'B',
}

print(d[argv[1]])
