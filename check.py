s1=(input("enter a first string:"))
s2=input("enter a second string:")
if len(s1)==len(s2):
    s1=s1.lower()
    s2=s2.lower()
    if sorted(s1)==sorted(s2):
        print("anagram")
    else:
        print("not anagram")
