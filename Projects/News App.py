
# ?
import requests
from bs4 import BeautifulSoup
import json
import aiohttp
import asyncio
import tracemalloc
tracemalloc.start()
from markdown import markdown


url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=51aa1d9eebab4d3ebfe873c6fbbeb530"
data = requests.get(url)

news = json.loads(data.text)

async def main():
    if(news['status'] == 'ok'):
        
        async def createRequest (category):
            
            url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&pageSize=20&apiKey=51aa1d9eebab4d3ebfe873c6fbbeb530"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    news = await response.json()
                    print(f"\n\n\t\t\t\t\t{category.capitalize()} - Top Result ({news['totalResults']})\n\n")
                    renderNews(news)
                    
        def renderNews(news):
            
            articles = news['articles']
            for article in articles :
                print('\n')
                print('Title - ', article['title'])
                print('Description - ', article['description'])
                print('Published - ', article['publishedAt'].split('T')[0])
                print('READ MORE - ', article['url'])
                print('\n')

        while(True):
            print("\n\n\t\t\t\t\t News 18 - The ultimate news option 📰\n\n\n")

            print("1. Technology\n2. Business\n3. Entertainment\n4. General\n5. Health\n6. Science\n7. Sports\n\n ")
            
            try:
                choice = int(input("Choose your category of news : "))
            except ValueError:
                print("Enter the valid choice (1 to 7)")

            match choice:
                case 1:
                    await createRequest('technology')
                case 2:
                    await createRequest('business')
                case 3:
                    await createRequest('entertainment')
                case 4:
                    await createRequest('general')
                case 5:
                    await createRequest('health')
                case 6:
                    await createRequest('science')
                case 7:
                    await createRequest('sports')

    else:
        print("Server Error , Check your connection 🌐")
        

asyncio.run(main())
