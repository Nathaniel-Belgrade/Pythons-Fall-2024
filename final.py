#How many articles does the New York Times cover about Microsoft's acquisition deals in the video games
#industry and their consequences on a monthly/yearly basis since the beginning of 1990? Are there any noticeable trends?
import requests
import pandas as pd
import math
import time

API_KEY = 'TMJh6hf0uy6a4akKAOfwJn6GeBnTWufC'

URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

#All the nessecary parameters I want to search with
parameters = {
    'api-key':API_KEY, 
    'q':'Microsoft "video game" acquisition', #I have to put video game in quotes 
    #(or else it'll look for both video and game as separate terms)
    'begin_date':'19900101', #Year, Month, Day, starts at January 1st, 1990
    'end_date':'20241213', #end on today's date of writing this code.
    'fq':'document_type:("article") AND news_desk.contains:("Business", "Technology", "Arts")',
    #Filter for articles only, and that the articles came from these three sections in particular.
    'facet_fields':'pub_year, pub_month',
    #Make sure to find the facet fields for publication year and month
    #This became useless after I realized "pub_date" is something I can find on individual articles.
    'facet':True,
    #First page. Duh.
    'page':0,
    #Start with the oldest articles, from earliest of 1990 onwards.
    'sort':'oldest'
    }

response = requests.get(URL, params = parameters)

content = response.json()

#This is an example of all the dates in the first page of searching.
#This is what we want for all results on all pages.
#for key in (content['response']['docs']):
#    dates.append(key['pub_date'][:10])

def get_hits(url=URL, params=parameters):
    results = requests.get(url,params=params)
    content = results.json()
    response = content.get('response')
    if response:
        meta_hits = response.get('meta').get('hits')
        return meta_hits
    else:
        return None

#Shows all the articles and pages that it would take to go through all of them.
#None and 0 are there in the cases that the API doesn't fetch the numbers when requesting, and breaks the code.
print(get_hits())
if get_hits() == None:
    page_count = 0
else:
    page_count = math.ceil(get_hits()/10)
print(page_count)


def get_content(url=URL, params=parameters):
    results = requests.get(url,params=params)
    try:
        results.raise_for_status()
        content = results.json()
        docs = content.get('response')
        if docs:
            docs = content.get('response').get('docs')
            return docs
        else:
            return None
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occured: {err}")

#This is going to be a list that stores all the dates of articles from the scraping. 
dates = []

#The code used to scrape the pub_date from each article on all pages.
for i in range(page_count):
    parameters['page']=i
    articles = get_content()
    if articles:
        #You don't call the first page "Page 0", you call it "Page 1".
        print(f"printing dates for page {i+1}")
        for date in articles:
            #[:10] gets the year, month, and day the article was released. Nothing extra, like time of day.
            dates.append(date['pub_date'][:10])
        #          This entire piece of code will take about...15 minutes. 
        #           I couldn't make it shorter because it would crash.
        #       Watch a video for a bit, why dontcha? Take care of yourself.
        #                         You earned it.
        #                              [as]
        #(Its an adult swim bumper)
        time.sleep(45)
    else:
        break

#This will store all the nessecary information that will be turned into a csv
analyzed_dates = {
    'year':[],
    'month':[],
    'day':[]
}

#Sorts all the info from the Dates list into 3 categories to be evaluated.
for count in dates:
    analyzed_dates['year'].append(count[0:4])
    analyzed_dates['month'].append(count[5:7])
    analyzed_dates['day'].append(count[8:10])

#This is a dictionary for each month of the year and their individual number.
month_alphabet = {
    '01':'January',
    '02':'February',
    '03':'March',
    '04':'April',
    '05':'May',
    '06':'June',
    '07':'July',
    '08':'August',
    '09':'September',
    '10':'October',
    '11':'November',
    '12':'December'
}

#This piece of code turns the month number into the english name based on the dict above. 
#It's technically unessecary, but it just helps evaulate the data a little better
for i in range(len(analyzed_dates['month'])):
    analyzed_dates['month'][i] = month_alphabet[analyzed_dates['month'][i]]

#This code turns the filtered information into a spreadsheet
#It gets sorted by year of article release, though the original search was done by oldest first...
df = pd.DataFrame(analyzed_dates).sort_values('year')
print(df)
df.to_csv('Microsoft_VG_acquisitions_yearly.csv', index=False)