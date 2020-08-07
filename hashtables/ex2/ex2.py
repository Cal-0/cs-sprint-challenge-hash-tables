#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    cache = {}
    route = []

    for i in tickets:
        cache[i.source] = i.destination

    next_dest = cache['NONE']

    for i in range(length):
        route.append(next_dest)
        next_dest = cache[next_dest]

    return route