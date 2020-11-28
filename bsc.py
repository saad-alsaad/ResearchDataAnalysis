import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from calc import pie_chart
from calc import hist_chart
from calc import descriptiveAnalysis
from calc import runAnalysis
#import rpy2

bsc_stage1_dir = 'E:\\Books\\Software engineering\\Master\\RESEARCH METHODS\\Project\\Data\\BscStage1.xlsx'
bsc_stage2_dir = 'E:\\Books\\Software engineering\\Master\\RESEARCH METHODS\\Project\\Data\\BscStage2.xlsx'

df_bsc_stage1 = pd.read_excel(bsc_stage1_dir)
df_bsc_stage2 = pd.read_excel(bsc_stage2_dir)

df_bsc_stage1.dropna(inplace=True)
df_bsc_stage2.dropna(inplace=True)

print('Stage1 count: ' + str(df_bsc_stage1['IEEE_ACM'].count()))
print('Stage2 count: ' + str(df_bsc_stage2['IEEE_ACM'].count()))

pie_chart(('Did not take\nCode Of Ethics course', 'Did take\nCode Of Ethics course'),
          list(df_bsc_stage1['taken_c_e_e'].value_counts(normalize=True)),
          (0, 0.1),'./BA/CodeOfEthicsCourse')

print('--------------------------- Stage 1 ---------------------------------')
IEEE_ACM_yes = df_bsc_stage1[df_bsc_stage1['IEEE_ACM'] == 1]
IEEE_ACM_no = df_bsc_stage1[df_bsc_stage1['IEEE_ACM'] == 0]

pie_chart(('Do not know\n about ACM', 'Know about ACM'),
          list(df_bsc_stage1['IEEE_ACM'].value_counts(normalize=True)),(0, 0.1),'./BA/acm')

pie_chart(('Year 4', 'Year 3', 'Year 5'),
          list(df_bsc_stage1['year'].value_counts(normalize=True)),(0, 0.1,0.1),'./BA/years')

hist_chart(df_bsc_stage1['taken_c_e_e'],df_bsc_stage1['software_engineering_impact'].size - 20,
           'Code Of Ethics Course','Number Of Students', './BA/Hist_taken_c_e_e')

boxplot_chart = df_bsc_stage1\
    .boxplot(column=['software_engineering_impact',
                     'support_training_on_job',
                     'support_req_credit_hrs'])
plt.savefig('./BA/BscBox.png')

## Impact + ACM Yes
print('Impact + ACM Yes: ' + str(IEEE_ACM_yes['software_engineering_impact'].count()))
pie_chart(('Somewhat Large', 'Very Large', 'Fairly Small'),
          list(IEEE_ACM_yes['software_engineering_impact'].value_counts(normalize=True))
          ,(0, 0.1, 0),'./BA/acm_yes_impact')
#######

## Impact + ACM No
print('Impact + ACM No: ' + str(IEEE_ACM_no['software_engineering_impact'].count()))
pie_chart(('Somewhat Large', 'Very Large', 'No Impact'),
          list(IEEE_ACM_no['software_engineering_impact'].value_counts(normalize=True))
          ,(0, 0.1, 0),'./BA/acm_no_impact')
########

## ACM yes
runAnalysis(IEEE_ACM_yes,'ACM Yes')

## ACM no
print('----------------- ACM No ------------------')
runAnalysis(IEEE_ACM_no,'ACM No')

############### Years Of Study
## Year 3
print('------------------- Year 3 ------------------')
runAnalysis(df_bsc_stage1[df_bsc_stage1['year'] == 3],'year3')
####

## Year 4
print('------------------- Year 4 ------------------')
runAnalysis(df_bsc_stage1[df_bsc_stage1['year'] == 4],'year4')
####

## Year 5
print('------------------- Year 5 ------------------')
runAnalysis(df_bsc_stage1[df_bsc_stage1['year'] == 5],'year5')
####
###############

### Histogram Chart
hist_chart(df_bsc_stage1['year'],df_bsc_stage1['software_engineering_impact'].size - 20,
           'Year','Number Of Students', './BA/Hist_software_engineering_impact')
##########

## Taken Course Yes
runAnalysis(df_bsc_stage1[df_bsc_stage1['taken_c_e_e'] == 1],'Taken Course Yes')
####

## Taken Course No
runAnalysis(df_bsc_stage1[df_bsc_stage1['taken_c_e_e'] == 0],'Taken Course No')
####


print('--------------------------- Stage 2 ---------------------------------')

boxplot_chart_stage2 = df_bsc_stage2\
    .boxplot(column=['software_engineering_impact',
                     'support_training_on_job',
                     'support_req_credit_hrs'])
plt.savefig('./BA/BscBox_stage2.png')
plt.show()
runAnalysis(df_bsc_stage2,'All Students')

df_bsc_stage2['software_engineering_impact'].hist()
plt.savefig('./BA/BA_Hist_stage2.png')
plt.show()
df_bsc_stage1['software_engineering_impact'].hist()
plt.savefig('./BA/BA_Hist_stage1.png')
plt.show()

support_impact = df_bsc_stage1[df_bsc_stage1['software_engineering_impact'] >= 4]
print('Impact count: ' + str(support_impact['IEEE_ACM'].count()))
print('Support ' + str(support_impact[support_impact['software_engineering_impact'] == 4]
      ['software_engineering_impact'].count()))
print('Strongly Support ' + str(support_impact[support_impact['software_engineering_impact'] == 5]
      ['software_engineering_impact'].count()))

