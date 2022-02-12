text = 'Hello this is yash wakekar yashwakekar231@gmail.com with  https://stackoverflow.com/questions/3392354/append-values-to-a-set-in-python    www.google.com jaywant patil bluiding plot no 127 near hanuman mandir shiravane gaon nerul navi mumbai 400706'
import re

def url_grabber(text):
    url =["",""]
    for i in range(0,2):
        url[i] = re.search("(?P<url>https?://[^\s]+)", text"{i}").group("url")
        name = "text" + "{i}"
        name = text.replace(url[0],"")
    return url

x=url_grabber(text)

print(x)

