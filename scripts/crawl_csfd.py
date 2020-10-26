import requests


def run(*args):
    movie_title = "What.Just.Happened.2008.DvDRip-FxM.avi"
    url = f"https://www.csfd.cz/hledat/?q={movie_title}"

    response = requests.get(
        "https://www.csfd.cz/hledat/?q=What.Just.Happened.2008.DvDRip-FxM.avi"
    )
