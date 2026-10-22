# ### Pick the Longer Word

# Write a function called `longerWord(first, second)` that returns whichever word has more characters.

# If both words have the same length, return the first word.
# first = str(input("First word: "))
# second = str(input("Second word: "))

# def longerWord(first, second):
#     if len(first)>=len(second):
#         return first
#     else:
#          return second

# print(longerWord(first, second))

### Dictionary Practice

# In the dictionary below:

# 1. What are the keys?
# 2. Show how to access the age value
# 3. Insert a key called hairColor with a value of black
# 4. Now change that value of hairColor from black to brown
# 5. Delete the height key and it's value
# 6. Check if the dictionary has a key called eyeColor, and if it doesn't, print out: "Missing key"
# 7. Loop through the object, printing the key and value for each pair.

# person = { "name": "Sarah", "height": "6 feet", "age": 22 }

# print(person.keys())
# print(person["age"])
# person("hairColor") = "black"
# if "eyecolor" in person: 

# def  countLongWords(words, minimumLength):
#     count = 0

#     for word in words:
#         if len(word)>=minimumLength:
#             count +=1
#     return count 

# def removeRepeats(items):
#     no_repeat = []

#     for item in items:
#         if not item in no_repeat: 
#             no_repeat.append(item)
#     return no_repeat

# securityQuestions = [
#     {"question": "What is your mother's hometown? ", "expectedAnswer": "Toronto" },
#     {"question": "What is your father's favourite song? ", "expectedAnswer": "Out of Touch" },
#     {"question": "What is your cousin's middle name? ", "expectedAnswer": "Renzo"}
# ]

# def security():
#     correctquestions = True
#     for question in securityQuestions:
#         answer = input(question["question"])
#         if answer != question["expectedAnswer"]:
#             print("Invalid response, please try again later")
#             correctquestions = False
#             break
#     if correctquestions:
#         print("Success. You may now access your account")

# security()

# login = {"username": "R3nzo", "password": "1ced.Tea21"}

# count = 0

# while count < 3:
    
#     answer = input(f"Enter password for {login["username"]}: ")
#     if answer == login["password"]:
#         print("You may access your account")
#         break
#     count += 1
# if count >= 3:
#     print("You have tried too many times. ／༼ ༏༏ີཻ༾ﾍ ༏༏ີཻ༾༾༽༽")

# def uppercaseOddWords():

#     phrase.split
#     for even in phrase:
#         if even % 2 == 0
#         print(even.strip().higher())
#         continue 
    
# phrase = "fur pillows are hard to actually sleep on"

# def uppercaseOddWords():
#     splitPhrase = phrase.split()
#     num = 0
#     newString = ""
#     for word in splitPhrase:
#         num += 1
#         if num != 1:
#             newString += " "
#         if num % 2 == 0:
#             newString += word.upper()
#         else:
#             newString += word
#     return newString

# print(uppercaseOddWords())

# phrase = "fur pillows are hard to actually sleep on"

# def upperCamelCase():
#     splitPhrase = phrase.split()
#     newString = ""
#     for word in splitPhrase:
#        newString += word.capitalize()
#     return newString

# print(upperCamelCase())

# def countWords(inputs):
#     count = {}
#     words = inputs.split()
#     for word in words:
#         if word in count:
#             count[word] += 1
#         else:
#             count[word] = 1
#     return count
        

# inputs = "buy it use it break it fix it trash it change it mail upgrade it"
# output = countWords(inputs)
# print(output)

# inputs = [
#   "buy",
#   "it",
#   "use",
#   "it",
#   "break",
#   "it",
#   "fix",
#   "it",
#   "trash",
#   "it",
#   "change",
#   "it",
#   "mail",
#   "upgrade",
#   "it",
# ]

# def wordPosition(inputs):
#     position = {}
#     words = inputs
#     index = 0
#     for word in words:
#         if word in position:
#             indexList = position[word]
#             position[word].append(index)
#         else: 
#             position[word] = [index]
#         index += 1
#     return position

# output = wordPosition(inputs)
# print(output)

artists = [
  {
    "song": "HOLIDAY",
    "name": "Lil Nas X",
    "year": 2020,
  },
  {
    "song": "Say So",
    "name": "Doja Cat",
    "year": 2020,
  },
  {
    "song": "Old Town Road",
    "name": "Lil Nas X",
    "year": 2019,
  },
  {
    "song": "Bad Guy",
    "name": "Billie Eilish",
    "year": 2019,
  },
  {
    "song": "God's Plan",
    "name": "Drake",
    "year": 2018,
  },
]

def artistsByYear(artists):
    sortedYear = {}
    minYear = 9999
    maxYear = 0000
    for artist in artists:
        year = artist["year"]
        if year < minYear:
            minYear = year
        if year>maxYear:
            maxYear = year
    for year in range(minYear, maxYear+1):
        for artist in artists:
            if artist["year"] == year:
                if year in sortedYear:
                    sortedYear[year].append(artist)
                else:
                    sortedYear[year] = [artist]
    return sortedYear

print(artistsByYear(artists))
