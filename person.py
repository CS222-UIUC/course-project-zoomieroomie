import math

class Person:
    def __init__(self, name, age, major, place_preference, time):
        self.name = name
        self.age = age
        self.major = major #Major in UIUC, Need to find a way to translate into different score
        self.place_preference = place_preference #North, south, etc., Need to find a way to translate into different score
        self.time = time #Most active, Need to find a way to translate into different score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_major(self):
        return self.major

    def get_place_preference(self):
        return self.place_preference

    def get_time(self):
        return self.time

    def set_name(self, n):
        self.name = n

    def set_age(self, a):
        self.age = a

    def set_major(self, m):
        self.major = m

    def set_place_preference(self, p):
        self.place_preference = p

    def set_time(self, t):
        self.time = t

    #Euclidean distance
    def distance(self, other_person):
        age_diff = abs(self.age - other_person.get_age())
        #Need better classification instead of 0 and 1
        major_diff = 0 if self.major == other_person.get_major() else 1
        place_diff = 0 if self.place_preference == other_person.get_place_preference() else 1
        time_diff = 0 if self.time == other_person.get_time() else 1
        #Actual formula
        distance = math.sqrt(age_diff ** 2 + major_diff ** 2 + place_diff ** 2 + time_diff ** 2)
        return distance
    
    #Find best possible roomate given the array of all person
    def find_best(self, person_array):
        best_person = None
        best_distance = float('inf')
        for person in person_array:
            if person is self:
                continue
            distance = self.distance(person)
            if distance < best_distance:
                best_person = person
                best_distance = distance
        return best_person
    

