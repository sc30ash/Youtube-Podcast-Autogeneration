import pandas as pd
from scraper import scrapper
from summarizer import summarizer
from IPython.display import display

def launch_excel_storage_bot():
    topics = {'WORLD':4, 'NATION':5, 'BUSINESS':2, 'ENTERTAINMENT':2, 'SPORTS':3, 'SCIENCE':2, 'HEALTH':2}
    
    news = pd.DataFrame(columns = ['Title', 'Content', 'Summary', 'Keywords'])
    
    for topic in topics.keys():
        headlines, content = scrapper(topic, topics[topic])
        if len(headlines) == 0:
            continue
        for n in range(topics[topic]):
            summary, keywords = summarizer(content[n])
            news.loc[len(news.index)] = [headlines[n], content[n], summary, keywords] 
            
    display(news)
    news.to_csv('daily_news.csv')
    

launch_excel_storage_bot()
        
