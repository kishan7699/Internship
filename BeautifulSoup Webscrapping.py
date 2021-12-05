#!/usr/bin/env python
# coding: utf-8

# # 1. Write a python program to display all the header tags

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[1]:


from bs4 import BeautifulSoup
import requests


# In[3]:


wiki=requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[4]:


wiki


# In[5]:


info=BeautifulSoup(wiki.text,'lxml')


# In[6]:


info


# In[7]:


heading_tags = ["h1", "h2", "h3","h4","h5","h6"]
for tags in info.find_all(heading_tags):
    print(tags.text.strip())


# In[ ]:





# # 2.Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# 

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


imdb=requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")


# In[4]:


imdb


# In[5]:


movie=BeautifulSoup(imdb.content)


# In[6]:


movie


# In[7]:


movies=movie.find_all("h3", class_="lister-item-header")


# In[8]:


movies


# In[9]:


name=[]
for i in movies:
    for j in i.find_all('a'):
        name.append(j.text)


# In[10]:


name


# In[11]:


r=requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt")


# In[12]:


r


# In[13]:


n=BeautifulSoup(r.content)


# In[14]:


n


# In[15]:


m=n.find_all("h3", class_="lister-item-header")


# In[16]:


m


# In[17]:


y=[]
for i in m:
    for j in i.find_all('a'):
        y.append(j.text)


# In[18]:


y


# In[19]:


movie_name=name+y


# In[20]:


len(movie_name)


# In[21]:


RATE=[]
for i in movie.find_all('div', class_="inline-block ratings-imdb-rating"):
    RATE.append(i.text)


# In[22]:


RATE


# In[23]:


C=[]
for i in RATE:
    C.append(i.strip())


# In[24]:


C


# In[25]:


R_a_t_e=[]
for i in n.find_all('div', class_="inline-block ratings-imdb-rating"):
    R_a_t_e.append(i.text)


# In[26]:


F=[]
for i in R_a_t_e:
    F.append(i.strip())


# In[27]:


F


# In[28]:


Rating_=(C+F)


# In[29]:


Rating_


# In[30]:


len(Rating_)


# In[31]:


year=[]
for i in movie.find_all("span", class_="lister-item-year text-muted unbold"):
    year.append(i.text)


# In[32]:


len(year)


# In[33]:


year_=[]
for i in n.find_all("span", class_="lister-item-year text-muted unbold"):
    year_.append(i.text)


# In[34]:


len(year_)


# In[35]:


YEAR=year+year_


# In[36]:


len(YEAR)


# In[37]:


import pandas as pd


# In[38]:


len(movie_name),len(YEAR),len(Rating_)


# In[39]:


ranking=[]
for i in range(1,101):
    ranking.append(i)


# In[40]:


df=pd.DataFrame({'Ranking':ranking,'Name': movie_name,'Year of release':YEAR,'Rating':Rating_})


# In[41]:


df=df.set_index('Ranking')
df


# # 3.  Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release)
# 
# 

# In[50]:


IMDB=requests.get('https://www.imdb.com/india/top-rated-indian-movies/')


# In[51]:


IMDB


# In[52]:


MOVIES=BeautifulSoup(IMDB.content)


# In[53]:


MOVIES


# In[54]:


MOVIE_=MOVIES.find('tbody', class_="lister-list").find_all("tr")


# In[55]:


MOVIE_


# In[56]:


MOVIE_LIST=[]
for i in MOVIE_:
    title=i.find('td', class_="titleColumn").find('a').get_text()
    raw_list=title
    MOVIE_LIST.append(raw_list)

    


# In[57]:


len(MOVIE_LIST)


# In[58]:


year=[]
for i in MOVIE_:
    time=i.find('td', class_="titleColumn").find('span', class_="secondaryInfo").get_text()
    raw_year=time
    year.append(raw_year)

    


# In[59]:


year


# In[60]:


