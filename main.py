import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from calc import pie_chart
from calc import hist_chart
from calc import descriptiveAnalysis
from calc import runAnalysis

#msc_stage1_dir = 'C:\\Personal\\Project\\Data\\stage1.csv'
msc_stage1_dir = 'E:\\Books\\Software engineering\\Master\\RESEARCH METHODS\\Project\\Data\\stage1.csv'
#msc_stage2_dir = 'C:\\Personal\\Project\\Data\\stage2.csv'
msc_stage2_dir = 'E:\\Books\\Software engineering\\Master\\RESEARCH METHODS\\Project\\Data\\stage2.csv'

df_msc_stage1 = pd.read_csv(msc_stage1_dir, usecols=['major', 'undergraduate_major', 'year', 'sw_experince',
                                                     'IEEE_ACM', 'taken_c_e_e', 'software_engineering_impact',
                                                     'support_req_credit_hrs', 'support_training_on_job',
                                                     'support_pro_licensing'])
df_msc_stage2 = pd.read_csv(msc_stage2_dir, usecols=['major', 'undergraduate_major', 'year', 'sw_experince',
                                                     'IEEE_ACM', 'taken_c_e_e', 'software_engineering_impact',
                                                     'support_req_credit_hrs', 'support_training_on_job',
                                                     'support_pro_licensing'])

#print(df_msc_stage1.dtypes)
df_msc_stage1.dropna(inplace=True)
df_msc_stage2.dropna(inplace=True)
print('Stage1 count: ' + str(df_msc_stage1['IEEE_ACM'].count()))
print('Stage2 count: ' + str(df_msc_stage2['IEEE_ACM'].count()))

pie_chart(('Did not take\nCode Of Ethics course', 'Did take\nCode Of Ethics course'),
          list(df_msc_stage1['taken_c_e_e'].value_counts(normalize=True)),
          (0, 0.1),'./MA/MA_CodeOfEthicsCourse')


IEEE_ACM_yes = df_msc_stage1[df_msc_stage1['IEEE_ACM'] == 1]
IEEE_ACM_no = df_msc_stage1[df_msc_stage1['IEEE_ACM'] == 0]

pie_chart(('Do not know about\nIEEE/ACM Code\nOf Ethics', 'Know about\nIEEE/ACM Code\nOf Ethics'),
          list(df_msc_stage1['IEEE_ACM'].value_counts(normalize=True)),(0, 0.1),'./MA/acm')

pie_chart(('0-2 Years', '3-6 Years', '7-More Years'),
          list(df_msc_stage1['sw_experince'].value_counts(normalize=True)),(0, 0.1,0.1),'./MA/sw_experince')

hist_chart(df_msc_stage1['taken_c_e_e'],df_msc_stage1['software_engineering_impact'].size - 20,
           'Code Of Ethics Course','Number Of Students', './MA/Hist_taken_c_e_e')

boxplot_chart = df_msc_stage1\
    .boxplot(column=['software_engineering_impact',
                     'support_training_on_job',
                     'support_req_credit_hrs'])
#plt.show()
plt.savefig('./MA/MscBox.png')


## ACM yes
print('----------------- ACM Yes ------------------')
runAnalysis(IEEE_ACM_yes, 'MA ACM Yes')
###########

## ACM no
print('----------------- ACM No ------------------')
runAnalysis(IEEE_ACM_no, 'MA ACM No')
###########

############### Years Of Study
## Year 0-2
print('------------------- 0-2 ------------------')
runAnalysis(df_msc_stage1[df_msc_stage1['sw_experince'] == '0_2'],'0_2')
####

## Year 3-6
print('------------------- 3-6 ------------------')
runAnalysis(df_msc_stage1[df_msc_stage1['sw_experince'] == '3_6'],'3_6')
####

## Year 7-more
print('------------------- 7-more ------------------')
runAnalysis(df_msc_stage1[df_msc_stage1['sw_experince'] == '7_more'],'7_more')
####
###############

## Taken Course Yes
runAnalysis(df_msc_stage1[df_msc_stage1['taken_c_e_e'] == 1],'Taken Course Yes')
####

## Taken Course No
runAnalysis(df_msc_stage1[df_msc_stage1['taken_c_e_e'] == 0],'Taken Course No')
####


print('--------------------------- Stage 2 ---------------------------------')

boxplot_chart_stage2 = df_msc_stage2\
    .boxplot(column=['software_engineering_impact',
                     'support_training_on_job',
                     'support_req_credit_hrs'])
plt.savefig('./MA/MA_Box_stage2.png')
plt.show()
runAnalysis(df_msc_stage2,'All Students')
df_msc_stage2['software_engineering_impact'].hist()
plt.savefig('./MA/MA_Hist_stage2.png')
plt.show()
df_msc_stage1['software_engineering_impact'].hist()
plt.savefig('./MA/MA_Hist_stage1.png')
plt.show()

