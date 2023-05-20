# en lista ventas tengo las ventas realizadas los 30 dias de un mes
# quiero conocer las ventas que se realizaron en cada dia de la semana
# sup el primero de mes es lunes 
#(si correspondiera a otro dia lo asignariamos como indice cero de diasSem)

ventas = [120,310,320,330,340,350,360,370,380,390,100,130,140,150,160,170,180,190,200,210,211,220,230,240,250,260,270,280,290,300]
diasSem = ['lun', 'mar', 'mier', 'jue', 'vie', 'sab', 'dom']
vtaxDiaSem = [0,0,0,0,0,0,0]

#distribuyo los elem de la lista ventas en loa elem de la lista vtaxDiaSem 
for i in range(len(ventas)):
    #indiceDia oscilara entre valores del 0 al 6 que permite asociar a cada dia de la semana
    indiceDia = i%7
    print(indiceDia)

    #para cada dia de la semana acumulo venta realizada en ese dia
    vtaxDiaSem[indiceDia] += ventas[i]

print("las ventas diarias realizadas durante el mes clasificadas por dia de semana son:")
for i in range(len(diasSem)):
    print(diasSem[i], vtaxDiaSem[i])
   