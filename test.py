import random

lst = ['notzero','notone','randomthing',3]
random_thing = random.randint(0,len(lst)-1)

print(len(lst), lst[random_thing], sep='\n')
