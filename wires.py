# Most wire colors are just the first letter of their name except for black.
# black is 'l' since 'b' is already taken for blue.
from sys import argv

def test(w, p):
  def parity():
    if p is None:
      a = test(w, 'e')
      b = test(w, 'o')
      if a == b:
        return a

      raise Exception('need parity of last digit of serial number')

    if p not in ('e', 'o'):
      raise Exception('invalid parity: ' + p)

    return p

  if len(w) == 3:
    if 'r' not in w:
      return 'second wire'
    elif w[-1] == 'w':
      return 'last wire'
    elif w.count('b') > 1:
      return 'last blue wire'
    else:
      return 'last wire'
  elif len(w) == 4:
    if w.count('r') > 1 and parity() == 'o':
      return 'last red wire'
    elif w[-1] == 'y' and 'r' not in w:
      return 'first wire'
    elif w.count('y') > 1:
      return 'last wire'
    else:
      return 'second wire'

  elif len(w) == 5:
    if w[-1] == 'l' and parity() == 'o':
      return 'fourth wire'
    elif w.count('r') == 1 and w.count('y') > 1:
      return 'first wire'
    elif 'l' not in w:
      return 'second wire'
    else:
      return 'first wire'

  elif len(w) == 6:
    if 'y' not in w and parity() == 'o':
      return 'third wire'
    elif w.count('y') == 1 and w.count('w') > 1:
      return 'fourth wire'
    elif 'r' not in w:
      return 'last wire'
    else:
      return 'fourth wire'

  else:
    return 'invalid number of wires'

print(test(argv[1], argv[2] if len(argv) > 2 else None))