support_impact = df_msc_stage1[df_msc_stage1['software_engineering_impact'] >= 4]
print('Impact count: ' + str(support_impact['IEEE_ACM'].count()))
print('Support ' + str(support_impact[support_impact['software_engineering_impact'] == 4]
      ['software_engineering_impact'].count()))
print('Strongly Support ' + str(support_impact[support_impact['software_engineering_impact'] == 5]
      ['software_engineering_impact'].count()))

print('Fairly Small impact count: ' + str(df_msc_stage1[df_msc_stage1['software_engineering_impact'] == 3]['software_engineering_impact'].count()))
print('Very Small impact count: ' + str(df_msc_stage1[df_msc_stage1['software_engineering_impact'] == 2]['software_engineering_impact'].count()))
print('No impact count: ' + str(df_msc_stage1[df_msc_stage1['software_engineering_impact'] == 1]['software_engineering_impact'].count()))
#sns.load_dataset('data')
#sns.distplot(support_impact['software_engineering_impact'])

plt.hist(support_impact['software_engineering_impact'],
         support_impact['software_engineering_impact'].count())
plt.ylim(top=support_impact['software_engineering_impact'].count())
plt.show()

print('Strongly Support + ACM Yes : ' + str(support_impact[(support_impact['IEEE_ACM'] == 1) & (support_impact['software_engineering_impact'] == 5)]['IEEE_ACM'].count()))
print('Support + ACM Yes: ' + str(support_impact[(support_impact['IEEE_ACM'] == 1) & (support_impact['software_engineering_impact'] == 4)]['IEEE_ACM'].count()))
print('Strongly Support + ACM No: ' + str(support_impact[(support_impact['IEEE_ACM'] == 0) & (support_impact['taken_c_e_e'] == 0) & (support_impact['software_engineering_impact'] == 5)]['IEEE_ACM'].count()))
print('Support + ACM No: ' + str(support_impact[(support_impact['IEEE_ACM'] == 0) & (support_impact['taken_c_e_e'] == 0) & (support_impact['software_engineering_impact'] == 4)]['IEEE_ACM'].count()))
print('Support + ACM No + took a course: ' + str(support_impact[(support_impact['IEEE_ACM'] == 0) & (support_impact['taken_c_e_e'] == 1) & (support_impact['software_engineering_impact'] == 4)]['IEEE_ACM'].count()))
print('Strongly Support + ACM No + took a course: ' + str(support_impact[(support_impact['IEEE_ACM'] == 0) & (support_impact['taken_c_e_e'] == 1) & (support_impact['software_engineering_impact'] == 5)]['IEEE_ACM'].count()))
print('Strongly Support + ACM Yes + took a course: ' + str(support_impact[(support_impact['IEEE_ACM'] == 1) & (support_impact['taken_c_e_e'] == 1) & (support_impact['software_engineering_impact'] == 5)]['IEEE_ACM'].count()))
print('Support + ACM Yes + took a course: ' + str(support_impact[(support_impact['IEEE_ACM'] == 1) & (support_impact['taken_c_e_e'] == 1) & (support_impact['software_engineering_impact'] == 4)]['IEEE_ACM'].count()))

plt.hist(support_impact['IEEE_ACM'],
         support_impact['IEEE_ACM'].count())
plt.ylim(top=support_impact['IEEE_ACM'].count())
plt.show()

support_impact['taken_c_e_e'] = support_impact['taken_c_e_e'].astype(int)
print('Support impact and did not take course: ' + str(support_impact[(support_impact['taken_c_e_e'] == 0) & (support_impact['software_engineering_impact'] == 4)]
          ['software_engineering_impact'].count()))

print('Support impact and take course: ' + str(support_impact[(support_impact['taken_c_e_e'] == 1) & (support_impact['software_engineering_impact'] == 4)]
          ['software_engineering_impact'].count()))

support_impact['taken_c_e_e'] = support_impact['taken_c_e_e'].astype(int)
print('Strongly Support Impact and did not take course: ' + str(support_impact[(support_impact['taken_c_e_e'] == 0) & (support_impact['software_engineering_impact'] == 5)]
          ['software_engineering_impact'].count()))

print('Strongly Support Impact and take course: ' + str(support_impact[(support_impact['taken_c_e_e'] == 1) & (support_impact['software_engineering_impact'] == 5)]
          ['software_engineering_impact'].count()))


#plt.hist(support_impact['taken_c_e_e'],
#         support_impact['software_engineering_impact'])
#plt.ylim(top=support_impact['IEEE_ACM'].count())
#plt.show()