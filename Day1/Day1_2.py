num = int(input("Enter the number : "))

temp=num
a = int(temp%10)
temp=temp/10

b = int(temp%10)
temp=temp/10

c= int(temp%10)
temp=temp/10

d = int(temp)

print(f"{d} {c} {b} {a} ")
print(f"{num} = {d*1000}+{c*100}+{b*10}+{a}")

rev=0
temp1=num
while temp1!=0 : 
    n=temp1%10
    rev = rev*10+n
    temp1 = int(temp1/10)
print(rev)