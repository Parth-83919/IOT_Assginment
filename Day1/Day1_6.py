def fact(num):
    temp=num
    sum=1
    while temp!=0:
        sum = int(sum * temp)
        temp = temp - 1
    return sum


num = int(input("Enter the number : "))

print(f"factorial of {num}: {fact(num)}")


