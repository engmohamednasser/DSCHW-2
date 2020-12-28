
import pandas as pd

import numpy as np

df = pd.DataFrame(np.random.randint(0,100,size=(20, 6)), columns=list('ABCDEF'))
print(df)

df.to_csv('/home/user/HW2_Docker/volume/df.csv')
print("done, The Mean value of column D is :")
print(df["D"].mean())
