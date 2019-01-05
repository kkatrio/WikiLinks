import wikipediaapi
import random

class Wiki_scrapper():

    def __init__(self):
        # data:
        # wiki api object
        # random object
        self.wiki = wikipediaapi.Wikipedia('en')
        self.random = random

    def wiki_content(self, link):
        # starting page
        page = self.wiki.page(link)
        print("Page - Exists: %s" % page.exists())
        # list with links
        links = list(page.links)
        l = len(links)
        print('links len =', l)
        if not l > 0:
            raise AssertionError()
        # random link
        r = self.random.randint(0, l)
        next_link_title = links[r]
        print("nextlink: ", next_link_title)
        # get next page
        next_page = self.wiki.page(next_link_title)
        print("Next Page - Exists: %s" % next_page.exists())

        content = next_link_title + ' - ' + next_page.fullurl
        return content
