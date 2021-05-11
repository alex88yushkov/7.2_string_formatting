# Exercise #1
# Create a program that will output everything in lowercase whatever the user will input.
# The program should run until the client enters the word “STOP”.
enter = ""
while enter != "STOP":
    print("Enter any uppercase word or 'STOP' for quit")
    enter = input()
    print(enter, "->", enter.lower())

# Exercise #2
# You have a dictionary {'Jake': '$100K', 'Anand': '$120K'}.
# Using the string formatting print what salaries every person has.
dic = {'Jake': '$100K', 'Anand': '$120K'}
print("Jake = {Jake}, Anand = {Anand}".format(**dic))

# Exercise #3
# Given a 5 element tuple: (4, 30, 2017, 2, 27). Using the string formatting print: '2 27 2017 4 30'
# Hint! use index numbers to specify positions.
tup = (4, 30, 2017, 2, 27)
print("{} {} {} {} {}".format(tup[3], tup[4], tup[2], tup[0], tup[1]))