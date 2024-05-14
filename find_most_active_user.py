import requests

def fetch_top_starred_repos(num_repos):
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': 'stars:>1',
        'sort': 'stars',
        'order': 'desc',
        'per_page': num_repos
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return [repo['full_name'] for repo in data['items']]
    else:
        print(f"Failed to fetch top {num_repos} starred repositories")
        return []

# Number of top repositories you want to fetch
num_repos = 10
top_repos = fetch_top_starred_repos(num_repos)
print("Top Starred Repositories:")
for repo in top_repos:
    print(repo)
