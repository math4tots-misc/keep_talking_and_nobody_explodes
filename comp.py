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
  'b00': 'S',
  'b01': 'D',
  'b10': 'P',
  'b11': 'P',
  'r00': 'S',
  'r01': 'C',
  'r10': 'B',
  'r11': 'B',
  'v00': 'S',
  'v10': 'S',
  'v01': 'P',
  'v11': 'D',
  'w00': 'C',
  'w01': 'C',
  'w10': 'D',
  'w11': 'B',
}

print(d[argv[1]])
