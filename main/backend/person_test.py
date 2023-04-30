"""Testing file for the person class"""
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from models import User, Preferences
from person import Person

# Create 4 Person instances
# Update: Every person has 3 arrays, arr1 for acc, arr2 for self info, arr3 for ideal roomate.

# # create an engine that connects to the database file
# engine = create_engine("sqlite:///users.db")

# # create a session factory
# Session = sessionmaker(bind=engine)

# # create a session object
# session = Session()

# # retrieve all users from the database
# users = session.query(User).all()

# user_data = []

# for user in users:
#     # extract the user data into an array
#     acc_info = [user.username, user.password, user.firstname, user.lastname]

#     # turn the preferences into arrays (one for 'l_', and one for the rest)
#     rm_arr = [
#         getattr(user.preferences, col)
#         for col in Preferences.__table__.columns.keys()
#         if col.startswith("l_")
#     ]
#     self_arr = [
#         getattr(user.preferences, col)
#         for col in Preferences.__table__.columns.keys()
#         if not col.startswith("l_")
#     ]

#     person = Person(acc_info, self_arr, rm_arr)
#     # add the user data and preference data to the nested user array
#     user_data.append(person)

# # close the session
# session.close()


def process_csv(csv_line, num):
    """Analyze the line and give an array"""
    # extract the first x items of the line into a list
    # arr1: account info, arr2: self info, arr3: prefered roommate info
    arr1 = csv_line.split(",")[:num]
    # initialize two empty lists for the remaining items
    arr2 = []
    arr3 = []

    # iterate through the remaining items and distribute them alternately
    for i, item in enumerate(csv_line.split(",")[num:]):
        if i % 2 == 1:
            arr2.append(int(item))
        else:
            arr3.append(int(item))

    return arr1, arr2, arr3


print("START OF THE TRIAL!!!")
CVS1 = "John12,ddddd,John,Ngu,1,3,1,2,5,9,4,3,4,4,5,6,7,1,7,5,5,1"
CVS2 = "Jane23,ccccc,Jane,Doe,4,9,2,6,3,8,2,4,2,8,2,4,3,4,2,1,4,3"
CVS3 = "Pete23,bbbbb,Pete,Ngu,5,2,3,7,8,6,1,7,1,2,5,2,9,3,4,1,7,2"
CVS4 = "Abby69,aaaaa,Abby,Sta,7,5,7,2,4,3,5,6,5,1,3,3,1,1,5,3,9,5"

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
print(
    f"The distance between {person1.get_username()} and {person4.get_username()} is {distance:.2f}."
)

for p in p_arr:
    best_w_p = p.find_best(p_arr)
    print(
        "Best for "
        + p.get_username()
        + " is "
        + best_w_p.get_username()
        + " with "
        + str(p.distance(best_w_p))
    )
