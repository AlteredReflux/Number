print("The current operands are Multiplication() Subtraction() Addition() Division() Exponent()")

Multiplication = ("Multiplication ()")
Subtraction = ("Subtraction ()")
Addition = ("Addition ()")
Division = ("Division ()")
Exponent = ("Exponent ()")

def Multiplication():
    print ("Enter two numbers  and I will multiply them")

        # First variable
    astring = input ("Enter the first number: ")
    a = int (astring)
        # Second variable
    bstring = input ("Enter a second number: ")
    b = int (bstring)
        # Prints the output of the two numbers
    print (a, "times", b, "equals", a*b)
    
def Subtraction():
    print ("Enter two numbers  and I will subtract them")

        # First variable
    cstring = input ("Enter the first number: ")
    c = int (cstring)
        # Second variable
    dstring = input ("Enter a second number: ")
    d = int (dstring)
        # Prints the output of the two numbers
    print ("The difference of", c, "and", d, "is", c-d)

def Addition():
    print ("Enter two numbers  and I will add them")

        # First variable
    estring = input ("Enter the first number: ")
    e = int (estring)
        # Second variable
    fstring = input ("Enter a second number: ")
    f = int (fstring)
        # Prints the output of the two numbers
    print ("The sum of", e, "and", f, "is", e+f)
    
def Division():
    print ("Enter two numbers  and I will divide them")

        # First variable
    gstring = input ("Enter the first number: ")
    g = int (gstring)
        # Second variable
    hstring = input ("Enter a second number: ")
    h = int (hstring)
        # Prints the output of the two numbers
    print (g, "divided by", h, "is", g/h)

def Exponent():
    print ("Enter two numbers and I will time them by the exponent")

        # First variable
    istring = input ("Enter the exponent: ")
    i = int (istring)
        # Second variable
    jstring = input ("Enter the second value: ")
    j = int (jstring)
        # Prints the output of the two numbers
    print ("The exponent", j, "times", i, "is", j**i)
    
