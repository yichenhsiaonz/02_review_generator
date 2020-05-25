
import math
import csv


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
            else:
                return user_input

            input_loop = 1
        except ValueError:
            print("Only numbers!!!")

    return user_input

# Converted XLSX into CSV files so that they can be opened by python

genres = open("02_genres.csv")
adjectives = open("02_adjectives.csv")

csv_genres = csv.reader(genres)
csv_adjectives = csv.reader(adjectives)

# Asks for the rating of the book, recycled

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
        break

    if genre_group == "":

        # Cycles through the dictionary and sets the genre group attached to the genre if the input matches a genre name
        # on the list

        for x in range(len(genre_dict)):
            if genre_dict[str(x + 1)][0] == selected_genre:
                genre_group = genre_dict[str(x + 1)][1]
                break
        else:
            print("Please enter one of the options!!!")
adjective_list = []

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

for x in csv_adjectives:
    if x[1] == "0" or x[1] == genre_group:
        if x[0] in rating_adjectives:
            adjective_list.append(x[2])
for x in adjective_list:
    print(x)
