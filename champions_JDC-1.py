#! /usr/bin/env python3
#Jonathan Christopher
#Created 7/7/2019
#Mod 12 Champions Counter

def winning_teams():
    # read file 
    with open("world_cup_champions.txt","r") as champs:
        lines = champs.readlines()

    # init dict
    dict_values = {}

    # process
    for line in lines[1:]:
        year    = line.split(",")[0]
        country = line.split(",")[1]        
        coach   = line.split(",")[2]
        captain = line.split(",")[3]     

        # fill in dict
        if not(country in dict_values.keys()):
            dict_values[country] = [[year, coach, captain]]
        else: 
            dict_values[country].append([year, coach, captain])

    # sorting dictionaries
    sorted_list = sorted(dict_values.items(), key=lambda x: x[0])

    # printing
    for country, values in sorted_list:
        years    = [value[0] for value in values]
        coaches  = [value[1] for value in values]
        captains = [value[2] for value in values]
        print(" " + country.ljust(15) \
              + " " + str(len(years)).ljust(8) + " "  \
              + str(years).replace('[', "").replace(']', "").replace("'", ""))


def main():
    print("FIFA World Cup Winners")
    print()
    print(" Country".ljust(14) + " Wins".center(8)  + "Years".rjust(9))
    print("{:15} {:9} {:}".format("="*7, "="*4, "="*5))
    winning_teams()


if __name__ == "__main__":
    main()
