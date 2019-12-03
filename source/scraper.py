from lxml import html
from lxml.etree import tostring

def scrape(response):
    tree = html.fromstring(response.content)
    scrape.name = tree.xpath("/html/body/div[1]/div[1]/div[2]/div/ul/li[1]/span")
    scrape.classes = tree.xpath("//*[@id=\"courseName\"]")
    scrape.teacher = tree.xpath("//*[@id=\"staffName\"]")
    scrape.grades = tree.xpath("//*[@id=\"average\"]")
    print("Scraped successfully")

def clean(list):
    clean.newList = []
    temp = 0
    clean.np = 0
    for i in list:
        if list[temp].text == None:
            clean.newList.append("NP")
            clean.np = 1
        else:
            clean.newList.append(list[temp].text)
        temp += 1
        

def printGr():
    print("Hi " + scrape.name[0].text + "! Here are your grades.")
    print("There are " + str(len(scrape.classes)) + " classes.")
    print("There are " + str(len(scrape.teacher)) + " teachers.")
    print("There are " + str(len(clean.newList)) + " grades.")
    if clean.np == 1:
        print("There are classes with grades that aren't published, denoted by NP.")
    temp = 0
    for i in scrape.teacher:
       #print(scrape.classes[temp].text)
       print(scrape.teacher[temp].text)
       #print(clean.newList[temp])
       temp +=1
