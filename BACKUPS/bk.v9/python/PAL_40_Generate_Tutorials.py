#!/user/bin/env python

from collections import defaultdict

import os
import random

class PAL_40_Generate_Tutorials(object):
	
	def __init__(self):
		
		self.ROOT_DIR 			= os.path.dirname(os.getcwd())
		self.BACKUPS_DIR		= os.path.join(self.ROOT_DIR, 'backups')
		self.CSS_DIR			= os.path.join(self.ROOT_DIR, 'css')
		self.IMAGES_DIR			= os.path.join(self.ROOT_DIR, 'images')
		self.JAVASCRIPT_DIR		= os.path.join(self.ROOT_DIR, 'js')
		self.PYTHON_DIR			= os.getcwd()

		self.MAIN_DIR			= os.path.join(self.ROOT_DIR, 'main')
		self.CONTENTS_DIR 		= os.path.join(self.MAIN_DIR, 'data')
		self.PUZZLES_DIR 		= os.path.join(self.MAIN_DIR, 'puzzles')
		self.TEMPLATES_DIR 		= os.path.join(self.MAIN_DIR, 'templates')
		self.TUTORIALS_DIR 		= os.path.join(self.MAIN_DIR, 'tutorials')
		self.UPDATES_DIR 		= os.path.join(self.MAIN_DIR, 'updates')

		self.LOCAL_ARCHIVE_DIR	= os.path.join(self.TUTORIALS_DIR, 'archive')
		self.LOCAL_CONTENTS_DIR	= os.path.join(self.TUTORIALS_DIR, 'data')
		self.LOCAL_PAGES_DIR	= os.path.join(self.TUTORIALS_DIR, 'pages')
		
		self.HEADER_PATH		= os.path.join(self.TEMPLATES_DIR, 'template_subpages_header.html')
		self.NAVIGATION_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_subpages_navigation.html')
		self.CLOSING_TAGS_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_closingtags.html')

		self.CONTENT_PATHS		= os.path.join(self.LOCAL_CONTENTS_DIR, 'content_tutorial_')
		self.HTML_PATHS			= os.path.join(self.LOCAL_PAGES_DIR, 'tutorial_')

		self.Header_Data		= []
		self.Navigation_Data	= []
		self.Closing_Tags_Data	= []
		self.Tutorials_Data		= []
		self.Tutorials_Info		= defaultdict(list)

		self.Keywords_Delimiter = '$%$%'

		self.Keywords_Formats	= { 'str': "<span class=keyword-teal>str</span>", \
									'print': "<span class=keyword-orange>print</span>", \
									}


	def PAL_40_Load_Header_Template(self):

		# Load Header
		if not os.path.isfile(self.HEADER_PATH):
			print "ERROR: HEADER TEMPLATE FILE NOT FOUND"

		fileStream = open(self.HEADER_PATH, 'r')
		allLines = fileStream.readlines()

		for line in allLines[0:]:
			line_list = line
			if line_list != ['']:
				self.Header_Data.append(line_list)
		fileStream.close()


	def PAL_40_Print_Header_Template(self, outFile):
		for header_line in self.Header_Data:
			outFile.write(header_line)


	def PAL_40_Load_Navigation_Template(self):

		# Load Navigation
		if not os.path.isfile(self.NAVIGATION_PATH):
			print "ERROR: NAVIGATION TEMPLATE FILE NOT FOUND"

		fileStream = open(self.NAVIGATION_PATH, 'r')
		allLines = fileStream.readlines()

		for line in allLines[0:]:
			line_list = line
			if line_list != ['']:
				self.Navigation_Data.append(line_list)
		fileStream.close()


	def PAL_40_Print_Navigation_Template(self, outFile):
		for navigation_line in self.Navigation_Data:
			outFile.write(navigation_line)


	def PAL_40_Load_Closing_Tags_Template(self):

		if not os.path.isfile(self.CLOSING_TAGS_PATH):
			print "ERROR: CLOSING TAGS TEMPLATE FILE NOT FOUND"

		fileStream = open(self.CLOSING_TAGS_PATH, 'r')
		allLines = fileStream.readlines()

		for line in allLines[0:]:
			line_list = line
			if line_list != ['']:
				self.Closing_Tags_Data.append(line_list)
		fileStream.close()


	def PAL_40_Print_Closing_Tags_Template(self, outFile):
		for closing_tag in self.Closing_Tags_Data:
			outFile.write(closing_tag)


	def PAL_40_Load_Tutorial_Content(self, tutorial_num):
		
		current_content_file = self.CONTENT_PATHS + unicode(tutorial_num) + '.txt'

		fileStream = open(current_content_file, 'r')
		allLines = fileStream.readlines()
		#print allLines

		# Create sections of content
		SECTIONS 	= []
		TEMP 		= []
		for i in allLines:
			if i == '________________________________\n':
				SECTIONS.append(TEMP)
				TEMP = []
			else:
				TEMP.append(i)
		# Remove empty lists
		while True:
			try:
				SECTIONS.remove([])
			except ValueError:
				break
		# Create dictionary of values
		for section in SECTIONS:
			self.Tutorials_Info[section[0]] = section[1:]

		# Process content to format colours of new/key terms
		for heading in self.Tutorials_Info:
			current_section = self.Tutorials_Info[heading]
			tempString = self.Keywords_Delimiter.join(self.Tutorials_Info[heading])
			tempString = tempString.replace('^keyword^str', self.Keywords_Formats['str'])
			tempString = tempString.replace('^keyword^print', self.Keywords_Formats['print'])

			self.Tutorials_Info[heading] = tempString.split(self.Keywords_Delimiter)

		fileStream.close()


	def PAL_40_Print_Title(self, tutorial_num, outFile):
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--       TITLE      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <title>Tutorial | Pythons and Ladders</title>\n')
		outFile.write('\n')


	def PAL_40_Print_Body(self, tutorial_num, outFile):

		previous_Tutorial = 'tutorial_'+unicode(tutorial_num-1)+'.html'
		next_Tutorial 	= 'tutorial_'+unicode(tutorial_num+1)+'.html'

		if previous_Tutorial not in os.listdir(self.LOCAL_PAGES_DIR):
			if previous_Tutorial == 'tutorial_0.html':
				previous_Tutorial = '../../index.html'
			else:
				previous_Tutorial = '../../pagenotfound.html'

		if next_Tutorial not in os.listdir(self.LOCAL_PAGES_DIR):
			if next_Tutorial == 'tutorial_11.html':
				next_Tutorial = '../../puzzles/pages/puzzle_1.html'
			else:
				next_Tutorial = '../../pagenotfound.html'

		outFile.write('\n')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--        BODY      -->')
		outFile.write('\n    <!-- **************** -->')

		#--------------------
		# Print a middle pane
		#--------------------
		outFile.write('\n    <div class="middlepane">')
		outFile.write('\n    </div>')

		#--------------------
		# Print the left pane
		#--------------------
		outFile.write('\n    <!-- LEFT PANE -->')
		outFile.write('\n    <div class="welcomehome2">')

		# Print tutorial progress circles
		outFile.write('\n      <div class="tutorial-nav-circles">')
		if unicode(tutorial_num) == '1':
			outFile.write('\n        <a href="tutorial_1.html"><div class="circle-tutorial"><div class="circle-tutorial-on">1</div></div></a>')
			outFile.write('\n        <a href="tutorial_2.html"><div class="circle-tutorial"><div class="circle-tutorial-off">2</div></div></a>')
			outFile.write('\n        <a href="tutorial_3.html"><div class="circle-tutorial"><div class="circle-tutorial-off">3</div></div></a>')
			outFile.write('\n        <a href="tutorial_4.html"><div class="circle-tutorial"><div class="circle-tutorial-off">4</div></div></a>')
			outFile.write('\n        <a href="tutorial_5.html"><div class="circle-tutorial"><div class="circle-tutorial-off">5</div></div></a>')
			outFile.write('\n        <a href="tutorial_6.html"><div class="circle-tutorial"><div class="circle-tutorial-off">6</div></div></a>')
			outFile.write('\n        <a href="tutorial_7.html"><div class="circle-tutorial"><div class="circle-tutorial-off">7</div></div></a>')
			outFile.write('\n        <a href="tutorial_8.html"><div class="circle-tutorial"><div class="circle-tutorial-off">8</div></div></a>')
			outFile.write('\n        <a href="tutorial_9.html"><div class="circle-tutorial"><div class="circle-tutorial-off">9</div></div></a>')
			outFile.write('\n        <a href="tutorial_10.html"><div class="circle-tutorial"><div class="circle-tutorial-off">10</div></div></a>')
		elif unicode(tutorial_num) == '2':
			outFile.write('\n        <a href="tutorial_1.html"><div class="circle-tutorial"><div class="circle-tutorial-off">1</div></div></a>')
			outFile.write('\n        <a href="tutorial_2.html"><div class="circle-tutorial"><div class="circle-tutorial-on">2</div></div></a>')
			outFile.write('\n        <a href="tutorial_3.html"><div class="circle-tutorial"><div class="circle-tutorial-off">3</div></div></a>')
			outFile.write('\n        <a href="tutorial_4.html"><div class="circle-tutorial"><div class="circle-tutorial-off">4</div></div></a>')
			outFile.write('\n        <a href="tutorial_5.html"><div class="circle-tutorial"><div class="circle-tutorial-off">5</div></div></a>')
			outFile.write('\n        <a href="tutorial_6.html"><div class="circle-tutorial"><div class="circle-tutorial-off">6</div></div></a>')
			outFile.write('\n        <a href="tutorial_7.html"><div class="circle-tutorial"><div class="circle-tutorial-off">7</div></div></a>')
			outFile.write('\n        <a href="tutorial_8.html"><div class="circle-tutorial"><div class="circle-tutorial-off">8</div></div></a>')
			outFile.write('\n        <a href="tutorial_9.html"><div class="circle-tutorial"><div class="circle-tutorial-off">9</div></div></a>')
			outFile.write('\n        <a href="tutorial_10.html"><div class="circle-tutorial"><div class="circle-tutorial-off">10</div></div></a>')
		elif unicode(tutorial_num) == '3':
			outFile.write('\n        <a href="tutorial_1.html"><div class="circle-tutorial"><div class="circle-tutorial-off">1</div></div></a>')
			outFile.write('\n        <a href="tutorial_2.html"><div class="circle-tutorial"><div class="circle-tutorial-off">2</div></div></a>')
			outFile.write('\n        <a href="tutorial_3.html"><div class="circle-tutorial"><div class="circle-tutorial-on">3</div></div></a>')
			outFile.write('\n        <a href="tutorial_4.html"><div class="circle-tutorial"><div class="circle-tutorial-off">4</div></div></a>')
			outFile.write('\n        <a href="tutorial_5.html"><div class="circle-tutorial"><div class="circle-tutorial-off">5</div></div></a>')
			outFile.write('\n        <a href="tutorial_6.html"><div class="circle-tutorial"><div class="circle-tutorial-off">6</div></div></a>')
			outFile.write('\n        <a href="tutorial_7.html"><div class="circle-tutorial"><div class="circle-tutorial-off">7</div></div></a>')
			outFile.write('\n        <a href="tutorial_8.html"><div class="circle-tutorial"><div class="circle-tutorial-off">8</div></div></a>')
			outFile.write('\n        <a href="tutorial_9.html"><div class="circle-tutorial"><div class="circle-tutorial-off">9</div></div></a>')
			outFile.write('\n        <a href="tutorial_10.html"><div class="circle-tutorial"><div class="circle-tutorial-off">10</div></div></a>')
		elif unicode(tutorial_num) == '4':
			outFile.write('\n        <a href="tutorial_1.html"><div class="circle-tutorial"><div class="circle-tutorial-off">1</div></div></a>')
			outFile.write('\n        <a href="tutorial_2.html"><div class="circle-tutorial"><div class="circle-tutorial-off">2</div></div></a>')
			outFile.write('\n        <a href="tutorial_3.html"><div class="circle-tutorial"><div class="circle-tutorial-off">3</div></div></a>')
			outFile.write('\n        <a href="tutorial_4.html"><div class="circle-tutorial"><div class="circle-tutorial-on">4</div></div></a>')
			outFile.write('\n        <a href="tutorial_5.html"><div class="circle-tutorial"><div class="circle-tutorial-off">5</div></div></a>')
			outFile.write('\n        <a href="tutorial_6.html"><div class="circle-tutorial"><div class="circle-tutorial-off">6</div></div></a>')
			outFile.write('\n        <a href="tutorial_7.html"><div class="circle-tutorial"><div class="circle-tutorial-off">7</div></div></a>')
			outFile.write('\n        <a href="tutorial_8.html"><div class="circle-tutorial"><div class="circle-tutorial-off">8</div></div></a>')
			outFile.write('\n        <a href="tutorial_9.html"><div class="circle-tutorial"><div class="circle-tutorial-off">9</div></div></a>')
			outFile.write('\n        <a href="tutorial_10.html"><div class="circle-tutorial"><div class="circle-tutorial-off">10</div></div></a>')
		elif unicode(tutorial_num) == '5':
			outFile.write('\n        <a href="tutorial_1.html"><div class="circle-tutorial"><div class="circle-tutorial-off">1</div></div></a>')
			outFile.write('\n        <a href="tutorial_2.html"><div class="circle-tutorial"><div class="circle-tutorial-off">2</div></div></a>')
			outFile.write('\n        <a href="tutorial_3.html"><div class="circle-tutorial"><div class="circle-tutorial-off">3</div></div></a>')
			outFile.write('\n        <a href="tutorial_4.html"><div class="circle-tutorial"><div class="circle-tutorial-off">4</div></div></a>')
			outFile.write('\n        <a href="tutorial_5.html"><div class="circle-tutorial"><div class="circle-tutorial-on">5</div></div></a>')
			outFile.write('\n        <a href="tutorial_6.html"><div class="circle-tutorial"><div class="circle-tutorial-off">6</div></div></a>')
			outFile.write('\n        <a href="tutorial_7.html"><div class="circle-tutorial"><div class="circle-tutorial-off">7</div></div></a>')
			outFile.write('\n        <a href="tutorial_8.html"><div class="circle-tutorial"><div class="circle-tutorial-off">8</div></div></a>')
			outFile.write('\n        <a href="tutorial_9.html"><div class="circle-tutorial"><div class="circle-tutorial-off">9</div></div></a>')
			outFile.write('\n        <a href="tutorial_10.html"><div class="circle-tutorial"><div class="circle-tutorial-off">10</div></div></a>')
		elif unicode(tutorial_num) == '6':
			outFile.write('\n        <a href="tutorial_1.html"><div class="circle-tutorial"><div class="circle-tutorial-off">1</div></div></a>')
			outFile.write('\n        <a href="tutorial_2.html"><div class="circle-tutorial"><div class="circle-tutorial-off">2</div></div></a>')
			outFile.write('\n        <a href="tutorial_3.html"><div class="circle-tutorial"><div class="circle-tutorial-off">3</div></div></a>')
			outFile.write('\n        <a href="tutorial_4.html"><div class="circle-tutorial"><div class="circle-tutorial-off">4</div></div></a>')
			outFile.write('\n        <a href="tutorial_5.html"><div class="circle-tutorial"><div class="circle-tutorial-off">5</div></div></a>')
			outFile.write('\n        <a href="tutorial_6.html"><div class="circle-tutorial"><div class="circle-tutorial-on">6</div></div></a>')
			outFile.write('\n        <a href="tutorial_7.html"><div class="circle-tutorial"><div class="circle-tutorial-off">7</div></div></a>')
			outFile.write('\n        <a href="tutorial_8.html"><div class="circle-tutorial"><div class="circle-tutorial-off">8</div></div></a>')
			outFile.write('\n        <a href="tutorial_9.html"><div class="circle-tutorial"><div class="circle-tutorial-off">9</div></div></a>')
			outFile.write('\n        <a href="tutorial_10.html"><div class="circle-tutorial"><div class="circle-tutorial-off">10</div></div></a>')
		elif unicode(tutorial_num) == '7':
			outFile.write('\n        <a href="tutorial_1.html"><div class="circle-tutorial"><div class="circle-tutorial-off">1</div></div></a>')
			outFile.write('\n        <a href="tutorial_2.html"><div class="circle-tutorial"><div class="circle-tutorial-off">2</div></div></a>')
			outFile.write('\n        <a href="tutorial_3.html"><div class="circle-tutorial"><div class="circle-tutorial-off">3</div></div></a>')
			outFile.write('\n        <a href="tutorial_4.html"><div class="circle-tutorial"><div class="circle-tutorial-off">4</div></div></a>')
			outFile.write('\n        <a href="tutorial_5.html"><div class="circle-tutorial"><div class="circle-tutorial-off">5</div></div></a>')
			outFile.write('\n        <a href="tutorial_6.html"><div class="circle-tutorial"><div class="circle-tutorial-off">6</div></div></a>')
			outFile.write('\n        <a href="tutorial_7.html"><div class="circle-tutorial"><div class="circle-tutorial-on">7</div></div></a>')
			outFile.write('\n        <a href="tutorial_8.html"><div class="circle-tutorial"><div class="circle-tutorial-off">8</div></div></a>')
			outFile.write('\n        <a href="tutorial_9.html"><div class="circle-tutorial"><div class="circle-tutorial-off">9</div></div></a>')
			outFile.write('\n        <a href="tutorial_10.html"><div class="circle-tutorial"><div class="circle-tutorial-off">10</div></div></a>')
		elif unicode(tutorial_num) == '8':
			outFile.write('\n        <a href="tutorial_1.html"><div class="circle-tutorial"><div class="circle-tutorial-off">1</div></div></a>')
			outFile.write('\n        <a href="tutorial_2.html"><div class="circle-tutorial"><div class="circle-tutorial-off">2</div></div></a>')
			outFile.write('\n        <a href="tutorial_3.html"><div class="circle-tutorial"><div class="circle-tutorial-off">3</div></div></a>')
			outFile.write('\n        <a href="tutorial_4.html"><div class="circle-tutorial"><div class="circle-tutorial-off">4</div></div></a>')
			outFile.write('\n        <a href="tutorial_5.html"><div class="circle-tutorial"><div class="circle-tutorial-off">5</div></div></a>')
			outFile.write('\n        <a href="tutorial_6.html"><div class="circle-tutorial"><div class="circle-tutorial-off">6</div></div></a>')
			outFile.write('\n        <a href="tutorial_7.html"><div class="circle-tutorial"><div class="circle-tutorial-off">7</div></div></a>')
			outFile.write('\n        <a href="tutorial_8.html"><div class="circle-tutorial"><div class="circle-tutorial-on">8</div></div></a>')
			outFile.write('\n        <a href="tutorial_9.html"><div class="circle-tutorial"><div class="circle-tutorial-off">9</div></div></a>')
			outFile.write('\n        <a href="tutorial_10.html"><div class="circle-tutorial"><div class="circle-tutorial-off">10</div></div></a>')
		elif unicode(tutorial_num) == '9':
			outFile.write('\n        <a href="tutorial_1.html"><div class="circle-tutorial"><div class="circle-tutorial-off">1</div></div></a>')
			outFile.write('\n        <a href="tutorial_2.html"><div class="circle-tutorial"><div class="circle-tutorial-off">2</div></div></a>')
			outFile.write('\n        <a href="tutorial_3.html"><div class="circle-tutorial"><div class="circle-tutorial-off">3</div></div></a>')
			outFile.write('\n        <a href="tutorial_4.html"><div class="circle-tutorial"><div class="circle-tutorial-off">4</div></div></a>')
			outFile.write('\n        <a href="tutorial_5.html"><div class="circle-tutorial"><div class="circle-tutorial-off">5</div></div></a>')
			outFile.write('\n        <a href="tutorial_6.html"><div class="circle-tutorial"><div class="circle-tutorial-off">6</div></div></a>')
			outFile.write('\n        <a href="tutorial_7.html"><div class="circle-tutorial"><div class="circle-tutorial-off">7</div></div></a>')
			outFile.write('\n        <a href="tutorial_8.html"><div class="circle-tutorial"><div class="circle-tutorial-off">8</div></div></a>')
			outFile.write('\n        <a href="tutorial_9.html"><div class="circle-tutorial"><div class="circle-tutorial-on">9</div></div></a>')
			outFile.write('\n        <a href="tutorial_10.html"><div class="circle-tutorial"><div class="circle-tutorial-off">10</div></div></a>')
		elif unicode(tutorial_num) == '10':
			outFile.write('\n        <a href="tutorial_1.html"><div class="circle-tutorial"><div class="circle-tutorial-off">1</div></div></a>')
			outFile.write('\n        <a href="tutorial_2.html"><div class="circle-tutorial"><div class="circle-tutorial-off">2</div></div></a>')
			outFile.write('\n        <a href="tutorial_3.html"><div class="circle-tutorial"><div class="circle-tutorial-off">3</div></div></a>')
			outFile.write('\n        <a href="tutorial_4.html"><div class="circle-tutorial"><div class="circle-tutorial-off">4</div></div></a>')
			outFile.write('\n        <a href="tutorial_5.html"><div class="circle-tutorial"><div class="circle-tutorial-off">5</div></div></a>')
			outFile.write('\n        <a href="tutorial_6.html"><div class="circle-tutorial"><div class="circle-tutorial-off">6</div></div></a>')
			outFile.write('\n        <a href="tutorial_7.html"><div class="circle-tutorial"><div class="circle-tutorial-off">7</div></div></a>')
			outFile.write('\n        <a href="tutorial_8.html"><div class="circle-tutorial"><div class="circle-tutorial-off">8</div></div></a>')
			outFile.write('\n        <a href="tutorial_9.html"><div class="circle-tutorial"><div class="circle-tutorial-off">9</div></div></a>')
			outFile.write('\n        <a href="tutorial_10.html"><div class="circle-tutorial"><div class="circle-tutorial-on">10</div></div></a>')
		outFile.write('\n      </div>')
		outFile.write('\n    </div>')

		outFile.write('\n    <div class="leftpane">')
		# Print question
		outFile.write('\n        <!-- LEFT: QUESTION AND EDITOR -->')
		outFile.write('\n        ')

		# MAIN
		for sentence in self.Tutorials_Info['$LEFTPANEL_MAIN$\n']:
			outFile.write('\n        <h2>'+sentence.strip('\n')+'</h2>')
		for sentence in self.Tutorials_Info['$LEFTPANEL_MAINAREA$\n']:
			outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')

		if unicode(tutorial_num) in ['3', '4', '5', '6', '7', '8', '9', '10']:
			
			# INSTRUCTIONS
			if unicode(tutorial_num) in ['5','8','9','10']:
				for sentence in self.Tutorials_Info['$LEFTPANEL_INSTRUCTIONSAREA$\n']:
					if '<code>' in sentence:
						outFile.write('\n        <p class="small">'+sentence.strip('\n')+'</p>')
					else:
						outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')

			# TOOLBAR
			if unicode(tutorial_num) in ['3','4','5','6','7','8','9','10']:
				for sentence in self.Tutorials_Info['$LEFTPANEL_TOOLBARAREA$\n']:
					outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')
				outFile.write('\n          <div class="editor">')
				outFile.write('\n            <div class="editortoolbar">')
				outFile.write('\n              <div class="editortoolbaritems" onclick="runit()">RUN</div>')
				outFile.write('\n              <div class="editortoolbaritems" onclick="clearBox()">CLEAR</div>')
				outFile.write('\n              <div class="editortoolbarsave">')
				outFile.write('\n                <div class="editortoolbaritems" id="save" onclick="saveTextAsFile()">SAVE</div>')
				outFile.write('\n              </div>')
			
			# Print hint
			if unicode(tutorial_num) in ['6', '7','8','9','10']:
				titles = ['What gives?', 'Out of ideas?', 'Not your day?', 'Coder\'s block?', 'Puzzled?', 'Dazed and confused?', 'Battered and bruised?', 'Losing hope?', 'Under the weather?', 'Need a little help?']
				hintcontent = ''
				outFile.write('\n              <div class="editortoolbaritems">')
				for sentence in self.Tutorials_Info['$LEFTPANEL_HINT$\n']:
					hintcontent += '<p>' + sentence + '</p>'
				outFile.write('\n                <a href="#" class="bootstrap-popover" title="'+random.choice(titles).lower()+'" data-content="'+hintcontent+'">')
				outFile.write('\n                HINT')
				outFile.write('\n                </a>')
				outFile.write('\n              </div>')

			outFile.write('\n            </div>')
			#outFile.write('\n        <p class="small">&nbsp;</p>')

			# EDITOR
			if unicode(tutorial_num) in ['3','4','5','6', '7','8','9','10']:
				for sentence in self.Tutorials_Info['$LEFTPANEL_EDITORAREA$\n']:
					outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')
				outFile.write('\n          <form align="left"> ')
				number_of_editor_rows		 = unicode(len(self.Tutorials_Info['$LEFTPANEL_EDITOR$\n'])+4)
				outFile.write('\n            <textarea id="yourcode" class="editortextarea" rows="'+number_of_editor_rows+'">')
				outFile.write('\n')
				for sentence in self.Tutorials_Info['$LEFTPANEL_EDITOR$\n']:
					outFile.write(sentence)
				outFile.write('\n</textarea>')
				outFile.write('\n          </form>')

			# OUTPUT
			if unicode(tutorial_num) in ['3','4','5','6','7','8','9','10']:
				for sentence in self.Tutorials_Info['$LEFTPANEL_OUTPUTAREA$\n']:
					if sentence != '':
						outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')
				outFile.write('\n          <div class="editoroutput">')
				outFile.write('\n          <pre align="left" id="output"></pre>')
				outFile.write('\n          </div>')
				outFile.write('\n')
				outFile.write('\n        </div>')
				outFile.write('\n        <p class="small">&nbsp;</p>')

			# QUESTIONS FOR YOU
			if unicode(tutorial_num) in ['7','9']:
				if len(self.Tutorials_Info['$RIGHTPANEL_QUESTIONS$\n']) <= 1: 
					if tutorial_num == 1:
						outFile.write('\n          <h4 class="h4gold">Questions for You</h4>')
					else:
						outFile.write('\n          <h4 class="h4gold">Question for You</h4>')
					for question in self.Tutorials_Info['$RIGHTPANEL_QUESTIONS$\n']:
						outFile.write('\n            <p>'+question.strip('\n')+'</p>')
				else:
					outFile.write('\n          <h4 class="h4gold">QUESTIONS FOR YOU</h4>')
					outFile.write('\n            <ol>')
					for question in self.Tutorials_Info['$RIGHTPANEL_QUESTIONS$\n']:
						outFile.write('\n              <li>'+question.strip('\n'))
					outFile.write('\n            </ol')

		# NAVIGATION BUTTONS
		outFile.write('\n        <a href="'+previous_Tutorial+'">')
		outFile.write('\n          <button>&lang; PREVIOUS</button>')
		outFile.write('\n        </a>')
		outFile.write('\n        <a href="'+next_Tutorial+'">')
		if unicode(tutorial_num) == '10':
			outFile.write('\n          <button class="start">START &rang; </button>')
		else:
			outFile.write('\n          <button>NEXT &rang; </button>')
		outFile.write('\n        </a>')

		outFile.write('\n      </div>')


		#--------------------
		# Print a middle pane
		#--------------------
		outFile.write('\n      <div class="middlepane">')
		outFile.write('\n      </div>')

		#---------------------
		# Print the right pane
		#---------------------

		if unicode(tutorial_num) in ['1','2','3','4','5', '6', '7', '8', '9', '10']:

			outFile.write('\n      <!-- RIGHT PANEL -->')
			# outFile.write('\n      <div class="rightpane">')

			# # PYTHON SHELL
			# outFile.write('\n          <h4 class="h4gold">PYTHON SHELL</h4>')
			# for sentence in self.Tutorials_Info['$RIGHTPANEL_PYTHONSHELL$\n']:
			# 	outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')
			# outFile.write('\n            <textarea id="interactive" cols="85" rows="1" style="display: none;">')
			# outFile.write('\n            </textarea>')


			# QUESTIONS FOR YOU
			# if unicode(tutorial_num) in ['1']:
			# 	outFile.write('\n          <h4 class="h4gold">TEST CASES</h4>')
			# for question in self.Tutorials_Info['$RIGHTPANEL_TESTCASES$\n']:
			# 	outFile.write('\n            <p>'+question.strip('\n')+'</p>')
			# outFile.write('\n        <p class="small">&nbsp;</p>')

		# outFile.write('\n      </div>')
		outFile.write('\n    </div>')
		outFile.write('\n')


	def PAL_40_Generate_Tutorials(self):
		
		# Load the header
		self.PAL_40_Load_Header_Template()
		
		# Load the navigation
		self.PAL_40_Load_Navigation_Template()

		# Load the closing tags
		self.PAL_40_Load_Closing_Tags_Template()

		for page_num in range(1,11):
			
			# Open web page for writing
			current_Tutorial_html_file = self.HTML_PATHS + unicode(page_num) + '.html'
			outFile = open(current_Tutorial_html_file, 'w')

			# Load the content to go in this file
			self.PAL_40_Load_Tutorial_Content(page_num)
			
			# Print the header
			self.PAL_40_Print_Header_Template(outFile)
			
			# Print the navigation
			self.PAL_40_Print_Navigation_Template(outFile)

			# Print the body
			self.PAL_40_Print_Body(page_num, outFile)

			# Print the title
			self.PAL_40_Print_Title(page_num, outFile)

			# Print closing tags
			self.PAL_40_Print_Closing_Tags_Template(outFile)

			outFile.close()

			# Reset variables
			self.Template_Data		= []
			self.Tutorials_Data		= []
			self.Tutorials_Info		= defaultdict(list)


	def __del__(self):
		pass



if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------

	Generate_Tutorials = PAL_40_Generate_Tutorials()
	Generate_Tutorials.PAL_40_Generate_Tutorials()
