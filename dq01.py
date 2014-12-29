#-*- coding: utf-8 -*-
import re

kor_len = len('가') # 2 on win and 3 on osx, ...
pattern = re.compile('&#\d+;|[가-힣ㄱ-ㅣ]{%d}' % kor_len)

while True:
  try:
    raw = raw_input()
  except (EOFError):
    break
  if not raw:
    break

  raw = raw.split('/')
  string, ellipsis, desired_len = raw[0], raw[1], int(raw[2])
  
  if len(string) <= desired_len:
    print(string)
    continue

  desired_len -= len(ellipsis)
  result = []
  count = 0
  while count < desired_len:
    match = pattern.match(string)
    if match:
      if count+2 <= desired_len:
        result.append(match.group())
      string = string[match.end():]
      count += 2
    else:
      result.append(string[:1])
      string = string[1:]
      count += 1
  result.append(ellipsis)
  print(''.join(result))
