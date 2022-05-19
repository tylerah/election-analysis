counties = ["Arapahoe", "Denver", "Jefferson"]

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson":432438}


# this lists the items in the list
for county in counties:
    print(county)


# this gets the keys of the dictionary
for county in counties_dict:
    print(county)


# this gets the values of the dictionary
for voters in counties_dict.values():
    print(voters)


# this gets the values of the key/value pair
for county in counties_dict:
    print(counties_dict.get(county))


# these two do the same thing
for key, value in counties_dict.items():
    print(key, value)

for county, voters in counties_dict.items():
    print(county, voters)

# the "placeholder1" refers to the key and the "placeholder2" refers to the value
# by using this for loop, it establishes each key and value in the dictionary as a part of this variable
# the next line is the output of the variables we just acquired
# placeholder2 is an integer in the dictionary, thus we have to convert it to a string for it to display
for placeholder1, placeholder2 in counties_dict.items():
    print((placeholder1) + " county has " + str(placeholder2) + " registered voters.")