Rating=[]
for i in MOVIE_:
    rate=i.find('td', class_="ratingColumn imdbRating").find('strong').get_text()
    rate=float(rate)
    raw_rating=rate
    Rating.append(raw_rating)


# In[61]:


Rating


# In[62]:


MOVIES_LIST=[]
RATING=[]
YEAR_=[]
for j in MOVIE_LIST[0:100]:
    MOVIES_LIST.append(j)
    
for i in Rating[0:100]:
    RATING.append(i)
for k in year[0:100]:
    YEAR_.append(i)


# In[63]:


MOVIES_LIST


# In[48]:


import pandas as 


# In[64]:


ranking_=[]
for x in range(1,101):
    ranking_.append(x)


# In[65]:


df2=pd.DataFrame({'#Ranking':ranking,'Name':MOVIES_LIST,'Year of release':YEAR_,'Rating':RATING})
df2


# In[66]:


df2=df2.set_index('#Ranking')
df2


# # 4.Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# 

# ## a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating

# In[55]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")


# In[56]:


page


# In[57]:


soup=BeautifulSoup(page.content)
soup


# In[58]:


team1=soup.find('tr', class_="rankings-block__banner").find_all('td', class_="rankings-block__banner--team-name")
team1


# In[60]:


Team=[]
for i in team1:
    for j in i.find_all('span',class_="u-hide-phablet"):
        Team.append(j.text)
        
Team


# In[61]:


team_1=soup.find('tbody').find_all('tr', class_="table-body" )
team_1


# In[62]:


Team_=[]
for i in team_1:
    T=i.find('td', class_="table-body__cell rankings-table__team").find('span', class_="u-hide-phablet").get_text()
    raw_listt=T
    Team_.append(raw_listt)
    
    


# In[63]:


Team_


# In[64]:


TEAMS=Team+Team_


# In[65]:


TEAM=TEAMS[0:10]


# In[66]:


mat=soup.find('tr', class_="rankings-block__banner").find_all('td', class_="rankings-block__banner--matches")


# In[68]:


Match=[]
for i in mat:
    
    Match.append(i.text)
Match        


# In[69]:


match=[]
for i in team_1:
    MT=i.find('td', class_="table-body__cell u-center-text")
    
    match.append(MT.text)
    


# In[70]:


MATCH=Match+match


# In[72]:


MATCHES=MATCH[0:10]
MATCHES


# In[73]:


pnt=soup.find('tr', class_="rankings-block__banner").find_all('td', class_="rankings-block__banner--points")


# In[75]:


point=[]
for i in pnt:
    
    point.append(i.text)
    
point    


# In[77]:


points=[]
for i in team_1:
    for j in i.find_all('td', class_="table-body__cell u-center-text"):
        points.append(j.text)
points        


# In[78]:


point_=points[1:39:2]
point_


# In[79]:


POINTS=point+point_
POINTS


# In[80]:


POINTS__=POINTS[0:10]


# In[81]:


rat=soup.find('tr', class_="rankings-block__banner").find_all('td', class_="rankings-block__banner--rating u-text-right")


# In[82]:


rating=[]
for i in rat:
    rating.append(i.text)


# In[83]:


Rating=[]
for i in rating:
    Rating.append(i.strip())


# In[84]:


Rating_=[]
for i in team_1:
    rt=i.find('td', class_="table-body__cell u-text-right rating")
    
    Rating_.append(rt.text)
    


# In[85]:


Rating__=Rating+Rating_


# In[86]:


R_A_TING=Rating__[0:10]


# In[87]:


ranking=[]
for x in range(1,11):
    ranking.append(x)
    
ranking    
    


# In[2]:


import pandas as pd


# In[89]:


df=pd.DataFrame({'RANKING':ranking,'TEAM':TEAM,"MATCHES":MATCHES,'POINTS':POINTS__,'RATING':R_A_TING})


# In[90]:


