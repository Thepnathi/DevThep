import datetime

def monthSwitch(month):
    currMonth = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return currMonth.get(month, "Invalid month")

def getCurrentDate():
    date = datetime.datetime.now() 
    return(date.strftime('%d ' + monthSwitch(date.month) + ' %Y'))
