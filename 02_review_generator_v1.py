
import math
import csv
import random


def return_title(question, condition):

    input_loop = ""
    while input_loop == "":

        user_input = input(question)

        # returns anonymous if no author name entered

        if condition == 1 and user_input.strip() == "":
            return "Anonymous"

        # does not allow for blanks when not asking for author

        elif user_input.strip() == "":
            print("Enter something!!!")

        # returns everything else

        else:
            return user_input


def return_input(question):

    input_loop = ""
    while input_loop == "":
        try:

            user_input = float(input(question))

            if user_input == "":
                print("Enter something!!!")
            elif user_input > 5:
                return 5
            elif user_input < 1:
                return 1
            elif user_input % 1 != 0:
                rounding_loop = ""
                while rounding_loop == "":
                    rounding = input("Would you like to round up or down?: ")
                    if rounding == "up":
                        user_input = math.ceil(user_input)
                        rounding_loop = 1
                    elif rounding == "down":
                        user_input = math.floor(user_input)
                        rounding_loop = 1
                    else:
                        print("Please enter \"up\" or \"down!!!\"")

            return user_input

        except ValueError:
            print("Only numbers!!!")


def pick_skeleton(skeleton_group):
    rng_number = random.randint(1, 2)
    adjective1 = random.choice(adjective_list)
    adjective2 = random.choice(adjective_list)
    if adjective1[0] != adjective2[0]:
        conjunction = "but"
    else:
        conjunction = "and"
    if skeleton_group == 1:
        if rng_number == 1:
            return ["{} {} {}, {} is {}.", [adjective1[2], conjunction, adjective2[2], title, summary]]
        else:
            setting = input("Where does the book take place?")
            return ["Set in {}, {} is the story of {}.", [setting, title, summary]]
    else:
        if rng_number == 1:
            return ["{}, {} has created a {} {}.", [adjective1[2], author, adjective2[2], "{} novel".format(genre)]]
        else:

            # detecting if a word needs a / an is difficult due to all the exceptions to the rule so I will only an
            # if it starts with a vowel even if this is sometimes untrue

            vowels = ["a", "e", "i", "o", "u"]
            if adjective1[0] in vowels:
                conjunction = "an"
            else:
                conjunction = "a"

            adjective2 = random.choice(feeling_list)

            print("1. Male\n2. Female\n3. Other")
            pronoun = ""
            while pronoun == "":
                gender = input("What gender is the author?")
                if gender == 1 or gender == "male":
                    pronoun = "he"
                elif gender == 2 or gender == "female":
                    pronoun = "she"
                elif gender == 3 or gender == "other":
                    pronoun = "other"
                else:
                    print("Enter a valid choice !!!")

            return ["{}	has written {} {} {} which "
                    "will {} both {} fans and first-time "
                    "readers.", [author, conjunction, adjective1[2], genre, adjective2[2], pronoun]]


def fill_skeleton(sentence, list1, list2):
    adjective1 = random.choice(list1)
    adjective2 = random.choice(list2)
    return [sentence, [adjective1[2], adjective2[2]]]


def edit_sentence(sentence):
    edit_loop = ""
    while edit_loop == "":
        final_sentence = sentence[0].format(*sentence[1])
        print(final_sentence)
        print("would you like to change anything?")
        for y in range(len(sentence[1])):
            print(y + 1, ":", sentence[1][y])
        edit = input("Please enter a number to edit it or <enter> to exit")
        if edit.isnumeric() is True:
            edit = int(edit)
            if 1 <= edit <= len(sentence[1]):
                edit -= 1
                sentence[1][int(edit)] = input("what would you like to change it to?")

            else:
                print("Enter a valid option !!!")
        elif edit == "":
            return final_sentence
        else:
            print("Enter a valid option !!!")


# Converted xlsx into CSV files so that they can be opened by python

genres = open("02_genres.csv")
adjectives = open("02_adjectives.csv")

csv_genres = csv.reader(genres)
csv_adjectives = csv.reader(adjectives)

# Asks for the rating of the book, recycled
# condition of 0 shows that program isn't asking for author
title = return_title("Please enter the title: ", 0)

