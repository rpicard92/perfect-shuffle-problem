import time

def simulate(deckSize):

    #Create the Deck
    def createDeck(start, array):
        #Create the 50 Card Deck
        cardNum = 1
        while cardNum <= deckNum:
            start.append(cardNum)
            array.append(cardNum)
            cardNum = cardNum + 1  
        return [start,array]

    #Perform a Perfect Shuffle
    def perfectShuffle(array):    

        #Split into an upper and lower deck
        upperHalf = []
        lowerHalf = []
        index = 1
        for num in array:
            if index <= middle:
                upperHalf.append(num)
            elif index > middle:
                lowerHalf.append(num)
            index = index + 1

        #print 'UPPER_HALF: ' + str(upperHalf)
        #print 'LOWER_HALF: ' + str(lowerHalf)

        #Fill in every other index with upperHalf
        index = 1    
        for numUpper in upperHalf:
            array[index] = numUpper
            index = index + 2

        #Fill in every other index with lowerHalf    
        index = 0
        for numLower in lowerHalf:
            array[index] = numLower
            index = index + 2

        #print 'CURRENT_SHUFFLE: ' + str(lowerHalf)
        return array

    # deckSize must be an even number
    if deckSize % 2 == 0:

        #Initialize Shuffle Count
        count = 0

        #Number of cards used
        deckNum = deckSize - 2

        #If there are middle cards
        if deckNum != 0:

            #Find lower-middle of the deck
            middle = deckNum/2
            start = []
            array = []
            count = 0

            #Create the deck
            [start,array] = createDeck(start,array)        

            #First Shuffle
            array = perfectShuffle(array)
            count = count + 1

            #Continue Shuffling Until A Solution is Reached
            while start != array:
                array = perfectShuffle(array)
                count = count + 1

        timeElapsed = time.time() - startTime

        print "FOR '" + str(deckSize) + "' CARDS THE SOLUTION IS '" + str(count) + "' PERFECT SHUFFLES |" " SIMULATION_TIME: '" + str(timeElapsed) + "' SECONDS."

    else:

        print ""
        print "The deck must be an even number."
        print ""
 

# Set Simulation Size
simulateTo = 1000
startTime = time.time()

# Run simulation for specified number of deck sizes
for run in range(0, simulateTo):
    if run % 2 == 0 and run != 0:
        simulate(run)