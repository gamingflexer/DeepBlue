from asyncio.format_helpers import extract_stack
import re
# text = 'Hello this is yash wakekar yashwakekar231@gmail.com with  https://stackoverflow.com/questions/3392354/append-values-to-a-set-in-python    www.google.com jaywant patil bluiding plot no 127 near hanuman mandir shiravane gaon nerul navi mumbai 400706'


# def url_grabber(text):
#     url = ["", ""]
#     for i in range(0, 2):
#         url[i] = re.search("(?P<url>https?://[^\s]+)", text"{i}").group("url")
#         name = "text" + "{i}"
#         name = text.replace(url[0], "")
#     return url


# x = url_grabber(text)

# print(x)

links = ['https://www.linkedin.com/in/aju-palleri-248798a4/',
         'https://github.com/gamingflexer/DeepBlue', 'https://github.com/', 'new.com']

git_link = []
lid_link = []
extras = []


# def link_seprator(links):
# for i in range(len(links)):
#     k = re.search(r'\bwww.linkedin.com\b', links[i]).group(0)
#     print(k)

for i in range(len(links)):
    if 'linkedin' in links[i]:
        lid_link = lid_link + [links[i]]
    elif 'github' in links[i]:
        git_link = git_link + [links[i]]
    else:
        extras = extras + [links[i]]

print(lid_link)
print(git_link)
print(extras)

# regex = re.compile("linkedin+\w*")
# match_object = regex.findall(links[0])
# prin
