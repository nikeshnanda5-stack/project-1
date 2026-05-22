
n1 = int(input("enter the first number:"))
n2 = int(input("enter the second number:"))
op = input("enter the operator:")
if op == "+":
    print("sum:",n1+n2)
elif op == "-":
    print("difference:",n1-n2)
elif op == "*":
    print("product:",n1*n2)
elif op == "/":
    print("division:",n1/n2)
else:
    print("you have not put any operator")

