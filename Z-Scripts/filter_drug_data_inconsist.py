import pandas as pd
import sys
data = pd.read_csv('/home/adeolu/valid_dataset.csv', sep = '\t', header = 0)
#data.head()

#filter-out all drug incosistencies in the dataset to produce the valid dataset 

#open empty DataFrame so as to be able to added/merged all the roles in the dataset
dataset = pd.DataFrame()
for bcr_patient_barcode in data['bcr_patient_barcode']:
    df = data.loc[data['bcr_patient_barcode'] == bcr_patient_barcode, :]
    for drug_name in df['drug_name']:
        df1 = df.loc[df['drug_name'] == drug_name,:]
        if len(set(df1['measure_of_response'])) == 1:
            dataset = pd.concat([dataset,df1])
            #print(dataset)
            #the dataset was duplicated, so remove the duplicate by
            nn = dataset.drop_duplicates()
            

#To get those with inconsistency drug_respond use:

#open empty DataFrame so as to be able to added/merged all the roles in the dataset
dataset2 = pd.DataFrame()
for bcr_patient_barcode in data['bcr_patient_barcode']:
    df = data.loc[data['bcr_patient_barcode'] == bcr_patient_barcode, :]
    for drug_name in df['drug_name']:
        df1 = df.loc[df['drug_name'] == drug_name,:]
        if len(set(df1['measure_of_response'])) != 1:
            dataset2 = pd.concat([dataset2,df1])
            mm = dataset2.drop_duplicates()

#Note: the two scripts above are thesame but it only differs at 'if' line i.e ==1 changes to != 0. other things remain thesame.
