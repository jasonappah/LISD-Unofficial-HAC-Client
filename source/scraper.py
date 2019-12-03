from lxml import html
from lxml.etree import tostring

def scrape(response):
    tree = html.fromstring(response.content)
    scrape.name = tree.xpath("/html/body/div[1]/div[1]/div[2]/div/ul/li[1]/span")
    scrape.classes = tree.xpath("//*[@id=\"courseName\"]")
    scrape.teacher = tree.xpath("//*[@id=\"staffName\"]")
    scrape.grades = tree.xpath("//*[@id=\"average\"]")
    print("Scraped successfully")

def cleanGr(list):
    cleanGr.newList = []
    temp = 0
    cleanGr.np = 0
    for i in list:
        if list[temp].text == None:
            cleanGr.newList.append("NP")
            cleanGr.np = 1
        else:
            cleanGr.newList.append(list[temp].text)
        temp += 1

def cleanTchrs(list):
    cleanTchrs.newList = []
    temp = 0
    cleanTchrs.np = 0
    for i in list:
        if list[temp].text.find == 1:
           list[temp].text = list[temp].text.replace(' ', '') 
        else:
            cleanGr.newList.append(list[temp].text)
        temp += 1
        

def printGr():
    print("Hi " + scrape.name[0].text + "! Here are your grades.")
    print("There are " + str(len(scrape.classes)) + " classes.")
    print("There are " + str(len(scrape.teacher)) + " teachers.")
    print("There are " + str(len(cleanGr.newList)) + " grades.")
    if cleanGr.np == 1:
        print("There are classes with grades that aren't published, denoted by NP.")
    temp = 0
    for i in scrape.teacher:
       #print(scrape.classes[temp].text)
       print(scrape.teacher[temp].text)
       #print(cleanGr.newList[temp])
       temp +=1
