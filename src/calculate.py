def calc(ops):
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

    # These will act as our two operands and c as our sum/product/difference/etc.
    a = 0
    b = 0
    c = 0

    for i in range(len(ops)):
        if ops[i] == "^":
            # Find the remaning ints to the left and set it to our a operand and add one because
            # for loops do not run the last item in a range
            left = range(((len(ops) - 1) - ((len(ops) - 1) - i) + 1)) 
            for k in left: # Go through the list from the current index to the left most item in the index
                if type(ops [i - k]) is int: # If the item we are currently on is an int
                    a = ops[i - k] # Then set it to the a operand
                    ops[i - k] = " " # Leave the space blank
                    break # Break so that we don't print an error when we've already found the operand
                elif (ops[i - k] == "^" or ops[i - k] == "*" or ops[i - k] == "/" or ops[i - k] == "+" or ops[i - k] == "-") and ops.index(ops[i - k ]) != ops.index(ops[i]):
                    print("Incorrect Syntax left ^")
                    exit()

            # Find the remaining ints to the right and set it to our b operand and add one because
            # for loops do not the run the last item in a range
            right = range((((len(ops) - 1) - i) + 1)) 
            for j in right: # loop through the list to find an int
                if type(ops[i + j]) is int: # If we have one then 
                    b = ops[i + j] # assign it to the b variable
                    ops[i + j] = " " # make the space empty
                    break # Break so that we don't print an error when we already found the operand
                elif (ops[i + j] == "^" or ops[i + j] == "*" or ops[i + j] == "/" or ops[i + j] == "+" or ops[i + j] == "-") and ops.index(ops[i + j]) != ops.index(ops[i]):
                    print("Incorrect Syntax right ^")
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

        # We need to go through each operator with
        # a for loop
    for i in range(len(ops)):
        if ops[i] == "*":
            # Find the remaning ints to the left and set it to our a operand and add one because
            # for loops do not run the last item in a range
            left = range(((len(ops) - 1) - ((len(ops) - 1) - i) + 1)) 
            for k in left: # Go through the list from the current index to the left most item in the index
                if type(ops [i - k]) is int: # If the item we are currently on is an int
                    a = ops[i - k] # Then set it to the a operand
                    ops[i - k] = " " # Leave the space blank
                    break # Break so that we don't print an error when we've already found the operand
                elif (ops[i - k] == "^" or ops[i - k] == "*" or ops[i - k] == "/" or ops[i - k] == "+" or ops[i - k] == "-") and ops.index(ops[i - k ]) != ops.index(ops[i]):
                    print("Incorrect Syntax left ^")
                    exit()

            # Find the remaining ints to the right and set it to our b operand and add one because
            # for loops do not the run the last item in a range
            right = range((((len(ops) - 1) - i) + 1)) 
            for j in right: # loop through the list to find an int
                if type(ops[i + j]) is int: # If we have one then 
                    b = ops[i + j] # assign it to the b variable
                    ops[i + j] = " " # make the space empty
                    break # Break so that we don't print an error when we already found the operand
                elif (ops[i + j] == "^" or ops[i + j] == "*" or ops[i + j] == "/" or ops[i + j] == "+" or ops[i + j] == "-") and ops.index(ops[i + j]) != ops.index(ops[i]):
                    print("Incorrect Syntax right ^")
                    exit()

            c = a * b
            ops[i] = c
            ops[i - 1] = " "
            ops[i + 1] = " "

    for i in range(len(ops)):
        if ops[i] == "/":
            # Find the remaning ints to the left and set it to our a operand and add one because
            # for loops do not run the last item in a range
            left = range(((len(ops) - 1) - ((len(ops) - 1) - i) + 1)) 
            for k in left: # Go through the list from the current index to the left most item in the index
                if type(ops [i - k]) is int: # If the item we are currently on is an int
                    a = ops[i - k] # Then set it to the a operand
                    ops[i - k] = " " # Leave the space blank
                    break # Break so that we don't print an error when we've already found the operand
                elif (ops[i - k] == "^" or ops[i - k] == "*" or ops[i - k] == "/" or ops[i - k] == "+" or ops[i - k] == "-") and ops.index(ops[i - k ]) != ops.index(ops[i]):
                    print("Incorrect Syntax left ^")
                    exit()

            # Find the remaining ints to the right and set it to our b operand and add one because
            # for loops do not the run the last item in a range
            right = range((((len(ops) - 1) - i) + 1)) 
            for j in right: # loop through the list to find an int
                if type(ops[i + j]) is int: # If we have one then 
                    b = ops[i + j] # assign it to the b variable
                    ops[i + j] = " " # make the space empty
                    break # Break so that we don't print an error when we already found the operand
                elif (ops[i + j] == "^" or ops[i + j] == "*" or ops[i + j] == "/" or ops[i + j] == "+" or ops[i + j] == "-") and ops.index(ops[i + j]) != ops.index(ops[i]):
                    print("Incorrect Syntax right ^")
                    exit()

            c = a / b
            ops[i] = c
            ops[i - 1] = " "
            ops[i + 1] = " "

    for i in range(len(ops)):
        if ops[i] == "+":
            # Find the remaning ints to the left and set it to our a operand and add one because
            # for loops do not run the last item in a range
            left = range(((len(ops) - 1) - ((len(ops) - 1) - i) + 1)) 
            for k in left: # Go through the list from the current index to the left most item in the index
                if type(ops [i - k]) is int: # If the item we are currently on is an int
                    a = ops[i - k] # Then set it to the a operand
                    ops[i - k] = " " # Leave the space blank
                    break # Break so that we don't print an error when we've already found the operand
                elif (ops[i - k] == "^" or ops[i - k] == "*" or ops[i - k] == "/" or ops[i - k] == "+" or ops[i - k] == "-") and ops.index(ops[i - k ]) != ops.index(ops[i]):
                    print("Incorrect Syntax left ^")
                    exit()

            # Find the remaining ints to the right and set it to our b operand and add one because
            # for loops do not the run the last item in a range
            right = range((((len(ops) - 1) - i) + 1)) 
            for j in right: # loop through the list to find an int
                if type(ops[i + j]) is int: # If we have one then 
                    b = ops[i + j] # assign it to the b variable
                    ops[i + j] = " " # make the space empty
                    break # Break so that we don't print an error when we already found the operand
                elif (ops[i + j] == "^" or ops[i + j] == "*" or ops[i + j] == "/" or ops[i + j] == "+" or ops[i + j] == "-") and ops.index(ops[i + j]) != ops.index(ops[i]):
                    print("Incorrect Syntax right ^")
                    exit()

            c = a + b
            ops[i] = c
            ops[i - 1] = " "
            ops[i + 1] = " "
            
    for i in range(len(ops)):
        if ops[i] == "-":
            # Find the remaning ints to the left and set it to our a operand and add one because
            # for loops do not run the last item in a range
            left = range(((len(ops) - 1) - ((len(ops) - 1) - i) + 1)) 
            for k in left: # Go through the list from the current index to the left most item in the index
                if type(ops [i - k]) is int: # If the item we are currently on is an int
                    a = ops[i - k] # Then set it to the a operand
                    ops[i - k] = " " # Leave the space blank
                    break # Break so that we don't print an error when we've already found the operand
                elif (ops[i - k] == "^" or ops[i - k] == "*" or ops[i - k] == "/" or ops[i - k] == "+" or ops[i - k] == "-") and ops.index(ops[i - k ]) != ops.index(ops[i]):
                    print("Incorrect Syntax left ^")
                    exit()

            # Find the remaining ints to the right and set it to our b operand and add one because
            # for loops do not the run the last item in a range
            right = range((((len(ops) - 1) - i) + 1)) 
            for j in right: # loop through the list to find an int
                if type(ops[i + j]) is int: # If we have one then 
                    b = ops[i + j] # assign it to the b variable
                    ops[i + j] = " " # make the space empty
                    break # Break so that we don't print an error when we already found the operand
                elif (ops[i + j] == "^" or ops[i + j] == "*" or ops[i + j] == "/" or ops[i + j] == "+" or ops[i + j] == "-") and ops.index(ops[i + j]) != ops.index(ops[i]):
                    print("Incorrect Syntax right ^")
                    exit()

            c = a - b
            ops[i] = c
            ops[i - 1] = " "
            ops[i + 1] = " "

    for i in ops: # Check every item in the list
        if type(i) is int: # If that item is an int
            print("Your answer is: " + str(i)) # Then print it
            exit() # and exit
    # We should not see this since we exit early but if we don't have any ints in
    # the list then this will be printed
    print("Answer not found")

def logic(): # This handles setting up the equation before we run it through the calc function

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
    #print(eq)
    ops = []
    noParen = True


    for i in range(len(eq)):
        if eq[i] == "^" or eq[i] == "*" or eq[i] == "+" or eq[i] == "-" or eq[i] == "/" or eq[i] == "(" or eq[i] == ")" or eq[i] == " ":
            pass
        else: 
            try:
                eq[i] = int(eq[i])

            except ValueError:
                    print("Invalid input")
                    exit()

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
        calc(eq)
    else: 
        print("We have parenthesis")
        

if __name__ == "__main__":
    logic()
