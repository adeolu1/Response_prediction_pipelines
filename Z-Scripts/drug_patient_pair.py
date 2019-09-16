#import necessary modules
import pandas as pd
import os
os.chdir('/home/adeolu/Downloads/GDC/OUTPUT/Research')
new = pd.read_csv('valid_dataset_filtered.csv', sep ='\t')
#new.head()
#count the number of patients that were treated with a particular drug using barcode and drugname
#df['nunique'] = new.groupby('drug_name')['bcr_patient_barcode'].nunique() or
#print(new.shape)
counts = new[['drug_name','bcr_patient_barcode']].groupby(['drug_name']).agg('count')
#print(new.shape)
#type(counts)-(if data is not in dataframe convert to dataframe using (ddf = pd.DataFrame(counts)) but here our data is alrady a dataframe

counts['drug_name'] = counts.index
#print(counts)
dda = counts.reset_index(drop = True)
#print(dda)
#dda.columns

#filter out pateint_drug pair that is grater than 60 (this can be increased or decreased depending on desire)
cut_dda = dda.loc[dda['bcr_patient_barcode'] > 60, :]
print(cut_dda)
print(cut_dda.shape)

#get the total number of patients with pateint_drug pair that is grater than 60
cut_dda['bcr_patient_barcode'].sum() #(optional)

#get all the details pateint_drug pair that is grater than 60 from the main dataframe using the specified drug names
new_dd = new.loc[new['drug_name'].isin(['Bevacizumab','Capecitabine','Carboplatin','Cisplatin','Cyclophosphamide',
                                       'Docetaxel','Doxorubicin','Etoposide','Fluorouracil','Gemcitabine',
                                       'Leucovorin','Oxaliplatin','Paclitaxel','Pemetrexed','Temozolomide']), :]
