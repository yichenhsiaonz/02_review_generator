# Component 9 and 10.

import csv

genres = open("02_genres.csv")

csv_genres = csv.reader(genres)

genre_dict= {}

for row in csv_genres:
    genre_dict[row[1]] = row[0]
genre_dict.pop("Source: https://gladreaders.com/types-or-genres-of-books/", None)
for key in genre_dict:
    print(key, ":", genre_dict[key])
