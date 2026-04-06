s=input("enter a string:")
if len(s)<=3:
    res=s
elif s.endswith("ing"):
    res=s+"ly"
else:
    res=s+"ing"
print("result=",res)
