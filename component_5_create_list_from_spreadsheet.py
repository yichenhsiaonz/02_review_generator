# Component 9 and 10.

import csv

genres = open("02_genres.csv")

csv_genres = csv.reader(genres)

genre_dict = {}

for row in csv_genres:
    genre_dict[row[1]] = [row[0], row]
genre_dict.pop("Source: https://gladreaders.com/types-or-genres-of-books/")
genre_dict.pop("all")
x = 1
for key in genre_dict:
    print(str(x).zfill(2), ": ", key.capitalize())
    x += 1
input("Please select one of the genres above by typing the number or name listed.")
