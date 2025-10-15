import requests

from bs4 import BeautifulSoup

import pandas as pd

import time

import datetime
 
# User-Agent header to mimic a real browser

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'

}
 
urls = [

    'https://upstox.com/stocks/bajaj-finserv-ltd-share-price/INE918I01026/',
    'https://upstox.com/stocks/hdfc-life-ins-co-ltd-share-price/INE795G01014/',
    'https://upstox.com/stocks/sbi-life-insurance-co-ltd-share-price/INE123W01016/',
    'https://upstox.com/stocks/tata-consumer-product-ltd-share-price/INE192A01025/',
    'https://upstox.com/stocks/apollo-hospitals-enter-l-share-price/INE437A01024/',
    'https://upstox.com/stocks/britannia-industries-ltd-share-price/INE216A01030/',
    'https://upstox.com/stocks/adani-enterprises-limited-share-price/INE423A01024/',
    'https://upstox.com/stocks/hero-motocorp-limited-share-price/INE158A01026/',
    'https://upstox.com/stocks/bharat-petroleum-corp-lt-share-price/INE029A01011/',
    'https://upstox.com/stocks/hdfc-bank-ltd-share-price/INE040A01034/',
    'https://upstox.com/stocks/icici-bank-ltd-share-price/INE090A01021/',
    'https://upstox.com/stocks/reliance-industries-ltd-share-price/INE002A01018/',
    'https://upstox.com/stocks/infosys-limited-share-price/INE009A01021/',
    'https://upstox.com/stocks/bharti-airtel-limited-share-price/INE397D01024/',
    'https://upstox.com/stocks/larsen-toubro-ltd-share-price/INE018A01030/',
    'https://upstox.com/stocks/itc-ltd-share-price/INE154A01025/',
    'https://upstox.com/stocks/tata-consultancy-serv-lt-share-price/INE467B01029/',
    'https://upstox.com/stocks/axis-bank-limited-share-price/INE238A01034/',
    'https://upstox.com/stocks/kotak-mahindra-bank-ltd-share-price/INE237A01028/',
    'https://upstox.com/stocks/state-bank-of-india-share-price/INE062A01020/',
    'https://upstox.com/stocks/mahindra-mahindra-ltd-share-price/INE101A01026/',
    'https://upstox.com/stocks/hindustan-unilever-ltd-share-price/INE030A01027/',
    'https://upstox.com/stocks/sun-pharmaceutical-ind-l-share-price/INE044A01036/',
    'https://upstox.com/stocks/hcl-technologies-ltd-share-price/INE860A01027/',
    'https://upstox.com/stocks/maruti-suzuki-india-ltd-share-price/INE585B01010/',
    'https://upstox.com/stocks/ntpc-ltd-share-price/INE733E01010/',
    'https://upstox.com/stocks/tata-motors-limited-share-price/INE155A01022/',
    'https://upstox.com/stocks/titan-company-limited-share-price/INE280A01028/',
    'https://upstox.com/stocks/ultratech-cement-limited-share-price/INE481G01011/',
    'https://upstox.com/stocks/tata-steel-limited-share-price/INE081A01020/',
    'https://upstox.com/stocks/power-grid-corp-ltd-share-price/INE752E01010/',
    'https://upstox.com/stocks/trent-ltd-share-price/INE849A01020/',
    'https://upstox.com/stocks/asian-paints-limited-share-price/INE021A01026/',
    'https://upstox.com/stocks/tech-mahindra-limited-share-price/INE669C01036/',
    'https://upstox.com/stocks/hindalco-industries-ltd-share-price/INE038A01020/',
    'https://upstox.com/stocks/jsw-steel-limited-share-price/INE019A01038/',
    'https://upstox.com/stocks/bharat-electronics-ltd-share-price/INE263A01024/',
    'https://upstox.com/stocks/oil-and-natural-gas-corp-share-price/INE213A01029/',
    'https://upstox.com/stocks/bajaj-auto-limited-share-price/INE917I01010/',
    'https://upstox.com/stocks/shriram-finance-limited-share-price/INE721A01047/',
    'https://upstox.com/stocks/grasim-industries-ltd-share-price/INE047A01021/',
    'https://upstox.com/stocks/grasim-industries-ltd-share-price/INE047A01021/',
    'https://upstox.com/stocks/coal-india-ltd-share-price/INE522F01014/',
    'https://upstox.com/stocks/wipro-ltd-share-price/INE075A01022/',
    'https://upstox.com/stocks/nestle-india-limited-share-price/INE239A01024/',
    'https://upstox.com/stocks/adani-port-sez-ltd-share-price/INE742F01042/',
    'https://upstox.com/stocks/cipla-ltd-share-price/INE059A01026/',
    'https://upstox.com/stocks/dr-reddy-s-laboratories-share-price/INE089A01031/',
    'https://upstox.com/stocks/indusind-bank-limited-share-price/INE095A01012/',
    'https://upstox.com/stocks/eicher-motors-ltd-share-price/INE066A01021/',
]

 
data = []
 
