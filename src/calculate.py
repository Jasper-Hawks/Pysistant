def calc(): # Calculator function

    # Plan:
    # We first separate every character in the equation
    # in an array. Then check the entire array for 
    # parenthesis. If we have none we evaluate from left
    # to right. If we do we evaluate the equation inside
    # the rightmost parenthesis then continue until we can
    # evaluate without having to worry about parenthesis.

    # Problems:
    # Solving more complex equations that 
    # are inside more parenthesis (specifically
    # those that have more than 2 operands.
    #
    # Operators that are on the outside of parenthesis
    # For Example (2 + 2)* 2
    eq = input("Submit your equation: ")
    eq = list(eq)
    ops = []
    noParen = True
    # These will act as our two operands and c as our sum/product/difference/etc.
    a = 0
    b = 0
    c = 0

    for i in range(len(eq)):
        if eq[i] != " ":
            
            try: # Convert all ints to ints
                eq[i] = int(eq[i])
            except:
                pass

            ops.append(eq[i])

        try: 
            if eq[i].count("(") != 0 or eq[i].count(")") != 0:

                noParen = False # We have parenthesis
                # TODO Insert count code here
                # Count the number of parenthesis if this is the case
        except AttributeError:
            pass

        else:
            noParen = True

        
    print(ops)
    if noParen is True:
        # Then we simply have to evaluate each operator and operand according
        # to the order of operations as follows
        # Exponents 
        # Multiplication
        # Division
        # Addition
        # Subtraction
        #
        # So the first thing we have to do is find the symbols and their operands
        # We'll also have to setup some error handling if symbols or operands are
        # not in their proper places

        # I'm going to try using error handling to detect when we have no
        # more operators. 
        for i in range(len(ops)):
            if ops[i] == "^":

                # This is something I made that will help us identify ints
                # When they are separated by spaces it will be useful later
                # down the line
                if type(ops[i - 1]) is int: # If the first item to the left is a number
                    a = ops[i - 1] # Make that the variable a
                else: # Otherwise 
                    try:  #We'll loop through the remaining ints to the left
                        for j in range(ops.index(ops[i])): 
                            if type(ops[i - j]) is int :
                                a = ops[i - j]
                            else:
                                print("Something went wrong else")
                    except IndexError:
                        print("Indexing went wrong except")

                b = ops[i + 1] # Find the operand on the right of the ^
                c = a ** b
                ops[i] = c
                # We can either delete the items in the list which will mess up 
                # the for loop or replace them with a space and worry about
                # cleaning it out later. Now I'm leaning towards the former.

                # Empty the strings since we're going to raise this operand
                # We can't delete them entirely because the length of ops
                # won't be modifed
                ops[i - 1] = " "
                ops[i + 1] = " "
                print(ops)
                i = 0

            # Then continue this process with every operator

            if ops[i] == "*":
                a = ops[i - 1] 
                a = a
                b = ops[i + 1] 
                b = b
                c = a * b
                ops[i] = c
                ops[i - 1] = " "
                ops[i + 1] = " "

            if ops[i] == "/":
                a = ops[i - 1] 
                a = int(a)
                b = ops[i + 1] 
                b = int(b)
                c = a / b
                ops[i] = c
                ops[i - 1] = " "
                ops[i + 1] = " "

            if ops[i] == "+":
                a = ops[i - 1] 
                a = int(a)
                b = ops[i + 1] 
                b = int(b)
                c = a + b
                ops[i] = c
                ops[i - 1] = " "
                ops[i + 1] = " "

            if ops[i] == "-":
                a = ops[i - 1] 
                a = int(a)
                b = ops[i + 1] 
                b = int(b)
                c = a - b
                ops[i] = c
                ops[i - 1] = " "
                ops[i + 1] = " "




    
    print(ops)
    print(noParen)

if __name__ == "__main__":
    pass
