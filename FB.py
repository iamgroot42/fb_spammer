import time
import requests


def inputz(token):
	go = str(raw_input("Enter event link : "))
	print "Enter message :"
	temp = str(raw_input())
	mess = ""
	i = 0
	while temp!="potato":
		if(i == 1):
			mess = mess + '\n' + temp
  		else:
   			mess = temp
   			i = 1 
  		temp = str(raw_input())
	return mess,go


def read_names(path):
	f = file(path,'r')
	ret = []
	for x in f:
		ret.append(x.split('\n')[0])
	shuffle(ret)
	return ret


def main_spam(mess, go, names, token):
	total = 0
	check = 0
	suc = 0
	base_url = "https://graph.facebook.com/v2.7/"
	suffix = "access_token=" + token
	print 'Spamming ',len(names),' pages'
	for i in names:
  		try:
	  		j = requests.get(base_url + i + "?" + suffix).json()
	  		k = j['id']
	  		payload = {'message': mess, 'link': go}
	  		k = requests.post(base_url + i + "/feed?" + suffix, data = payload)
	  		print 'Done with '+j['name']
	  		time.sleep(5)
	  		suc += 1
	  		if suc >= 100 and check == 0:
	  			check = 1
  			if check == 1:
  				total += suc
  				check = 0
  				suc = 0
			  	token = str(raw_input("Enter ANOTHER access token (limit reached): "))
  				suffix = "access_token=" + token
  				print "Sleeping for 2 minutes "
  				time.sleep(120)
  		except:
  			print "error"
	return total


if __name__ == "__main__":
	token = str(raw_input("Enter access token : "))
	mess,go = inputz(token)
	names = read_names("list")
	print main_spam(mess, go, names, token)