# condition of 1 shows that program is asking for author
author = return_title("Please enter the author: ", 1)

rating = return_input("Please enter the rating: ")

# Creates a dictionary that retains the order of the rows from spreadsheet by assigning numbers as the key to make
# it easy to print in the same order the entries were added since this version of python doesn't retain the order
# of dictionaries

# Dictionary contains the name of the genre and the adjective group used for the genre

genre_dict = {}
numbering = -1
for row in csv_genres:
    genre_dict[str(numbering)] = [row[1].lower(), row[0]]
    numbering += 1

# Removes irrelevant lines in the spreadsheet since I didn't want to edit the spreadsheet

genre_dict.pop("-1")
genre_dict.pop("0")

# Prints all options with padding zeroes for readability

for x in range(len(genre_dict)):
    print(str(x+1).zfill(2), ": ", genre_dict[str(x+1)][0])

# Searches for the user input as a key in the dictionary or as the value for name
# Converts to lower case and strips padding zeroes to increase the number of valid inputs

genre_group = ""
while genre_group == "":
    selected_genre = ((input("Please select one of the genres above by "
                             "typing the number or name listed: ")).lower()).lstrip("0")

    # Sets the genre group to the entry attached to the key if the key is found

    if selected_genre in genre_dict.keys():
        genre_group = genre_dict[selected_genre][1]
        genre = genre_dict[selected_genre][0]
        break

    if genre_group == "":

        # Cycles through the dictionary and sets the genre group attached to the genre if the input matches a genre name
        # on the list

        for x in range(len(genre_dict)):
            if genre_dict[str(x + 1)][0] == selected_genre:
                genre_group = genre_dict[str(x + 1)][1]
                genre = genre_dict[str(x + 1)][0]
                break
        else:
            print("Please enter one of the options!!!")

# Sets tags allowed for adjectives based on the rating given by user

if rating == 3:
    rating_adjectives = ["neutral"]
elif rating == 4:
    rating_adjectives = ["neutral", "positive"]
elif rating == 2:
    rating_adjectives = ["neutral", "negative"]
elif rating == 5:
    rating_adjectives = ["positive"]
else:
    rating_adjectives = ["negative"]

# Finds all adjectives that fit either all genre groups or fit the selected genre group that have either the
# positive, neutral, or negative tag based on the rating provided by the user

adjective_list = []
feeling_list = []
overall_list = []
book_is_list = []
ending_list = []
underlying_story_list = []
writing_style_list = []

for x in csv_adjectives:
    if x[0] in rating_adjectives:
        if x[1] == "0" or x[1] == genre_group:
            adjective_list.append(x)
        if x[1] == "14":
            feeling_list.append(x)
        if x[1] == "13":
            overall_list.append(x)
        if x[1] == "12":
            book_is_list.append(x)
        if x[1] == "11":
            ending_list.append(x)
        if x[1] == "10":
            underlying_story_list.append(x)
        if x[1] == "9":
            writing_style_list.append(x)

summary = input("summary?")
if summary != "":
    sentence_1 = pick_skeleton(1)
else:
    sentence_1 = ["{} is both {} and {}", [title, random.choice(adjective_list), random.choice(adjective_list)]]

final_sentence_1 = edit_sentence(sentence_1)

sentence_2 = pick_skeleton(2)

final_sentence_2 = edit_sentence(sentence_2)

sentence_3 = fill_skeleton("The writing style is {} and this makes the book {}.", writing_style_list, book_is_list)

final_sentence_3 = edit_sentence(sentence_3)

sentence_4 = fill_skeleton("The underlying story is {} and the ending is {}", underlying_story_list, ending_list)

final_sentence_4 = edit_sentence(sentence_4)

sentence_5 = fill_skeleton("Overall, I <adjective> this book and would <recommend / not recommend> it to others.<title> deserves a <rating> star rating.  Ultimately it was a / an <adjective> novel which was <worth / not worth> readingThis is <rating.5> stars rounded <up / down> because <reason for rating>")

print(final_sentence_1)
print(final_sentence_2)
print(final_sentence_3)
print(final_sentence_4)
