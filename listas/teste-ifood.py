#list1 = ["a", "b", "c"]
#list2 = [2, 3, 1]

#ordem que deve ser: Kibon, Makis, Sukiya, Viena, Giraffas, A feijoada

list1 = ["Kibon", "Sukiya", "A Feijoada", "Makis", "Giraffas", "Viena"]
list2 = [4.9, 4.6, 4.4, 4.7, 4.4, 4.4]

zipped_lists = zip(list2, list1)

sorted_zipped_lists = sorted(zipped_lists, reverse=True)

sorted_list1 = [element for _, element in sorted_zipped_lists]

print(sorted_list1)