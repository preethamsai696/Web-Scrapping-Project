from posixpath import split
from turtle import home
from urllib import request
import requests
import lxml
import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


class webscrapping():
    def __init__(self,url):
        self.url_ = url

        def Run(url):
            response = requests.get(url)
            print(response)
            soup = BeautifulSoup(response.text,"lxml")

            name_pattern = re.compile("\w+\s\w+[,]\s\w+[,]\s\w+\sProfessor|\w+\s\w+[-]\w+[,]\s\w+[,]\s\w+\sProfessor|\w+\s\w+[,]\sInstructor")
            first_name = []
            last_name = []
            title = []
            for prof in soup.find('div', class_ = "col-sm-12 two-col"):
                for info in prof.stripped_strings:
                    name = re.findall(name_pattern,info)
                    if len(name)>0:
                        name1 = name[0].split(',')
                        name2 = name1[0].split(' ')
                        first_name.append(name2[0])
                        last_name.append(name2[1])
                        title.append((name1[0:][-1].strip()))

            home_page = []
            h = []
            for prof in soup.find('div', class_ = "col-sm-12 two-col").find_all(href=True):
                h.append(prof['href'])
            for i in range(len(h)):
                if i%2==0:
                    continue
                else:
                    home_page.append(h[i])         

            df1 = pd.DataFrame({'firstname':first_name,'lastname':last_name,'title':title,'homepage':home_page})

#---------------------------------------------------------------------------------------------------------------------

            l = []
            first_names = []
            last_names = []
            titles = []
            for profs in soup.find('div',class_ = "js-view-dom-id-47d66a3c43c715f33fd4f63d56b9dcda66a61c86b8a3eab8b2d0b20a4b0b2a80"):
                for info in profs.stripped_strings:
                    l.append(info)
    
            for i in range(len(l)):
                if i%3==0:
                    a = l[i].split(' ')
                    if a[0][1]=='.':
                        first_names.append(a[1])
                    else:
                        first_names.append(a[0])
                    last_names.append(a[-1])

            n = np.arange(1,144,3)
            for j in n:
                titles.append((l[j].strip()))
            
            home_pages = []
            for profs in soup.find('div',class_= "js-view-dom-id-47d66a3c43c715f33fd4f63d56b9dcda66a61c86b8a3eab8b2d0b20a4b0b2a80").find_all(href=True):
                link = "https://schulich.ucalgary.ca"
                home_pages.append(link+profs['href'])

            df2 = pd.DataFrame({'firstname':first_names,'lastname':last_names,'title':titles,'homepage':home_pages})

#----------------------------------------------------------------------------------------------------------------------

            office = []
            phone_number = []
            for i in df1['homepage']:
                request = requests.get(i)
                soup = BeautifulSoup(request.text,"lxml")
                try:
                    loc =  soup.find_all(class_ = "contact-section col-sm-4")
                    loc1 = loc[-1].p.a.text
                    office.append(loc1)

                except:
                    office.append(np.nan)
        
                try:
                    loc =  soup.find_all(class_ = "contact-section col-sm-4")
                    loc2 = loc[-2].p.a.text
                    phone_number.append(loc2)
                except:
                    phone_number.append(np.nan)

            df1['phone_number'] = phone_number
            df1['office'] = office

#-----------------------------------------------------------------------------------------------------------------------

            office1 = []
            phone_number1 = []

            for j in df2['homepage']:
                request = requests.get(j)
                soup = BeautifulSoup(request.text,"lxml")
                try:
                    loc = soup.find_all(class_ = "col-md-6")
                    office1.append(loc[-1].div.div.a.text)
                except:
                    office1.append(np.nan)

                try:
                    loc = soup.find_all(class_ = "col-md-6")
                    loc1 = loc[-2].find_all('div')
                    phone_number1.append(loc1[1].div.a.text)
                except:
                    phone_number1.append(np.nan)
            
            df2['phone_number'] = phone_number1
            df2['office'] = office1
    
            frames = [df1,df2]
            df = pd.concat(frames,ignore_index=True)
            df.to_csv("/Users/preethamsai/Documents/U of C/SEM3/Intro to Digital Engineering - ENGG 680/MidTerm/ENGG680_Midterm/data/uofc_prof.csv")
            df3 = df['title'].value_counts().to_frame()
            df3.to_csv("/Users/preethamsai/Documents/U of C/SEM3/Intro to Digital Engineering - ENGG 680/MidTerm/ENGG680_Midterm/data/generated_report.csv")

            return df
    
        Run(url)