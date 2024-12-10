import json
import random
from datetime import datetime

currentYear = datetime.now().year

def getAge():
    while True:
        try:
            age = int(input("Please enter your Age: "))
            if age < 0:
                raise ValueError("Age cannot be negative. Who are you trying to fool?")
            elif age > 120:
                raise ValueError("Uh huh,trying out boundaries are we?")
            return age
        except ValueError as e:
            print(f"Invalid input: {e} . Please try again!")

def openJSON():
    with open ('feelOld\movies.json', 'r', encoding='utf-8') as file:
        movieData = json.load(file)
        return movieData
    
def chooseMovie(age, movieData):
    movieRange = (currentYear-age)+random.randint(0, 3)
    foundMovie = [movie['film'] for movie in movieData if movie['jahr'] == movieRange]
    return movieRange, foundMovie

def output(movieRange, foundMovie):
    movieAge = currentYear-movieRange
    if movieAge < 6:
        print(f"Did you realize that {', '.join(foundMovie)} came out less than half a decade ago?")
    elif movieAge < 12:
        print(f"Did you realize that {', '.join(foundMovie)} came out more than half a decade ago?")
    elif movieAge < 15:
        print(f"Did you realize that {', '.join(foundMovie)} came out not last decade but the one before that?")
    elif movieAge < 20:
        print(f"Did you realize that {', '.join(foundMovie)} came out {movieAge} years ago?")
    elif movieRange < 1969:
        print(f"Did you realize that {', '.join(foundMovie)} came out closer to the moon landing than today's day?")
    else:
        print(f"Did you realize that {', '.join(foundMovie)} came out {movieAge} years ago?")

def main():
    age = getAge()
    movieData = openJSON()
    movieRange, foundMovie = chooseMovie(age, movieData)
    output(movieRange, foundMovie)
main()