import pandas as pd
import numpy as np
data = pd.read_excel("G:/pyWork/pyProjects/pyAnalytics/Assignment_3_Excel_Sheet.xlsx")

# Lets add two more columns, 10th and 12th ranks
data["Rank10"] = data["class10"].rank() 
data["Rank12"] = data["class12"].rank() 
data


#%% Find Student with Highest 10th and 12th rank
index_rank_10 = int(data[["Rank10"]].idxmax())
rollno_10th = data["rollno"].iloc[index_rank_10]
pct_10th    = data["class10"].iloc[index_rank_10]
sname_10th  = data["sname"].iloc[index_rank_10]

index_rank_12 = int(data[["Rank12"]].idxmax())
rollno_12th = data["rollno"].iloc[index_rank_12]
pct_12th    = data["class12"].iloc[index_rank_12]
sname_12th  = data["sname"].iloc[index_rank_12]

print("{} with roll number {} had the highest percentage of {} in 10th".format(sname_10th,rollno_10th,pct_10th))
# Output : student20 with roll number 119 had the highest percentage of 36 in 10th
print("{} with roll number {} had the highest percentage of {} in 10th".format(sname_12th,rollno_12th,pct_12th))
# Output : student12 with roll number 111 had the highest percentage of 46 in 12th


#%% Find the number of people born in 1992 and 1991
from datetime import date
value_to_check = pd.Timestamp(1992, 1, 1)
filter_mask = data['dob'] > value_to_check
filtered_data = data[filter_mask]
print("{} students are born in 1992 and {} students are born in 1991".format(len(filtered_data),len(data)-len(filtered_data)))
