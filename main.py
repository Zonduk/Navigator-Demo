#формула вычисления дистанции точек - ((x2[0] - x1[0])**2 + (y2[1] - y1[1])**2 ) ** 0.5

#Задаю переменные координат точек

Postal_office = (0, 2)
Griboedov = (2, 5)
Baker_Street = (5, 2)
Wide_garden = (6, 6)
Evergreen_alley = (8, 3) 

x = (Griboedov[0], Baker_Street[0], Wide_garden[0], Evergreen_alley[0]) #Сортирую координаты
y = (Griboedov[1], Baker_Street[1], Wide_garden[1], Evergreen_alley[1]) 

b = 0 #каунтер для номера ячейки
c1 = 0 #1 каунтер для номера наименьшего пути
c2 = 0 #2 каунтер для номера наименьшего пути
c3 = 0 #3 каунтер для номера наименьшего пути
c4 = 0 #4 каунтер для оставшегося номера

first_path = [] #длина пути от почтового отделения
second_path = [] #длина второго пути
third_path = [] #длина третьего пути
fourth_path = [] #длина четвёртого пути
fifth_path = [] #длина пятого пути

true_path = [] #минимальный путь

while b < len(x):                                                             #Цикл для проверки длины пути от точки местоположения
    i = ((x[b] - Postal_office[0])**2 + (y[b] - Postal_office[1])**2 ) ** 0.5
    b += 1
    first_path.append(i)

if b >= len(x):                                      #Проверка на != 0 и наименьшего пути.
    if first_path[0] != 0:
        if first_path[0] < first_path[1]:
            if first_path[0] < first_path[2]:
                if first_path[0] < first_path[3]:
                    true_path.append(first_path[0])
                elif first_path[3] != 0:
                    true_path.append(first_path[3])
                    c1 += 3
                else:
                    true_path.append(first_path[0])            
            elif first_path[2] != 0:
                if first_path[2] < first_path[3]:
                    true_path.append(first_path[2])
                    c1 += 2
                elif first_path[3] != 0:
                    true_path.append(first_path[3])
                    c1 += 3
                else:
                    true_path.append(first_path[2])
                    c1 += 2        
            elif first_path[3] != 0:
                if first_path[3] < first_path[0]:
                    true_path.append(first_path[3])
                    c1 += 3
                else:
                    true_path.append(first_path[0])    
            else:
                true_path.append(first_path[0])                
        elif first_path[1] != 0:            
            if first_path[1] < first_path[2]:
                if first_path[1] < first_path[3]:
                    true_path.append(first_path[1])
                    c1 += 1
                elif first_path[3] != 0:
                    true_path.append(first_path[3])
                    c1 += 3
                else:
                    true_path.append(first_path[1])
                    c1 += 1        
            elif first_path[2] != 0:        
                if first_path[2] < first_path[3]:
                        true_path.append(first_path[2])
                        c1 += 2
                elif first_path[3] != 0:
                    true_path.append(first_path[3])
                    c1 += 3 
                else:
                    true_path.append(first_path[2])
                    c1 += 2
            elif first_path[3] != 0:
                if first_path[3] < first_path[1]:
                    true_path.append(first_path[3])
                    c1 += 3
                else:
                    true_path.append(first_path[1])
                    c1 += 1    
            else:
                true_path.append(first_path[1])
                c1 += 1        
        elif first_path[2] != 0:
            if first_path[2] < first_path[3]:
                true_path.append(first_path[2])
                c1 += 2
            elif first_path[3] != 0:
                true_path.append(first_path[3])
                c1 += 3
            else:
                true_path.append(first_path[2])
                c1 += 2    
        elif first_path[3] != 0:
            if first_path[3] < first_path[0]:
                true_path.append(first_path[3])
                c1 += 3
            else:
                true_path.append(first_path[0])    
        else:
            true_path.append(first_path[0])                  
    elif first_path[1] != 0:
        if first_path[1] < first_path[2]:
            if first_path[1] < first_path[3]:
                true_path.append(first_path[1])
                c1 += 1
            elif first_path[3] != 0:
                true_path.append(first_path[3])
                c1 += 3
            else:
                true_path.append(first_path[1])
                c1 += 1    
        elif first_path[2] != 0:        
            if first_path[2] < first_path[3]:
                true_path.append(first_path[2])
                c1 += 2
            elif first_path[3] != 0:
                true_path.append(first_path[3])
                c1 += 3
            else:
                true_path.append(first_path[2])
                c1 += 2    
        elif first_path[3] != 0:
            if first_path[3] < first_path[1]:
                true_path.append(first_path[3])
                c1 += 3
            else:
                true_path.append(first_path[1])
                c1 += 1
        else:
            true_path.append(first_path[1])
            c1 += 1                        
    elif first_path[2] != 0:
        if first_path[2] < first_path[3]:
            true_path.append(first_path[2])
            c1 += 2
        elif first_path[3] !=0:
            true_path.append(first_path[3])
            c1 += 3
        else:
            true_path.append(first_path[2])
            c1 += 2     
    elif first_path[3] != 0:
        true_path.append(first_path[3])
        c1 += 3 
    else:
        print('Неверный ввод')
                                         

