#-*- coding: utf-8 -*-
import re

pattern = re.compile('(&#\d+;)|([가-힣]{2})')

while True:
  raw = raw_input()
  if not raw:
    break

  raw = raw.split('/')
  string, ellipsis, desired_len = raw[0], raw[1], int(raw[2])
  if len(string) <= desired_len:
    print(string)
    continue
  desired_len -= len(ellipsis)
  result = []
  i = 0
  while string and (i < desired_len):
    match = pattern.match(string)
    if match:
      #print('match: %s, %d, %d'%(match.group(), match.start(), match.end()))
      if i+2 <= desired_len:
        result.append(match.group())
      string = string[match.end():]
      #print('string afrter match: %s'%string)
      i += 2
    else:
      #print('else')
      result.append(string[0:1])
      string = string[1:]
      i += 1
  result.append(ellipsis)
  print(''.join(result))


# &#65378;가나다&#65379; /../5