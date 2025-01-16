a = int(input("Enter the Number: "))
b = int(input("Enter the Number: "))
sum_of_a_and_b = a + b
def calculation(a,b):
    is_lessthan_then_10 = sum_of_a_and_b < 10
    if is_lessthan_then_10:
        return a + b
    else:
        return a * b
    
result = calculation(a,b)
print(result)