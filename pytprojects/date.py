from time import strftime

def getDate():
    return strftime(" %d/%m/%y/%X ")

def getSec():
    timme = list(strftime("%X").split(":"))
    return timme[2]