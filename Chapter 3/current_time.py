''' This script tells you the current time.'''

import datetime

# get the current time
curr_time = datetime.datetime.now().time() # this part is a bit tricky

# print only if script is to be executed
if __name__ == "__main__":
    print(curr_time)