#TODO Refactor the logic function since we 
# changed the noParen boolean to a parameter
def calc(ops,noParen):
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
                    print("Incorrect Syntax")
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
                    print("Incorrect Syntax")
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
                    print("Incorrect Syntax")
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
                    print("Incorrect Syntax")
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
                    print("Incorrect Syntax")
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
                    print("Incorrect Syntax")
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
                    print("Incorrect Syntax")
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
                    print("Incorrect Syntax")
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
                    print("Incorrect Syntax")
                    exit()

            c = a - b
            ops[i] = c
            ops[i - 1] = " "
            ops[i + 1] = " "
    if noParen is True:
        for i in ops: # Check every item in the list
            if type(i) is int: # If that item is an int
                print("Your answer is: " + str(i)) # Then print it
                exit() # and exit
    elif noParen is False:
        for i in ops:
            if type(i) is int:
                return i
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
    ops = []
    #TODO Rename this variable
    d = [] # This will be the parethesis array

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

    if eq.count("(") != 0 or eq.count(")") != 0:

        noParen = False # We have parenthesis
        # Count the number of parenthesis if this is the case
        leftPar = eq.count("(")
        rightPar = eq.count(")")

        if leftPar == rightPar:
            print("Parenthesis code")
            # Plan:
            # We could find the equation in the innermost parethesis
            # then calculate the answer return it and continue until
            # we have answers within parenthesis. Then we remove all 
            # of the parenthesis and plug that into the calc function
            #
            # Problems:
            # After we make sure that we have an equal amount of parenthesis
            # then we only have to worry about how they are formatted within
            # the equation. We should be able to develop something that matches
            # right parenthesis with left parenthesis. 
            print(eq)
            for i in range(len(eq)):# Go through the indexes of items within the eq list
                if eq[i] == ")": # If we find a right parenthesis
                    # We can reuse this code from the calc function 
                    # to find parenthesis to the left
                    left = range(((len(eq) - 1) - ((len(eq) - 1) - i) + 1))
                    for j in left: # Then we search the list
                        if eq[i - j] == "(": # We look for the left parenthesis
                            k = (i - j) + 1 # We don't want to append the left parenthesis to the equation
                            while eq[k] != ")": # While we aren't on a right parenthesis
                                d.append(eq[k]) #Append the values to a new list
                                k += 1 # Increment the variable for finding indexes
                                print(d) # TEST CODE
                            # TODO Rename this variable too
                            e = calc(d,noParen=False) # Then calculate the answer to the equation within the parenthesis
                            eq[i - j] = e # Replace the left with the answer
                            #eq[i] = " " # Delete the right parenthesis
                            # I wonder if we should just make this into a function
                            # or keep going with these nested loops. Let's try the
                            # latter
                            print(eq) # TEST CODE
                            for l in range(len(eq)): # Go through the equation again
                                #TODO this if is not working correctly
                                if eq[l] == "(" or eq[l] == ")": # If we find a parenthesis
                                    break # Then break out of the for loop
                                else: # Otherwise
                                    try: 
                                        eq[l + 1] = " " # Try to empty out the rest of the variables skipping over the first index
                                    except: # We'll run into an out of bounds error
                                        pass # So we'll pass
                            print(eq)
        
        else:
            print("Invalid input of parenthesis")
    else:
        noParen = True

    if noParen is True:
        calc(eq,noParen=True)

if __name__ == "__main__":
    logic()
