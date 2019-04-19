import requests
import traceback
from bs4 import BeautifulSoup


def get_translated_text(text):
    try:
        parameters = {'text': text}
        r = requests.post('https://www.topster.de/deutsch-schwaebisch/', data = parameters)
        soup = BeautifulSoup(r.text, features="html.parser")
        elements = soup.find_all(attrs={"name": "output"})

        if len(elements) > 0:
            output = elements[0]
            return output['value']
        else:
            return text
    except:
        traceback.print_exc()
        return text


if __name__ == '__main__':
    print(get_translated_text('Ich bin arbeiten'))
