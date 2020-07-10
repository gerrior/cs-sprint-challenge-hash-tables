# Your code here



def finder(files, queries):
    result = [] # arrray
    store = {} # dictionary 

    # convert to dictionary
    for path in files:
        pathAndFilename = path.rsplit("/", 1)
        if pathAndFilename[1] in store:
            # We've got a colision 
            store[pathAndFilename[1]] = store[pathAndFilename[1]] + ":" + pathAndFilename[0]
        else:
            # First time we've seen this filename 
            store[pathAndFilename[1]] = pathAndFilename[0]
    
    for candidate in queries: 
        if candidate in store:
            result.append(store[candidate] + "/" + candidate)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/application/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
