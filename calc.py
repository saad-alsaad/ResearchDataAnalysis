import matplotlib.pyplot as plt

def pie_chart(labels, sizes, explode, image_name):
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(image_name + '.png')
    plt.show()

def hist_chart(columnx,columny, xName, yName, imageName):
    plt.hist(columnx,20)
    plt.ylim(top=columny)
    plt.xlabel(xName)
    plt.ylabel(yName)
    plt.savefig(imageName + '.png')
    plt.show()

def descriptiveAnalysis(df, column, ColumnName, dfName):
    print('Mean ' + ColumnName + ' + ' + dfName + ' ' + str(df[column].mean()))
    print('Mode ' + ColumnName + ' + ' + dfName + ' ' + str(df[column].mode().values[0]))
    print('Median ' + ColumnName + ' + ' + dfName + ' ' + str(df[column].median()))
    print('Frequency ' + ColumnName + ' + ' + dfName + '\n' + str(df[column].value_counts()))  ## Frequency
    print('Percentage ' + ColumnName + ' + ' + dfName + '\n' + str(df[column].value_counts(normalize=True)))  ## Percentage


def runAnalysis(df, caseName):
    df_impact = df['software_engineering_impact'].value_counts(normalize=True)
    descriptiveAnalysis(df, 'software_engineering_impact', 'Impact', caseName)

    df_training = df['support_training_on_job'].value_counts(normalize=True)
    descriptiveAnalysis(df, 'support_training_on_job', 'Training', caseName)

    df_credit_hrs = df['support_req_credit_hrs'].value_counts(normalize=True)
    descriptiveAnalysis(df, 'support_req_credit_hrs', 'credit_hrs', caseName)

    df_licensing = df['support_pro_licensing'].value_counts(normalize=True)
    descriptiveAnalysis(df, 'support_pro_licensing', 'Licensing', caseName)