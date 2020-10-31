# Extracting Data from JSON
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file and enter the sum below.

import json
import urllib.request, urllib.parse, urllib.error

url = ' http://py4e-data.dr-chuck.net/comments_1021640.json'
#url = input('Enter URL: ')
address = urllib.request.urlopen(url)
data = address.read()

print('Retrieving', url)
print('Retrieved', len(data), 'characters')

info = json.loads(data)
info = info["comments"]

total = 0
count = 0

for item in info:
    #print("Count: ",item["count"])
    total = total + int(item["count"])
    #print("Sum: ", total)
    count += 1

print('Count:', count)
print("Sum: ", total)

