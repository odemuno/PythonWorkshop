''' This script runs sorting algorithms for a list'''

# Bubble Sort - simple but inefficient -> O(n^2)
# l: list

def bubblesort(l):
    # indicator to stop looping through the list
    still_swapping = True
    
    # start the loop
    while still_swapping:
        still_swapping = False # once while loop is false, it terminates
        for i in range(len(l) - 1):
            # swapping condition
            if l[i] > l[i+1]: # if current is bigger than next, swap them
                l[i], l[i+1] = l[i+1], l[i]
                still_swapping = True # just swapped so need to enter while loop again after for loop
    
    # check the result
    return(l)
                
    