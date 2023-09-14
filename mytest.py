import unittest

class MyArray:
    # def __init__(self, arr):
    # self.array = arr

    def size(self, m_len):
        return len(m_len)

    def reverse(self, rev):
        rev.reverse()
        return rev

    def max(self, list):
        return max(list)

        '''
        # Mій метод 1
        list.sort()
        e_max = len(list) - 1
        return list[e_max]
        '''

        '''
        # Mій метод 2
        list.sort()
        list.reverse()
        return list[0]
        '''

    def min(self, list):
        return min(list)

        '''
        # Мій метод 1
        list.sort()
        return list[0]
        '''

    def desc(self, list):
        list.sort()
        list.reverse()
        return list

    def asc(self, list):
        list.sort()
        return list

    def odd(self, x):
        return [i for i in x if i % 2 != 0]

    def multiple_to_three(self, x):
        return [i for i in x if i % 3 == 0]

    def uniq(self, list):
        return set(list)

    def divide_on_ten(self, x):
        '''
        new_mass = []
        for y in x:
            result = y / 10
            new_mass.append(result)
        return new_mass
        '''
        return [i / 10 for i in x]

    def chars(self):
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
        '''
        index = []
        for y in x:
            i = abc[y]
            index.append(i)
        return index
        '''
        return [abc[i] for i in x]

    def switch(self, list):
        x = min(list)
        y = max(list)
        index1 = list.index(max(list))
        index2 = list.index(min(list))
        list[index1] = x
        list[index2] = y
        return list

    def before_min(self, list):
        return list[:list.index(min(list))]

    def three_smallest(self, list):
        list.sort()
        return list[:3]

class TesMyArray(unittest.TestCase):

    def setUp(self):
        self.mylist1 = [1, 2, 3, 4, 5, 1]
        self.mylist2 = [3, 0, 9, 7, 8]

    def test1_size(self):
        my_arr = MyArray()
        self.assertEqual(my_arr.size(self.mylist1), 6)
        self.mylist1.append(2)
        self.assertEqual(my_arr.size(self.mylist1), 7)

    def test2_size(self):
        my_arr = MyArray()
        self.assertEqual(my_arr.size(self.mylist2), 5)


myar = MyArray()
print(myar.reverse([10, 2, 25, 88, 15, 28, 33, 1, 0]))

'''
if __name__ == '__main__':
    unittest.main()
'''
