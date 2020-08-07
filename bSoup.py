# User Story

# I want a script that automatically updates a Google Sheets document with Software Engineering jobs from X states 

# This code will be used to fetch Junior Software Engineer jobs from Indeed.comm from a particular 
# state, in the last 14 days.

#  https://www.indeed.com/jobs?q=junior+software+engineer&l=California&jt=fulltime&explvl=entry_level&fromage=14

# Jobs should be 
    # Entry Level
    # Full Time
    # Posted in the last 14 days

# URL Construction
 
# Features
    # Updates code a single .csv // Google Sheets document
    # No repeated entries

# Data Model:
    # Job Title
    # Company
    # Location 
    # Date Posted
    # Application Link

from bs4 import BeautifulSoup
import requests

url = 'https://www.indeed.com/jobs?q=junior+software+engineer&l=Washington&jt=fulltime&explvl=entry_level&fromage=14'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# soup.find_all("p", "title")

jobsList = soup.find_all("div", "result")

# print( len(results) )
for job in jobsList:
    
    title = job.h2.a['title']
    print(title)




# print( results.prettify() )

# print(page.title.name)