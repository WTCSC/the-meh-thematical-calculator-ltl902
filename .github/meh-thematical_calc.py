import time
error = 0
def errors():
    
    if error == 3:
        time.sleep(0.5)
        print("\nWow fool me once shame on you fool me twice shame on me fool me three time and your just plain dumb im not dealing with you anymore.\n do your own math from now on\n")
        exit()
    elif error == 2:
        time.sleep(0.5)
        print("\nokay how many more times are you going to mess up before you get it right?\n try again and maybe read the instructions this time\nTHIS IS THE FINAL STRAW DONT MESS IT UP\n")
    elif error == 1:
        time.sleep(1)
        print("\nThat is not a valid input why are you stupid?\n try again and maybe read the instructions this time\n")
    else:
        exit()
    
def add(a, b):
    time.sleep(1)
    return a + b

def subtract(a, b):
    time.sleep(0.1)
    return a - b

def multiply(a, b):
    time.sleep(1)
    return a * b

def divide(a, b):
    time.sleep(1)
    if b == 0:
        print ("are you really that dumb?/n everyone knows you can't divide by zero\ well i guess everyone but you")
    return a / b

def power(a, b):
    time.sleep(1)
    return a ** b

print("The Meh-thematical Calculator")
print("Oh great another person coming to bother me with two plus two or whatever")

while True:
    time.sleep(1)
    math = input("Fine I guess ill do math for you, what operation do you want to do?\n type add, subtract, multiply, divide, or power: ")
    if math in ('add', 'subtract', 'multiply', 'divide', 'power'):
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        if math == 'add':
            print (add(num1, num2))
        elif math == 'subtract':
            print (subtract(num1, num2))
        elif math == 'multiply':
            print (multiply(num1, num2))
        elif math == 'divide':
            print (divide(num1, num2))
            
        elif math == 'power':
            print (power(num1, num2))
        else:
            errors()
    else:
        error += 1
        errors()