b = 0 # Сбрасываю каунтер для подсчёта ячейки

while b < len(x):                                        #Цикл для проверки длины пути от точки местоположения
    j = ((x[b] - x[c1])**2 + (y[b] - y[c1])**2 ) ** 0.5
    b += 1
    second_path.append(j)

if b >= len(x):                                          #Проверка на != 0 и наименьшего пути.
    if second_path[0] != 0:
        if second_path[0] < second_path[1]:
            if second_path[0] < second_path[2]:
                if second_path[0] < second_path[3]:
                    true_path.append(second_path[0])
                elif second_path[3] != 0:
                    true_path.append(second_path[3])
                    c2 += 3
                else:
                    true_path.append(second_path[0])            
            elif second_path[2] != 0:
                if second_path[2] < second_path[3]:
                    true_path.append(second_path[2])
                    c2 += 2
                elif second_path[3] != 0:
                    true_path.append(second_path[3])
                    c2 += 3
                else:
                    true_path.append(second_path[2])
                    c2 += 2        
            elif second_path[3] != 0:
                if second_path[3] < second_path[0]:
                    true_path.append(second_path[3])
                    c2 += 3
                else:
                    true_path.append(second_path[0])    
            else:
                true_path.append(second_path[0])                
        elif second_path[1] != 0:            
            if second_path[1] < second_path[2]:
                if second_path[1] < second_path[3]:
                    true_path.append(second_path[1])
                    c2 += 1
                elif second_path[3] != 0:
                    true_path.append(second_path[3])
                    c2 += 3
                else:
                    true_path.append(second_path[1])
                    c2 += 1        
            elif second_path[2] != 0:        
                if second_path[2] < second_path[3]:
                        true_path.append(second_path[2])
                        c2 += 2
                elif second_path[3] != 0:
                    true_path.append(second_path[3])
                    c2 += 3 
                else:
                    true_path.append(second_path[2])
                    c2 += 2
            elif second_path[3] != 0:
                if second_path[3] < second_path[1]:
                    true_path.append(second_path[3])
                    c2 += 3
                else:
                    true_path.append(second_path[1])
                    c2 += 1    
            else:
                true_path.append(second_path[1])
                c2 += 1        
        elif second_path[2] != 0:
            if second_path[2] < second_path[3]:
                true_path.append(second_path[2])
                c2 += 2
            elif second_path[3] != 0:
                true_path.append(second_path[3])
                c2 += 3
            else:
                true_path.append(second_path[2])
                c2 += 2    
        elif second_path[3] != 0:
            if second_path[3] < second_path[0]:
                true_path.append(second_path[3])
                c2 += 3
            else:
                true_path.append(second_path[0])    
        else:
            true_path.append(second_path[0])                  
    elif second_path[1] != 0:
        if second_path[1] < second_path[2]:
            if second_path[1] < second_path[3]:
                true_path.append(second_path[1])
                c2 += 1
            elif second_path[3] != 0:
                true_path.append(second_path[3])
                c2 += 3
            else:
                true_path.append(second_path[1])
                c2 += 1    
        elif second_path[2] != 0:        
            if second_path[2] < second_path[3]:
                true_path.append(second_path[2])
                c2 += 2
            elif second_path[3] != 0:
                true_path.append(second_path[3])
                c2 += 3
            else:
                true_path.append(second_path[2])
                c2 += 2    
        elif second_path[3] != 0:
            if second_path[3] < second_path[1]:
                true_path.append(second_path[3])
                c2 += 3
            else:
                true_path.append(second_path[1])
                c2 += 1
        else:
            true_path.append(second_path[1])
            c2 += 1                        
    elif second_path[2] != 0:
        if second_path[2] < second_path[3]:
            true_path.append(second_path[2])
            c2 += 2
        elif second_path[3] !=0:
            true_path.append(second_path[3])
            c2 += 3
        else:
            true_path.append(second_path[2])
            c2 += 2     
    elif second_path[3] != 0:
        true_path.append(second_path[3])
        c2 += 3 
    else:
        print('Неверный ввод')

b = 0 # Снова сбрасываю каунтер

while b < len(x):                                        #Цикл для проверки длины пути от точки местоположения
    k = ((x[b] - x[c2])**2 + (y[b] - y[c2])**2 ) ** 0.5
    b += 1
    third_path.append(k)
    
