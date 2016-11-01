import csv
from langdetect import detect

with open('data/petitions.csv', 'r', encoding = 'utf8') as file, open('data/fr_petitions.csv', 'w', encoding = 'utf8') as w_file :
    first_line = file.readline()
    dic_1stline = eval(first_line) #We can trust the string as it is already the transcription of a dic to a str
    writer = csv.DictWriter(w_file, fieldnames= dic_1stline.keys())
    writer.writeheader()
    for i,l in enumerate(file) :
        line = eval(l)
        if i%1000 == 6 :
            print(i)
        try :
            if detect(line['overview']) == 'fr' :
                writer.writerow(line)
        except Exception as e :
            print(e)
            print(i)
            continue