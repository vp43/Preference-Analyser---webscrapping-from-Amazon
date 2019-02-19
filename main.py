# -*- coding: utf-8 -*-
DEBUG=True
from flask import Flask, render_template,request
import urllib2
from bs4 import BeautifulSoup
import productAnalyzer
import codecs

app = Flask(__name__)
  
@app.route('/',methods=['POST', 'GET'])

def index():
	i=1
	answer=""

	p = productAnalyzer.ProductAnalyzer()
 	if request.method == 'POST':
		text=request.form['text']
		if ((' ' in text) == True):
			text = "+".join( text.split() )

        
		

		while(True):
	    		try:
	        		source = urllib2.urlopen("http://www.amazon.in/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords="+text	+"&page="+str(i)).read()
	    		except:
	        		print "except"
	        		break

	    		soup = BeautifulSoup(source)

	    		for tag in soup.find_all('a'):
	        		try:
					
	        	    		if 's-access-detail-page' in tag.get('class'):
						answer = ""
	        	        		answer += tag.get_text()
						print answer

	        	        		if(p.initialize(str(tag.get('href')))):
								
	        	            			
	                    
	        	            			site_rating = p.getRating()
	        	            			site = site_rating
	        	            			
	                    
	        	            			reviews = p.getReviews()
	        	            			fo = codecs.open('outfile.txt','w','utf-8')
	        	            			fo.writelines("%s" % item for item in reviews)
	        	            			file = 'outfile.txt'
	
			    				post=0;
			    				neg=0;
		            				total=1;
			    				diff=0;
			    				rev_rating=float(0.000);
		            				rev_rating=float(rev_rating)
	                    				site_rating=float(site_rating)
	
			    				gd = 	["good","excellent","average","nice","superb","like","best","excited","better","tremendous","durable","modest","love","cool","tidy","great","wonderful","legend","pretty","easy","quickly","easily","happy","satisfied","super","amazing","faster","fast","clear"]
			    				bd =    ["bad","no","rubbish","waste","disaster","wrong","bore","doesn't","not","cant","poorly","poor","disappointed","lack","heavy","haven't","couldn't","don't","embarassing"]


			    # create a dictionary for all search words, setting each count to 0
			    				count = dict.fromkeys(gd, 0)
			    				count1 = dict.fromkeys(bd,0)


			    				with open(file, 'r') as f:
	    							for line in f:
	        							for word in line.lower().split():
	            								if word in count:
	                			# found a word you wanted to count, so count it
	                								count[word] += 1	
											post=post+1
	
		    								if word in count1:
	               			        # found a word you wanted to count, so count it
	                								count1[word] += 1
											neg=neg+1
	                 			
	
			    				total=post+neg
			    				diff=(post-neg)
			    				rev_rating=float(((float(diff*5))/float(total)))
			    				
	                    
			    				#print "Customer Preference Analyser Ratings :"
	                    				#print ("\n")
			    				#print "Review Rating : " ,rev_rating
	                    				#print "Rating from sites : " ,site_rating
	                    				#print "Combined Rating : " ,(float(site_rating) + float(rev_rating))
			    				#print ("\n")

			    				answer +=  "Customer Preference Analyser Ratings :"
	                    				answer +=  ("\n")
			    				answer +=  "Review Rating : " +rev_rating
	                    				answer +=  "Rating from sites : " +site_rating
	                    				answer +=  "Combined Rating : " +(float(site_rating) + float(rev_rating))
			    				answer +=  ("\n")

							
							print answer


	                    
                    
                    
                    
	        		except TypeError:
	            			pass
	        		except AttributeError:
	            			pass
	    	        i=i+1
		return render_template('ss.html',text=text)
	else:
		return render_template('home.html')


if __name__ == '__main__':
  app.run(debug='0.0.0.0')
