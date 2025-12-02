from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
headers = {'User-Agent': 'greta.tautaviciute@gmail.com)'}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)

# find_table = soup.find_all('table')[1]
# print(find_table)

table = soup.find_all('table')[0]
# print(table)

world_titles = table.find_all('th')
# print(world_titles)

world_table_titles = [title.text.strip() for title in world_titles]
# print(world_table_titles)


df = pd.DataFrame(columns = world_table_titles)
print(df)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)

    length = len(df)
    df.loc[length] = individual_row_data

csv = df.to_csv(r'C:\Users\greta\Desktop\Companies.csv', index=False)
