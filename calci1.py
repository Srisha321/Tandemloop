class calculator:
    def calculate(self,a,b,operation):
        if operation=="+" or operation== "add" or operation== "addition":
            return a+b
        elif operation=="-" or operation== "subtract" or operation== "subtraction":
            return a-b
        elif operation=="*" or operation== "multiply" or operation== "multiplication":
            return a*b
        elif operation=="/" or operation== "divide":
            if b==0:
                return "Cant divide by zero"
            else:
                return a/b
            
a=float(input("Enter a number(a):"))
b=float(input("Enter a number(b):"))
operation=(input("Enter the operation:"))
calc=calculator()
result=calc.calculate(a,b,operation)
print(f"{a} {operation} {b}=",result)
