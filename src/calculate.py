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

        for i in range(len(ops)):
            if ops[i] == "^":

                # Find the remaning ints to the left and set it to our a operand
                left = range((len(ops) - 1) - ((len(ops) - 1) - i))
                for k in left: # Go through the list from the current index to the left most item in the index
                    if type(ops [i - k]) is int: # If the item we are currently on is an int
                        a = ops[i - k] # Then set it to the a operand
                        ops[i - k] = " " # Leave the space blank
                    elif ops[i - k] == "^" or ops[i - k] == "*" or ops[i - k] == "/" or ops[i - k] == "+" or ops[i - k] == "-":
                        print("Incorrect Syntax")
                        exit()

                # Find the remaining ints to the right and set it to our b operand
                right = range((len(ops) - 1) - i) 
                for j in right: # loop through the list to find an int
                    if type(ops[i + j]) is int: # If we have one then 
                        b = ops[i + j] # assign it to the b variable
                        ops[i + j] = " " # make the space empty
                    elif ops[i + j] == "^" or ops[i + j] == "*" or ops[i + j] == "/" or ops[i + j] == "+" or ops[i + j] == "-":
                        print("Incorrect Syntax")
                        exit()
                   
                c = a ** b
                ops[i] = c
                # We can not delete the items because it will mess up the for
                # loop so for know we will just empty them

                # Empty the strings since we're going to raise this operand
                # We can't delete them entirely because the length of ops
                # won't be modifed
                ops[i - 1] = " "
                ops[i + 1] = " "
                i = 0

            # We need to go through each operator with
            # a for loop
        for i in range(len(ops)):
            if ops[i] == "*":
               # Find the remaning ints to the left and set it to our a operand
                left = range((len(ops) - 1) - ((len(ops) - 1) - i))
                for k in left: # Go through the list from the current index to the left most item in the index
                    if type(ops [i - k]) is int: # If the item we are currently on is an int
                        a = ops[i - k] # Then set it to the a operand
                        ops[i - k] = " " # Leave the space blank
                    elif ops[i - k] == "^" or ops[i - k] == "*" or ops[i - k] == "/" or ops[i - k] == "+" or ops[i - k] == "-":
                        print("Incorrect Syntax")
                        exit()

                # Find the remaining ints to the right and set it to our b operand
                right = range((len(ops) - 1) - i) 
                for j in right: # loop through the list to find an int
                    if type(ops[i + j]) is int: # If we have one then 
                        b = ops[i + j] # assign it to the b variable
                        ops[i + j] = " " # make the space empty
                    elif ops[i + j] == "^" or ops[i + j] == "*" or ops[i + j] == "/" or ops[i + j] == "+" or ops[i + j] == "-":
                        print("Incorrect Syntax")
                        exit()

                c = a * b
                ops[i] = c
                ops[i - 1] = " "
                ops[i + 1] = " "
                i = 0

        for i in range(len(ops)):
            if ops[i] == "/":
                # Find the remaning ints to the left and set it to our a operand
                left = range((len(ops) - 1) - ((len(ops) - 1) - i))
                for k in left: # Go through the list from the current index to the left most item in the index
                    if type(ops [i - k]) is int: # If the item we are currently on is an int
                        a = ops[i - k] # Then set it to the a operand
                        ops[i - k] = " " # Leave the space blank
                    elif ops[i - k] == "^" or ops[i - k] == "*" or ops[i - k] == "/" or ops[i - k] == "+" or ops[i - k] == "-":
                        print("Incorrect Syntax")
                        exit()

                # Find the remaining ints to the right and set it to our b operand
                right = range((len(ops) - 1) - i) 
                for j in right: # loop through the list to find an int
                    if type(ops[i + j]) is int: # If we have one then 
                        b = ops[i + j] # assign it to the b variable
                        ops[i + j] = " " # make the space empty
                    elif ops[i + j] == "^" or ops[i + j] == "*" or ops[i + j] == "/" or ops[i + j] == "+" or ops[i + j] == "-":
                        print("Incorrect Syntax")
                        exit()
                c = a / b
                ops[i] = c
                ops[i - 1] = " "
                ops[i + 1] = " "

        for i in range(len(ops)):
            if ops[i] == "+":
                # Find the remaning ints to the left and set it to our a operand
                left = range((len(ops) - 1) - ((len(ops) - 1) - i))
                for k in left: # Go through the list from the current index to the left most item in the index
                    k + 1
                    if type(ops [i - k]) is int: # If the item we are currently on is an int
                        a = ops[i - k] # Then set it to the a operand
                        ops[i - k] = " " # Leave the space blank
                    elif ops[i - k] == "^" or ops[i - k] == "*" or ops[i - k] == "/" or ops[i - k] == "+" or ops[i - k] == "-":
                        print("Incorrect Syntax left +")
                        exit()

                # Find the remaining ints to the right and set it to our b operand
                right = range((len(ops) - 1) - i) 
                for j in right: # loop through the list to find an int
                    j + 1
                    if type(ops[i + j]) is int: # If we have one then 
                        b = ops[i + j] # assign it to the b variable
                        ops[i + j] = " " # make the space empty
                    elif ops[i + j] == "^" or ops[i + j] == "*" or ops[i + j] == "/" or ops[i + j] == "+" or ops[i + j] == "-":
                        print("Incorrect Syntax right +")
                        exit()
                c = a + b
                ops[i] = c
                ops[i - 1] = " "
                ops[i + 1] = " "
                
        for i in range(len(ops)):
            if ops[i] == "-":
                # Find the remaning ints to the left and set it to our a operand
                left = range((len(ops) - 1) - ((len(ops) - 1) - i))
                for k in left: # Go through the list from the current index to the left most item in the index
                    if type(ops [i - k]) is int: # If the item we are currently on is an int
                        a = ops[i - k] # Then set it to the a operand
                        ops[i - k] = " " # Leave the space blank
                    elif ops[i - k] == "^" or ops[i - k] == "*" or ops[i - k] == "/" or ops[i - k] == "+" or ops[i - k] == "-":
                        print("Incorrect Syntax")
                        exit()

                # Find the remaining ints to the right and set it to our b operand
                right = range((len(ops) - 1) - i) 
                for j in right: # loop through the list to find an int
                    if type(ops[i + j]) is int: # If we have one then 
                        b = ops[i + j] # assign it to the b variable
                        ops[i + j] = " " # make the space empty
                    elif ops[i + j] == "^" or ops[i + j] == "*" or ops[i + j] == "/" or ops[i + j] == "+" or ops[i + j] == "-":
                        print("Incorrect Syntax")
                        exit()
                c = a - b
                ops[i] = c
                ops[i - 1] = " "
                ops[i + 1] = " "
                
    
    print(ops)
    print(noParen)

if __name__ == "__main__":
    pass
