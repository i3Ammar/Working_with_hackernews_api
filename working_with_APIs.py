import requests 
import json 
from operator import itemgetter 

#make an api call , and store the response. 
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# #Explore the structure of the data 
# response_dict = r.json()
# response_string = json.dumps(response_dict, indent= 4)
# print(response_string)

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # make a new api call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"    
    r = requests.get(url)    
    print(f"id: {submission_id}\tstatus: {r.status_code}")    
    response_dict = r.json()
    
    #build a dictionary for each article 
    submission_dict ={
        'title' : response_dict["title"],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments' : response_dict["descendants"]

    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"),
                        reverse = True)
for submission_dict in submission_dicts :
    print(f"\nTitleL {submission_dict['title']}")
    print(f"Discussion Link {submission_dict['hn_link']}")
    print(f"Comment {submission_dict['comments']}")