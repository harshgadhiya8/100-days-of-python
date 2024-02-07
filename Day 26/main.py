import random
import pandas as pd
# names = ['Harsh','Max','Patel','Gadhiya']
# scores = {name:random.randint(1,100) for name in names}
# print(scores)
students_dict = {'students':['Harsh','Max','Patel','Gadhiya'],
                 'score':[random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]}

student_df = pd.DataFrame(students_dict)
for (index, row) in student_df.iterrows():
    print(row.score)
