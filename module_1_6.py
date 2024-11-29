print('Словари')
my_dict = {'Ilya': 2005, 'Anna': 2004}
print(my_dict)
my_dict ['Ivan'] = 2003
print(my_dict)
print('Ilya: ', my_dict.get('Ilya'))
print('Ivan: ', my_dict.get('Ivan'))
my_dict.update({'Michael': 2008,
                'Vera': 2006})
print(my_dict)
a = my_dict.pop('Anna')
print(my_dict)
print('Anna: ', a)
print(my_dict)


#------------------------------------------------
print('множества')
my_set = {1, 5, 6, 5, 3, 4, 1, 'mouse', 'nose', 'mouse'}
print('Set: ', my_set)
(my_set.add(8))
(my_set.add('sunder'))
(my_set.discard(5))
print('Modified set: ', my_set)