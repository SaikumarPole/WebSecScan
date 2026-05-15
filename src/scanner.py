import requests
from bs4 import BeautifulSoup
import lxml

class Scanner:
    def __init__(self, url):
        self.url = url

    def scan(self):
        # Send request to web application
        response = requests.get(self.url)

        # Parse HTML response
        soup = BeautifulSoup(response.content, 'lxml')

        # Scan for vulnerabilities
        vulnerabilities = []
        for script in soup.find_all('script'):
            if 'eval' in script.text:
                vulnerabilities.append('Potential XSS vulnerability: ' + script.text)

        return vulnerabilities
