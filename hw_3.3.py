lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [1, 2, 3]
lst3 = [1, 2, 3, 4, 5]
lst4 = [1]
lst5 = []

all_lists = [lst1, lst2, lst3, lst4, lst5]

for lst in all_lists:
    mid = (len(lst) + 1) // 2
    result = [lst[:mid], lst[mid:]]
    print(result)
