"""write a progrem to check if a list contains a palindrome of element"""
a=int(input("1st="))
b=int(input("2nd="))
c=int(input("3rd="))
d=int(input("4th="))
print("all num=",a,b,c,d)

e=[]
e.append(a)
e.append(b)
e.append(c)
e.append(d)

print(e)

copied_e=e.copy()
copied_e.reverse()
if(copied_e==d):
    print("palindrome")
else:
    print("not")