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
  print "Spammable posts : ",len(idlist)
  nos=input("How many do you want to spam on ? (Recommended : 3-5)")
  idlist.reverse()
  count=0
  for indid in (idlist[(len(idlist)-nos):]):
    facebook.publish(cat="comments",id=indid,message=mess) #Comments on each post
    time.sleep(5)
    print "Commented"
    count+=1

token=str(raw_input("Enter access token : "))
# token="CAACEdEose0cBAIy438fI7okxJU63jIPK6Kb1dRMA3ZBlYWq0PyZC9wSOjsfIi7zi7uQNHYDFZAtVRZAPUIBYzXXh2JZBLGTveWjWnEErtojn825bGD4uF6tsd1ZADjfBUSDow8DV6YRgrDtexqhh04ZBCZB6JJnjzbac46RV1M4MCe49nFKzEmxFNiVZCZBl8AZA4ezvY64EpDyZBzCxob4XQuAo1gTii0PZBmoUZD"
graph = facebook.GraphAPI(token)
go=str(raw_input("Enter event link : "))
# go="https://www.facebook.com/events/1596690117274104/"
print "Enter message :"
temp=str(raw_input())
mess=""
i=0
while temp!="potato":
  if(i==1):
    mess=mess+'\n'+temp
  else:
    mess=temp
    i=1 
  temp=str(raw_input())
# mess="Hurry! Register today before midnight at esya.iiitd.edu.in/pcj"
# profile = graph.get_object("IEEE.org")
# print profile['name']
# print profile
# x=profile['location']['name']

