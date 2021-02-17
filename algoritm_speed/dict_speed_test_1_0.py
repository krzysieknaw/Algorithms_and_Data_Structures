import timeit
import random
import matplotlib.pyplot as plt

times_data = []
list_data = []
dict_data = []
for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(i) in x", setup = "from __main__ import random,x,i")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("{:d},{:10.3f},{:10.3f}".format(i, lst_time, d_time))
    times_data.append(i)
    list_data.append(lst_time)
    dict_data.append(d_time)
    

plt.plot(times_data, list_data, 'ro', label = "list")
plt.plot(times_data, dict_data, 'g^', label = "dict")
plt.xlabel('Size of list or dict')
plt.ylabel('Time')
plt.legend()
plt.title("comparing 'in' operator in dict and list")

plt.show()

