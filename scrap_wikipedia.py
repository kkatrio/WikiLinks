import wikipediaapi
import random


def wiki_content():

    # starting page
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page('Python_(programming_language)')
    print("Page - Exists: %s" % page.exists())

    # list with links
    links = list(page.links)
    l = len(links)
    print('links len =', l)
    if not l > 0:
        raise AssertionError()

    # random link
    r = random.randint(0, l)
    next_link_title = links[r]
    print("nextlink: ", next_link_title)

    # get next page
    next_page = wiki_wiki.page(next_link_title)
    print("Next Page - Exists: %s" % page.exists())

    content = next_link_title + ' - ' + next_page.fullurl

    return content
