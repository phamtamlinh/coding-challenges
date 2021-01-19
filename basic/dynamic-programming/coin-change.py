# https://www.geeksforgeeks.org/understanding-the-coin-change-problem-with-dynamic-programming/

def getNumberOfWays(N, Coins): 
  
    # Create the ways array to 1 plus the amount 
    # to stop overflow 
    ways = [0] * (N + 1)
  
    # Set the first way to 1 because its 0 and 
    # there is 1 way to make 0 with 0 coins 
    ways[0] = 1
  
    # Go through all of the coins 
    for i in range(len(Coins)): 
  
        # Make a comparison to each index value 
        # of ways with the coin value. 
        print("Coins[i]", Coins[i])
        for j in range(len(ways)): 
            if (Coins[i] <= j):
                print("j", j, "ways[j]", ways[j])
                print("ways[(int)(j - Coins[i])]", ways[(int)(j - Coins[i])])
  
                # Update the ways array 
                ways[j] += ways[(int)(j - Coins[i])]
        print(ways)
  
    # return the value at the Nth position 
    # of the ways array. 
    return ways[N]

Coins = [2, 3, 7]

print(getNumberOfWays(12, Coins))