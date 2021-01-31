import time

start = time.time()


for i in range(5000):
    print('python '*i)


end = time.time()
n = (4999*5000)/2
result = end - start
print(result)
print(f'Python was printed %d time', n)
