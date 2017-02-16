import urllib.request
from bs4 import BeautifulSoup
import csv

url = 'http://www.icd10data.com/ICD10PCS/Codes'

response = urllib.request.urlopen(url)
content = response.read()
soup = BeautifulSoup(content, "html.parser")
keys = soup.select("div.contentBody div.col-md-10 a")
values = soup.select("div.contentBody div.col-md-10 li")
firstLayer = {}
secondLayer = {}
thirdLayer = {}
fourthLayer = {}
with open('icd10pcs_1.csv', 'w') as csv_file_1, open('icd10pcs_2.csv', 'w') as csv_file_2, open('icd10pcs_3.csv', 'w') as csv_file_3, open('icd10pcs_4.csv', 'w') as csv_file_4:
    writer_1 = csv.writer(csv_file_1)
    writer_2 = csv.writer(csv_file_2)
    writer_3 = csv.writer(csv_file_3)
    writer_4 = csv.writer(csv_file_4)
    for i in range(len(keys)):
        key = str(keys[i].contents[0])
        value = values[i].contents[1]
        print("First Layer - {}: {}".format(key, value))
        writer_1.writerow([key+'\t', value])
        #firstLayer[key] = value

        # Second Layer
        url2 = url + "/" + key
        # print(url2)
        response2 = urllib.request.urlopen(url2)
        content2 = response2.read()
        soup2 = BeautifulSoup(content2, "html.parser")
        keys2 = soup2.select("ul.noTopPadding li a")
        # for key2 in keys2:
        #     print(key2.contents[0])
        values2 = soup2.select("ul.noTopPadding li")
        # for value2 in values2:
        #     print(value2.contents[3])
        for j in range(len(keys2)):
            key2 = str(keys2[j].contents[0])
            value2 = values2[j].contents[3]
            print("Second Layer - {}: {}".format(key2, value2))
            writer_2.writerow([key2+'\t', value2])
            #secondLayer[key2] = value2

            # Third Layer
            url3 = url2 + "/" + key2[-1]
            #print(url3)
            response3 = urllib.request.urlopen(url3)
            content3 = response3.read()
            soup3 = BeautifulSoup(content3, "html.parser")
            keys3 = soup3.select("ul.noTopPadding li a")
            values3 = soup3.select("ul.noTopPadding li")
            for k in range(len(keys3)):
                key3 = str(keys3[k].contents[0])
                value3 = values3[k].contents[3]
                print("Third Layer - {}: {}".format(key3, value3))
                writer_3.writerow([key3+'\t', value3])
                #thirdLayer[key3] = value3

                #FourthLayer
                url4 = url3 + "/" + key3[-1]
                # print(url4)
                response4 = urllib.request.urlopen(url4)
                content4 = response4.read()
                soup4 = BeautifulSoup(content4, "html.parser")
                keys4 = soup4.select("ul.noTopPadding li a")
                values4 = soup4.select("ul.noTopPadding li")
                for l in range(len(keys4)):
                    key4 = str(keys4[l].contents[0])
                    value4 = values4[l].contents[3]
                    print("Fourth Layer - {}: {}".format(key4, value4))
                    writer_4.writerow([key4+'\t', value4])
                    #fourthLayer[key4] = value4