df=df.set_index('RANKING')
df


# # b) Top 10 ODI Batsmen in men along with the records of their team and rating.

# In[91]:


page_=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')


# In[92]:


soup_=BeautifulSoup(page_.content)


# In[93]:


soup_


# In[95]:


pyr1=soup_.find('div', class_="rankings-block__top-player").find_all('div', class_="rankings-block__banner--player-info")
pyr1


# In[96]:


pyr1_=[]
for i in pyr1:
    py=i.find('div', class_="rankings-block__banner--name")
    
    pyr1_.append(py.text)
  


# In[97]:


pyr1_


# In[98]:


pyrs=soup_.find('tbody').find_all('tr', class_="table-body")


# In[99]:


players_=[]
for i in pyrs:
    PLS=i.find('td', class_="table-body__cell name").find('a').get_text()
    raw_list=PLS
    players_.append(raw_list)


# In[100]:


players_


# In[102]:


PLAYERS=pyr1_+players_
PLAYERS


# In[104]:


n_t=[]
for i in pyr1:
    ntss=i.find('div', class_="rankings-block__banner--nationality").get_text()
    nta=ntss
    n_t.append(nta)
n_t    


# In[105]:


n_t_ya=[]
for i in n_t:
    n_t_y=i.split()
    
    n_t_ya.append(n_t_y)


# In[106]:


n_t_ya


# In[107]:


nation=[]
for i in n_t_ya:
    h=i[0]
    it=h
    nation=it
    


# In[108]:


nation


# In[109]:


Nation__=[nation]


# In[110]:


nationrrr=[]
for i in pyrs:
    NTN=i.find('td', class_="table-body__cell nationality-logo").find('span', class_="table-body__logo-text").get_text()
    raw_lists=NTN
    nationrrr.append(raw_lists)


# In[112]:


NATION=Nation__+nationrrr
NATION


# In[113]:


R_A_T=[]
for i in pyr1:
    R_T_G=i.find('div', class_="rankings-block__banner--nationality").find('div', class_="rankings-block__banner--rating").get_text()
    raw=R_T_G
    R_A_T.append(raw)
    


# In[114]:


R_A_T


# In[115]:


R_A_T_S_=[]
for i in pyrs:
    r_t_g=i.find('td', class_="table-body__cell u-text-right rating").get_text()
    rawlistt=r_t_g
    R_A_T_S_.append(rawlistt)


# In[116]:


R_A_T_I_N_G=R_A_T+R_A_T_S_


# In[117]:


ranking=[]
for x in range(1,11):
    ranking.append(x)


# In[118]:


df2=pd.DataFrame({'Ranking':ranking,'PLAYERS':PLAYERS,'TEAM':NATION,'RATING':R_A_T_I_N_G})


# In[119]:


df2=df2.set_index('Ranking')
df2


# # c) Top 10 ODI bowlers along with the records of their team and rating.

# In[120]:


P_A_G_E=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')


# In[121]:


P_A_G_E


# In[122]:


SouP=BeautifulSoup(P_A_G_E.content)


# In[123]:


bowler=[]
for i in SouP.find_all('div', class_="rankings-block__banner--name-large"):
    bowler.append(i.text)


# In[124]:


bowler


# In[125]:


for i in SouP.find_all('td', class_="table-body__cell rankings-table__name name"):
    for j in i.find_all('a'):
        bowler.append(j.text)


# In[127]:


pla=bowler[0:10]

pla


# In[128]:


t_e_a_m=[]
for i in SouP.find_all('div', class_="rankings-block__banner--nationality"):
    t_e_a_m.append(i.text)


# In[129]:


t_e_a_m


# In[130]:


TEAMS_=[]
for i in t_e_a_m:
    tn=i.strip()
    TN=tn
    TEAMS_.append(TN)
    


# In[131]:


TEAMS_


# In[132]:


