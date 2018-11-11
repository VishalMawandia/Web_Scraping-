from selenium import webdriver

import time
driver=webdriver.Chrome()
driver.get("https://www.hindustantimes.com")


list_of_classes=["subhead4","random-heading","para-txt","bigstory-h2","bigstory-mid-h3","top-thumb-rgt"]
list_of_classes+=["subhead4 pt-10","media-heading headingfour","headingfour","media-heading headingfive"]
list_of_classes+=["headingfive"]


#print(driver)
#time.sleep(5)


#f = open('result.csv','w')
for x in range(len(list_of_classes)):
	s="//div[@class=\""
	s+=list_of_classes[x]
	s+="\"]"
	#print(s)
	ans=driver.find_elements_by_xpath(s)
	#print(len(ans))
	for i in ans:
		#print(i.text)
		if(i.text==None or i.text==""):
			continue
		else:
			with open('result.csv','a') as f:
				string = i.text.replace(',','[comma]') if ',' in i.text else i.text
				f.write(string+",")
	#f.write('\n'+'-'*30+'\n')
f.close()
driver.close()