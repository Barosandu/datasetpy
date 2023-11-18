from dataset import dataset
from time import time
start_time = time()

for i in range(1000):
    print(dataset[i][-3:-1])
    
end_time = time()
print(end_time - start_time)