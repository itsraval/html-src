import requests
import hashlib
import time
import webbrowser
import sys
import csv

fileLocation = "C:\Prog_Python\html_update.csv"

def title():
#   print the title
    print("\n\n")
    print("===================================================================")
    print("===================================================================")
    print("HH   HH  TTTTTTT  MM   MM  LLL            SSSSSSS  RRRRRRR  CCCCCCC")
    print("HH   HH    TTT    MMM MMM  LLL            SSS      RR   RR  CCC    ")
    print("HHHHHHH    TTT    MM M MM  LLL            SSSSSSS  RR  RR   CCC    ")
    print("HHHHHHH    TTT    MM   MM  LLL            SSSSSSS  RRRR     CCC    ")
    print("HH   HH    TTT    MM   MM  LLL                SSS  RR  RR   CCC    ")
    print("HH   HH    TTT    MM   MM  LLLLLLLL       SSSSSSS  RR   RR  CCCCCCC")
    print("===================================================================")
    print("===================================================================")


def scan(webUrl):
#   scan the url to check if there is any update (every 5 minutes)
    try:
        urlReq = requests.get(webUrl)
    except requests.exceptions.RequestException:
        print("Error: url not correct...\n")
        menuURL()

    print("\nSearching: ", webUrl, "...\n")
    state1 = hashlib.md5(urlReq.text.encode('utf-8')).hexdigest()
    state2 = state1
    
    t = 5;
    
    while state1 == state2:
        time.sleep(300)
        urlReq = requests.get(webUrl)
        state2 = hashlib.md5(urlReq.text.encode('utf-8')).hexdigest()
        h = t // 60
        if h > 0:
            m = t % 60
            print("Page not updated for: ", h, "hours and ", m, "minutes\r", end = "")
        else:
            print("Page not updated for: ", t, "minutes\r", end = "")
        t += 5

    print("The page has been updated")
    print(webUrl)
    webbrowser.open(webUrl, new=1, autoraise=True)

  
def save():
#   save url in the csv file
    print("\nSave url")
    print("Insert url: ", end = "")
    webUrl = input()
    #controlla se url giusto
    try:
        urlReq = requests.get(webUrl)
    except requests.exceptions.RequestException:
        print("Error: url not correct...\n")
        return save()
    with open(fileLocation, newline = '') as csvfile:
        webList = list(csv.reader(csvfile, delimiter = ','))
    with open(fileLocation, 'a', newline = '') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([webUrl])


def delete():
#   delete a url from the csv file
    print("\nDelete url")
    with open(fileLocation, newline = '') as csvfile:
        webList = list(csv.reader(csvfile, delimiter = ','))
    for i in range(len(webList)):
        print(i," - ", webList[i][0])
    print("Insert number: ", end = "")
    n = int(input())
    with open(fileLocation, 'w', newline = '') as csvfile:    
        spamwriter = csv.writer(csvfile, delimiter=',')
        for i in range(len(webList)):
            if i != n:
                spamwriter.writerow([webList[i][0]])


def menuURL():
#   scan menu
## aggiornare menu da array a matrice
    print("\n\nMenu Url")
    print("0  -  Insert url")
    with open(fileLocation, newline = '') as csvfile:
        webList = list(csv.reader(csvfile, delimiter = ','))
    for i in range(len(webList)):
        print(i+1," - ", webList[i][0])
    print("Insert number: ", end = "")
    n = int(input()) - 1
    if n == -1:
        print("url: ", end = "")
        webUrl = input()
    elif n<-1 or n >len(webList)-1:
        print("Error: index out of range...\n")
        return menuURL()
    else:
        webUrl = webList[n][0]
    return webUrl


def menu():
#   main menu
    title()
    print("\n\nMenu")
    print("0  -  scan")
    print("1  -  save url")
    print("2  -  delete url")
    print("Insert number: ", end = "")
    n = int(input())
    if n == 0:
        webUrl = menuURL()
        scan(webUrl)
    elif n == 1:
        save()
        menu()
    elif n == 2:
        delete()
        menu()
    else:
        print("Error: index out of range...\n")
        menu()


#####     MAIN    #####
try:
    open(fileLocation, newline = '')
except Exception :
    open(fileLocation, 'x')
menu()
