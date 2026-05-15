import argparse
import requests
from bs4 import BeautifulSoup
import lxml

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='WebSecScan')
    parser.add_argument('--url', help='URL of web application to scan')
    parser.add_argument('--output-file', help='file to write scan results to')
    args = parser.parse_args()

    # Send request to web application
    response = requests.get(args.url)

    # Parse HTML response
    soup = BeautifulSoup(response.content, 'lxml')

    # Scan for vulnerabilities
    vulnerabilities = []
    for script in soup.find_all('script'):
        if 'eval' in script.text:
            vulnerabilities.append('Potential XSS vulnerability: ' + script.text)

    # Write scan results to file
    with open(args.output_file, 'w') as f:
        for vulnerability in vulnerabilities:
            f.write(vulnerability + '\n')
