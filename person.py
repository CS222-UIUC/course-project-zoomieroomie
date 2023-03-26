'''The Person Class'''

import math

class Person:
    '''Simple implementation of the class'''
    def __init__(self, arr_self, arr_rm):
        self.name = arr_self[0]
        self.age = arr_self[1]
        self.major = arr_self[2] #Major in UIUC, turn into different score
        self.place = arr_self[3] #North, etc., turn into different score
        self.time = arr_self[4] #Most active, turn into different score
        self.info = self.numberize(arr_self[1:]) #Array w/o name
        self.ideal_rm = self.numberize(arr_rm)

    # GETTER
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

    def get_info(self):
        '''Getter for self's info'''
        return self.info

    def get_ideal_rm(self):
        '''Getter for ideal rm array'''
        return self.ideal_rm

    # SETTER
    def set_name(self, new_name):
        '''Setter for name'''
        self.name = new_name

    def set_age(self, new_age):
        '''Setter for age'''
        self.age = new_age
        self.info[0] = new_age

    def set_major(self, new_major):
        '''Setter for major'''
        self.major = new_major
        self.info[1] = new_major
        self.info = self.numberize(self.info)

    def set_place(self, new_place):
        '''Setter for place'''
        self.place = new_place
        self.info[2] = new_place
        self.info = self.numberize(self.info)

    def set_time(self, new_time):
        '''Setter for time'''
        self.time = new_time
        self.info[3] = new_time
        self.info = self.numberize(self.info)

    # ALGORITHM
    def numberize(self, arr):
        '''Turn info into number'''
        #Major
        if arr[1] == "Science":
            arr[1] = 100
        elif arr[1] == "Entertainment":
            arr[1] = 300
        elif arr[1] == "Economic":
            arr[1] = 200
        #Place
        if arr[2] == "North quad":
            arr[2] = 500
        elif arr[2] == "Main quad":
            arr[2] = 300
        elif arr[2] == "South quad":
            arr[2] = 100
        #Time
        if arr[3] == "Morning":
            arr[3] = 10
        elif arr[3] == "Noon":
            arr[3] = 20
        elif arr[3] == "Afternoon":
            arr[3] = 30
        elif arr[3] == "Evening":
            arr[3] = 40
        elif arr[3] == "Midnight":
            arr[3] = 50
        return arr

    def euclidean(self, arr1, arr2):
        '''Helper for distance()'''
        if len(arr1) != len(arr2):
            raise ValueError("Arrays must have the same length.")
        squared_distance = 0
        for i, val in enumerate(arr1):
            squared_distance += (val - arr2[i]) ** 2
        return math.sqrt(squared_distance)

    def distance(self, other):
        '''Euclidean distance'''
        dis1to2 = self.euclidean(self.info, other.get_ideal_rm())
        dis2to1 = self.euclidean(self.ideal_rm, other.get_info())
        return (dis1to2 + dis2to1)/2

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
    