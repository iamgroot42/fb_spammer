# -*- coding: utf-8 -*-
import json
import time
import facebook #sudo pip install facebook
import fb  #sudo pip install fb 
from facepy import GraphAPI #sudo pip install facepy

#Reference : https://github.com/kirankaranth1/facebook-comment-spammer/blob/master/FB_commentSpam.py
def spam(x,token,mess):
  facebook=fb.graph.api(token)
  graph1 = GraphAPI(token)
  query=x+"/posts?fields=id&limit=5000000000"
  r=graph1.get(query)
  idlist=[y['id'] for y in r['data']]
  # print "Available posts ",len(idlist)
  # nos=input("Enter number of posts to be spammed with comments: ")
  nos=min(len(idlist),3)
  # idlist.reverse()
  count=0
  for indid in (idlist[(len(idlist)-nos):]):
    facebook.publish(cat="comments",id=indid,message=mess) #Comments on each post
    time.sleep(5)
    count+=1

token=str(raw_input("Enter token ID : "))
# token="CAACEdEose0cBAIy438fI7okxJU63jIPK6Kb1dRMA3ZBlYWq0PyZC9wSOjsfIi7zi7uQNHYDFZAtVRZAPUIBYzXXh2JZBLGTveWjWnEErtojn825bGD4uF6tsd1ZADjfBUSDow8DV6YRgrDtexqhh04ZBCZB6JJnjzbac46RV1M4MCe49nFKzEmxFNiVZCZBl8AZA4ezvY64EpDyZBzCxob4XQuAo1gTii0PZBmoUZD"
graph = facebook.GraphAPI(token)
go=str(raw_input("Enter event link : "))
# go="https://www.facebook.com/events/1596690117274104/"
print "Enter message :"
mess=str(raw_input())
# mess="Hurry! Register today before midnight at esya.iiitd.edu.in/pcj"
# profile = graph.get_object("IEEE.org")
# print profile['name']
# print profile
# x=profile['location']['name']

# friends = graph.get_connections("me", "friends")
# for i in friends:
# 	print i['name']
names=["stjosephsschoool","holychildschoolsnp","776008992432916","gomayo","481461865323112","stawberryfieldsworldschool","dpsvn","Prabhu-dayal-public-school","IndraprasthaInternationalSchoolParents","byjusclasses","explosm","Maths-and-Physics-Club-IIT-Bombay","ResurrectSempiternalKindle","248106793203","LinuxQuestions.org","185238108180410","isoeh.in","dpsyamunanagar","dps.sushantlok","383036338431709","dpsind","dpsgmun15","dpskhr","dsswpage","dsm.dtu","163595823823097","242601565902694","3pusaroad","gregorian.delhi","Cabinet.Reloaded","dpsCore","webdesignpinas","HackerifyOfficial","PythonDevelopers","GoPythonDjango","1424345014462852","cplusplus","cpptovlee","Angular","nodejs.vn","BootstrapDesigners","getbootstrap","railstutorial","xaviersdelhi","MyCodeSchool","codeforces","codenation.india","GitHub","codecademy","khanacademy","officialstackoverflow","CodeSchool","TheLinuxFoundation","Trickonics","Er.Fosla","googlecodejam2013","dukhiengineerpage","mysimplereminders","ThousandthoughtsbyRohitkumAr","ScienceAlert","TheObjectivistObserver","epicquotes.in","GirlsWhoCode","iitgwt","IEEE.org","NotShyJustAwkward","iiitdfoobar","prakriti.nitdgp","ExunClan","HackIndiaOfficial","CodeChef.NSIT","Daredevil","ModernFamily","memecenter","moviefone","humansofnewyork","iptrolls","HahaCricketOfficial","OfficialTrollBollywood","Troll.Football","Greenwaytroll","25725614894","TrollTennis","PokemonMemes","amillionredbricksmemes","TheIndianMemes","gameoflaughs","hackerranklnmiit","NIECDelhiHackerRankClub","jaypeehackerrank","hackerrank.iitbbsr","topcoder","HackerEarth","dpsrkpculinaryclub","SpringdalesSchool","PhoneixCSIDTU","IITJEEhelp","crackthejee2015","CarDekho","Bal-Bhavan-Public-School","GeeksforGeeks","Ryan-International-School","Air-Force-Bal-Bharati-School","Amity-International-School-Saket","mcsmun14","NIRMA-UNIVERSITY","TAFSSP","Kulachi-Hansraj-Model-School","BPVMS","stmarksmeerabagh","st.johnsschul","St.Marys09876","DPS-Noida","Kendriya-Vidyalaya-Gole-Market","gyanbharati","dpsvaranasi","MANAV-STHALI-SCHOOL","fiitjeenorthwest","iitkgphe","vidyamandirclasses","xfapsian","HappySchoolNewDelhi","spvdelhi","NewGreenFieldPublicSchoolSaket","gangainternationalschooldhabigujran","SCSNewDelhi","LoretoConventSchoolMumbai","loretoconventgirls","QMSTH","southdelhipublicschool","presidiumschool","TeriUniversityConclave2013","sgtuniversitygurgaon","Amity-University-confessions","thinkdigit","cornitos.in","MotorolaInIndia","ReachIITM","techfest.iitb","Crack.IIT.JEE.Main","sanskritischool","DaisyDalesCosmicSchool","ARMY-Public-SchoolNOIDA","APS.Chandimandir","kvmmsn"]
# names=set(names) 
print 'Spamming ',len(names),' pages'
for i in names:
  try:
  	j=graph.get_object(i)
  	k=j['id']
  	graph.put_object(k, "feed", message=mess, link=go)
    # graph.put_object(k,"feed", message=mess)
  	print 'Done with '+j['name']
  	time.sleep(5)
  	# spam(k,token,go) #Uncomment this line to spam on comments,not recommended 
  except:
  	print "Error :("  

