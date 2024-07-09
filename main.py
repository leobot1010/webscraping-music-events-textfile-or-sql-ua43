import requests
import selectorlib
import smtplib, ssl
from email.message import EmailMessage
import time


URL = "https://programmer100.pythonanywhere.com/tours"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """ Scrape the page source from the url parameter"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    """ Filter out the specific tours information from the entire scraped data  """
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']
    return value

def send_email(tour_info):
    """ Send email with details of new tour info """
    host = "smtp.gmail.com"
    port = 465

    sender = "leobot1010@gmail.com"
    password = 'vuihokpyyfphutnc'

    receiver = 'kieran303@hotmail.com'
    # receiver = 'leobot1010@gmail.com'

    context = ssl.create_default_context()

    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = 'New Tour Announced'
    em.set_content(tour_info)


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, em.as_string())

    print("Email was sent")


def store_data(extracted):
    """ Append the new tour info into the text file"""
    with open("data.txt", "a") as f:
        f.write(extracted + "\n")


def read_data():
    """ Open the text file"""
    with open("data.txt", "r") as f:
        return f.read()


if __name__ == '__main__':
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)

        if extracted != "No upcoming tours":
            stored_data = read_data()
            print(stored_data)
            if extracted not in stored_data:
                store_data(extracted)
                send_email(extracted)
        time.sleep(5)
        print(extracted)



