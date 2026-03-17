import pandas as pd
import os

df = pd.DataFrame({"name":["vivek","darshan","ajay","ghanshyam"], "age":[32,23,30,18],"city":["Surat","surat","valsad","gandhada"]})

data_dir = "data"

os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "mysample.csv")

df.to_csv(file_path, index=False)