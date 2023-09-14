'''
list = 'word'
for i in list:
    print(i)

list2 = [1, 2, 3, 4]
for i in list2:
    print(i)
'''
#list = [item for item in items]
items = [8, 2, 3, 4, 5, 8, 2, 1]
items = [5, 3, 2, 4, 5, 6, 5, 3]
'''
x = min(items)
y = max(items)
index1 = items.index(max(items))
index2 = items.index(min(items))
items[index1] = x
items[index2] = y
print(items)
'''

#print (items[:items.index(min(items))])

'''
x = 123
рядок_x = str(x)
цифри = [int(digit) for digit in рядок_x]
сума_цифр = sum(цифри)
print(сума_цифр)
'''

'''
a = [1, 4, 2, 3]
def switch(list):
  min_el, max_el = min(list), max(list)
  min_i, max_i = list.index(min_el), list.index(max_el)
  list[min_i], list[max_i] = max_el, min_el
  return list
'''

