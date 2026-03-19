list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

common_items = set(list_a) & set(list_b)

all_items = set(list_a).union(set(list_b))

print(common_items)
print(all_items)
