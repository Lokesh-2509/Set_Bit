def set_bits_and_convert(A, B):
    num = (1 << A) | (1 << B)
    return num
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
result = set_bits_and_convert(A, B)
print("Output:", result)
