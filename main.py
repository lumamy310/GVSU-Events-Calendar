# requests library = python -m pip install requests
# beautiful soup = python -m pip install beautifulsoup4
import requests
import datetime
from bs4 import BeautifulSoup


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# URL = "https://www.gvsu.edu/events/"
# page = requests.get(URL)

# print the raw html text
# print(page.text)

# soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find("div", class_="col-sm-12 col-sm-push-0 col-md-9 col-md-push-3")

# print the html of the results object
# print(results.prettify())

# find all the h2 tags in results
# dates = results.findAll("h2")
# print all the h2 tags in results
# for date in dates:
#    print(date, end="\n" * 2)

# .next_sibling gets the next element in the same tree (use with h2 to get time, location, etc)

# strip() only removes from beginning and end, use replace() to get rid of \n and \t inside


calendarDate = datetime.date.today()


def today():
    global calendarDate
    calendarDate = datetime.date.today()

    URL = "https://www.gvsu.edu/events/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="col-sm-12 col-sm-push-0 col-md-9 col-md-push-3")
    dates = results.findAll("h2")
    for date in dates:
        dateName = date.string.replace("\n", "")
        dateName = dateName.replace("\t", "")
        print(color.BOLD + color.YELLOW + dateName + color.END)
        for sibling in date.next_siblings:
            if sibling.name == "p":
                print("No events")
                print("\n")
            if sibling.name == "h2":
                break
            if sibling.name == "a":
                print("*" * 68)
                for info in sibling.contents[1].contents:
                    if info == "\n":
                        continue
                    if info.name == "h3":
                        print(color.CYAN + info.text.strip() + color.END)
                    else:
                        print(info.text.strip())
                print("*" * 68)
                print("\n")
    print(color.BOLD + "1) Previous Week | 2) Today | 3) Next Week | 4) Enter Date | 5) Quit" + color.END)
    print("\n")


def nextWeek():
    global calendarDate
    calendarDate = calendarDate + datetime.timedelta(days=7)
    month = calendarDate.month
    day = calendarDate.day
    year = calendarDate.year

    URL = "https://www.gvsu.edu/events/?date=" + str(month) + "/" + str(day) + "/" + str(year)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="col-sm-12 col-sm-push-0 col-md-9 col-md-push-3")
    dates = results.findAll("h2")
    for date in dates:
        dateName = date.string.replace("\n", "")
        dateName = dateName.replace("\t", "")
        print(color.BOLD + color.YELLOW + dateName + color.END)
        for sibling in date.next_siblings:
            if sibling.name == "p":
                print("No events")
                print("\n")
            if sibling.name == "h2":
                break
            if sibling.name == "a":
                print("*" * 68)
                for info in sibling.contents[1].contents:
                    if info == "\n":
                        continue
                    if info.name == "h3":
                        print(color.CYAN + info.text.strip() + color.END)
                    else:
                        print(info.text.strip())
                print("*" * 68)
                print("\n")
    print(color.BOLD + "1) Previous Week | 2) Today | 3) Next Week | 4) Enter Date | 5) Quit" + color.END)
    print("\n")


def previousWeek():
    global calendarDate
    calendarDate = calendarDate - datetime.timedelta(days=7)
    month = calendarDate.month
    day = calendarDate.day
    year = calendarDate.year

    URL = "https://www.gvsu.edu/events/?date=" + str(month) + "/" + str(day) + "/" + str(year)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="col-sm-12 col-sm-push-0 col-md-9 col-md-push-3")
    dates = results.findAll("h2")
    for date in dates:
        dateName = date.string.replace("\n", "")
        dateName = dateName.replace("\t", "")
        print(color.BOLD + color.YELLOW + dateName + color.END)
        for sibling in date.next_siblings:
            if sibling.name == "p":
                print("No events")
                print("\n")
            if sibling.name == "h2":
                break
            if sibling.name == "a":
                print("*" * 68)
                for info in sibling.contents[1].contents:
                    if info == "\n":
                        continue
                    if info.name == "h3":
                        print(color.CYAN + info.text.strip() + color.END)
                    else:
                        print(info.text.strip())
                print("*" * 68)
                print("\n")
    print(color.BOLD + "1) Previous Week | 2) Today | 3) Next Week | 4) Enter Date | 5) Quit" + color.END)
    print("\n")


def isValidDate(year, month, day):
    lastDay = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year):
        lastDay[2] = 29
    else:
        lastDay[2] = 28

    if (len(str(year))) != 4:
        return False
    elif month < 1 or month > 12:
        return False
    elif day < 1 or day > lastDay[month]:
        return False
    else:
        return True


def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def getWeek():
    print("Please enter a date in the format: month/day/year")

    while True:
        try:
            inputDate = str(input())
            inputDate = inputDate.split("/")
            inputDate = [int(x) for x in inputDate]

            if len(inputDate) == 3:
                month = inputDate[0]
                day = inputDate[1]
                year = inputDate[2]
                if isValidDate(year, month, day):
                    break
                else:
                    raise Exception("Illegal Argument")
            else:
                raise Exception("Illegal Argument")

        except Exception:
            print("Please enter a date in the format: month/day/year")

    URL = "https://www.gvsu.edu/events/?date=" + str(month) + "/" + str(day) + "/" + str(year)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="col-sm-12 col-sm-push-0 col-md-9 col-md-push-3")
    dates = results.findAll("h2")
    for date in dates:
        dateName = date.string.replace("\n", "")
        dateName = dateName.replace("\t", "")
        print(color.BOLD + color.YELLOW + dateName + color.END)
        for sibling in date.next_siblings:
            if sibling.name == "p":
                print("No events")
                print("\n")
            if sibling.name == "h2":
                break
            if sibling.name == "a":
                print("*" * 68)
                for info in sibling.contents[1].contents:
                    if info == "\n":
                        continue
                    if info.name == "h3":
                        print(color.CYAN + info.text.strip() + color.END)
                    else:
                        print(info.text.strip())
                print("*" * 68)
                print("\n")
    print(color.BOLD + "1) Previous Week | 2) Today | 3) Next Week | 4) Enter Date | 5) Quit" + color.END)
    print("\n")


today()
while True:
    try:
        option = int(input())
        break
    except ValueError:
        print("Please enter a valid option")

while option != 5:
    if option == 1:
        # get previous week
        previousWeek()
    elif option == 2:
        # get this week
        today()
    elif option == 3:
        # get next week
        nextWeek()
    elif option == 4:
        # enter a date
        getWeek()
    else:
        print("Please enter a valid option")
    while True:
        try:
            option = int(input())
            break
        except ValueError:
            print("Please enter a valid option")

# exit program
