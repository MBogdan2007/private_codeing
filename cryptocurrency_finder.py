from bs4 import BeautifulSoup
import requests
import time
from tqdm import tqdm

count = 0
success = 0

print("Hello! Welcome to the cryptocurrency price finder")
time.sleep(1)
print("To get started, type the name of the currency that you are interested in")

while True:
    if count > 0:
        print("What currency are you looking for this time ?")

    user_crypto = input()
    url = f"https://coinmarketcap.com/currencies/{user_crypto}"
    doc = BeautifulSoup(requests.get(url).text, "html.parser")

    ver = doc.p.string.split()
    val = ''
    for i in ver:
        val += i
        val += ' '

    if val == 'Opps, something went wrong ':
        print("This currency isn't available or doesn't exist")
        time.sleep(1)
        print("Do you want to know what are the most interesting currencies at the moment ? Y/N")
        if input().capitalize()[0] == 'Y':
            print()

            page = "https://coinmarketcap.com/currencies"
            obj = BeautifulSoup(requests.get(page).text, "html.parser")
            body = obj.tbody.contents

            for tr in body[:10]:
                n, p = tr.contents[2:4]
                print(n.p.string)
                print(p.a.string)
                print()

    else:
        success += 1
        price = doc.h1.parent.span.string
        for i in tqdm(range(100)):
            time.sleep(0.01)
        print(f"The current price for {user_crypto[0].capitalize()}{user_crypto[1:]} is {price}")

    count += 1

    time.sleep(1)
    print("Do you want to search for another currency ? Y/N")
    if input().capitalize()[0] != 'Y':
        print()
        print(f"You've searched for {count} currencies and we've succeeded in finding {success}")
        break