# friends = graph.get_connections("me", "friends")
# for i in friends:
# 	print i['name']
names=["strobotix2","Arduino.Projects.Page","ArduinoPro","official.arduino","roboticsclub.iist","lums.literary.society","EnglishLiterarySocietyKalindi","161130953919582","Grubstreet.kmc","147013968728649","Vivaad2013","Parola.LiteraryHub","EntourageDscDebSoc","LitSoc.TU","DebSoc.SSC","Unesquo","YouthConference13","brainwizmun","srcc.els","sahitya.dtu","MajlisDTS","dictum.shivaji","182759531778657","DelhiUniversityBeat","poetsandwriters","187289351370572","Scrabble","157629567620964","St.GGSHyderabad","131109903588083","christuniversityparliamentarydebate","debsocindia","GrammarUpdates","grammarly","hinducollege","istartcup","innovatedelhi","startupcareers","HerStory.YS","delhistartupsofficial","216994391681424","125437850861195","fantasialiteraryfest13","vituela","Unleashed2013","LitInsignia","gscbitj","csa.bits","196157350399685","pratikpoddarcseblog","CseismDhanbad","hackerrankiiita","interview.street.1","HackerRank.IITD","hackerrankbitspilani","iiith.admissions","CodeSchool","elektronica.iith","PwCAUStudentCareers","techazillion","191084684303805","trollingclasses","iitchicagoinindia","iitpowai","IIT.Kgp","iitgwt","iitdalumni","iitd.delhi","Dance.Society.DTU","delhitechnologicaluniversity","DTUpapersolution","AUV.DTU","petroltuning","ffdtu","nitallahabadindia","1526430094278903","ecell.nsit","EnactusNsit","nsitonline","hrclubnsit","nsitconfessions","csinsit","nsitsolarconcept","crosslinks.nsit","Times.NSIT","nsitqc","jiitofficial","stjosephsschoool","holychildschoolsnp","776008992432916","gomayo","481461865323112","stawberryfieldsworldschool","dpsvn","Prabhu-dayal-public-school","IndraprasthaInternationalSchoolParents","byjusclasses","explosm","Maths-and-Physics-Club-IIT-Bombay","ResurrectSempiternalKindle","248106793203","LinuxQuestions.org","185238108180410","isoeh.in","dpsyamunanagar","dps.sushantlok","383036338431709","dpsind","dpsgmun15","dpskhr","dsswpage","dsm.dtu","163595823823097","242601565902694","3pusaroad","gregorian.delhi","Cabinet.Reloaded","dpsCore","webdesignpinas","HackerifyOfficial","PythonDevelopers","GoPythonDjango","1424345014462852","cplusplus","cpptovlee","Angular","nodejs.vn","BootstrapDesigners","getbootstrap","railstutorial","xaviersdelhi","MyCodeSchool","codeforces","codenation.india","GitHub","codecademy","khanacademy","officialstackoverflow","CodeSchool","TheLinuxFoundation","Trickonics","Er.Fosla","googlecodejam2013","dukhiengineerpage","mysimplereminders","ThousandthoughtsbyRohitkumAr","ScienceAlert","TheObjectivistObserver","epicquotes.in","GirlsWhoCode","iitgwt","IEEE.org","NotShyJustAwkward","iiitdfoobar","prakriti.nitdgp","ExunClan","HackIndiaOfficial","CodeChef.NSIT","Daredevil","ModernFamily","memecenter","moviefone","humansofnewyork","iptrolls","HahaCricketOfficial","OfficialTrollBollywood","Troll.Football","Greenwaytroll","25725614894","TrollTennis","PokemonMemes","amillionredbricksmemes","TheIndianMemes","gameoflaughs","hackerranklnmiit","NIECDelhiHackerRankClub","jaypeehackerrank","hackerrank.iitbbsr","topcoder","HackerEarth","dpsrkpculinaryclub","SpringdalesSchool","PhoneixCSIDTU","IITJEEhelp","crackthejee2015","CarDekho","Bal-Bhavan-Public-School","GeeksforGeeks","Ryan-International-School","Air-Force-Bal-Bharati-School","Amity-International-School-Saket","mcsmun14","NIRMA-UNIVERSITY","TAFSSP","Kulachi-Hansraj-Model-School","BPVMS","stmarksmeerabagh","st.johnsschul","St.Marys09876","DPS-Noida","Kendriya-Vidyalaya-Gole-Market","gyanbharati","dpsvaranasi","MANAV-STHALI-SCHOOL","fiitjeenorthwest","iitkgphe","vidyamandirclasses","xfapsian","HappySchoolNewDelhi","spvdelhi","NewGreenFieldPublicSchoolSaket","gangainternationalschooldhabigujran","SCSNewDelhi","LoretoConventSchoolMumbai","loretoconventgirls","QMSTH","southdelhipublicschool","presidiumschool","TeriUniversityConclave2013","sgtuniversitygurgaon","Amity-University-confessions","thinkdigit","cornitos.in","MotorolaInIndia","ReachIITM","techfest.iitb","Crack.IIT.JEE.Main","sanskritischool","DaisyDalesCosmicSchool","ARMY-Public-SchoolNOIDA","APS.Chandimandir","kvmmsn"]
names2=["TeamKapilSharma","1461944214041429","posdg","ReDevils.Memes","FeelingOfMyHeart","hottestandfamouspersonalitiesofjaipur","photogalaxy.dhiyavasu","99entertainmentsindia",
"900340656671003","privacyindia","650689358383185","654095591323442","ActressIleanaDCruz","chitvsagar","MTVSPLITSVILLA7","DiegoMaradonaOficial","CelebitesPage","ChrisGayleSpartan",
"SurveenChawla","IndiaBakchod","dumbaliafan","jecrcrenaissance","mnitnews","vitcampusjpr","vibrationsbit","oasis.bitspilani","BitsPilaniCampusConnect","PunjabEngineeringCollege",
"103694163002944","217863331602408","rendezvous.iitd","Amity-University-Jaipur-Campsaur","436709079785920","136569053117876","tushar.singh.33","152653471481338","ManipalUniversityJaipur","vostro1000","vitcampusjpr",
"JecrcUniversity","jnujaipur","Anand.International.College.Of.Engineering.Jaipur","297077880485510","techkriti","149655508402372",
"LPUDistanceEducation?fref=ts&rf=109625599064479","219812471388067","ApgShimlaUniversity","ccet.mech.engg.09","PunjabEngineeringCollege",
"bits.hyderabad.9","cogni.iitr","GalgotiasUniversity","jiitofficial","jklu.edu.in","109528019070112","LPUDistanceEducation","krmuniversity",
"amityuni","roorkeerit","glauniv","ManavRachnaInternationalUniversity","MotilalNehruNationalInstituteOfTechnology","142726462504721",
"SDCET","Aurora.IIITM","roorkeerit","141769082528466","Official.IITBHUVaranasi","GurukulkangriUniversity","nitkurukshetra","nitpatna","NIT.UTTARAKHAND","pages/Doon-Institute-of-Engineering-and-technology/624758150928290?fref=ts","riemrohtakcse?fref=ts","BRCMCETBahal?fref=ts","roboticsclub.iist",
"182901205112103","techkriti","antaragni.iitk","130690123609286","pdmgroup","NIT.Srinagar","Aurora.IIITM","JECJabalpur","akgecweb","IEC.greaternoida","IIT.BHU.Varanasi",
"Nitdelhiofficial","itmindia","bitnowandthen","LinuxUsrGrp.ThaparUniversity","iitmhackerrankclub","dsceblr","113174068723373","201001016611599",
"BitsPilaniCampusConnect","IIIT.SriCity","dmunc","110527765642956","amityuni","147697465315269","209705569219214","jumechanicaldept"]
names3=["Heritageit","tiukolkata","techkriti","lpu.in","219812471388067","ApgShimlaUniversity","ccet.mech.engg.09","PunjabEngineeringCollege","tmsgargi",
"111679645587580","436709079785920","jecrcrenaissance","Vivacity.LNMIIT","vitcampusjpr","vibrationsbit","gscbitj","poornimagroup","officialmuj",
"111679645587580","MaharishiArvindGroupOfInstitutes","655917561133559","130346193705183","JaipurMGEC","gomayo","AryanCollegeAjmer",
"smp.mnitjaipur","lpu.in","363581693670681","LinuxUsrGrp.ThaparUniversity","TUEnactus","100146520078252","rietvnp","390711357667892",
"FDDI.Institute.jodhpur","1494337650851415","1652928691590408","307484622635193","324999287602834","124668990992938","139276006137499",
"DrBRAmbedkarNationalInstituteofTechnology","114153365295562","130588257106538","lpu.in","PunjabiUniversityPatialaPunjab","PTUGZS",
"sbsstcFzr","108653845826516","238839049481276","iitbbs","hackerrank.iitbbsr","ReachIITM","Shaastra","769552939828195","techfest.iitb","ecell.in",
"iitpowai","insight.iitbombay","rendezvous.iitd","iitd.delhi","FansOfIndianInstituteOfTechnologyDelhi","IndianInstituteOfTechnologyIitd","iitgwt",
"alcheringaiitg","1458523307791723","iitg.racing","Reflux.iitg","codingclubiitg","iithyderabad","ItJobsHyderabad","iitgnAA","iitjhrclub",
"Science.IITJ","iitjsports","synchronicity.iitk",
"groups/IITKanpurJEE/members/","IIT.Knp","aieseciitkgp","TSG.IITKharagpur","bclubkgp","ktj.iitkgp","ReachIITM","Shaastra","769552939828195","IITMandifacts",
"212340022135020","roorkeerit","cogni.iitr","iitrms.in","bajasaeiitr","236028889879502","iitropar","iitbhumun","DelhiUniversityBeat",
"DUNB.DELHI","IECROCKSTARS","lftdrc","782210305153678","brokenaperture","1414291988877893"]
name=names+names2+names3
#Names2,3 credits : Aashay Mittal
names=set(names) 
suc=0
print 'Spamming ',len(names),' pages'
for i in names:
  try:
  	j=graph.get_object(i)
  	k=j['id']
  	graph.put_object(k, "feed", message=mess, link=go)
    # graph.put_object(k,"feed", message=mess)
  	print 'Done with '+j['name']
  	time.sleep(5)
  	suc+=1
  	spam(k,token,go) #Uncomment this line to spam on comments,not recommended 
  except:
  	print "Error :("  

print "Successfully spammed ",suc," pages"
