table = [
  ['23567890'],
  ['456890', '12347890'],
  ['2345689'],
  ['2680', '134567890'],
  ['2356890']
]
e, d, p = ' ', '-', '|'

while True:
  s, n = raw_input().split(' ')
  if s == '0' and n == '0':
    break
  s = int(s)
  for row in range(0, 5):
    t = table[row]
    if len(t) == 1:
      for digit in n:
        c = d if digit in t[0] else e
        print (' %s  '%(c*s)),
      print
    else:
      for r in range(0, s):
        for digit in n:
          c1 = p if digit in t[0] else e
          c2 = p if digit in t[1] else e
          print('%s%s%s '%(c1, e*s, c2)),
        print
  print