for url in urls:

    try:

        # Fetch the page

        response = requests.get(url, headers=headers)
 
        if response.status_code != 200:

            print(f"Failed to fetch {url}, status code: {response.status_code}")

            continue
 
        soup = BeautifulSoup(response.text, 'html.parser')

        #Adding Date at Excel sheet
        now = (datetime.datetime.now().strftime("%x"))
        print(now)

 
        # Extract company name

        company = soup.find('p', {'class': 'text-[13px] font-medium leading-5 text-[#6A6A6A]'})

        company = company.get_text(strip=True) if company else "N/A"
 
        # Extract price

        price = soup.find('span', {'class': 'text-[32px] font-semibold leading-[42px]'})

        price = price.get_text(strip=True) if price else "N/A"
 
        # Extract change

        change = soup.find('span', {'class': 'text-base font-semibold text-[#148564]'})

        change = change.get_text(strip=True) if change else "N/A"
 
        # Extract "Open" dynamically

        td_elements = soup.find_all('td', {'class': 'flex w-auto items-center justify-between py-4 sm:w-[270px] sm:py-2.5 border-b border-gray-accent2'})
 
        open_value = "N/A"  # Default value
 
        for td in td_elements:

            label_div = td.find('div', {'class': 'text-sm font-medium leading-5 text-gray-accent3'})

            if label_div and 'Open' in label_div.text:  # Checking for "Open"

                value_div = td.find('div', {'class': 'text-sm font-medium leading-5 text-light-black'})

                if value_div:

                    open_value = value_div.text.strip()

                break  # Stop searching once found
 
        print("Open:", open_value)

        # Extract "Close" dynamically

        td_elements = soup.find_all('td', {'class': 'flex w-auto items-center justify-between py-4 sm:w-[270px] sm:py-2.5 border-b border-gray-accent2'})
 
        close_value = "N/A"  # Default value
 
        for td in td_elements:

            label_div = td.find('div', {'class': 'text-sm font-medium leading-5 text-gray-accent3'})

            if label_div and 'Close' in label_div.text:  # Checking for "Close"

                value_div = td.find('div', {'class': 'text-sm font-medium leading-5 text-light-black'})

                if value_div:

                    close_value = value_div.text.strip()

                break  # Stop searching once found
 
        print("Close:", close_value)
 
        # Append data

        data.append([now, company, price, change, open_value, close_value])
 
        print(f"Fetched data for {company}")
 
        # Wait to avoid being blocked

        time.sleep(10)
 
    except Exception as e:

        print(f"Error processing {url}: {e}")
 
# Save to DataFrame

df = pd.DataFrame(data, columns=["Date", "Company", "Price", "Change", "Open", "Close"])
 
# Save to Excel

df.to_excel('stocks.xlsx', index=False)

print("Data saved to stocks.xlsx")

 