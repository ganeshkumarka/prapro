#Create a 1000 x 1000 random numpy array
#Measure how long the creation takes
#Convert the array into bytes
#Recreate the array from the bytes

import numpy as np
import time
initial = time.time()
array=np.random.rand(1000,1000)
end = time.time()
taken_time = end - initial
print(array)
print("time taken: ",taken_time)

#to bytes
new_array=array.tobytes()

#recreate array from bytes
recreated_array=np.frombuffer(new_array,dtype=array.dtype).reshape(array.shape)
print(recreated_array)

