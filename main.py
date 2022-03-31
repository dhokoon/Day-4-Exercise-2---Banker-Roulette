import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_people = len(names)

random_person = random.randint(0, total_people - 1)

choice_payer = names[random_person]

print(f'{choice_payer} is going to buy he meal today!')

