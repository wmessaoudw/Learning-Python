v1="thirty "+"days "+"of "+"python"
print(v1)
v2="Coding"+" For"+" All"
print(v2)


company="Coding for all"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company[6:])
print(company.find("Coding"))
print(company.replace("Coding","Python"))
print(company.replace("all","Everyone"))
print(company.replace("Coding for all","Python For All"))
print(company.split())
V="Facebook,Google,Ibm,Apple"
print(V.split(', '))
print(company[0])
print(company[-1])
print(company[10])
PFE="PFE"
CFA="CFA"
print(company.index("C"))
print(company.index("f"))
print(company.rfind("l"))
sentence="You can't end a sentence with  because because because is a conjuction "
print(sentence.index("because"))
print(sentence.rindex("because"))
print(sentence.split("because"))
print("Coding"==company.split(' ',1)[0])
print("all"==company.rsplit(' ',1)[-1])
print("days_ofC_oding".isidentifier())
python_libaries=["django","numpy","mathpy"]
space=' '
print(space.join(python_libaries))
print("Name    \t age\t country \t city" )
print("Messaoud\t 20 \t algeria \t m'sila")
print("Hello my name is {} iam {} i was born in {}".format("Messaoud",20,"Algeria"))
print("{}+{}={}".format(5,5,5+5))