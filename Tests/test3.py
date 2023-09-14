class MyArray:

    def size(self, abs):
        return len(abs)

    def alphabet(self, x):
        #abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        '''
        index = []
        for y in x:
            i = abc[y]
            index.append(i)
        return index
        '''

        return [chr(i + 97) for i in x]



val1 = MyArray()


#list = [1, 3, 6, True, False, 5.72, 25, 2, 0]
#for i in list:
    #if
'''
x = 6
if x % 3 == 0:
    print(x)

x = [1, 2, 3]
for y in x:
    res = y / 10
    print(res)
'''

print(val1.alphabet([0, 5]))
#print(ord('a'))