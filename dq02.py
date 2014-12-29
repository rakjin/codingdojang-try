#-*- coding: utf-8 -*-
import re

pattern = re.compile(u'&#\d+;|[가-힣ㄱ-ㅣ]')
MULTIBYTE_CHARACTER_SIZE = 2

def len_considering_multibyte_character(string):
  length = 0
  while string:
    match = pattern.match(string)
    if match:
      string = string[match.end():]
      length += MULTIBYTE_CHARACTER_SIZE
    else:
      string = string[1:]
      length += 1
  return length

def trim_tail(string, ellipsis, desired_len):
  if len_considering_multibyte_character(string) <= desired_len:
    return string

  result = []
  output_len = 0
  ellipsis_len = len_considering_multibyte_character(ellipsis)
  desired_len -= ellipsis_len

  while output_len < desired_len:
    match = pattern.match(string)
    if match:
      if output_len + MULTIBYTE_CHARACTER_SIZE <= desired_len:
        result.append(match.group())
      string = string[match.end():]
      output_len += MULTIBYTE_CHARACTER_SIZE
    else:
      result.append(string[:1])
      string = string[1:]
      output_len += 1
  
  result.append(ellipsis)
  return ''.join(result)

if __name__ == '__main__':
  while True:
    try:
      raw = unicode(raw_input(), 'utf8')
      raw = raw.split('/')
      string, ellipsis, desired_len = raw[0], raw[1], int(raw[2])
    except EOFError, e:
      break
    
    print(trim_tail(string, ellipsis, desired_len))
