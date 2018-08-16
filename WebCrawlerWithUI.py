from tkinter import *
import requests, re, urllib.request


def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def crawlTheWeb():
    website = e1.get()
    
    try:
      data = requests.get(website)
      links = data.text
      allLinks =  []


      #for links in re.findall('''href=["'](.[^"']+)["']''',links,0):
       # pass
      for moreLinks in re.findall('''href=["'](.[^"']+)["']''', links, 0):
         if(".com" not in moreLinks and ".org" not in moreLinks):
            pass
         else:
            #print(moreLinks)
            allLinks.append(moreLinks)
    except:
      print('You entered an invalid URL. Please try again beginning with http.')


    print ("The found links are")
    print(allLinks)
    depthOf5 = allLinks[30:35]
    print("The first 5 URLs are...")
    print ("\n".join(depthOf5))
    e2 = Label(master, text = depthOf5).grid(row=3)


master = Tk()
master.title("Simple Webcrawler")
master.geometry("300x300+300+300")
Label(master, text="Enter a URL to search").grid(row=0)
Label(master, text="Output").grid(row=1)
e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Search', command=crawlTheWeb).grid(row=10, column=0, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=10, column=1, sticky=W, pady=4)



#mainloop( )
