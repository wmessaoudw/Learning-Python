import re
test={}

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
p2=re.split(r'[. ]+',paragraph)
for i in p2:
    test[i]=test.get(i,0)+1


for i in test.items():
    print(i)
notValidPython=r'^[0-9]|[^a-zA-Z0-9_]'
test1='hello'
if re.search(notValidPython,test1) is  None:
    print(' true')
else:
    print('false')
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
freq={}
print(re.sub(r'[#@$%&;?!,.]','',sentence))
sentence2=re.sub(r'[#@$%&;?!]','',sentence)
print(sentence2)
sentence2=sentence2.split(' ')
for i in sentence2:
   freq[i]=freq.get(i,0)+1
sentence2.sort()
for i in freq.items():
    print(i)





