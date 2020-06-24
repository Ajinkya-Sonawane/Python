import requests
from bs4 import BeautifulSoup
profile_urls = [] #To store the Profile URLs
ctr = 0 #To traverse through Google results pages

#Loop through first 15 pages 
#(10 per page, so count 15*10=150)
while ctr < 150:
  query = 'https://google.com/search?q=site:linkedin.com/in \
      AND "Technical Recruiter" AND "Pune"&start='+str(ctr)
  
  response = requests.get(query)
  soup = BeautifulSoup(response.text,'html.parser')
  for anchor in soup.find_all('a'):
    url = anchor["href"]
    if 'https://www.linkedin.com/' in url:
      url = url[7:url.find('&')]
      profile_urls.append([url])
      print(url)
  ctr = ctr+10




  