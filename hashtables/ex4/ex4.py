def has_negatives(a):
    result = [] # arrray
    input = {} # dictionary 

    # convert to dictionary
    # I was just going to test if True but the problem is I don't know the order the + and - will come in. 
    for number in a:
        if abs(number) in input:
            # already in dictionary
            if number < 0:
                if input[abs(number)] == "+":
                    input[abs(number)] = "+-"
            else: 
                if input[number] == "-":
                    input[number] = "+-"
        else:
            # Add to dictionary
            if number < 0:
                input[abs(number)] = "-"
            else: 
                input[number] = "+"


    for theValue, wereBothFound in input.items():
        if wereBothFound == "+-":
            result.append(theValue)

    return result


if __name__ == "__main__":
#    print(has_negatives([1,2,3,-4]))
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
