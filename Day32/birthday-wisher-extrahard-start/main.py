##################### Extra Hard Starting Project ######################
import datetime as dt
import random

# 1. Update the birthdays.csv
now = dt.datetime.now()

# 2. Check if today matches a birthday in the birthdays.csv
with open("birthdays.csv") as bd:
    birth = bd.readlines()

for i in range(1, len(birth)):
    birthday = birth[i].split(',')
    if int(birthday[3]) == now.month and int(birthday[4]) == now.day:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        idx = random.randint(1, 3)
        with open(f"letter_templates/letter_{idx}.txt") as lt:
            letter = lt.read()
            new_letter = letter.replace("[NAME]", birthday[0])
            print(new_letter, end='\n\n\n')
# 4. Send the letter generated in step 3 to that person's email address.
