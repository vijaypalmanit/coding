input = 'aaabcccdeeef'
inpt_dict=dict.fromkeys(input,0)
# inpt_dict = {i:0 for i in input}
for chr in input:
  inpt_dict[chr]+=1
for chr in input:
  if inpt_dict[chr]==1:
    print(chr)
    break