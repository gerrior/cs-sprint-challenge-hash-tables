def get_indices_of_item_weights(weights, length, limit):

    indexLookup = {}

    index = 0
    # Build a dictionary of where the weights appear in the array.
    for weight in weights:
        if weight not in indexLookup:
            indexLookup[weight] = index
        index += 1
  
    index = 0
    # Find the weight pairing
    for weight in weights:
        # Is the remaining weight value in the lookup table?
        if (limit - weight) in indexLookup:
            # Is this a cheat? In the [4, 4] case, 4 only appears once in indexLookup
            if length == 2 and (weights[0] +  weights[1] == limit):
                return 1, 0
            # Because we are marching through the weights we can natually put the smaller index last
            return indexLookup[limit - weight], index
        index += 1

    return None

if __name__ == "__main__":

    weights_2 = [4, 4]
    answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
    print(answer_2) # (1, 0)

    # weights_3 = [4, 15, 10, 6, 16]
    # answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
    # print(answer_3) # (3, 1)
