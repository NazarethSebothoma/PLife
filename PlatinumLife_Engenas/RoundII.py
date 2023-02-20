import pandas as pd
import numpy as np
import json

df_teacher = pd.DataFrame({
    "name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
    "married": [True, True, False, True],
    "school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
})

df_student = pd.DataFrame({
    "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
    "name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino", "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
    "age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
    "height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m']
})


grouped_students = df_student.groupby('teacher')

teachers = []
for teacher, df_students in grouped_students:
    teacher_info = df_teacher[df_teacher['name'] == teacher].to_dict(orient='records')[0]
    students = df_students.drop(columns=['teacher']).to_dict(orient='records')
    teacher_info['students'] = students
    teachers.append(teacher_info)

output = json.dumps(teachers, indent=4)
print(output)
