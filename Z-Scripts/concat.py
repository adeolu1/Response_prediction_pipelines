#concat many files
import pandas as pd
import glob
import os
os.chdir('/home/adeolu/Downloads/GDC/Clinical(CSV)/')
df = pd.concat([pd.read_csv(f,sep = '\t', header =0) for f in glob.glob('*.csv')], ignore_index = True, sort = False)
df.to_csv('output.csv', sep ='\t')

#concat many file and add new column(s)
file_list = list()

for file in os.listdir():
    if file.endswith('.csv'):
        df = pd.read_csv(file,sep = '\t', header =0)
        df['Project_Id'] = file
        file_list.append(df)

all_days = pd.concat(file_list, axis=0, ignore_index=True)
all_days['Project_Id'] = all_days['Project_Id'].map(lambda x: str(x)[:-4])
all_days.to_csv('out1.csv', sep = '\t').

#concat many file and add new column(s) with column and index removed
file_list = list()

for file in os.listdir():
    if file.endswith('.csv'):
        df = pd.read_csv(file,sep = '\t', header = 0)
        df['Project_Id'] = file
        file_list.append(df)

all_days = pd.concat(file_list)
all_days['Project_Id'] = all_days['Project_Id'].map(lambda x: str(x)[:-4])
all_days.drop(['0'], axis = 1, inplace = True)
print(all_days.columns)
all_days.to_csv('out2.csv', sep = '\t', index = False)
