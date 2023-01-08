##using giphy api to create and find memes to attach to each email
import requests
import json
import secrets


def generate_meme(search_term):
    # makes a request to giphy api
    response = requests.get(
        f"https://api.giphy.com/v1/gifs/search?api_key={secrets.GIPHY_KEY}&q={search_term}&limit=1&offset=0&rating=G&lang=en")

    # Load the response data into a Python dictionary
    response_data = json.loads(response.text)

    # Get the URL of the first GIF in the search results
    gif_url = response_data['data'][0]['images']['original']['url']

    return gif_url

# searches giphy based upon what you put here
search_term = 'motivation'

# generate a random a meme from giphy
gif_url = generate_meme(search_term)

print(gif_url)

