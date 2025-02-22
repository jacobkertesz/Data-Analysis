import pandas as pd

def main():
    dataFile = pd.read_csv("sleep_deprivation_dataset_detailed.csv")

    #Question 1:
    #Is sleep time directly correlated with performance?

    #'Participant_ID', 'Sleep_Hours', 'Sleep_Quality_Score', 'Daytime_Sleepiness', 'Stroop_Task_Reaction_Time', 'N_Back_Accuracy', 
    #'Emotion_Regulation_Score', 'PVT_Reaction_Time', 'Age', 'Gender', 'BMI', 'Caffeine_Intake', 'Physical_Activity_Level', 'Stress_Level'
    columnNames = dataFile.columns.tolist() 
    
    hours = columnNames[1] #Sleep_Hours
    daySleep = columnNames[3] #Daytime_Sleepiness
    stroop = columnNames[4] #Stroop_Task_Reaction_Time
    nBack = columnNames[5] #N_Back_Accuracy
    emoReg = columnNames[6] #Emotion_Regulation_Score
    reTime = columnNames[7] #PVT_Reaction_Time
    stressLvl = columnNames[13] #Stress_Level

    #Sleep_Hours to Daytime_Sleepiness
    showCorrelation(dataFile, hours, daySleep)

    #Sleep_Hours to Stroop_Task_Reaction_Time
    showCorrelation(dataFile, hours, stroop)

    #Sleep_Hours to N_Back_Accuracy
    showCorrelation(dataFile, hours, nBack)

    #Sleep_Hours to Emotion_Regulation_Score
    showCorrelation(dataFile, hours, emoReg)

    #Sleep_Hours to PVT_Reaction_Time
    showCorrelation(dataFile, hours, reTime)

    #Sleep_Hours to Stress_Level
    showCorrelation(dataFile, hours, stressLvl)

    #Question 2:
    #Is there a noticable difference between higher and lower half of the sleep data?

    numRows = len(dataFile)
    mid = numRows // 2
    sorted_df_hours = dataFile.sort_values(by=[hours])

    showSplitDescription(mid, sorted_df_hours, stroop)
    showSplitDescription(mid, sorted_df_hours, nBack)
    showSplitDescription(mid, sorted_df_hours, emoReg)
    showSplitDescription(mid, sorted_df_hours, reTime)


def showSplitDescription(mid, df, column):
    firstDesc = df[column].head(mid)
    lastDesc = df[column].tail(mid)

    print(firstDesc.describe())
    print(lastDesc.describe())
    print()


def showCorrelation(df, n1, n2):
    corr = getCorrelation(df, n1, n2)
    print(f'{n1} -- {n2}: {corr}')


# Will find the correlation between column1 and 2
def getCorrelation(df, column1, column2):
    size = df[column1].size
    sumC1 = df[column1].sum()
    sumC2 = df[column2].sum()
    sumC1C2 = sumOfProd(df[column1], df[column2])
    sumC1sq = sumOfSquare(df[column1])
    sumC2sq = sumOfSquare(df[column2])

    corrCoef = equateCorrelation(size, sumC1, sumC2, sumC1C2, sumC1sq, sumC2sq)
    return corrCoef


#Returns the sum of the product of each entry in c1 and c2
def sumOfProd(c1, c2):
    sumC1C2 = 0
    i = 0
    while i < c1.size:
        sumC1C2 = sumC1C2 + (c1.iloc[i] * c2.iloc[i])
        i=i+1
    return sumC1C2


#Returns the sum of each entry in c after the entry is squared
def sumOfSquare(c):
    sumSquare = 0
    i = 0
    while i < c.size:
        sumSquare = sumSquare + (c.iloc[i] ** 2)
        i=i+1
    return sumSquare


def equateCorrelation(n, x, y, xy, x2, y2):
    answer = ((n * xy) - (x * y)) / ((((n * x2) - (x ** 2)) * ((n * y2) - (y ** 2))) ** 0.5) #Pearson correlation coefficient formula
    return answer


#getCorrelation test
def testGetCorrelation():
    d = {'col1': [1,2,3,4,5,6,7,8,9,10], 'col2': [10,20,30,40,50,60,70,80,90,100]}
    df = pd.DataFrame(data= d)
    r = getCorrelation(df, 'col1', 'col2')
    print(r) # r should be 1


main()