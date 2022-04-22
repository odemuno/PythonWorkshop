''' This script runs search algorithms for a list'''

# Linear Search - simple but inefficient -> O(n)
# l: list
# s: item to search for

def linearsearch(l, s):
    result = -1 # if search was unsuccessful, it stays as this
    
    # loop
    for i in range(len(l)):
        if s == l[i]:
            result = i
            break # exit loop
    
    return(i)


# Binary Search
# l: list
# s: item to search for

def binarysearch(l, s):
    # variables for the start and end of the sublist
    slice_start = 0
    slice_end = len(l) - 1
    
    # variable to check if search was successful
    found = False
    
    # find midpoint of list
    while slice_start <= slice_end and not found:
        mid = (slice_start + slice_end) // 2
        # if value at mid is what we are searching for, we have found it
        if l[mid] == s:
            found = True
        # re-slice the sublist
        else: 
            if s < l[mid]:
                slice_end = mid - 1
            else:
                slice_start = mid + 1
                
    return found, mid