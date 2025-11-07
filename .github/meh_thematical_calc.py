import time

# Global counter for how many invalid inputs the user has given.
# Starts at 0. Several parts of the program rely on reading and
# incrementing this variable to change behavior (e.g., warn the user,
# then exit after too many invalid tries).
error = 0

def errors():
    """
    Display progressively sterner messages based on the global 'error' count.
    Side effects:
      - may call time.sleep() to pause for user readability
      - may call exit() to terminate the whole script when threshold reached

    NOTE: This function *reads* the global variable 'error'. It does not
    declare 'global error' because it only reads it. If you intend to
    modify 'error' from inside this function you'd need a global
    declaration.
    """
    # If the user has made 3 invalid inputs, print final message and quit
    if error == 3:
        # brief pause to make message feel dramatic
        time.sleep(0.5)
        print(
            "\nWow fool me once shame on you fool me twice shame on me "
            "fool me three time and your just plain dumb im not dealing "
            "with you anymore.\n do your own math from now on\n"
        )
        # Terminate the program immediately
        exit()

    # If the user has made 2 invalid inputs, print a stern warning but continue
    elif error == 2:
        time.sleep(0.5)
        print(
            "\nokay how many more times are you going to mess up before you get it right?\n"
            " try again and maybe read the instructions this time\n"
            "THIS IS THE FINAL STRAW DONT MESS IT UP\n"
        )

    # If the user has made 1 invalid input, print a milder scolding and let them continue
    elif error == 1:
        time.sleep(1)
        print(
            "\nThat is not a valid input why are you stupid?\n"
            " try again and maybe read the instructions this time\n"
        )

    # Any other value (including 0) will simply exit — *this branch will run
    # only if none of the above conditions match*.
    else:
        # This immediately terminates the program for any value not matched above.
        # In normal program flow this is unlikely to be useful since errors()
        # is only called when input errors exist; but be mindful of this behavior.
        exit()

def add(a, b):
    """
    Return the addition of a and b.
    No side effects.
    Parameters are expected to be numeric (int or float).
    """
    return a + b

def subtract(a, b):
    """
    Return the subtraction result a - b.
    A tiny sleep is used to make the program feel like it's 'thinking'.
    """
    time.sleep(0.1)
    return a - b

def multiply(a, b):
    """
    Return the product a * b.
    """
    return a * b

def divide(a, b):
    """
    Return the division a / b.

    IMPORTANT:
    - This implementation prints an error message if b == 0, but after
      printing it still continues to execute `return a / b`, which will
      raise a ZeroDivisionError. That means printing the message is not
      enough — you must prevent the division from happening when b == 0.
    - The error message contains incorrect escape sequences like "/n" (backslash-n),
      which will not produce a newline. Use "\n" instead.
    """
    if b == 0:
        # This prints a (rude) error message notifying the user they attempted
        # division by zero. Because of the stray "/n" and missing backslash
        # in the string, the output may not behave as intended.
        print("are you really that dumb?/n everyone knows you can't divide by zero\ well i guess everyone but you")
    # This will raise if b == 0. See the note above.
    return a / b

def power(a, b):
    """
    Return a raised to the power b (a ** b).
    """
    return a ** b

# The usual Python idiom to ensure this block runs only when the script is
# executed directly (not when imported as a module).
if __name__ == "__main__":
    # Greeting messages printed once at program start
    print("The Meh-thematical Calculator")
    print("Oh great another person coming to bother me with two plus two or whatever")

    # Main input loop. This will continue until an exit() is called either in
    # errors() or elsewhere. The loop asks for an operation then two numbers.
    while True:
        # Pause briefly so messages don't flash too quickly
        time.sleep(1)

        # Ask the user which operation to perform.
        # The accepted literal strings are: 'add', 'subtract', 'multiply', 'divide', 'power'
        math = input(
            "Fine I guess ill do math for you, what operation do you want to do?\n"
            " type add, subtract, multiply, divide, or power: "
        )

        # If user typed one of the accepted operations, proceed to get numbers
        if math in ('add', 'subtract', 'multiply', 'divide', 'power'):
            # Prompt for two numbers. The code uses float() to accept integers or decimals.
            # If the user types something that can't be converted to float, a ValueError
            # will be raised and crash the program unless you catch it.
            num1 = float(input("What is the first number: "))
            num2 = float(input("What is the second number: "))

            # Dispatch to the appropriate operation, with a small pause before showing result.
            if math == 'add':
                time.sleep(0.5)
                print(add(num1, num2))

            elif math == 'subtract':
                time.sleep(0.5)
                print(subtract(num1, num2))

            elif math == 'multiply':
                time.sleep(0.5)
                print(multiply(num1, num2))

            elif math == 'divide':
                time.sleep(0.5)
                print(divide(num1, num2))

            elif math == 'power':
                time.sleep(0.5)
                print(power(num1, num2))

            else:
                # This branch is unreachable because we already checked membership
                # in the 'if math in (...)' guard above. It's defensive programming.
                errors()

        else:
            # The user typed an invalid operation string.
            # The intention is to increment the global error counter, then call errors(),
            # so they see progressively sterner warnings and eventually the program exits.
            #
            # PROBLEM: This line attempts to rebind the name 'error' from within a function
            # scope (the __main__ block). In Python, assigning to a name in a local scope
            # makes it local; because 'error' is referenced earlier in errors() as a global,
            # and we have an assignment here, this will raise an UnboundLocalError unless
            # you declare 'global error' before assigning to it.
            error += 1
            errors()
