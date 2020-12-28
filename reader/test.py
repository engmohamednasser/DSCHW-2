
import pandas as pd 


data = pd.read_csv('/home/user/HW2_Docker/volume/df.csv')

print(data)

data.to_csv('/home/user/HW2_Docker/volume/df_copy.csv')
print("done, The Mean value of column D is :")

print(data["D"].mean())
