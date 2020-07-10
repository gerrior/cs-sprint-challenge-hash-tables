def has_negatives(a):
    result = [] # arrray
    input = {} # dictionary 

    # convert to dictionary
    # Value is True if negative number found. 
    for number in a:
        if number in input:
            if number < 0:
                input[abs(number)] = True
        else:
            if number < 0:
                input[abs(number)] = True
            else: 
                input[number] = False


    for theValue, foundNegative in input.items():
        if foundNegative == True:
            result.append(theValue)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
