class Lesson1:
    def sum(self, val):

        self.val = val
        list = [int(i) for i in str(self.val)]
        return sum(list)

    def age(self, birthday):

        self.birthday = birthday
        day = self.birthday * 365
        hour = day * 24
        minute = hour * 60
        sec = minute * 60
        # return f'Я живу, {self.birthday}, років або, {day}, днів або, {hour}, годин або, {minute}, хвилин або, {sec}, секунд.'
        return 'Я живу, '+ str(self.birthday) + " років або, "+ str(day) + " днів або, "+ str(hour) + " годин або, "+ str(minute) + " хвилин або, "+ str(sec) + " секунд"

    def name(self):

        #self.lname = lname
        lastname = input('Привіт, напиши будь ласка своє прізвище: ')
        #self.lastname = lastname
        firstname = input("Привіт, напиши будь ласка своє ім'я: ")
        #self.firstname = firstname
        fathername = input('Привіт, напиши будь ласка своє по-батькові: ')
        #self.fathername = fathername
        print('Вітаю', lastname, firstname, fathername, end='!')

value1 = Lesson1()
value2 = Lesson1()

'''value1.age(15)
print(f'{value1.age(15)} і люблю це.')'''

print(value1.sum(564))