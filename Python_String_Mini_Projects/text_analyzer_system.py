t=input("Enter text: ")

print("Total chars:",len(t))

w=t.split()
print("Total words:",len(w))

sen=t.count('.')+t.count('!')+t.count('?')
print("Total sentences:",sen)

v=0
c=0
d=0
s=0

for x in t:
    if x.lower() in "aeiou":
        v+=1
    elif x.isalpha():
        c+=1
    elif x.isdigit():
        d+=1
    elif x!=" ":
        s+=1

print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("Special chars:",s)

print("Uppercase:",t.upper())
print("Lowercase:",t.lower())

a=input("Enter word to search: ")

if a.lower() in t.lower().split():
    print("Word found")
else:
    print("Word not found")

print("Word frequency:")

for x in w:
    print(x,":",w.count(x))

t=t.strip()

while "  " in t:
    t=t.replace("  "," ")

print("New text:",t)