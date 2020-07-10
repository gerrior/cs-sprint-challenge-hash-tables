def get_indices_of_item_weights(weights, length, limit):

    weightTable = {} # dictionary 
    indexTable = {} # dictionary 

    # convert to dictionaries
    index = 0

    for item in weights:
        weightTable[item] = limit - item
        indexTable[item] = index
        index += 1
    
    # find the two weights
    for item in weights:
        if weightTable[item] in weightTable:
            if weightTable[item] > item:
                a = indexTable[weightTable[item]]
                b = indexTable[item]
                return (a, b)
            else:
                return (indexTable[item], indexTable[weightTable[item]])

    return None

if __name__ == "__main__":

    weights_2 = [4, 4]
    answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
    print(answer_2) # (1, 0)

    # weights_3 = [4, 6, 10, 15, 16]
    # answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
    # print(answer_3) # (3, 1)
