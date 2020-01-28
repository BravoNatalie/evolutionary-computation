import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

student_fitnessFunction = np.loadtxt('student_fitnessFunction.txt')
#print(student_fitnessFunction)

df = pd.DataFrame.from_records(student_fitnessFunction, columns=["Conceitos_Cobertos", "Dificuldade", "Tempo_Total", "Distribuição_de_Materiais", "Estilo_de_Aprendizagem", "Soma"])
print(df)
