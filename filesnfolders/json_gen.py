import json

FILE_NAME = input('File Name: ')
if not FILE_NAME:
    print('No File Name Provided Exiting The Program Now.')
    exit()
myDict = {}
while True:
    try:
        key = input('Key: ')
        value = input('Value: ')
        with open(FILE_NAME, 'w') as myfile:
            myDict[key] = value
            json.dump(myDict, myfile)
    except:
        print('Exiting the program.')
        exit()
