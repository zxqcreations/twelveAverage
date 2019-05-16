import numpy as np

baseHertz = [440]

a = list(np.asarray([(2**i, 1/(2**i)) for i in range(1,5)]).reshape(-1))
a.append(1)
a.sort()
a = np.multiply(baseHertz[0],a)
print(a)


times = [2**(i/12) for i in range(0,12)]
print(times)

twelveAnswer = np.asarray([np.multiply(times, a[i]) for i in range(0,len(a)-1)]).reshape(-1)

print(twelveAnswer[:88])
print(len(twelveAnswer[:88]))
