# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
import codecs



class ProductAnalyzer:

    url = ""
    source = ""
    soup = ""
    rating = 1
    reviews = ""
    list1 = []
    

    def __init__(self):
        pass


    def initialize(self, url):
        self.url = url
        

        try:
            self.source = urllib2.urlopen(url).read()
        except:
            return False

        self.soup = BeautifulSoup(self.source)

    

        return True

    def getRating(self):
	

        for tag in self.soup.find_all('div'):
            if tag.get('id') == "avgRating":
                rtg = tag.get_text()
		try:                
			self.rating = re.findall('[0-5] out of 5 stars',rtg)[0][0]
                except IndexError:

			pass
        return self.rating

    def getReviews(self):
        list1=""
        for tag in self.soup.find_all('div'):
            if tag.get('id') == 'revMHRL':
                for rev in tag.find_all('div'):
                    if ('a-section','celwidget' in rev.get('class'))[1]:
                        for subDiv in rev.find_all('div'):
                            if 'a-section' in subDiv.get('class'):
                                if not re.findall("amznJQ", subDiv.get_text()):
                                    self.reviews = subDiv.get_text()
                                    #print self.reviews
                                                    
                                    list1+=self.reviews
        return list1                         
