# Bo'sh set yaratish
# my_set = set()

# Elementlar bilan set yaratish
# my_set = {1, 2, 3, 4, 5}
# my_set.add("Hello")
# my_set.update([6, 7, 8])
# print(my_set)  # {1, 2, 4, 5, 6, 7, 8}
# print(my_set)  # {1, 2, 3, 4, 5}
# my_set.remove(9)
# my_set.discard(9)
# print(my_set)  # {1, 2, 4, 5}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {3, 4, 5, 6}
print(set1.intersection(set2, set3))  # {3, 4}