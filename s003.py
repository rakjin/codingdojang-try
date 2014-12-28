table = [
  ['23567890'],
  ['456890', '12347890'],
  ['2345689'],
  ['2680', '134567890'],
  ['2356890']
]

while True:
  s, n = raw_input().split(' ')
  if s == '0' and n == '0':
    break
  s = int(s)
  for row in range(0, 5):
    t = table[row]
    if len(t) == 1:
      for digit in n:
        print (' '),
        if digit in t[0]:
          print ('-'*s),
        else:
          print (' '*s),
        print (' '),
        print (' '),
      print('')
    else:
      for r in range(0, s):
        for digit in n:
          if digit in t[0]:
            print ('|'),
          else:
            print (' '),
          print (' '*s),
          if digit in t[1]:
            print ('|'),
          else:
            print (' '),
          print (' '),
        print('')