t_e_a_ms=[]
for i in SouP.find_all('td', class_="table-body__cell nationality-logo rankings-table__team"):
    t_e_a_ms.append(i.text)


# In[133]:



for i in t_e_a_ms:
    tn=i.strip()
    TN=tn
    TEAMS_.append(TN)
    


# In[134]:


TEAMS_=TEAMS_[0:10]


# In[135]:


TEAMS_


# In[136]:


RATI=[]
for i in SouP.find_all('div', class_="rankings-block__banner--rating"):
    RATI.append(i.text)


# In[137]:


RATI


# In[138]:


for i in SouP.find_all("td", class_="table-body__cell rating"):
    RATI.append(i.text)


# In[139]:


RATI=RATI[0:10]


# In[140]:


RATI


# In[141]:


rankingb=[]
for x in range(1,11):
    rankingb.append(x)


# In[142]:


dfb=pd.DataFrame({"RANKING":rankingb,"PLAYER":pla,'TEAM':TEAMS_,'RATING':RATI,})


# In[143]:


dfb=dfb.set_index('RANKING')
dfb


# # 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# 

# ## a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating¶

# In[3]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")


# In[4]:


page


# In[5]:


soup=BeautifulSoup(page.content)


# In[6]:


odi=soup.find('tbody').find_all('tr', class_="rankings-block__banner")


# In[7]:


Team_=[]
for i in odi:
    
    T=i.find('td', class_="rankings-block__banner--team-name").find('span', class_="u-hide-phablet").get_text()
    raw_listT=T
    Team_.append(raw_listT)


# In[8]:


odi_=soup.find('tbody').find_all('tr', class_="table-body")


# In[9]:


Team_women=[]
for i in odi_:
    W=i.find('td', class_="table-body__cell rankings-table__team").find('span', class_="u-hide-phablet").get_text()
    raw_listW=W
    Team_women.append(raw_listW)
    


# In[10]:


Team_women


# In[11]:


TEAM=Team_+Team_women


# In[13]:


Team_W=TEAM[:-1]
Team_W


# In[14]:


Team_m=[]
for i in odi:
    
    m=i.find('td', class_="rankings-block__banner--matches").get_text()
    raw_listm=m
    Team_m.append(raw_listm)


# In[15]:


Team_M=[]
for i in odi_:
    for j in i.find_all('td', class_="table-body__cell u-center-text"):
        
        Team_M.append(j.text)
        
Team_M        
        


# In[16]:


tdigi=[]
thdigi=[]
for i in Team_M:
    if len(i)<=2:
        tdigi.append(i)
    elif len(i)>=3:
        thdigi.append(i)


# In[17]:


teamM=tdigi[:-1]


# In[18]:


thdigi


# In[19]:


team_ma=teamM[:-1]


# In[20]:


team_ma


# In[21]:


TEAM_M=Team_m+team_ma


# In[22]:


TEAM_M


# In[23]:


Team_p=[]
for i in odi:
    p=i.find('td', class_="rankings-block__banner--points").get_text()
    raw_listp=p
    Team_p.append(raw_listp)


# In[24]:


TEAM_P=thdigi+Team_p


# In[25]:


Team_r=[]
for i in odi:
    r=i.find('td', class_="rankings-block__banner--rating u-text-right").get_text()
    raw_r=r
    Team_r.append(raw_r)


# In[26]:


Team_R=[]
for i in Team_r:
    Team_R.append(i.strip())


# In[27]:


Team_RR=[]
for i in odi_:
    for j in i.find_all('td', class_="table-body__cell u-text-right rating"):
        Team_RR.append(j.text)


# In[28]:


Team_RRR=Team_RR[:-1]


# In[29]:


TeamRating=Team_R+Team_RRR


# In[30]:


ranking=[]
for x in range(1,11):
    ranking.append(x)


# In[33]:


