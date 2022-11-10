'''
Name: Sarah Zimmer, ***
email: zimmese@mail.uc.edu, ***
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: 
Citations: 
Anything else that's relevant:
'''
import jsons
import requests
from _ast import Compare

response = requests.get('https://developer.nps.gov/api/v1/parkinglots?parkCode=acad&api_key=Ig9AOzpzV54Y7qfMzRkRjCvI4UlnuMjoin11586P')
json_string = response.content
    
parsed_json = jsons.loads(json_string)
#print(parsed_json)

totalLots = parsed_json['total']
print("There are " + totalLots + " parking lots in this park.")

data = list(parsed_json['data'])
print(data)
'''   
spaces = ()
for totalSpaces in parsed_json['data']:
    print(sum(int(totalSpaces)))
'''

