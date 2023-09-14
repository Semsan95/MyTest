# Цикли та оператори в них
# Цикл - конструкція за допомогою якої можна виконати певний код кілька раз поспіль.
# Цикл for - має в умові точку А і точку Б
'''for i in range(5, 16, 2):
    print("Number x2: ", i)'''
    # i - змінна, яка буде приймати значення кожного елемента під час ітерації
    # 5 - початок циклу з цифри 5,
    # 16 - закінцення циклу на цифрі 15,
    # 2 - крок циклу

'''word = 'Some text'
for i in word:
    if i == 'm':
        print('Літера m є у слові')'''

# Цикл while - в виконує код поки умова не стане true
'''i = 100
while i >= 10:
    print(i)
    i -= 10'''

# Практичне використання (цикл while краще використовувати, коли треба задати лише одну умову)
# Вихід з циклу відбувається тоді, коли While False.
'''work = True
while work:
    user_input = input("Enter word STOP: ")
    if user_input == "STOP":
        work = False
print("While loop is done")'''

# for - використовується коли є певний діапазон умов
# while - використовується коли є лише одна умова

# Оператори в циклах:
# break - повний вихід з циклу
'''for i in range(1, 11):

    if i == 7:
        break

    print('El: ', i)'''

# continue - пропускає певну ітерацію циклу
for i in range(1, 11):

    if i % 2 == 0:
        continue

    if i == 7:
        break

    print('El: ', i)

# else - виконується тоді коли в нас не виконано вихід з циклу, пишуть після break
for i in "Hello world":
    if i == "l":
        print("Done")
        break
else:
    print('Not found')