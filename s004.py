
def is_slurpy(s):
  l = len(s)
  if l < 5:
    return False
  for i in range(2, l-1):
    slimp = s[0:i]
    slump = s[i:]
    if is_slimp(slimp) and is_slump(slump):
      return True
  return False

def is_slump(s):
  l = len(s)
  if l < 3:
    return False
  if s[0] != 'D' and s[0] != 'E':
    return False
  i = 1
  while i < l and s[i] == 'F':
    i += 1
  if i == 1:
    return False
  rest = s[i:]
  if rest == 'G':
    return True
  else:
    return is_slump(rest)

def is_slimp(s):
  l = len(s)
  if l < 2:
    return False
  if s[0] != 'A':
    return False
  if l == 2:
    return (s[1] == 'H')
  if s[1] == 'B' and s[-1] == 'C':
    slimp = s[2:-1]
    return is_slimp(slimp)
  if s[-1] == 'C':
    slump = s[1:-1]
    return is_slump(slump)
  return False

print('SLURPYS OUTPUT')
c = int(raw_input())
while c:
  if is_slurpy(raw_input()):
    print('YES')
  else:
    print('NO')
  c -= 1
print('END OF OUTPUT')
