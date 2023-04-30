"""The Person Class"""
import math
from .models import User, Preferences

# When calculating compatability, self's arr2 will be calc w other's arr3, and vice versa.
# Then, the 2 distance will be average and that is the final score.


class Person:
    """Class to hold user's info and calculate the weighted euclidean distance between 2 Persons"""

    def __init__(self, user: User):
        """Initialize the Person object with user info and preferences"""

        # Retrieve user's preferences from the database
        prefs = user.preference

        # Save user info and preferences to object attributes
        self.email = user.email
        self.password = user.password
        self.firstname = user.firstname
        self.lastname = user.lastname
        self.info = {
            "smoke": prefs.smoke,
            "drink": prefs.drink,
            "extrovert": prefs.extrovert,
            "study": prefs.study,
            "sleep": prefs.sleep,
            "bedtime_school": prefs.bedtime_school,
            "bedtime_weekend": prefs.bedtime_weekend,
            "messy": prefs.messy,
            "guests": prefs.guests,
            "sexuality": prefs.sexuality,
            "gender": prefs.gender,
        }
        self.ideal_rm = {
            "l_smoke": prefs.l_smoke,
            "l_drink": prefs.l_drink,
            "l_extrovert": prefs.l_extrovert,
            "study": prefs.study,
            "sleep": prefs.sleep,
            "bedtime_school": prefs.bedtime_school,
            "bedtime_weekend": prefs.bedtime_weekend,
            "l_messy": prefs.l_messy,
            "guests": prefs.guests,
            "l_sexuality": prefs.l_sexuality,
            "l_gender": prefs.l_gender,
        }

    # GETTER
    def get_email(self):
        """Getter for username"""
        return self.email

    def get_first(self):
        """Getter for first name"""
        return self.firstname

    def get_last(self):
        """Getter for lastname"""
        return self.lastname

    def get_password(self):
        """Getter for password"""
        return self.password

    def get_info(self):
        """Getter for self's info"""
        return self.info

    def get_ideal_rm(self):
        """Getter for ideal rm array"""
        return self.ideal_rm

    # SETTER
    def set_email(self, new_name):
        """Setter for name"""
        self.email = new_name

    def set_first(self, new_first):
        """Setter for age"""
        self.firstname = new_first

    def set_last(self, new_last):
        """Setter for mail"""
        self.lastname = new_last

    def set_password(self, new_pass):
        """Setter for password"""
        self.password = new_pass

    # ALGORITHM
    def distance(self, other: "Person") -> float:
        """Calculates the weighted euclidean distance between self and other"""

        # Check that preferences have the same keys
        assert self.ideal_rm.keys() == other.info.keys()
        assert self.info.keys() == other.ideal_rm.keys()

        # Calculate distance
        distance = 0
        dis1 = 0
        dis2 = 0
        for key in self.info.items():
            dis1 += (self.ideal_rm[key] - other.info[key]) ** 2
            dis2 += (self.info[key] - other.ideal[key]) ** 2
            distance = (math.sqrt(dis1) + math.sqrt(dis2)) / 2

        if (self.ideal_rm["l_smoke"] == 1 and other.info["smoke"] > 4) or (
            self.ideal_rm["l_drink"] == 1 and other.info["drink"] > 4
        ):
            distance += 1000

        if (self.ideal_rm["l_extrovert"] == 1 and other.info["extrovert"] > 4) or (
            self.ideal_rm["l_messy"] == 1 and other.info["messy"] > 4
        ):
            distance += 1000

        if (
            self.ideal_rm["l_sexuality"] == 1
            and other.info["sexuality"] != self.info["sexuality"]
        ) or (
            self.ideal_rm["l_gender"] == 1
            and other.info["gender"] != self.info["gender"]
        ):
            distance += 1000

        return distance

    def find_best(self, person_array):
        """Find best possible roomate given the array of all person"""
        best_person = None
        best_distance = float("inf")
        for person in person_array:
            if person is self:
                continue
            distance = self.distance(person)
            if distance < best_distance:
                best_person = person
                best_distance = distance
        return best_person


# class Person:
#     """Simple implementation of the class"""

#     def __init__(self, arr_acc, arr_self, arr_rm):
#         self.username = arr_acc[0]
#         self.password = arr_acc[1]
#         self.first = arr_acc[2]
#         self.last = arr_acc[3]
#         self.info = arr_self
#         self.ideal_rm = arr_rm

#     # GETTER
#     def get_username(self):
#         """Getter for username"""
#         return self.username

#     def get_first(self):
#         """Getter for first name"""
#         return self.first

#     def get_last(self):
#         """Getter for lastname"""
#         return self.last

#     def get_password(self):
#         """Getter for password"""
#         return self.password

#     def get_info(self):
#         """Getter for self's info"""
#         return self.info

#     def get_ideal_rm(self):
#         """Getter for ideal rm array"""
#         return self.ideal_rm

#     # SETTER
#     def set_username(self, new_name):
#         """Setter for name"""
#         self.username = new_name

#     def set_first(self, new_first):
#         """Setter for age"""
#         self.first = new_first

#     def set_last(self, new_last):
#         """Setter for mail"""
#         self.last = new_last

#     def set_password(self, new_pass):
#         """Setter for password"""
#         self.password = new_pass

#     # ALGORITHM

#     def euclidean(self, arr1, arr2):
#         """Helper for distance()"""
#         if len(arr1) != len(arr2):
#             raise ValueError("Arrays must have the same length.")

#         squared_distance = 0
#         for i, val in enumerate(arr1):
#             squared_distance += (val - arr2[i]) ** 2
#         return math.sqrt(squared_distance)

#     def distance(self, other):
#         """Euclidean distance"""
#         dis1to2 = self.euclidean(self.info, other.get_ideal_rm())
#         dis2to1 = self.euclidean(other.get_info(), self.ideal_rm)
#         return (dis1to2 + dis2to1) / 2

#     def find_best(self, person_array):
#         """Find best possible roomate given the array of all person"""
#         best_person = None
#         best_distance = float("inf")
#         for person in person_array:
#             if person is self:
#                 continue
#             distance = self.distance(person)
#             if distance < best_distance:
#                 best_person = person
#                 best_distance = distance
#         return best_person
