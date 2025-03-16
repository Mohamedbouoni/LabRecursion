def minCoins(N, coins, memo):
    if N == 0:
        return 0
    
    if N < 0:
        return -1
    if N in memo:
        return memo[N]

    if len(coins) == 0:
        return -1

    include = minCoins(N - coins[-1], coins, memo)  
    exclude = minCoins(N, coins[:-1], memo)  

    if include == -1 and exclude == -1:
        result = -1  
    elif include == -1:
        result = exclude  
    elif exclude == -1:
        result = 1 + include  
    else:
        result = min(1 + include, exclude)  
    
    memo[N] = result
    return result

n = int(input("Enter number of coins: "))
coins = []

print(f"Enter {n} coin values (e.g., 0.5, 1.25, 2.75):")
for i in range(n):
    while True:
        try:
            value = float(input(f"Element {i+1}: "))
            if value <= 0:
                print("Please enter a positive number!")
                continue
            coins.append(int(value * 100))  # Convert to cents
            break
        except ValueError:
            print("Please enter a valid number!")

# Ensure N is positive
while True:
    try:
        N = float(input("Enter the amount to change: "))
        if N <= 0:
            print("Please enter a positive amount!")
            continue
        N = int(N * 100)  # Convert amount to cents
        break
    except ValueError:
        print("Please enter a valid number!")

# Initialize memoization dictionary
memo = {}

# Call the memoized minCoins function
result = minCoins(N, coins, memo)

# Output the result
if result == -1:
    print("\nChange cannot be made with given coins.")
else:
    print(f"\nMinimum coins needed: {result}")
