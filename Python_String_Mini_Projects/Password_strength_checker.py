p=input("Enter password: ")

u=0
l=0
d=0
s=0

for x in p:
    if x.isupper():
        u=1
    elif x.islower():
        l=1
    elif x.isdigit():
        d=1
    elif not x.isalnum():
        s=1

if len(p)<6:
    print("Weak")
elif u and l and d and s:
    print("Strong")
else:
    print("Medium")