import pandas as pd
print ("extract data")

data = {
         'ID' : [101, 102, 103],
         'Name' : ['Alice', 'Bob', 'Charlie'],  
         'Age' : [25, 30, 35]
    }
df = pd.DataFrame(data)
print(df)