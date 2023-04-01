'''Testing file for the person class'''
from person import Person

# create 4 Person instances
# Algorithm Update: Every person has 2 arrays, arr1 for self info, and arr2 for ideal roomate.

# When calculating compatability, self's arr1 will be calc w other's arr2, and vice versa.
# Then, the 2 distance will be average and that is the final score.

# Arr format: name, age, major, place to live, active time.
# Name: not important in the calculatioin
# Age: minimum important
# Major: realtive important w/ Science(CS, ECE, etc), Economic, Entertainment(Art, Sport, etc.)
# Place: very important North quad = 500, Main quad = 300, South quad = 100
# Active time: (Morning = 10, Noon = 20, Afternoon = 30, Evening = 40, Midnight = 50)

def process_csv(csv_line, num):
    '''Analyze the line and give an array'''
    # extract the first x items of the line into a list
    # arr1: account info, arr2: self info, arr3: prefered roommate info
    arr1 = csv_line.split(", ")[:num]
    # initialize two empty lists for the remaining items
    arr2 = []
    arr3 = []

    # iterate through the remaining items and distribute them alternately
    for i, item in enumerate(csv_line.split(", ")[num:]):
        if i % 2 == 1:
            arr2.append(item)
        else:
            arr3.append(item)

    return arr1, arr2, arr3

print("START OF THE TRIAL!!!")
CVS1 = "John, 20, gmail, joemama10, yes, often, yes, sometimes, 3, 3, yes, straight, no, cisgender"
CVS2 = "Jane, 18, uiuc, minecraft, no, sometimes, maybe, sometimes, 2, 5, no, gay, yes, transgender"
CVS3 = "Pete, 24, gmail, northern, no, never, maybe, sometimes, 5, 1, no, bisexual, no, other"
CVS4 = "Abby, 22, uiuc, 123456789, no, never, yes, sometimes, 4, 3, yes, other, yes, other"

info1, self1, rm1 = process_csv(CVS1, 4)
person1 = Person(info1, self1, rm1)

info2, self2, rm2 = process_csv(CVS2, 4)
person2 = Person(info2, self2, rm2)

info3, self3, rm3 = process_csv(CVS3, 4)
person3 = Person(info3, self3, rm3)

info4, self4, rm4 = process_csv(CVS4, 4)
person4 = Person(info4, self4, rm4)

p_arr = [person1, person2, person3, person4]

# use the calculate_distance method to calculate the distance between the two people
distance = person1.distance(person4)
print(f"The distance between {person1.get_name()} and {person4.get_name()} is {distance:.2f}.")

for p in p_arr:
    best_w_p = p.find_best(p_arr)
    print("Best for "+p.get_name()+" is "+best_w_p.get_name()+" with "+str(p.distance(best_w_p)))
