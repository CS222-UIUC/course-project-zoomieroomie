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

print("START OF THE TRIAL!!!")
arr1 = ["John", 20, "Science", "North quad", "Evening"]
arr1rm = [18, "Science", "North quad", "Evening"]

arr2 = ["Jane", 18, "Entertainment", "South quad", "Morning"]
arr2rm = [20, "Entertainment", "South quad", "Evening"]

arr3 = ["Pete", 24, "Economic", "North quad", "Evening"]
arr3rm = [22, "Science", "North quad", "Afternoon"]

arr4 = ["Abby", 22, "Science", "Main quad", "Noon"]
arr4rm = [18, "Entertainment", "North quad", "Midnight"]

person1 = Person(arr1, arr1rm)
person2 = Person(arr2, arr2rm)
person3 = Person(arr3, arr3rm)
person4 = Person(arr4, arr4rm)
p_arr = [person1, person2, person3, person4]

# use the calculate_distance method to calculate the distance between the two people
person1.set_time("Morning")
distance = person1.distance(person4)
print(f"The distance between {person1.get_name()} and {person4.get_name()} is {distance:.2f}.")

for p in p_arr:
    best_w_p = p.find_best(p_arr)
    print("Best for "+p.get_name()+" is "+best_w_p.get_name()+" with "+str(p.distance(best_w_p)))
