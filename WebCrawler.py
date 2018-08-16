import requests, re, urllib.request

website = input("Enter a URL to view: ")

try:
  data = requests.get(website)
  links = data.text
  for links in re.findall('''href=["'](.[^"']+)["']''',links,0):
    print (links) 
  #for moreLinks in re.findall('''href=["'](.[^"']+)["']''', links, re.I):
   # print (moreLinks,"****")

except:
  print('You entered an invalid URL. Please try again beginning with http.')
