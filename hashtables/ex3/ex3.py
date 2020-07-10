def intersection(arrays):
    result = [] # arrray
    input = {} # dictionary 
    numOfArrays = len(arrays) # Does compiler not optimize this without assignment?

    # convert to dictionary
    for array in arrays:
        for number in array: 
            if number in input:
                # already in dictionary; increament that we've seen it again
                input[number] += 1
            else:
                # Add to dictionary
                input[number] = 1

    
    for number, count in input.items():
        if count == numOfArrays:
            result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
