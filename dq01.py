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
  while i < desired_len:
    match = pattern.match(string)
    if match:
      if i+2 <= desired_len:
        result.append(match.group())
      string = string[match.end():]
      i += 2
    else:
      result.append(string[:1])
      string = string[1:]
      i += 1
  result.append(ellipsis)
  print(''.join(result))
