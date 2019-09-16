#plotting bar chart
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#sort by drug_name and barcode:
new = pd.read_csv('valid_dataset_filtered.csv', sep ='\t')
counts = new[['drug_name','bcr_patient_barcode']].groupby(['drug_name']).agg('count')
#counts = new[['drug_name','bcr_patient_barcode']].groupby(['drug_name']).agg('count').sum() #get the total

#plotting/visualization
#sorted by index
new_dd['Project_Id'].value_counts().sort_index().plot.bar()
plt.title('Pancancer subtype patients')
plt.xlabel('Project_Id')
plt.ylabel('total number of patients')
plt.show()

#not sorted by index
new_dd['Project_Id'].value_counts().plot.bar()
plt.title('Pancancer subtype patients')
plt.xlabel('Project_Id')
plt.ylabel('total number of patients')
plt.show()

# stacked bat plot(more than one column or feature)
#for vertical kind = bar, for horizontal kind = barh)
test5 = pd.crosstab(index=new_dd['drug_name'], columns=new_dd['Project_Id'])
test5.sort_index().plot(kind='bar', stacked=True,figsize=(20, 16))
plt.title('Pancancer-Drugs pairs with aleast 60 patients per treatment')
plt.ylabel('total numbers of pateints treated by a particular drug')
plt.legend(bbox_to_anchor=(1.1, 1.05))
#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
or
#for vertical kind = bar, for horizontal kind = barh)
AA =new_dd.groupby(['drug_name','Project_Id']).size().unstack().plot(kind='bar',stacked=True, figsize=(20, 15))
plt.title('Pancancer-Drugs pairs with aleast 60 patients per treatment')
plt.xlabel('Drug name')
plt.ylabel('total numbers of pateints treated by a particular drug')
#there are my legend styles, choose anyone you like
#AA.legend(loc=7)
#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.legend(bbox_to_anchor=(1.1, 1.05))
plt.savefig('patient_druag_pair.png')
plt.show()

#counting patients by project_id
#sorted
new_dd['Project_Id'].value_counts().sort_index()

#Not sorted
new_dd['Project_Id'].value_counts()
