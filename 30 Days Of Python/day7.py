it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
lst=["Samsung","Xiaomi"]
it_companies.update(lst)
print(it_companies)
it_companies.remove("Facebook")
it_companies.discard("Apple")
print(it_companies)
#unlike remove discard does not issue an error if an element is not in set
C=A.union(B) #A.update(B) # A|B
print(C)
D=A.intersection(B)
print(D)
print(A.issubset(B)) #yes
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del it_companies
del A
del B
del C
del D
age_set=set(age)
print(len(age),len(age_set))

Sentence="I am a teacher and I love to inspire and teach people"
Sentence_list=Sentence.split(" ")
print(set(Sentence_list))