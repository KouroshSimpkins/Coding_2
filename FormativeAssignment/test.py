import numpy as np

f = -1.0456
int32bits = np.asarray(f, dtype=np.float32).view(np.int32).item()

print('{:032b}'.format(int32bits))