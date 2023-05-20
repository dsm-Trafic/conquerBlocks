import numpy as np

calificaciones = np.array([[7,8,7,9],[8,9,8,9],[9,7,8,7]])
exam1 = calificaciones[:,0]
exam2 = calificaciones[:,1]
exam3 = calificaciones[:,2]
exam4 = calificaciones[:,3]
#print(calificaciones[:,0])
#print(calificaciones[:,1])
#print(calificaciones[:,2])
#print(calificaciones[:,3])
notaFinal = exam1*0.3 + exam2*0.3 + exam3*0.3 + exam4*0.1
for i in range(len(notaFinal)):
    print(f"la nota final del estudiante {i+1} es: {notaFinal[i]}")