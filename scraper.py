from gnews import GNews

def scrapper(topic, n, country='IN'):
    list_of_articles_content = []
    list_of_articles_headlines = []
    
    google_news = GNews(language='en', country=country, period='1d')
    json_resp = google_news.get_news_by_topic(topic=topic)
    if len(json_resp) == 0:
        print('article not found for ')
        print(topic)
        return [],[]
    articles_done = 0
    while(articles_done < n):
        try:
            article = google_news.get_full_article(
                json_resp[articles_done]['url'])
            
            list_of_articles_content.append(article.text.replace('\n', ' ').replace('\r', ''))
            list_of_articles_headlines.append(article.title)
            articles_done +=1
        except:
            continue
    return list_of_articles_headlines, list_of_articles_content

if __name__ == "__main__":
    scrapper('TECHNOLOGY', 3)


    