import operator
import random
import re
import psycopg2 as pg2

with open(r"python_class_test.html", 'r') as html_doc:
    html = html_doc.read()

colourregex = re.findall(r"<td>(.*)</td>", html)

for colour in colourregex:
    if colour == "MONDAY" or colour == "TUESDAY" or colour == "WEDNESDAY" or colour == "THURSDAY" or colour == "FRIDAY":
        colourregex.remove(colour)
frequency = {}
allcolours = str(",".join(colourregex))
allcoloursn = allcolours.split(",")
allcoloursn.remove('')
finalfinal = []

for colorfrequency in allcoloursn:
    col = colorfrequency.strip()
    finalfinal.append(col)
    frequency_list = frequency.keys()
    frequency[colorfrequency] = frequency.get(colorfrequency, 0) + 1

print(finalfinal)

final_count = {}

for item in finalfinal:
    count = finalfinal.count(item)
    final_count[item] = count

del final_count["BLEW"]

for colour, colorfrequency in final_count.items():
    print(str(colour) + " : " + str(colorfrequency) + " times")

final_count_values = final_count.values()
final_count_keys = final_count.keys()

mean = int(sum(final_count_values) / len(final_count_values))

if mean in final_count_values:
    print("\nThe mean color of shirt is: ", list(final_count.keys())[list(final_count_values).index(mean)], " = ", mean)
else:
    print("\nThe mean color of shirt is: ", list(final_count.keys())[list(final_count_values).index(mean + 1)], " \n")

print("The color worn mostly throughout the week is " + max(final_count.items(), key=operator.itemgetter(1))[0])

ordered = sorted(final_count_keys)
median = int(len(ordered) / 2)

if len(ordered) % 2 != 0:
    mediancolour = ordered[median]
    print("\nThe median color is :", mediancolour)
else:
    mediancolour = int((ordered[median] + ordered[median - 1])) / 2
    print("\nThe median color is :", mediancolour)

mean_deviations = []
# deviation = mean minus item value
for number in final_count_values:
    mean_deviations.append((number - mean) ** 2)

# variance = "summation of each color's mean deviations divided by number of colors"
variance = sum(mean_deviations) / (len(final_count_values))
print("\nThe variance of the colors is: ", variance)

# probability of red is red count divided by the total colors count
print("\nThe probability of picking RED at random from the colors is: ", final_count["RED"] / sum(final_count_values),
      "\n")

#
#
#
#
#
#
# postgresql insert

database = input("Enter your database name preferably postgres: ")
username = input("Enter your database username e.g. postgres: ")
password = input("Enter your database password: ")

conn = pg2.connect(
    database=database,
    user=username,
    password=password,
    host="localhost",
    port="5432")

cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS opeyemi_color_data''')
cur.execute(
    '''CREATE TABLE opeyemi_color_data (colors VARCHAR NOT NULL, color_frequency VARCHAR NOT NULL)'''
)

for colourItem in final_count_keys:
    cur.execute('''INSERT INTO opeyemi_color_data (colors, color_frequency) VALUES (%s, %s)''',
                (colourItem, final_count[colourItem]))

table = pd.read_sql('''SELECT * from opeyemi_color_data''', conn)
print(table, "\n")

conn.commit()
cur.close()
conn.close()

# LIST SEARCH


List = [8, 6, 8, 10, 20, 10, 8, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
given = int(input("Enter number to search: "))
returned = 0
for num in List:
    if given == num:
        returned += 1
if returned != 0:
    print("\nNumber " + str(given) + " was found in list.\n")
elif returned == 0:
    print("\nNumber not found in list.\n")

# BINARY GENERATOR
binary = ""
for i in range(4):
    number = random.choice(range(0, 2))
    binary += str(number)
    decimal = int(binary, 2)
    print("generated number is : " + str(binary) + " in decimal it's :  " + str(decimal))

import pprint

n = 50
a, b = 0, 1

f = [a, b]
countf = 0

while countf < n - 2:
    c = a + b
    f = f + [c]
    a, b = b, c
    countf += 1

pprint.pprint("first 50 fibonacci's numbers starting with 0 and 1 are:  " + str(f))
print("Their sum is " + str(sum(f)))
