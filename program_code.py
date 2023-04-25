# Write a Python program that read a file containing the name of 20 students together with their GWA.
# The program will outputs the name of the student who got the highest GWA (including the GWA).


def find_highest():
    # open list_of_studs.txt
    with open('list_of_studs.txt') as stud_list:
        # read list_of_studs.txt by line
        for line in stud_list:
            # get name and gwa
            name_gwa = line.strip().split(',')
            name = name_gwa[0]
            gwa = name_gwa[-1]
            print(name_gwa)
            # store name and gwa in dict
            # store gwa in list for comparison
            # get highest gwa in gwa_list
            # search for name of stud with highest gwa in stud_dict
            # print out result


find_highest()
