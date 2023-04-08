'''The Person Class'''

import math

class Person:
    '''Simple implementation of the class'''
    def __init__(self, arr_acc, arr_self, arr_rm):
        self.name = arr_acc[0]
        self.age = arr_acc[1]
        self.mail = arr_acc[2]
        self.password = arr_acc[3]
        self.info = arr_self
        self.ideal_rm = arr_rm

    # GETTER
    def get_name(self):
        '''Getter for name'''
        return self.name

    def get_age(self):
        '''Getter for age'''
        return self.age

    def get_mail(self):
        '''Getter for mail'''
        return self.mail

    def get_password(self):
        '''Getter for password'''
        return self.password

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

    def set_mail(self, new_mail):
        '''Setter for mail'''
        self.mail = new_mail

    def set_password(self, new_pass):
        '''Setter for password'''
        self.password = new_pass

    # ALGORITHM
    def numberize(self, arr, type_arr):
        '''Turn info into number'''
        weight = []
        answer = []
        if type_arr == "self": # Self Info
            weight = [2, 3, 4, 3, 2]
            answer = [["often", "sometimes", "never"], ["often", "sometimes", "never"],
                    ["1", "2", "3", "4", "5"],
                    ["straight", "gay", "bisexual", "other", "prefer not to say"],
                    ["cisgender", "transgender", "other", "prefer not to say"]]
        else: # Roommate form
            weight = [2, 4, 6, 1, 2]
            answer = [["yes", "no", "maybe"], ["yes", "no", "maybe"], ["1", "2", "3", "4", "5"],
                      ["yes", "no"], ["yes", "no"]]

        for i, val in enumerate(arr):
            if val in answer[i]:
                arr[i] = weight[i] * (answer[i].index(val) + 1)
        return arr

    def euclidean(self, arr1, arr2):
        '''Helper for distance()'''
        arr_1 = self.numberize(arr1, "self")
        arr_2 = self.numberize(arr2, "rm")

        if len(arr1) != len(arr2):
            raise ValueError("Arrays must have the same length.")

        squared_distance = 0
        for i, val in enumerate(arr_1):
            squared_distance += (val - arr_2[i]) ** 2
        return math.sqrt(squared_distance)

    def distance(self, other):
        '''Euclidean distance'''
        dis1to2 = self.euclidean(self.info, other.get_ideal_rm())
        dis2to1 = self.euclidean(other.get_info(), self.ideal_rm)
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
    