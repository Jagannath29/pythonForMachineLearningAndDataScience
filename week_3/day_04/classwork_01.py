# from datetime import datetime

# print(datetime.now())

from time import perf_counter
start_time = perf_counter()
for i in range(100):
    print(i)

    
end_tme = perf_counter()

total_time = end_tme - start_time

print(total_time)

