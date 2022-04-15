#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: March 31, 2022
# This program asks the user to enter a year, and it will 
# check if it is a leap year or not


import random
import math


def main():
    # Get the year
    user_input_string = input("Enter a year: ")
    print("")

    # check if it is a leap year or not
    try:
        user_input = int(user_input_string)

        year_by_4 = user_input % 4
        year_by_100 = user_input % 100
        year_by_400 = user_input % 400

        if year_by_4 == 0:
            if (year_by_100 == 0) and (year_by_400 == 0):
                print("It's a leap year!!")
            elif year_by_100 != 0:
                print("It's a leap year!!")
            else:
                print("It's not a leap year!")
        else:
            print("It's not a leap year!")

    except Exception:
        print("That is not a number!!")


if __name__ == "__main__":
    main()
