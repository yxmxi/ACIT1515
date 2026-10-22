countries = ["a whole list of shit", "america", "cambodia", "germany", 8.6, 4, False]

def country_name(countries):
    safe_name = []
    for country in countries:
        if type(countries) == str:
            safe_name.append(country)
    return safe_name


def even_name(country_name):
    even = []
    for name in country_name:
        if len(safe_name) % 2 == 0:
            even.append(name)
    return even

def findLongestName(even_name):
    longest_name = ""
    for name in even:
        if len(even) > longest_name:
            longest_name = name
    return longest_name

print(findLongestName)
