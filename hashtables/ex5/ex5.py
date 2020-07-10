# Your code here



def finder(files, queries):
    result = [] # arrray
    store = {} # dictionary 

    # convert to dictionary
    for path in files:
        x = path.rsplit("/", 1)
        store[x[1]] = x[0]
    
    for candidate in queries: 
        if candidate in store:
            result.append(store[candidate] + "/" + candidate)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
