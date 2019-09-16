import pandas as pd
import os 
os.chdir('/home/adeolu/Downloads/Cli&Bio/GBM/')
df1 = pd.read_csv('nationwidechildrens.org_clinical_drug_gbm.txt', sep = "\t", header = 0)
df1.drop(["form_completion_date","clinical_trial_drug_classification","pharmaceutical_tx_total_dose_units","prescribed_dose",
          "pharmaceutical_tx_ongoing_indicator","regimen_number","stem_cell_transplantation","stem_cell_transplantation_type",
         "therapy_regimen","therapy_regimen_other","total_dose","tx_on_clinical_trial", 'days_to_stem_cell_transplantation','pharm_regimen','pharm_regimen_other','pharma_adjuvant_cycles_count',
          'pharma_type_other','pharmaceutical_tx_dose_units'], axis = 1, inplace = True)
df1 = df1.set_index("treatment_best_response")
out = df1.drop(["[Unknown]","[Not Available]","[Not Applicable]"], axis=0)
out.to_csv('out.csv', sep = '\t')
out = pd.read_csv('out.csv', sep = '\t', header = 0)
df2 = pd.read_csv('nationwidechildrens.org_ssf_tumor_samples_gbm.txt', sep = '\t', header = 0)
df3 = (out.merge(df2, left_on='bcr_patient_barcode', right_on='bcr_patient_barcode')
          .reindex(columns=['bcr_patient_uuid', 'bcr_patient_barcode', 'bcr_drug_barcode', 'bcr_drug_uuid','pharmaceutical_therapy_drug_name',
                           'treatment_best_response','pharmaceutical_therapy_type','pharmaceutical_tx_started_days_to','pharmaceutical_tx_ended_days_to',
                           'route_of_administration','tumor_sample_procurement_days_to','tumor_sample_procurement_method','cancer_procurement_method_other',
                           'history_neoadjuvant_treatment','site_of_disease']))
df4 = pd.read_csv('nationwidechildrens.org_clinical_patient_gbm.txt', sep = '\t', header = 0)
output = (df3.merge(df4, left_on='bcr_patient_barcode', right_on='bcr_patient_barcode')
          .reindex(columns=['bcr_patient_uuid', 'bcr_patient_barcode', 'bcr_drug_barcode', 'bcr_drug_uuid','pharmaceutical_therapy_drug_name',
                           'treatment_best_response','pharmaceutical_therapy_type','pharmaceutical_tx_started_days_to','pharmaceutical_tx_ended_days_to',
                           'route_of_administration','tumor_sample_procurement_days_to','tumor_sample_procurement_method','cancer_procurement_method_other',
                           'site_of_disease','gender','race','ethnicity','days_to_initial_pathologic_diagnosis']))
output.drop('bcr_patient_uuid', axis = 1, inplace = True)
output.to_csv('output.csv', sep = '\t')



import pandas as pd
df1 = pd.read_csv('/home/adeolu/Desktop/nationwidechildrens.org_clinical_drug_brca.txt', sep = "\t", header = 0)
df1.drop(["form_completion_date","clinical_trial_drug_classification","pharmaceutical_tx_total_dose_units","prescribed_dose",
          "pharmaceutical_tx_ongoing_indicator","regimen_number","stem_cell_transplantation","stem_cell_transplantation_type",
         "therapy_regimen","therapy_regimen_other","total_dose","tx_on_clinical_trial", 'days_to_stem_cell_transplantation','pharm_regimen','pharm_regimen_other','pharma_adjuvant_cycles_count',
          'pharma_type_other','pharmaceutical_tx_dose_units'], axis = 1, inplace = True)
df1 = df1.loc[~df1['treatment_best_response'].isin(["[Unknown]","[Not Available]","[Not Applicable]"]), :]
df2 = pd.read_csv('/home/adeolu/Downloads/nationwidechildrens.org_ssf_tumor_samples_brca.txt', sep = '\t', header = 0)
df3 = (df1.merge(df2, left_on='bcr_patient_barcode', right_on='bcr_patient_barcode')
          .reindex(columns=['bcr_patient_uuid', 'bcr_patient_barcode', 'bcr_drug_barcode', 'bcr_drug_uuid','pharmaceutical_therapy_drug_name',
                           'treatment_best_response','pharmaceutical_therapy_type','pharmaceutical_tx_started_days_to','pharmaceutical_tx_ended_days_to',
                           'route_of_administration','tumor_sample_procurement_days_to','tumor_sample_procurement_method','cancer_procurement_method_other',
                           'history_neoadjuvant_treatment','site_of_disease']))
df4 = pd.read_csv('/home/adeolu/Downloads/nationwidechildrens.org_clinical_patient_brca.txt', sep = '\t', header = 0)
output = (df3.merge(df4, left_on='bcr_patient_barcode', right_on='bcr_patient_barcode')
          .reindex(columns=['bcr_patient_uuid', 'bcr_patient_barcode', 'bcr_drug_barcode', 'bcr_drug_uuid','pharmaceutical_therapy_drug_name',
                           'treatment_best_response','pharmaceutical_therapy_type','pharmaceutical_tx_started_days_to','pharmaceutical_tx_ended_days_to',
                           'route_of_administration','tumor_sample_procurement_days_to','tumor_sample_procurement_method','cancer_procurement_method_other',
                           'site_of_disease','gender','race','ethnicity','days_to_initial_pathologic_diagnosis']))
output.to_csv('output.csv', sep = '\t')
