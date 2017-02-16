
import urllib.request
from bs4 import BeautifulSoup
import csv

def first_layer(url):
    response = urllib.request.urlopen(url)
    content = response.read()
    soup = BeautifulSoup(content, "html.parser")
    spans = soup.select("span a")
    result = []
    for span in spans:
        result.append(span.contents[0])
        #print(span.contents[0])
    return result
'''
def second_layer(url_list, url):
    result = {}
    with open('dict2.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        time.sleep(2)
        for i in range(len(url_list)):
            url1 = url + "/" + url_list[i]
            response = urllib.request.urlopen(url1)
            content = response.read()
            soup = BeautifulSoup(content, "html.parser")
            lis = soup.select("ul.noTopPadding li a")
            spans = soup.select("ul.noTopPadding li")
            for i in range(len(spans)):
                key = lis[i].contents[0]
                value = spans[i].contents[3]
                result[key] = value
                print("{}: {}".format(key, value))
                writer.writerow([key, value])
    return result
'''
def second_layer(url_list, url):
    result2 = {}
    for i in range(len(url_list)):
        url1 = url + "/" + url_list[i]
        response = urllib.request.urlopen(url1)
        content = response.read()
        soup = BeautifulSoup(content, "html.parser")
        lis = soup.select("ul.noTopPadding li a")
        spans = soup.select("ul.noTopPadding li")
        for i in range(len(spans)):
            key = lis[i].contents[0]
            value = spans[i].contents[3]
            result2[key] = value
            #print("{}: {}".format(key, value))
    del key
    del value
    return result2
'''
def third_layer(url_list, url):
    result = {}
    with open('dict2.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(len(url_list)):
            url1 = url + "/" + url_list[i]
            response = urllib.request.urlopen(url1)
            content = response.read()
            soup = BeautifulSoup(content, "html.parser")
            lis = soup.select("ul.noTopPadding li a")
            for i in range(len(lis)):
                path = url1 + "/" + lis[i].contents[0]
                response1 = urllib.request.urlopen(path)
                content1 = response1.read()
                soup1 = BeautifulSoup(content1, "html.parser")
                spans1 = soup1.select("ul.noTopPadding span a")
                lis1 = soup1.select("ul.noTopPadding li")
                for j in range(len(spans1)):
                    key = spans1[j].contents[0]
                    value = lis1[j].contents[3]
                    result[key] = value
                    print("{}: {}".format(key, value))
                    writer.writerow([key, value])

    return result
'''
def third_layer(url_list, url):
    result3 = {}
    for i in range(len(url_list)):
        url1 = url + "/" + url_list[i]
        response = urllib.request.urlopen(url1)
        content = response.read()
        soup = BeautifulSoup(content, "html.parser")
        lis = soup.select("ul.noTopPadding li a")
        for i in range(len(lis)):
            path = url1 + "/" + lis[i].contents[0]
            response1 = urllib.request.urlopen(path)
            content1 = response1.read()
            soup1 = BeautifulSoup(content1, "html.parser")
            spans1 = soup1.select("ul.noTopPadding span a")
            lis1 = soup1.select("ul.noTopPadding li")
            for j in range(len(spans1)):
                key = spans1[j].contents[0]
                value = lis1[j].contents[3]
                result3[key] = value
                #print("{}: {}".format(key, value))
    del key
    del value
    return result3

#print(first_layer(url))

url = 'http://www.icd10data.com/ICD10CM/Codes'

dict2 = second_layer(first_layer(url), url)

print(type(dict2))

dict3 = third_layer(first_layer(url), url)

print(type(dict3))

with open('dict3.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dict2.items():
       print ("{}: {}".format(key, value))
       writer.writerow([key, value])
    for key, value in dict3.items():
       print ("{}: {}".format(key, value))
       writer.writerow([key, value])



letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

count = 0
for i in range(100):
    for l in letters:
        if i < 10:
            s = l + "0" + str(i)
        else:
            s = l + str(i)
        #print(s)
        if s not in dict3:
            print ("{}: Missing key : {}".format(count,s))
            count +=1

print ("Done!")