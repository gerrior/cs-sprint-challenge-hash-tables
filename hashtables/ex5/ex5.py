# Your code here



def finder(files, queries):
    filename = 1
    directory = 0

    result = [] # arrray
    filenameDict = {} # dictionary 

    # convert to dictionary
    for path in files:
        split = path.rsplit("/", 1)
        if split[filename] in filenameDict:
            # We've got a colision 
            filenameDict[split[filename]] = filenameDict[split[filename]] + ":" + split[directory]
        else:
            # First time we've seen this filename 
            filenameDict[split[filename]] = split[directory]
    
    for candidate in queries: 
        if candidate in filenameDict:
            paths = filenameDict[candidate].split(":", 1)
            for path in paths:
                result.append(path + "/" + candidate)

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
