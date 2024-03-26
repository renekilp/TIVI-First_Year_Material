import requests


def search_shows(search_term):
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"

    try:
        response = requests.get(url)

        shows = response.json()
        #   tulostetaan haluttu hakutulos
        #    print(f"Ensimmäisen sarjan nimi on: {shows[0]['show']['name']}")
        #   tulostetaan kaikki hakutulokset
        if response.status_code == 200:
            print(f"Haun tulokset hakusanalla {search_term}")
            for show in shows:
                #   haetaan silmukalla
                genres = ""
                for genre in show['show']["genres"]:
                    genres = genres + genre + ", "
                print(f"Sarjan nimi on: {show['show']['name']} ({genres}): {show['show']['url']}")

    except requests.exceptions.RequestException as error:
        print(f"HTTP-pyyte meni pieleen!")
        print(error)

    except Exception as error:
        print(f"HTTP-pyyte meni pieleen!")
        print(error)


search_input = input("Anna hakusana:\n")
search_shows(search_input)
