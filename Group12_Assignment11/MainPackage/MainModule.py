'''
Name: Sarah Zimmer, Sara Jundi
email: zimmese@mail.uc.edu, jundisa@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This assignment demonstrates our ability to work with data from API
Citations: 
https://www.learndatasci.com/solutions/python-typeerror-list-indices-must-be-integers-or-slices-not-str/
https://stackoverflow.com/questions/15815976/group-count-list-of-dictionaries-based-on-value
https://bobbyhadz.com/blog/python-sum-values-in-list-of-dictionaries#:~:text=To%20sum%20the%20values%20in,to%20the%20sum()%20function.
https://stackoverflow.com/questions/61267353/how-to-access-the-first-element-or-number-in-counter-using-python
https://stackoverflow.com/questions/22903215/extract-tuple-from-list
Anything else that's relevant:
This data comes from the presidential elections of 2020 and documents the largest presidential contributions by state.
'''
import jsons
import requests
from collections import Counter

# request for API
response = requests.get('https://api.open.fec.gov/v1/presidential/contributions/by_state/?page=1&per_page=100&election_year=2020&sort_null_only=false&sort_nulls_last=false&api_key=Ig9AOzpzV54Y7qfMzRkRjCvI4UlnuMjoin11586P&sort_hide_null=false&sort=-contribution_receipt_amount')
json_string = response.content

# Parse through to get Python dictionaries
parsed_json = jsons.loads(json_string)
#print(parsed_json)

# Get results data to use in analysis
data = parsed_json['results']
#print(data)

# Create a count of contributions from state of California
caData = len([i for i in data if i['contribution_state'] == 'CA'])
print("Of the top", len(data), "largest state contributions to the 2020 elections, California is responsible for", caData, "of them.")

# Find the total contributions from California
count = Counter()
for i in data:
    count[i['contribution_state']] += i['contribution_receipt_amount'] # list of contribution sums by state
#print(count)
caTotal = count.most_common(1) #CA contribution
print("The total contributions for the 2020 elections from California was", caTotal[0][1]) 
