from sys import argv

d = {
    '2136': '1 1',
    '4225': '1 2',
    '4446': '1 3',
    '1141': '2 1',
    '3564': '2 2',
    '1553': '2 3',
    '1262': '3 1',
    '4143': '3 2',
    '5132': '3 3',
}

for k, v in d.items():
  d[k[2:] + k[:2]] = v

print(d[argv[1]])
