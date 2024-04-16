eng = float(input("enter english marks outof 100: "))
math = float(input("enter maths marks outof 100: "))
sci = float(input("enter science marks outof 100 : "))

avg = (eng+math+sci)/3

if avg>=90 and avg<=100:
    print(f"Marks : {avg} Grade: A")
elif avg>=80 and avg<=89:
    print(f"Marks : {avg} Grade: B")
elif avg>=70 and avg<=79:
    print(f"Marks : {avg} Grade: C")
elif avg>=60 and avg<=69:
    print(f"Marks : {avg} Grade: D")
else:
    print(f"Marks : {avg} Grade: F")
