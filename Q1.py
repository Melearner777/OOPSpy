'''n,a,b=map(int,  input().split())

def possible_positions(n, a, b):
    # Calculate the range of possible positions
    min_position = max(1, a + 1)
    max_position = min(n - b, n)
    
    # Calculate the number of possible positions
    num_possible_positions = max_position - min_position + 1
    
    return num_possible_positions



# Calculate the number of possible positions for Mani
result = possible_positions(n,a,b)
print(result)'''
# Input
n, a, b = map(int, input().split())

def possible_positions(n, a, b):
    min_position = a 
    max_position = n  -1- b
    return min_position-max_position + 2


# Calculate the number of possible positions for Mani
result = possible_positions(n, a, b)

# Output the result
print(result)
