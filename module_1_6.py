my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict['Egor'] )
print('Not existing value:', my_dict.get('Igor') )
my_dict.update({'Zhenya' : 2005, 'Karim': 1995})
a = my_dict.pop('Karim')
print('Deleted value:',a)
print('Modified dictionary:', my_dict)

my_set = {'One', 1, 1.1, 1, 2 , 8, 8}
print('Set:', my_set)
my_set.add(16)
my_set.add('Two')
my_set.remove(2)
print('Modified set:', my_set)