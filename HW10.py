import random, string

dict_1=dict(zip([random.choice(string.ascii_letters) for _ in range(10)], [random.randint(1,10) for _ in range (10)]))
print (dict_1)
dict_2 = dict(zip([random.choice(string.ascii_letters) for _ in range(10)], [random.randint(1,10) for _ in range (10)]))
print (dict_2)
dict_3 = dict_1 | dict_2
print (dict_3)
result = {key: max(dict_1[key], dict_2[key]) for key in dict_1 if key in dict_2}
print (result)
dict = dict_3 | result
print (dict)