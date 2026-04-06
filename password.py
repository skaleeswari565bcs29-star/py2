p=input("enter your password:")
digit=0
lower=0
upper=0
special=0
no_spa=1
length=0
if len(p)>=8 and len(p)<=15:
    length=1
for ch in p:
    if ch.isdigit():
        digit=1
    if ch.islower():
        lower=1
    if ch.isupper():
        upper=1
    if ch.isalnum()==0 and ch.isspace()==0:
        special=1
    if ch.isspace():
        no_spa=0
if length and digit and lower and upper and special and no_spa:
        print("valid password")
else:
        print("invalid password")
