# Web scrapper to get the list of beauty shots from IWCOA Marketing portal


from bs4 import BeautifulSoup

URL = open("html/beauty-shots.html")
soup = BeautifulSoup(URL, 'html.parser')


results = soup.find_all(class_="modelno")

filter = ''.join([chr(i) for i in range(1, 32)])
# used to remove the escape characters from strings

beauty_list = []

import csv

for result in results:
    if None in result:
        continue
    results_clean = result.text.translate(str.maketrans('', '', filter))
    beauty_list.append(results_clean)

with open('beatufylist.csv', 'w', newline='\n') as fileloc:
    writer = csv.writer(fileloc, delimiter=',')
    for each in beauty_list:
        writer.writerow([each])