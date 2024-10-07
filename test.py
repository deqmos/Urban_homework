n = int(input())
if n == 0:
    print("ZeroDivisionError: integer division or modulo by zero")
for i in range(0, 1000):
    if i % n == 0:
        print(i)