df=pd.DataFrame({'Ranking':ranking,'Team':Team_W,'Matches':TEAM_M,'Points':TEAM_P,'Rating':TeamRating})


# In[32]:


df=df.set_index('Ranking')
df


# # b)Top 10 women’s ODI players along with the records of their team and rating.¶

# In[34]:


p_a_g_e=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")


# In[35]:


p_a_g_e


# In[36]:


Soup5=BeautifulSoup(p_a_g_e.content)


# In[37]:


playerall=[]
for i in Soup5.find_all('div', class_="rankings-block__banner--name"):
     playerall.append(i.text)


# In[38]:


playerp=[playerall[0]]


# In[39]:


playerall2=[]
for i in Soup5.find_all('td', class_="table-body__cell name"):
    for j in i.find_all('a'):
        playerall2.append(j.text)


# In[40]:


playerp=playerp+playerall2[0:9]


# In[41]:


playerp


# In[42]:


T_Eam=[]
for i in Soup5.find_all('div', class_="rankings-block__banner--nationality"):
     T_Eam.append(i.text)


# In[43]:


T_Eam


# In[44]:


Team9=[T_Eam[0]]
Team9


# In[45]:


TEAM1=[]
for i in Team9:
    tn=i.strip()
    TEAM1.append(tn)


# In[48]:


nation=[]
for i in TEAM1:
    h=i[0]
    it=h
    nation=it
    


# In[49]:


nation__=[]
for i in TEAM1:
    h=i[1]
    it=h
    nation__=it
    


# In[50]:


Team99=[nation+nation__]
Team99


# In[52]:


Team12=[]
for i in Soup5.find_all('td', class_="table-body__cell nationality-logo"):
     Team12.append(i.text)


# In[54]:


TEAM14=[]
for i in Team12:
    tn=i.strip()
    TEAM14.append(tn)


# In[55]:


TEAM13=TEAM14[0:9]


# In[56]:


TEAM13


# In[57]:


TEAM13=Team99+TEAM13


# In[58]:


Ratt=[]
for i in TEAM1:
    h=i[-1]
    it=h
    Ratt=it  


# In[59]:


Ratt1=[]
for i in TEAM1:
    h=i[-2]
    it=h
    Ratt1=it  


# In[60]:


Ratt2=[]
for i in TEAM1:
    h=i[-3]
    it=h
    Ratt2=it  


# In[61]:


RATT=[Ratt2+Ratt1+Ratt]
RATT


# In[62]:


RAT67=[]
for i in Soup5.find_all('td', class_="table-body__cell u-text-right rating"):
     RAT67.append(i.text)


# In[63]:


RATIng=RAT67[0:9]


# In[64]:


RATIng=RATT+RATIng


# In[65]:


rankingww=[]
for x in range(1,11):
    rankingww.append(x)


# In[67]:


df5=pd.DataFrame({"RANKING":rankingww,"PLAYER":playerp,'TEAM':TEAM13,'RATING':RATIng,})


# In[68]:


df5=df5.set_index('RANKING')
df5


# # c)Top 10 women’s ODI all-rounder along with the records of their team and rating.¶

# In[69]:


playerwll=[playerall[2]]


# In[70]:


playerwll2=playerall2[18:27]
playerwll2


# In[71]:


playerwll=playerwll+playerwll2


# In[72]:


T_Eam


# In[73]:


T_e_a_M=[T_Eam[2]]


# In[74]:


na=[]
for i in T_e_a_M:
    h=i[-2]
    it=h
    na=it
    


# In[76]:


TEAM00=[]
for i in T_e_a_M:
    tn=i.strip()
    TEAM00.append(tn)


# In[77]:


naw=[]
for i in T_e_a_M:
    h=i[-3]
    it=h
    naw=it
    


# In[78]:


nab=[]
for i in T_e_a_M:
    h=i[-4]
    it=h
    nab=it


# In[80]:


RAT_ing=[nab+naw+na]
RAT_ing


