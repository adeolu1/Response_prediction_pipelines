import pandas as pd
import os
os.chdir('/home/adeolu/Downloads/Cli&Bio/BRCA/')
df1 = pd.read_csv('nationwidechildrens.org_clinical_drug_brca.txt', sep = "\t", header = 0)
df1.drop(["form_completion_date","bcr_drug_uuid",'bcr_patient_uuid',"clinical_trial_drug_classification",
          "pharmaceutical_tx_total_dose_units","prescribed_dose","pharmaceutical_tx_ongoing_indicator",
          "regimen_number","stem_cell_transplantation","stem_cell_transplantation_type","therapy_regimen",
          "therapy_regimen_other","total_dose","tx_on_clinical_trial",'days_to_stem_cell_transplantation',
          'pharm_regimen','pharm_regimen_other','pharma_adjuvant_cycles_count','pharma_type_other',
          'bcr_drug_uuid','pharmaceutical_tx_dose_units'], axis = 1, inplace = True)
df1 = df1.loc[~df1['treatment_best_response'].isin(["[Unknown]","[Not Available]","[Not Applicable]"]), :]
df2 = pd.read_csv('nationwidechildrens.org_ssf_tumor_samples_brca.txt', sep = '\t', header = 0)
df3 = (df1.merge(df2, left_on='bcr_patient_barcode', right_on='bcr_patient_barcode')
          .reindex(columns=['bcr_patient_barcode', 'bcr_drug_barcode','pharmaceutical_therapy_drug_name',
                           'treatment_best_response','pharmaceutical_therapy_type','pharmaceutical_tx_started_days_to',
                            'pharmaceutical_tx_ended_days_to','route_of_administration','tumor_sample_procurement_days_to',
                            'tumor_sample_procurement_method','cancer_procurement_method_other','bcr_sample_uuid','site_of_disease',
                            'history_neoadjuvant_treatment']))
df4 = pd.read_csv('nationwidechildrens.org_clinical_patient_brca.txt', sep = '\t', header = 0)
output = (df3.merge(df4, left_on='bcr_patient_barcode', right_on='bcr_patient_barcode')
          .reindex(columns=['bcr_patient_barcode', 'bcr_drug_barcode','pharmaceutical_therapy_drug_name',
                            'treatment_best_response','pharmaceutical_therapy_type','route_of_administration',
                            'pharmaceutical_tx_started_days_to','pharmaceutical_tx_ended_days_to',
                            'tumor_sample_procurement_days_to','tumor_sample_procurement_method',
                            'cancer_procurement_method_other','bcr_sample_uuid','site_of_disease', 'gender','race','ethnicity',
                            'days_to_initial_pathologic_diagnosis']))
output.to_csv('BRCA.csv', sep = '\t')
