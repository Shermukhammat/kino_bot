from fuzzywuzzy import process


chose = {1 : "Kino 1", 12 : "Kino 2", 15 : "Kino 3", 40 : "Kino 4", 50 : "Kino 5", 60 : "Kino 6"}


extract = process.extract("kino 3", chose, limit = 3)
print(extract)