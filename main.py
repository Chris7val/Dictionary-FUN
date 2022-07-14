# # simple dictionary
# person = {'first_name': 'Christopher', 'last_name': 'Valdez', 'age': 21, 'city': 'New York'}
#
# print(person['first_name'])
# print(person['last_name'])
# print(person['age'])
# print(person['city'])

# # favorite number dictionary
# favorite_num = {'jen': 7, 'chris': 3, 'ash': 4, 'alex': 9, 'mike': 14}
# print(f"jen favorite number is {favorite_num['jen']}.\n")
# print(f"chris favorite number is {favorite_num['chris']}.\n")
# print(f"ash favorite number is {favorite_num['ash']}.\n")

# glossary with loop
# keyword = {'.lower': 'makes all string values in to lowercase',
# '.append': 'add element to the last position of list', 'del': 'delete'}
# for key, value in keyword.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")
#
# River dictionary
# major_Rivers = {'nile': 'egypt', 'amazon': 'peru', 'ural': 'russia'}
#
# for key, value in major_Rivers.items():
#     print(f"\nThe {key} runs through {value}")
# for rivers in major_Rivers.keys():
#     print(f"\nRiver: {rivers}")
# for country in major_Rivers.values():
#     print(f"\nCountry: {country}")

# poll
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
# should = ['chris', 'ash', 'blake', 'jen', 'phil']
# for p in should:
#     if p in favorite_languages.keys():
#         print(f"Thanks {p} for taking the poll")
#     else:
#         print(f"{p} please participate in our poll")
#
# storing dictionaries in list
# person_0 = {'first_name': 'Christopher', 'last_name': 'Valdez', 'age': 21, 'city': 'New York'}
# person_1 = {'first_name': 'Ash', 'last_name': 'ro', 'age': 31, 'city': 'New York'}
# person_2 = {'first_name': 'greg', 'last_name': 'white', 'age': 12, 'city': 'New York'}
#
# peoples = [person_0, person_1, person_2]
#
# for people in peoples:
#     print(people)
#
# storing list in dictionaries
# favorite_places = {'claudia': ['cali', 'water'], 'chris': ['beach', 'river'], 'ash': ['lake', 'roof']}
#
# for name, places in favorite_places.items():
#     print(f"{name.title()} favorite places are:")
#     for place in places:
#         print(f"\t{place.title()}")

# dictionaries in dictionaries
# cities = {'New york': {'country': 'US', 'population': '8000000', 'Fact': 'Home of the stock exchange'},
#           'Chicago': {'country': 'US', 'population': '3000000', 'Fact': 'Home of the world first brownie'},
#           'Los Angeles': {'country': 'US', 'population': '4000000', 'Fact': 'There are secret tunnels under the city'}
#          , }
# for city, city_info in cities.items():
#     print(f"\nCity: {city.title()}")
#     country = city_info['country']
#     population = city_info['population']
#     fact = city_info['Fact']
#
#     print(f"Country: {country.title()}")
#     print(f"Population: {population.title()}")
#     print(f"Fact:{fact.title()}")

