import csv
import pandas

fout = open('age', 'wt')
with open('oscars2.csv', 'rt') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row['age']) < 25:
            print("8-24", file=fout)   
        elif int(row['age']) >= 25 and int(row['age']) < 40:
            print("25-39", file=fout)
        elif int(row['age']) >= 40 and int(row['age']) < 55:
            print("40-54", file=fout)  
        elif int(row['age']) >= 55 and int(row['age']) < 70:
            print("55-69", file=fout)
        elif int(row['age']) >= 70:
            print("70-87", file=fout)
        else:
            print("-----", file=fout)
                            
fout.close()

'''
with open('oscars2.csv', 'rt') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row['age']) < 15:
            print("< 15", file=fout)
        elif int(row['age']) >= 15 and int(row['age']) < 25:
            print("15-25", file=fout)
        elif int(row['age']) >= 25 and int(row['age']) < 35:
            print("25-35", file=fout)
        elif int(row['age']) >= 35 and int(row['age']) < 45:
            print("35-45", file=fout)
        elif int(row['age']) >= 45 and int(row['age']) < 55:
            print("45-55", file=fout)
        elif int(row['age']) >= 55 and int(row['age']) <= 65:
            print("55-65", file=fout)
        elif int(row['age']) > 65:
            print("> 65", file=fout)
        else:
            print("-----", file=fout)
                
'''
