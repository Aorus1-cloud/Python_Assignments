import pandas as pd

file = "student_performance_ml.csv"

dataset = pd.read_csv(file)

Attendance = dataset["Attendance"]
StudyHours = dataset["StudyHours"]
performance_index = []

for i in range(len(Attendance)):
    performance_index.append((StudyHours[i]*2)+Attendance[i])

dataset.insert(loc=5,value=performance_index,column="PerformanceIndex")

dataset.to_csv(file,index=False,encoding='utf-8',mode='w')