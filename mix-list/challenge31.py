#! usr/bin/python3

import random

wordbank= ["indentation", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

max_num = len(tlgstudents)

num = int(input(f"Enter a number from 1-{max_num}: "))

student_name = tlgstudents.pop(num)

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

random_num = random.randint(1,max_num)
print("This is a random name:", tlgstudents[random_num])
