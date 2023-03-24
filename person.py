'''The Person Class'''

import math

class Person:
    '''Simple implementation of the class'''
    def __init__(self, name, age, major, place, time):
        self.name = name
        self.age = age
        self.major = major #Major in UIUC, Need to find a way to translate into different score
        self.place = place #North, etc., Need to turn into different score
        self.time = time #Most active, Need to find a way to translate into different score

    def get_name(self):
        '''Getter for name'''
        return self.name

    def get_age(self):
        '''Getter for age'''
        return self.age

    def get_major(self):
        '''Getter for major'''
        return self.major

    def get_place(self):
        '''Getter for place'''
        return self.place

    def get_time(self):
        '''Getter for time'''
        return self.time

    def set_name(self, new_name):
        '''Setter for name'''
        self.name = new_name

    def set_age(self, new_age):
        '''Setter for age'''
        self.age = new_age

    def set_major(self, new_major):
        '''Setter for major'''
        self.major = new_major

    def set_place(self, new_place):
        '''Setter for place'''
        self.place = new_place

    def set_time(self, new_time):
        '''Setter for time'''
        self.time = new_time

    def distance(self, other_person):
        '''Euclidean distance'''
        age_diff = abs(self.age - other_person.get_age())
        #Need better classification instead of 0 and 1
        major_diff = 0 if self.major == other_person.get_major() else 1
        place_diff = 0 if self.place == other_person.get_place() else 1
        time_diff = 0 if self.time == other_person.get_time() else 1
        #Actual formula
        distance = math.sqrt(age_diff ** 2 + major_diff ** 2 + place_diff ** 2 + time_diff ** 2)
        return distance
    
    def find_best(self, person_array):
        '''Find best possible roomate given the array of all person'''
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
    