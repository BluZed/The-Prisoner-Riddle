'''
============================================================
============================================================

- The Prisoner Riddle
- Explanation: Veritasium - https://www.youtube.com/watch?v=iSNsgj1OCLA

: Program by BluZed#9413

============================================================
============================================================
'''
from random import shuffle

    
# simple creates a list containing numbers from 1 to the number of prisoners
def create_list():
    newlist = []
    for i in range(1,num_of_prisoners+1,1):
        newlist.append(i)
    return newlist

# simulates a prisoner checking the boxes
def simulate_prisoner(prisoner_num,boxes):
    last = prisoner_num
    tried = 0
    max_tries = num_of_prisoners/2
    while(tried < max_tries+1):
        tried+=1
        current_box_num = boxes[last]
        if(current_box_num==prisoner_num):
            return True
        else:
            last = current_box_num
    return False

# starts the experiment *shrug*
def start_experiment(boxes):
    for prisoner_num in range(1,num_of_prisoners+1,1):
        successfully_found_num = simulate_prisoner(prisoner_num,boxes)
        if(successfully_found_num is not True):
            return False
    return True


print('''\n
===========================================================
===========================================================

- The Prisoner Riddle
- Explanation: Veritasium - https://www.youtube.com/watch?v=iSNsgj1OCLA

: Program by BluZed#9413
\n''')
      
num_of_iterations = int(input("  Enter the Number of Iterations:\t"))
num_of_prisoners = int(input("  Enter the Number of Prisoners:\t"))

print("\n > Running the Experiment...")

boxes = create_list()
successes = 0
faliures = 0
for e in range(num_of_iterations):
    shuffle(boxes) # randomly shuffles the numbers "inside" the boxes 
    boxes.insert(0,"temp") # add an element to the 0th index of the list so that the boxes are mapped from 1 to n instead of 0 to (n-1) 
    result = start_experiment(boxes)
    if(result == True):
        successes += 1
    else:
        faliures += 1
    boxes.pop(0) # removes the element at the first position  that was purposefully added so that it does not got shuffled in the next iteration and cause innocent "execution"

print(" > Experiment finished.")

Success_Percent = (successes/num_of_iterations)*100
Faliure_Percent = 100-Success_Percent

print('''
  {} Iteration(s) resulted in the following:
  Success: {}% ({} in {})
  Faliure: {}% ({} in {})
\n
===========================================================
===========================================================
'''.format(num_of_iterations,Success_Percent,successes,num_of_iterations,Faliure_Percent,faliures,num_of_iterations))
