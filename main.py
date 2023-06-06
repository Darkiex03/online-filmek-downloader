import requests
import json

url = "https://filmezek.com/"
btn_string = "Beküldött linkek megtekintése"


def main():
    #filmnev = input("").strip()
    filmnev = "pókember"
    response = request_films(filmnev)
    
    if response.status_code != 200:
        print(response.status_code, " HIBA")

    content = json.loads(response.text)

    list_films(content)

    valasztott = int(input(f"Válassz egyet [0-{len(content)-1}]: "))

    film_url = f"{url}{content[valasztott]['type']}/{content[valasztott]['MovieSlug']}/"
    print(film_url)

    response = requests.get(film_url)
    response = response.text
    
    film_link = 'https://online-filmek.app/film/'
    film_link_index = response.index(film_link) + len(film_link) - 1

    while response[film_link_index+1] != '"':
        film_link_index += 1
        film_link += response[film_link_index]

    print(film_link)


def list_films(json_content):
    for i in range(len(json_content)):
        current = json_content[i]
        print(f"{i}. \t{current['MovieTitle']}")

def request_films(filmnev):
    request_url = url+"searchinput.php?searchType=1&term="+filmnev

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(request_url, headers=headers)
    
    return response

if __name__ == "__main__":
    main()

'''
{
    "MovieTitle": "A csodálatos Pókember",
    "MovieSlug": "a-csodalatos-pokember",
    "MovieTipus": "film",
    "MovieCover": "tt0948470.jpg",
    "type": "online-filmek"
}
'''