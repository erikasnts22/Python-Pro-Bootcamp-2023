print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

t = name1.lower().count("t") + name2.lower().count("t")
r = name1.lower().count("r") + name2.lower().count("r")
u = name1.lower().count("u") + name2.lower().count("u")
e = name1.lower().count("e") + name2.lower().count("e")

l = name1.lower().count("l") + name2.lower().count("l")
o = name1.lower().count("o") + name2.lower().count("o")
v = name1.lower().count("v") + name2.lower().count("v")
e = name1.lower().count("e") + name2.lower().count("e")

true = (t + r + u + e)
love = (l + o + v + e)
love_score = str(true) + str(love)

love_score = int(love_score)

# love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

#Solution 2

# combined_string = name1 + name2
# lower_case_strting = combined_string.lower()

# t = lower_case_strting.count("t")
# and so on..


#NOTES
# Program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.