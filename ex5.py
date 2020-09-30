import numpy as np

p=[1,2,3,4,5]

p_f = np.poly1d(p)
p_f(0.5)
p_f([1, 2, 3])
print(p_f)
