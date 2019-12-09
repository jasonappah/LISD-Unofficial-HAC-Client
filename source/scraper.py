from lxml import html
from lxml.etree import tostring

lunch = ["Lunch A (A Day)", "Lunch A (B Day)", "Lunch B (A Day)", "Lunch B (B Day)", "Lunch"]

def scrape(response):
    tree = html.fromstring(response.content)
    scrape.name = tree.xpath("/html/body/div[1]/div[1]/div[2]/div/ul/li[1]/span")
    scrape.classes = tree.xpath("//*[@id=\"courseName\"]")
    scrape.teacher = tree.xpath("//*[@id=\"staffName\"]")
    scrape.grades = tree.xpath("//*[@id=\"average\"]")
    print("Scraped successfully")

# to solve the dilemma with joseph's test (lunch issue), it needs to iterate through scrape.classes to see if there is a lunch.
# lunch = {"Lunch A (A Day)", "Lunch A (B Day)", "Lunch B (A Day)", "Lunch B (B Day)"}. 
# if there is a lunch, get the index of that lunch, then check if the values of scrape.teacher and scrape.grades for that index arent blank. if they aren't blank, add an empty string at the index before into scrape.teacher and scrape.grades, then rerun the function to check for multiple lunches

def fixLunch(classes, teachers, grades):
    for i in classes:
        for o in lunch:
            if classes[i].text == lunch[o]:
                teachers.insert(i, "No teacher")
                grades.insert(i, "No teacher")
                fixLunch(classes, teachers, grades)
            
        


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
        cleanTchrs.newList.append(list[temp].text.strip())
        temp += 1
        
def printGr():
    print("")
    print("Hi " + scrape.name[0].text + "! Here are your grades.")
    print("There are " + str(len(cleanTchrs.newList)) + " classes.")
    if cleanGr.np == 1:
        print("There are classes with grades that aren't published, denoted by NP.")
    print("")
    temp = 0
    for i in scrape.teacher:
       print(scrape.classes[temp].text + " | ", end="")
       print(cleanTchrs.newList[temp]  + " | ", end="")
       print("Avg: " + cleanGr.newList[temp])
       temp +=1
