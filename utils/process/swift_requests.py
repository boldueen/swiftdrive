import requests

def download_report():
    response = requests.get('https://swiftdrive.ru/app/customers-reports')
    print(response.text)

download_report()