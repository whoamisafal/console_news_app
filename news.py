import requests
import json

newsApi="http://newsapi.org/v2/everything?q=bitcoin&from=2020-11-08&sortBy=publishedAt&apiKey=YourApiKey"
#you can use your newsapi url



class News:
    def __init__(self,url):
        self.url=url

    def getNews(self):
        news=[]
        data=requests.get(self.url).text
        jsondata=json.loads(data)# in dict format
        for d in jsondata["articles"]:
            da= Model(d["author"],d["title"],d["description"],d["urlToImage"],d["publishedAt"],d["url"])
            news.append(da)
            
        return news



class Model:
    def __init__(self,author,title,description,imgUrl,publishedAt,resourceUrl):
        self.author=author
        self.title=title
        self.description=description
        self.imgUrl=imgUrl
        self.publishedAt=publishedAt
        self.resourceUrl=resourceUrl



news= News(newsApi)
d=news.getNews()

for n in d:
    print("author:\t"+(str)(n.author))
    print("title:\t"+(str)(n.title))
    print("Description:\t"+(str)(n.description))
    print("Image url:\t"+(str)(n.imgUrl))
    print("PublishAt:\t"+n.publishedAt)
    print("ResourceUrl:\t"+n.resourceUrl)

