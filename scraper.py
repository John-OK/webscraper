from bs4 import BeautifulSoup
import requests
import csv

url = 'https://remnantfromtheashes.wiki.fextralife.com/Weapon+Mods#List'
req = requests.get(url)
print(req)
soup = BeautifulSoup(req.text, "html.parser")

table = soup.find("table", class_ = "wiki_table sortable")
rows = table.find_all("tr")
# print(rows)

headers = []
for row in rows[0]:
    if row.text.strip() != '':
        headers.append(row.text.strip( ))
print(headers)

table_values = []
for row in rows[1:]:
    row_values = []
    for col in row:
        if col.text.strip() != '':
          row_values.append(col.text.strip())
    table_values.append(row_values)
print(table_values[:2])

with open('remnant_scraped_data.csv', mode='w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for row in table_values:
        writer.writerow(row)

