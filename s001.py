# http://codingdojang.com/scode/365?answer=1323#answer_1323

def generate(num):
  return num + sum([int(d) for d in str(num)])

generated = set([generate(n) for n in range(1, 5000)])
all_num = set(range(1, 5000))

print(sum(all_num-generated))