print('Fairly Small impact count: ' + str(df_bsc_stage1[df_bsc_stage1['software_engineering_impact'] == 3]['software_engineering_impact'].count()))
print('Very Small impact count: ' + str(df_bsc_stage1[df_bsc_stage1['software_engineering_impact'] == 2]['software_engineering_impact'].count()))
print('No impact count: ' + str(df_bsc_stage1[df_bsc_stage1['software_engineering_impact'] == 1]['software_engineering_impact'].count()))
#sns.load_dataset('data')
#sns.distplot(support_impact['software_engineering_impact'])

plt.hist(support_impact['software_engineering_impact'],
         support_impact['software_engineering_impact'].count())
plt.ylim(top=support_impact['software_engineering_impact'].count())
plt.xlabel('Software Engineering Impact')
plt.ylabel('Number of Students')
#plt.savefig('img1.png')
plt.show()

print('Strongly Support + ACM Yes : ' + str(support_impact[(support_impact['IEEE_ACM'] == 1) & (support_impact['software_engineering_impact'] == 5)]['IEEE_ACM'].count()))

print('Support + ACM Yes: ' + str(support_impact[(support_impact['IEEE_ACM'] == 1) & (support_impact['software_engineering_impact'] == 4)]['IEEE_ACM'].count()))

print('Strongly Support + ACM No: ' + str(support_impact[(support_impact['IEEE_ACM'] == 0) &
                                                         (support_impact['taken_c_e_e'] == 0) &
                                                         (support_impact['software_engineering_impact'] == 5)]['IEEE_ACM'].count()))

print('Support + ACM No: ' + str(support_impact[(support_impact['IEEE_ACM'] == 0) &
                                                (support_impact['taken_c_e_e'] == 0) &
                                                (support_impact['software_engineering_impact'] == 4)]['IEEE_ACM'].count()))

print('Support + ACM No + took a course: ' + str(support_impact[(support_impact['IEEE_ACM'] == 0) &
                                                                (support_impact['taken_c_e_e'] == 1) &
                                                                (support_impact['software_engineering_impact'] == 4)]['IEEE_ACM'].count()))

print('Strongly Support + ACM No + took a course: ' + str(support_impact[(support_impact['IEEE_ACM'] == 0) &
                                                                         (support_impact['taken_c_e_e'] == 1) &
                                                                         (support_impact['software_engineering_impact'] == 5)]['IEEE_ACM'].count()))

print('Strongly Support + ACM Yes + took a course: ' + str(support_impact[(support_impact['IEEE_ACM'] == 1) &
                                                                          (support_impact['taken_c_e_e'] == 1) &
                                                                          (support_impact['software_engineering_impact'] == 5)]['IEEE_ACM'].count()))

print('Strongly Support + ACM Yes + did not take a course: ' + str(support_impact[(support_impact['IEEE_ACM'] == 1) &
                                                                                  (support_impact['taken_c_e_e'] == 0) &
                                                                                  (support_impact['software_engineering_impact'] == 5)]['IEEE_ACM'].count()))

print('Support + ACM Yes + did not take a course: ' + str(support_impact[(support_impact['IEEE_ACM'] == 1) &
                                                                         (support_impact['taken_c_e_e'] == 0) &
                                                                         (support_impact['software_engineering_impact'] == 4)]['IEEE_ACM'].count()))

print('Strongly Support + ACM no + did not take a course: ' + str(support_impact[(support_impact['IEEE_ACM'] == 0) &
                                                                                 (support_impact['taken_c_e_e'] == 0) &
                                                                                 (support_impact['software_engineering_impact'] == 5)]['IEEE_ACM'].count()))

print('Support + ACM no + did not take a course: ' + str(support_impact[(support_impact['IEEE_ACM'] == 0) &
                                                                        (support_impact['taken_c_e_e'] == 0) &
                                                                        (support_impact['software_engineering_impact'] == 4)]['IEEE_ACM'].count()))

print('Support + ACM Yes + took a course: ' + str(support_impact[(support_impact['IEEE_ACM'] == 1) &
                                                                 (support_impact['taken_c_e_e'] == 1) &
                                                                 (support_impact['software_engineering_impact'] == 4)]['IEEE_ACM'].count()))

print('Support + Strongly Support + took a course: ' + str(support_impact[support_impact['taken_c_e_e'] == 1]['IEEE_ACM'].count()))

print(str(support_impact[support_impact['taken_c_e_e'] == 0]['IEEE_ACM'].value_counts(normalize=True)[0]))
print(str(support_impact[support_impact['taken_c_e_e'] == 0]['IEEE_ACM'].value_counts(normalize=True)[1]))

acm_yes_course = support_impact[support_impact['IEEE_ACM'] == 1]['taken_c_e_e'].value_counts(normalize=True)
acm = support_impact['IEEE_ACM'].value_counts(normalize=True)
print(str(support_impact['support_req_credit_hrs'].value_counts(normalize=True)))
print(str(acm))
print(str(support_impact[support_impact['IEEE_ACM'] == 0]['taken_c_e_e'].value_counts(normalize=True)))
print(str(acm_yes_course))
print(str(support_impact[(support_impact['IEEE_ACM'] == 0) & (support_impact['taken_c_e_e'] == 1)]['year'].value_counts(normalize=True)))
print(str(support_impact[(support_impact['IEEE_ACM'] == 0) & (support_impact['taken_c_e_e'] == 1)].count()))

plt.hist(support_impact['IEEE_ACM'],
         support_impact['IEEE_ACM'].count())
plt.ylim(top=support_impact['software_engineering_impact'].count())
#plt.savefig('img1.png')
plt.show()

labels = 'Does not know about ACM', 'Know about ACM'
sizes = list(acm)
explode = (0, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig('img1.png')
plt.show()
