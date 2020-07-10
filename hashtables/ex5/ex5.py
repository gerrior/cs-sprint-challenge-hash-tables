# Your code here



def finder(files, queries):
    filename = 1
    directory = 0

    result = [] # arrray
    filestore = {} # dictionary 

    # convert to dictionary
    for path in files:
        pathAndFilename = path.rsplit("/", 1)
        if pathAndFilename[1] in filestore:
            # We've got a colision 
            filestore[pathAndFilename[1]] = filestore[pathAndFilename[1]] + ":" + pathAndFilename[0]
        else:
            # First time we've seen this filename 
            filestore[pathAndFilename[1]] = pathAndFilename[0]
    
    for candidate in queries: 
        if candidate in filestore:
            paths = filestore[candidate].split(":", 1)
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
