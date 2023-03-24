'''Testing file for the person class'''
from person import Person

# create 4 Person instances
print("START OF THE TRIAL!!!")
arr1 = ["John", 25, "Computer Science", "North quad", "Evenings"]
arr2 = ["Jane", 18, "Engineering", "South quad", "Mornings"]
arr3 = ["Pete", 98, "Crop Science", "North quad", "Evenings"]
arr4 = ["Abbonegracho", 22, "Engineering", "South quad", "Evenings"]

person1 = Person(*arr1)
person2 = Person(*arr2)
person3 = Person(*arr3)
person4 = Person(*arr4)
p_arr = [person1, person2, person3, person4]

# use the calculate_distance method to calculate the distance between the two people
distance = person1.distance(person4)
print(f"The distance between {person1.get_name()} and {person4.get_name()} is {distance:.2f}.")

for p in p_arr:
    best_w_p = p.find_best(p_arr)
    print("Best for "+p.get_name()+" is "+best_w_p.get_name()+" with "+str(p.distance(best_w_p)))
