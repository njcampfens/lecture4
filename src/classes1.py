# We create a flight class
class Flight:
    # We define the contructor method
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

def main():

    # create af Flight
    f = Flight(origin='New York', destination='Paris', duration=540)

    #change the value of a variable
    f.duration += 10

    # Print details about Flight
    print(f.origin)
    print(f.destination)
    print(f.duration)


# Start of the programm
if __name__ == '__main__':
    main()


#
