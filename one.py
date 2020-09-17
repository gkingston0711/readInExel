# -*- coding: utf- 8 -*-
import csv
# from csv import reader # I do not need to do csv.reader
def explore_data(data, start, end):
    count = start
    while count <= end:
        print data[count]
        count += 1
    # Print the number of row, and colum
    print('Number of rows:', end-start+1)
    print('Number of column: ', len(data[start]))


def find_entry(data, name):
    name = name.lower()
    for row in data:
        Row = row[0].lower()
        if name == Row:
            print row


def check(data, name):
    for row in data:
        if row[0] == name:
            return True
    return False

def filter_entry(data):
    # Return 2 list containing duplicate_apps, and unique_apps
    duplicate_apps = []
    unique_apps = []

    for row in data:
        name = row[0]
        if check(unique_apps, name) == True:
            duplicate_apps.append(row)
        else:
            unique_apps.append(row)


    return duplicate_apps, unique_apps

def createReview(data):
    # Return the dictionary, with maximum review if they have duplicate entries
    appDict = {}

    for row in data:
        if row[0] in appDict:
            if row[3] >= appDict[row[0]]:
                appDict[row[0]] = row[3]
        else:
            appDict[row[0]] = row[3]

    return appDict


def check_english(name):
    # return True if name is all english letter
    # return False if name contain at least one non english letter

    for char in name:
        if ord(char) > 127:

            return False


    return True


def createNonEnglishApps(data):
    non_english_apps = []

    for line in data:
        if check_english(line[0]) == False:
            non_english_apps.append(line)

    return non_english_apps

def createEnglishApps(data):
    english_apps = []

    for line in data:
        if check_english(line[0]) == True:
            english_apps.append(line)

    return english_apps

def freq_table(data, index):
    # Function to generate the frequency tables that show percentages
    # Return dictionary based on index
    # For example, index =1, I populate the dictionary for column1
    # index = 0, I populate the dictionary for column 0

    Dictionary = {}

    for info in data:
        if info[index] in Dictionary:
            Dictionary[info[index]] += 1
        else:
            Dictionary[info[index]] = 1


    # Len = len(data)
    #go through each value in dictionary and weigh it against Len to give me a percentage
    #stor inside of new dictionary, using key and new key and percentage as the value



    return Dictionary



inFile = open('googleplaystore.csv')
readFile = csv.reader(inFile)
apple = list(readFile)
title = apple[0]
data = apple[1:]
#print(title)


#explore_data(apple,1,10)

#find_entry(data, "Instagram")
#find_entry(data, "insTagram")
#Dup,Uni = filter_entry(data)
#explore_data(Dup,0,len(Dup)-1)
#find_entry(Uni,'Poop FR')

#Dict = createReview(data)

#print (Dict['Instagram'])
#find_entry(Dup, "instagram")
#english_apps = createEnglishApps(data)
#explore_data(english_apps, 0, len(english_apps) - 1)

value = freq_table(data,1)

for k,v in value.items():
    print 'the key is : ' + str(k) + ' the value of that is : ' + str(v) + ' >>> '
