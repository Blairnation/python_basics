# json writing

import json

data = {'name': 'tony',
        'age': 25,
        'city': 'accra'}

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

# json reading

import json

with open('data.json', 'r') as infile:
    file = json.load(outfile)

print(file)


# converting python to json
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# convert json to python
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# regEx
# using findall
import re

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
text = "Contact us at info@example.com or support@example.org."

emails = re.findall(pattern, text)
print(emails)

# search
import re

pattern = r"apple"
text = "I have an apple and a banana."

match = re.search(pattern, text)
if match:
    print("Match found!")
else:
    print("No match.")

# splitting a string using a pattern
import re

pattern = r"\s+"   # splitting using whitespaces
# pattern = r"[\s,]+"  # Split on one or more whitespace or comma characters
text = "This is a sentence with multiple    spaces."

parts = re.split(pattern, text)
print(parts)


# replacing a string
import re

pattern = r"apple"
replacement = "orange"
text = "I have an apple and a banana."

new_text = re.sub(pattern, replacement, text)
print(new_text)
