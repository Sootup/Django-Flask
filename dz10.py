import csv
import datetime

############################  1
# table = [("Имя","Фамилия","Возраст"),
# ["имя1","фамилия1",20],
# ["имя2","фамилия2",24],
# ["имя3","фамилия3",55],
# ["имя4","фамилия4",34]
# ]

# with open("10dz.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerows(table)




# def search_by_age():
#     from1_to12 = 0
#     from13_to18 = 0
#     from19_to25 = 0
#     from40 = 0
#     with open("10dz.csv", "r") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             if row[2].isdigit():
#                 row[2] = int(row[2])
#                 if 1 <= row[2] and row[2] <= 12:
#                     if from1_to12 == 0:
#                         from1_to12 = 1
#                     else:
#                         from1_to12 += 1
#                 if 13 <= row[2] and row[2] <= 18:
#                     if from13_to18 == 0:
#                         from13_to18 = 1
#                     else:
#                         from13_to18 += 1 
#                 if 19 <= row[2] and row[2] <= 25:
#                     if from19_to25 == 0:
#                         from19_to25 = 1
#                     else:
#                         from19_to25 += 1
#                 if 26 <= row[2]:
#                     if from40 == 0:
#                         from40 = 1
#                     else:
#                         from40 += 1


#     return from1_to12,from13_to18,from19_to25,from40
                
# from1_to12,from13_to18,from19_to25,from40 = search_by_age()
            
# print(from1_to12,from13_to18,from19_to25,from40)

######################################3 2

pogoda = [("Дата" ,"Место" ,"Градусы" ,"Скорость ветра"),
["28.07","Минск",22,2.5],
["29.07","Минск",21,3,1],
["30.07","Минск",23,2.3],
["31.07","Минск",24,0.7],
["1.08","Минск",27,1.5],
["2.08","Минск",22,2.1],
["3.08","Минск",25,0.3],
]


with open("10dzpogoda.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(pogoda)

    
def sredn(file_name):
    veter = 0
    veter_kolvo = 0

    gradus = 0
    gradus_kolvo = 0

    with open(f'{file_name}.csv', 'r') as file :
        reader = csv.reader(file)
        firstline = True
        for row in reader:
            if firstline:
                firstline = False
                continue
            if row[2]:
                row[2] = int(row[2])
                gradus += row[2]
                gradus_kolvo += 1
            if row[3]:
                row[3] = float(row[3])
                veter += row[3]
                veter_kolvo += 1
    sr_veter = veter / veter_kolvo
    sr_gradus = gradus / gradus_kolvo
    return sr_gradus, sr_veter
sr_gradus, sr_veter = sredn("10dzpogoda")
print(sr_gradus, sr_veter)
