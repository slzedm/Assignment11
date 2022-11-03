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

response = requests.get('')
json_string = response.content
    
parsed_json = jsons.loads(json_string)