import wikipediaapi
import random

class Wiki_scrapper():

    def __init__(self):
        # data:
        # wiki api object
        # random object
        self.wiki = wikipediaapi.Wikipedia('en')
        self.random = random

    def select_link(self, links):
        l = len(links)
        r = self.random.randint(0, l)
        next_link = links[r]
        if ':' in next_link:
            print('rejecting ', selected)
            select_link(links)
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
        print("nextlink: ", next_link_title)
        # get next page
        next_page = self.wiki.page(next_link_title)
        print("Next Page - Exists: %s" % next_page.exists())

        content = next_link_title + ' - ' + next_page.fullurl
        return content
