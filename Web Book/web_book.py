from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup

#File path to store the webpages
FILE_PATH = ""
URL = ""
PAGES = []
IMAGES = []

#Function to fetch web page
def fetch_page(link):
    #Main page HTTP response
    html = urlopen(URL+"/"+link)

    #Extracting HTML from the response using BeautifulSoup
    pro = BeautifulSoup(html)
    
    return pro

#Function to store the first/main page
def first_page():
    pro = fetch_page("")
    write_file(pro,"main.html")

#Function to write html file and save in the given directory
def write_file(temp,link):
    #open a file to store the web page
    FILE = open(FILE_PATH+link,'w')
    #write the HTML
    FILE.write(str(temp))
    FILE.close()

def process():
    #Store the first page
    first_page()

    #fetch the first page to get all the links
    pro = fetch_page("")
    
    #Extract all links in the webpage 
    links = pro.find_all('a')

    #go through all the links
    for i in links:
        #get the reference of the link
        link = i.get('href')
        #if link is not blank or has no target and is not already downloaded
        if link is not None and link not in PAGES:
            print(link)
            PAGES.append(link)
            #request HTTP response of the link
            temp = fetch_page(link)
            for image in temp.find_all('img'):
                #get the image source
                img = image.get('src')

                #check if the image is already downloaded
                if img is not None and img not in IMAGES:
                    print(img)
                    IMAGES.append(img)

                    #Download the image
                    urlretrieve(URL+"/"+img,FILE_PATH+img)

            #Function to write the html file
            write_file(temp,link)
            
    #Print the total number html files and total number of images downloaded
    print("\nTotal Files : ",len(PAGES),"\n Total Images : ",len(IMAGES))


FILE_PATH = input("Directory to store the files : ")
FILE_PATH += "\\" 
URL = input("URL from which to store : ")
process()
