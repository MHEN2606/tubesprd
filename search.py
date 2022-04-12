from re import L
from thefuzz import fuzz, process
import csv
import os

os.system('cls')
#akses file database_judul
db_judul =[]
with open('./database/database_judul.csv','r') as data:
    csv_read = csv.reader(data,delimiter=';')
    for row in csv_read:
        db_judul.append(row)

#akses file database_kata
db_hubungan = []
with open('./database/hubungan_kata.csv','r') as data_hubungan:
    reader = csv.reader(data_hubungan,delimiter=';')
    for row in reader:
        db_hubungan.append(row)

#skema input
search = str(input("Masukkan artikel yang ingin dicari: "))
split_input = search.split(' ')

#skema cari hubungan kata
search1 = []
search2 = []
for z in range(0,2):
    for i in range(0,len(db_hubungan)):
        for j in range(0,len(db_hubungan[i])):
            if fuzz.partial_ratio(db_hubungan[i][j],split_input[z])>70: #klo kecocokan >70 maka masuk
                if z == 0:
                    search1 = db_hubungan[i]
                elif z == 1:
                    search2 = db_hubungan[i]
                break

#cari array hasil per kata
temp1 = []
temp2 = []
for z in range(0,len(search1)):
    for i in range(1,len(db_judul)):
        for j in range(1,len(db_judul[i])):
            if fuzz.partial_ratio(db_judul[i][j],search1[z])>70: #klo kecocokan >70 maka masuk
                temp1.append(db_judul[i][0])
                break

for z in range(0,len(search2)):
    for i in range(1,len(db_judul)):
        for j in range(1,len(db_judul[i])):
            if fuzz.partial_ratio(db_judul[i][j],search2[z])>70: #klo kecocokan >70 maka masuk
                temp2.append(db_judul[i][0])
                break

#ambil irisan kedua array temp lalu mgabungkan ke array result
result = []
for i in range(0,len(temp1)):
    for j in range(0,len(temp2)):
        if temp1[i] == temp2[j]:
            result.append(temp1[i])

#output result
print("Artikel relevan : ")
for i in range(0,len(result)):
    print(result[i])