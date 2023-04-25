# Write a Python program that read a file containing the name of 20 students together with their GWA.
# The program will outputs the name of the student who got the highest GWA (including the GWA).

import time
import pyfiglet
from colorama import Back

# create stud_dict and gwa_list
stud_dict = {}
gwa_list = []

# create list of colors for font
yellow = '\033[93m'
red = '\033[91m'
white = '\033[97m'
green = '\033[92m'
blue = '\033[94m'
cyan = '\033[96m'
colors = [red, green, yellow, white]


def find_highest():
    # open list_of_studs.txt
    with open('list_of_studs.txt') as stud_list:
        # read list_of_studs.txt by line
        for line in stud_list:
            # get name and gwa
            name_gwa = line.strip().split(',')
            name = name_gwa[0]
            gwa = name_gwa[-1]
            # store name and gwa in dict
            stud_dict[name] = gwa
            # store gwa in list for comparison
            gwa_list.append(gwa)

        # get highest gwa in gwa_list
        for grade in gwa_list:
            highest = gwa_list[0]
            if grade > highest:
                highest = grade

        # search for name of stud with highest gwa in stud_dict
        for name, gwa in stud_dict.items():
            if gwa == highest:
                # print out result
                print(f'The student with the highest GWA is {name} with a total average of {gwa.strip()}.')


find_highest()