if b >= len(x):                                          #Проверка на != 0 и наименьшего пути.
    if third_path[0] != 0:
        if third_path[0] < third_path[1]:
            if third_path[0] < third_path[2]:
                if third_path[0] < third_path[3]:
                    true_path.append(third_path[0])
                elif third_path[3] != 0:
                    true_path.append(third_path[3])
                    c3 += 3
                else:
                    true_path.append(third_path[0])            
            elif third_path[2] != 0:
                if third_path[2] < third_path[3]:
                    true_path.append(third_path[2])
                    c3 += 2
                elif third_path[3] != 0:
                    true_path.append(third_path[3])
                    c3 += 3
                else:
                    true_path.append(third_path[2])
                    c3 += 2        
            elif third_path[3] != 0:
                if third_path[3] < third_path[0]:
                    true_path.append(third_path[3])
                    c3 += 3
                else:
                    true_path.append(third_path[0])    
            else:
                true_path.append(third_path[0])                
        elif third_path[1] != 0:            
            if third_path[1] < third_path[2]:
                if third_path[1] < third_path[3]:
                    true_path.append(third_path[1])
                    c3 += 1
                elif third_path[3] != 0:
                    true_path.append(third_path[3])
                    c3 += 3
                else:
                    true_path.append(third_path[1])
                    c3 += 1        
            elif third_path[2] != 0:        
                if third_path[2] < third_path[3]:
                        true_path.append(third_path[2])
                        c3 += 2
                elif third_path[3] != 0:
                    true_path.append(third_path[3])
                    c3 += 3 
                else:
                    true_path.append(third_path[2])
                    c3 += 2
            elif third_path[3] != 0:
                if third_path[3] < third_path[1]:
                    true_path.append(third_path[3])
                    c3 += 3
                else:
                    true_path.append(third_path[1])
                    c3 += 1    
            else:
                true_path.append(third_path[1])
                c3 += 1        
        elif third_path[2] != 0:
            if third_path[2] < third_path[3]:
                true_path.append(third_path[2])
                c3 += 2
            elif third_path[3] != 0:
                true_path.append(third_path[3])
                c3 += 3
            else:
                true_path.append(third_path[2])
                c3 += 2    
        elif third_path[3] != 0:
            if third_path[3] < third_path[0]:
                true_path.append(third_path[3])
                c3 += 3
            else:
                true_path.append(third_path[0])    
        else:
            true_path.append(third_path[0])                  
    elif third_path[1] != 0:
        if third_path[1] < third_path[2]:
            if third_path[1] < third_path[3]:
                true_path.append(third_path[1])
                c3 += 1
            elif third_path[3] != 0:
                true_path.append(third_path[3])
                c3 += 3
            else:
                true_path.append(third_path[1])
                c3 += 1    
        elif third_path[2] != 0:        
            if third_path[2] < third_path[3]:
                true_path.append(third_path[2])
                c3 += 2
            elif third_path[3] != 0:
                true_path.append(third_path[3])
                c3 += 3
            else:
                true_path.append(third_path[2])
                c3 += 2    
        elif third_path[3] != 0:
            if third_path[3] < third_path[1]:
                true_path.append(third_path[3])
                c3 += 3
            else:
                true_path.append(third_path[1])
                c3 += 1
        else:
            true_path.append(third_path[1])
            c3 += 1                        
    elif third_path[2] != 0:
        if third_path[2] < third_path[3]:
            true_path.append(third_path[2])
            c3 += 2
        elif third_path[3] !=0:
            true_path.append(third_path[3])
            c3 += 3
        else:
            true_path.append(third_path[2])
            c3 += 2     
    elif third_path[3] != 0:
        true_path.append(third_path[3])
        c3 += 3 
    else:
        print('Неверный ввод')

b = 0

while b < len(x):                                        #Цикл для проверки длины пути от точки местоположения
    l = ((x[b] - x[c3])**2 + (y[b] - y[c3])**2 ) ** 0.5
    b += 1
    fourth_path.append(l)

if (c1 + c2 + c3) == 5:                                  #Проверка на оставшийся маршрут от местонахождения
    true_path.append(fourth_path[1])
    c4 = 1
elif (c1 + c2 + c3) == 3:
    true_path.append(fourth_path[3])
    c4 = 3
elif (c1 + c2 + c3) == 4:
    true_path.append(fourth_path[2])
    c4 = 2
elif (c1 + c2 + c3) == 6:
    true_path.append(fourth_path[0])
    c4 = 0    

z =((x[c4] - Postal_office[0])**2 + (y[c4] - Postal_office[1])**2 ) ** 0.5  #Финальная формула от конечной точки до стартовой
true_path.append(z)


print(Postal_office, "->", (x[c1],y[c1]),[true_path[0]], "->", (x[c2],y[c2]),[true_path[0] + true_path[1]], "->", 
(x[c3],y[c3]),[true_path[0] + true_path[1] + true_path[2]], "->",
(x[c4],y[c4]),[true_path[0] + true_path[1] + true_path[2] + true_path[3]], "->", 
(Postal_office),[true_path[0] + true_path[1] + true_path[2] + true_path[3] + true_path[4]], "=",
true_path[0] + true_path[1] + true_path[2] + true_path[3] + true_path[4])