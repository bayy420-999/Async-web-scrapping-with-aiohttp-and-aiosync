import asyncio, aiohttp, json
from aiohttp import ClientTimeout
from bs4 import BeautifulSoup

async def get_page(session, url):
  async with session.get(url) as r:
    return await r.text()

async def get_all(session, urls):
  tasks = []
  for url in urls:
    task = asyncio.create_task(get_page(session, url))
    tasks.append(task)
  results = await asyncio.gather(*tasks)
  return results

async def main(urls):
  timeout = ClientTimeout(total=600)
  async with aiohttp.ClientSession(timeout = timeout) as session:
    data = await get_all(session, urls)
    return data

def parse(results, filename):
  with open(f'list/{filename}.json', 'w') as f:
    photosets = []
    for html in results:
      soup = BeautifulSoup(html, 'lxml')
      titles = soup.find('title').text
      tags = titles.split()
      urls = [url.attrs['href'] for url in soup.find_all(class_ = 'shortc-button')]
      photosets.append(dict(title = titles, tag = tags[0], url = urls))
    dicts = {"photosets": photosets}
    print(dicts)
    json.dump(dicts, f, indent = 2)

if __name__ == '__main__':
  filename = input('input file: ')
  with open(f'{filename}.txt', 'r') as f:
    urls = f.read().split()
    #print(urls)
    results = asyncio.run(main(urls))
    parse(results, filename)