# In[81]:


Team99


# In[82]:


T_ea_m=TEAM14[18:27]


# In[83]:


T_ea_m=Team99+T_ea_m


# In[84]:


RAT__ING=RAT67[18:27]


# In[85]:


RATTINGG=RAT_ing+RAT__ING
RATTINGG


# In[86]:


rankingsss=[]
for x in range(1,11):
    rankingsss.append(x)


# In[87]:


df6=pd.DataFrame({"RANKING":rankingsss,"PLAYER":playerwll,'TEAM':T_ea_m,'RATING':RATTINGG,})


# In[88]:


df6=df6.set_index('RANKING')
df6


# # 6)Write a python program to scrape details of all the posts from coreyms.com. Scrape the heading, date, content and the code for the video from the link for the youtube video from the post.

# In[89]:


page=requests.get('https://coreyms.com/')


# In[90]:


page


# In[91]:


soup=BeautifulSoup(page.content)
soup


# In[92]:


head=soup.find('main', class_="content").find_all('header', class_="entry-header")


# In[97]:


head_=[]
for i in head:
    hd=i.find('h2', class_="entry-title").find('a', class_="entry-title-link").get_text()
    hds=hd
    head_.append(hds)

head_    


# In[98]:


del head_[4]


# In[99]:


Date_=[]
for i in head:
    DT=i.find('p', class_="entry-meta").find('time', class_="entry-time").get_text()
    dts=DT
    Date_.append(dts)
    


# In[100]:


del Date_[4]


# In[101]:


cont=soup.find('main', class_="content").find_all('div', class_="entry-content")


# In[102]:


cont_=[]
for i in cont:
    CT=i.find('p').get_text()
    ct=CT
    cont_.append(ct)    


# In[103]:


del cont_[4]


# In[104]:


read=soup.find('main', class_="content").find_all('span', class_="embed-youtube")


# In[105]:


video_=[]
for i in read:
    vid=i.find_all('iframe', class_="youtube-player")
    for j in vid:
        video=j.get('src')
        print(video)
        video_.append(video)


# In[106]:


video_


# In[107]:


ranking=[]
for x in range(1,10):
    ranking.append(x)


# In[109]:


df=pd.DataFrame({'Ranking':ranking,'Heading':head_,'Date':Date_,'content':cont_,'VIdeo':video_})


# In[110]:


df=df.set_index('Ranking')
df


# # 7) Write a python program to scrape house details from mentioned URL. It should include house title, location,area,EMI and price from nobroker.in.

# In[42]:


page=requests.get("https://www.nobroker.in/property/sale/bangalore/Electronic%20City?type=BHK4&searchParam=W3sibGF0IjoxMi44N%20DUyMTQ1LCJsb24iOjc3LjY2MDE2OTUsInBsYWNlSWQiOiJDaElKdy1GUWQ0cHNyanNSSGZkYXpnXzhYRW8%20iLCJwbGFjZU5hbWUiOiJFbGVjdHJvbmljIENpdHkifV0=&propertyAge=0&radius=2.0")


# In[43]:


page


# In[44]:


Soup4=BeautifulSoup(page.content)


# In[45]:


Soup4


# In[47]:


flat=Soup4.find('div', id="listCardContainer").find_all('div', class_="nb__2_XSE" )


# In[48]:


flat


# In[49]:


flat_=[]
for i in flat:
    flts=i.find('h2', class_="heading-6 font-semi-bold nb__25Cl7").find('span', itemprop="name").get_text()
    rwfl=flts
    flat_.append(rwfl)
    


# In[50]:


loc_=[]
for i in flat:
    lc=i.find('div', class_="nb__nXU01").find('div', class_="nb__1EwQz").get_text()
    lcr=lc
    loc_.append(lcr)


# In[51]:


emi=[]
for i in flat:
    for j in i.find_all('div', class_="font-semi-bold heading-6"):
        emi.append(j.text)


