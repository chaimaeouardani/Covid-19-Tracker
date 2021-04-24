from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0'}
info_source = 'https://www.worldometers.info/coronavirus/'


def import_data(info_source):
    data = requests.get(info_source, headers=headers)
    soup = BeautifulSoup(data.content, 'html.parser')

    id = 'main_table_countries_today'


    rows = soup.find_all('tr', attrs={"style": ""})

    data = []

    for i,item in enumerate(rows):

        if i == 0:
            data.append(item.text.strip().lower().split("\n")[1:12])
        elif i == 220:
            break
        else:
            data.append(item.text.strip().lower().split("\n")[:12])

    return data

def find_country(country ,data):
    i=1
    while i<len(data):

        if data[i][1] == country:
            return i
        else:
            i+=1
    return None

def print_data(index,data):
    for k, item in enumerate(data[0]):
        if k == 0 :
            print(country + ' is the country number ' + data[index][0] + ' with the most cases in the world.')
        else:
            print('  -' + item + ' : ' + data[index][k+1])
            if k+2 == len(data[index]):
                break


# main
print('----COVID 19 LIVE TRACKER----')
print()
print('Loading data ...')

data = import_data(info_source)

print('Covid latest information in the world.')
print('          -----------------              ')

# world data
for i in range(1,9):
    print(data[0][i] + ' : ' + data[1][i])

print('')
check_country = input('Do you want to check a country ? [y/n]')

# a country data
if check_country in ('y', 'Y', 'yes', 'YES'):
    asking = True
    while asking:
        country = input('Type a country : ')
        if not country.islower():
            country = country.lower()

        if not find_country(country,data):
            print('There must be a mistake when you typed the country.')
        else:
            pos = find_country(country, data)
            print_data(pos, data)

        print('')
        choice = input('Do you want to look for another country ? [y/n]')
        if choice.lower() in ('n', 'no'):
            quit = input('Are you sure you want to quit ? [y/n]')
            if quit.lower() in ('y', 'yes'):
                asking = False







