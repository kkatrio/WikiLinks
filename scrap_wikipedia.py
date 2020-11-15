import wikipediaapi
import random

class Wiki_scrapper():

    def __init__(self):
        # data:
        # wiki api object
        # random object
        self.wiki = wikipediaapi.Wikipedia('en')
        self.random = random
        self.counterrors = 0

    def reset(self):
        self.counterrors = 0

    def select_link(self, links):
        l = len(links)
        print("l= ", l)
        r = self.random.randint(0, l-1)
        print("r= ", r)
        next_link = links[r]
        if ':' in next_link:
            print('rejecting ', next_link)
            self.counterrors += 1
            if self.counterrors == 2: # quick escape
                return None
            self.select_link(links)
        if self.counterrors == 2:
            return None
        return next_link

    def wiki_content(self, link):
        # starting page
        page = self.wiki.page(link)
        print("Page - Exists: %s" % page.exists())
        # list with links
        links = list(page.links)

        print('links len =', len(links))
        if not len(links) > 0:
            raise AssertionError()

        # random link
        next_link_title = self.select_link(links)
        if next_link_title is None:
            return None
        print("nextlink: ", next_link_title)
        # get next page
        next_page = self.wiki.page(next_link_title)
        print("Next Page - Exists: %s" % next_page.exists())

        content = next_link_title + ' - ' + next_page.fullurl
        return content