# In[52]:


emi


# In[53]:


area=emi[0:48:3]


# In[54]:


emi__=emi[1:48:3]


# In[55]:


price=emi[2:49:3]


# In[56]:


serial=[]
for i in range(1,17):
    serial.append(i)


# In[57]:


df9=pd.DataFrame({'serial no.':serial,'Housetitle':flat_,'Location':loc_,'Area':area,'Emi':emi__,'Price':price})


# In[58]:


df9=df9.set_index('serial no.')
df9


# # 8) Write a python program to scrape mentioned details from dineout.co.in :

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[4]:


page


# In[5]:


soup=BeautifulSoup(page.content)


# In[6]:


soup


# In[7]:


resto=soup.find('div',class_="restnt-card-wrap-new").find_all('div', class_="restnt-card restaurant")


# In[8]:


resto_=[]
for i in resto:
    rt=i.find('div', class_="restnt-info cursor").find('a').get_text()
    rts=rt
    resto_.append(rts)


# In[9]:


resto_


# In[10]:


cus=[]
for i in resto:
    cs=i.find('span', class_="double-line-ellipsis").get_text()
    cue=cs
    cus.append(cue)


# In[11]:


cus


# In[12]:


cusine=[]
for i in cus:
    css=i.split("|")[1]
    cu=css
    cusine.append(cu)


# In[13]:


cusine


# In[14]:


loc_=[]
for i in resto:
    lo=i.find('div', class_="restnt-loc ellipsis").get_text()
    locs=lo
    loc_.append(locs)


# In[15]:


loc_


# In[16]:


rat=[]
for i in soup.find_all('div', class_="restnt-rating rating-4"):
    rat.append(i.text)
    


# In[17]:


img=[]
for i in soup.find_all('img',class_="no-img"):
    img.append(i['data-src'])


# In[18]:


img


# In[19]:


import pandas as pd


# In[20]:


serial=[]
for i in range(1,14):
    serial.append(i)


# In[21]:


df=pd.DataFrame({'SERIAL NO.':serial,'NAME':resto_,'CUSINE':cusine,'LOCATION':loc_,'RATING':rat,'IMAGE':img})


# In[22]:


df=df.set_index('SERIAL NO.')
df


# # 9)Write a python program to scrape weather details for last 24 hours from Tutiempo.net :
# i) Hour ii) Temperature iii) Wind iv) Weather condition v) Humidity vi) Pressure

# In[63]:


page=requests.get("https://en.tutiempo.net/delhi.html?data=last-24-%20hours")


#  the request is not working with this certification failed it shows,
# i have also raised ticket and they told me to leave it and show the file in the project

# # 10)Write a python program to scrape monument name, monument description, image URL about top 10 monuments from puredestinations.co.uk.¶

# In[26]:


Page=requests.get("https://www.puredestinations.co.uk/top-10-famous-monuments-to-visit-in-india/")


# In[27]:


Page


# In[28]:


soup=BeautifulSoup(Page.content)


# In[29]:


monu=[]
for i in soup.find_all('p'):
    monu.append(i.text)


# In[30]:


monument=monu[4:-10:3]
monument


# In[32]:


monu_desc=monu[5:-9:3]
monu_desc


# In[33]:


read=soup.select('p')


# In[34]:


images_=[]
for i in read:
    img=i.find_all('img')
    for j in img:
        image=j.get('data-srcset')
        print(image)
        images_.append(image)


# In[35]:


images_


# In[36]:


IMA_GES=images_[0:20:2]
IMA_GES


# In[37]:


ranking=[]
for x in range(1,11):
    ranking.append(x)


# In[38]:


df=pd.DataFrame({'Ranking':ranking,'Names':monument,'Description':monu_desc,'Image url':IMA_GES})


# In[39]:


df=df.set_index('Ranking')


# In[40]:


df


# In[ ]:




