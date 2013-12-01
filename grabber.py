#sample link to img = "http://cdn12.lbstatic.nu/files/looks/large/2013/06/09/3092823_lookbook.jpg?1370749303"

import unirest,re,urllib

d = {} #links dictionary
lpp = 34 #n of max looks per page = 34
nl = 0 #number of looks

def getpage(i):
	response = unirest.get("http://lookbook.nu/user/3106150-Antonio-C/looks/loved", params={ "page": i })
	return response.body

#np = number of pages
def getlinks(np):
	print 'getting links...'
	for c in range(1,np):
		site = getpage(c)
		links = re.findall(r'\"http://cdn\d\d.lbstatic.nu/files/looks/large.+\"', site)
		d[c] = links
		'''for link in links:
			print link, "\n"'''
			
def savelinks():
	j = 0 #jpg counter
	print 'saving pictures from looks in ./img folder...'
	for links in d:
		'''for link in d[links]:
			#print link, "\n"'''
		for link in d[links]:
			try:
				urllib.urlretrieve(link.replace('"',''),"./img/{0}.jpg".format(j))
				j += 1
			except Exception, e:
				print 'error saving links: ' + str(e)

site = getpage(1) #get first page 

match = re.search(r'class=\"subtab selected\">\w+\s\((\d+.*\d+)\)',site)

if match:
	nl = int(match.group(1).replace(',',''))
	if nl > lpp:
		#get all links from func
		getlinks(nl/lpp)
	else:
		#get them directly from the only page(1)
		links = re.findall(r'\"http://cdn\d\d.lbstatic.nu/files/looks/large.+\"', site)
		d[1] = links
		'''for link in links:
			"print link, "\n"'''
else:
  	print 'did not find looks to save'

savelinks()

