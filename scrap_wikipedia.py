import wikipediaapi
import random

# must be taken from file
#last_link = 'Python_(programming_language)'

def wiki_content(link):

    # starting page
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(link)
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
    print("Next Page - Exists: %s" % next_page.exists())

    content = next_link_title + ' - ' + next_page.fullurl
    return content


def retrieve_last_node(statuses):
    last_status = statuses[0]
    last_text = last_status.text

    wiki_wiki = wikipediaapi.Wikipedia('en')
    last_page = wiki_wiki.page(last_text)
    print("Last Page - Exists: %s" % last_page.exists())

    return last_page
