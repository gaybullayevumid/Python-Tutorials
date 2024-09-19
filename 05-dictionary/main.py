# dict_name = {
#     'key':'value'
# }

# my_dict = {}

# person = {
#     'name': 'Alice',
#     'age': 30,
#     'city': 'New York',
# }
# print(person)

# person['city'] = 'alice@example.com'
# print(person)
# {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}

# person['age'] = 26
# print(person)
# {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# del person['name']
# print(person)
# {'name': 'Alice', 'age': 26, 'city': 'New York'}

# age = person.pop('age')
# print(age)
# print(person)  # {'name': 'Alice', 'city': 'New York'}person



# keys = my_dict.keys()
# print(keys)  # dict_keys(['name', 'city'])

# values = my_dict.values()
# print(values)  # dict_values(['Alice', 'New York'])

# items = my_dict.items()
# print(items)  # dict_items([('name', 'Alice'), ('city', 'New York')])

# my_dict.clear()
# print(my_dict)  # {}

# new_dict = my_dict.copy()
# print(new_dict)
# print(my_dict)

# my_dict = {
#     # 'key':'value'
#     'name': 'Alice',
#     'age': 30,
#     'city': 'New York',
# }

# my_dict2 = {
    
# }

# name = my_dict.get('city', 'Not Found')
# name1 = my_dict.get('age', 'Not Found')
# print(name)  # 'Alice'
# print(name1)  # 'Alice'

# country = my_dict.setdefault('country', 'USA')
# print(country)  # 'USA'
# print(my_dict)  # {'name': 'Alice', 'city': 'New York', 'country': 'USA'}