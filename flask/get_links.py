
def get_links(links):
    extras=""
    git_link=""
    lid_link=""
    li = list(links.split(" "))

    for i in li:
        if 'linkedin' in i:
            lid_link = lid_link + i +","
        elif 'github' in i:
            git_link = git_link + i +","
        else:
            extras = extras + i +","

    l1=lid_link.split(",")
    l2=git_link.split(",")
    l3=extras.split(",")
    linkdedln=""
    github=""
    others=""
    for i in l1:
        if (i == ""):
            pass
        else:
            linkdedln=linkdedln+i+","

    for i in l2:
        if (i == ""):
            pass
        else:
            github=github+i+","

    for i in l3:
        if (i == ""):
            pass
        else:
            others=others+i+","
    print(linkdedln)
    print(github)
    print(others)
    return (linkdedln,github,others)