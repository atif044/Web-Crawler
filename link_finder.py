from html.parser import HTMLParser
from urllib import parse


#class gives the all the links that are existing in the website
class LinkFinder(HTMLParser):
    def __init__(self,base_url,page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set() 
        
    #gets all links from the given url and returns a list of links.
    def handle_starttag(self,tag,attrs):
        if tag == 'a':
            for (attribute,value) in attrs:
               if attribute == 'href':
                    url = parse.urljoin(self.base_url,value)
                    self.links.add(url)
    #returns a list of links
    def page_links(self):
        return self.links
    
    def error(self,message):
        pass















