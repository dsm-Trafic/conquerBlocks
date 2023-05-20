# # EMPRESA DE ELECTRONICA

import numpy as np

datos = np.array([['2022-01-01', 'Componente 1', 'Lote A', 80],
                ['2022-01-15', 'Componente 1', 'Lote B', 90],
                ['2022-02-01', 'Componente 2', 'Lote C', 85],
                ['2022-01-15', 'Componente 2', 'Lote D', 95],
                ['2022-03-01', 'Componente 1', 'Lote E', 75],
                ['2022-03-15', 'Componente 2', 'Lote F', 90],])

# datos = [fecha], [tipo], [lote], [calidad (0-100)]

## 1. Tipo de componente con calidad más alta

comp_calidad_max = np.argmax(datos[:,3])
print('El componente con la calidad mayor es:', datos[comp_calidad_max, 1])

## 2. Componenetes producidos por mes
print('-------------------------------------------------')
# Array de meses con igual posición a array datos
meses = np.array([mes[5:7] for mes in datos[:, 0]])

# Array de meses únicos
meses_unicos = np.unique(meses)

for mes in meses_unicos:
    meses_filtrados = datos[meses == mes]
    comp_mes = np.sum(meses_filtrados[:,3].astype('int8'))
    print(f'En el mes {mes} se produjeron {comp_mes} componentes')


## 3. Puntuación de calidad promedio por cada componente
print('-------------------------------------------------')
# Array de componentes con igual posición a array datos
componentes = np.array([componente for componente in datos[:,1]])

# Array de componentes únicos
comp_unicos = np.unique(componentes)

for componente in comp_unicos:
    comp_filtrados = datos[componentes == componente]
    comp_calidad_media = np.mean(comp_filtrados[:,3].astype('int8'))
    print(f'Para el componente {componente} la calidad promedio es {comp_calidad_media}')

