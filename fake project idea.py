# import the randomm module
import random

# create subject
subjects = [
    "Math",
    "Science",
    "English"
     "Mumbai",
     "Pune",
     "Bangalore" ,
     "prime minister"
]

actions = [
    "play",
    "run",
    "study",
    "joining",
    "eating",
    "hungry",
]

places_or_things = [
    "mumbai vadapav",
    "pune misal pav",
    "bangalore dosa",
    "mumbai local train",
    "Agra fort",
    "taj mahal",
]

# start the headling genatator loop
while True:
    subject = random .choice(subjects)
    action = random.choice(actions)
    place_or_things = random.choice(places_or_things)

    headline = f"{subject} {action} {place_or_things}"
    print("\n"+ headline )

    user_input = input("\n""Do you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
     break
      
#print goodbye message
print("thanks for using the headline generator!")
print("have a good day ahead")