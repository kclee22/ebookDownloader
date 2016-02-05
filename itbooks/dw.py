import os as _os
import re as _re
import time as _time

def fetch_info(From, To):
	count=0
	for book_no in range(From, To+1):
		fetch_info_one(book_no)
		count+=1
		if count%5==4: _time.sleep(1)
		if count%10==9: _time.sleep(1)
		if count%20==9: _time.sleep(1)
		if count%30==9: _time.sleep(1)
		if count%40==9: _time.sleep(1)
		if count%50==9: _time.sleep(1)
		if count%100==9: _time.sleep(2)

def fetch_info_one(book_no):
	base_url = "http://www.it-ebooks.info/book/"
	book_no = str(book_no)
	url = base_url + book_no
	print "fetch", book_no, url
	_os.system("wget -q %s -O %s" % (url, "tmp") )
	_next_line_is_important = False
	with open('tmp', 'rU') as infile: # for Unix newline: '\n' # rU: Unix New line
		for line in infile:
			line = line.rstrip()
			m = _re.match(r".+itemprop=\"name\">(.+)</h1>", line);
			if m is not None:
				Title = m.group(1)
				_next_line_is_important = True
			if _next_line_is_important:
				m = _re.match(r"<h3>(.+)</h3>.+", line);
				if m is not None:
					SubTitle = m.group(1)
					_next_line_is_important = False
				else:
					SubTitle = None
			m = _re.match(r".+<span itemprop=\"description\">(.+)", line);
			if m is not None:
				Description = m.group(1)
				while not line.endswith('</span>'):
					line = infile.next().strip()
					Description += line
				Description = _re.sub("<.*?>", "", Description).strip() # strip_tags
			m = _re.match(r".+itemprop=\"publisher\">(.+)</a>", line);
			if m is not None:
				Publisher = m.group(1)
			#Auther: Start
			m = _re.match(r".+<td>By:</td>.+title=\'(.+)\'.+", line);
			if m is not None:
				Auther = m.group(1)
			m = _re.match(r".+itemprop=\"author\".+\">(.+?)</b>.+", line)
			if m is not None:
				Auther = m.group(1)
			#Auther: End
			m = _re.match(r".+itemprop=\"datePublished\">([0-9]+)</b>", line);
			if m is not None:
				Year = m.group(1)
			m = _re.match(r".+Download:.+<a href='(http.+)'.+", line);
			if m is not None:
				Download = m.group(1)
			#
	text = ""
	text += "[" + url + "]"
	text += "\tit-ebooks.info\tbook\t\t\t\t\t" + Year
	if SubTitle!=None:
		text += "\t\t[" + Publisher + "] " + Title + ": " + SubTitle
	else:
		text += "\t\t[" + Publisher + "] " + Title
	text += "\t" + Description
	text += "\ten\t" + Auther
	text += "\t\t\t" + book_no + ".pdf"
	#print Publisher, Year, Auther, Download
	#print Title
	#print SubTitle
	#print Description
	f=open('_book_info.txt','ab')
	f.write(text+"\r\n")
	f.close()
	_os.system("wget --referer=\"%s\" %s -O %s.pdf" % (url, Download, book_no) ) # Download Book PDF
	_time.sleep(1)
	#
	pass




