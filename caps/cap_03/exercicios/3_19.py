import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_links(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        links = []

        for a in soup.find_all("a", href=True):
            absolute = urljoin(url, a["href"])

            if absolute.startswith("http"):
                links.append(absolute)

        return links

    except Exception as e:
        print("Erro ao acessar:", url)
        return []



from collections import deque

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        url, path = queue.popleft()
        print("Explorando:", url)

        if url == goal:
            return path

        if url not in visited:
            visited.add(url)
            for link in get_links(url):
                queue.append((link, path + [link]))

    return None

path = bfs("https://www.youtube.com/watch?v=t-eu6QGFgas&list=RDt-eu6QGFgas&start_radio=1", "https://www.youtube.com/watch?v=53gNFOqDFcE")

if path:
    print("\nCaminho completo:")
    for url in path:
        print(url)

    print("\nPassos:")
    for i in range(len(path)-1):
        print(f"{path[i]}  →  {path[i+1]}")