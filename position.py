a=input("enter a string:")
print("even position of characters...")
for i in range(1,len(a),2):
    print(a[i],end='\t')
print("\nodd position of characters...")
for i in range(0,len(a),2):
    print(a[i],end='\t')
