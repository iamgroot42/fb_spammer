import time
import requests


def get_info(token):
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
	return ret


def main_spam(mess, go, names, token):
	base_url = "https://graph.facebook.com/v2.7/"
	suffix = "access_token=" + token
	print 'Spamming ',len(names),' pages'
	for i in names:
  		try:
	  		j = requests.get(base_url + i + "?" + suffix).json()
	  		k = j['id']
	  		payload = {'message': mess, 'link': go}
	  		k = requests.post(base_url + i + "/feed?" + suffix, data = payload)
	  		print k.text
	  		print 'Done with '+j['name']
	  		time.sleep(15)
  		except Exception, e:
  			print e
  			print "error"


if __name__ == "__main__":
	token = str(raw_input("Enter access token : "))
	mess,go = get_info(token)
	names = read_names("list")
	main_spam(mess, go, names, token)
	print "Spamming done!"
