#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = [] # arrray
    itinerary = {} # dictionary 

    # convert to dictionary
    for ticket in tickets:
        itinerary[ticket.source] = ticket.destination

    # Find the first airport
    airport = itinerary["NONE"]

    # do while in python
    # Build route until we get to NONE
    while True: 
        route.append(airport)

        if airport == "NONE":
            break

        airport = itinerary[airport]

    return route
