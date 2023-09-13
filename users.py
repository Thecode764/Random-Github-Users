import random
import requests


search_query = input("Enter Your Search In Github: ")


response = requests.get(f'https://api.github.com/search/users?q={search_query}')
search_results = response.json()


if 'items' in search_results and len(search_results['items']) > 0:

    random_result = random.choice(search_results['items'])
    
    project_link = random_result['html_url']
    
    print(f"Random User: {project_link}")
else:
    print("No search results found.")