import requests
from bs4 import BeautifulSoup

def get_patients():
    url = "http://127.0.0.1:5000/list"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', id='patient-table')
        rows = table.find_all('tr')[1:] # Skip header
        
        for row in rows:
            cols = row.find_all('td')
            print(f"Scraped -> Name: {cols[0].text}, Doctor: {cols[3].text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_patients()