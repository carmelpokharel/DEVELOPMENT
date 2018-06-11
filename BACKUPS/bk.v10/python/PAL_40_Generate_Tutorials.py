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
		outFile.write('\n    <title>Tutorial | Pythons and Ladders</title>\n')
		outFile.write('\n')


	def PAL_40_Print_Body(self, tutorial_num, outFile):

		#-----------------
		# Print the banner
		#-----------------
		outFile.write('\n        <!-- BANNER -->')
		outFile.write('\n        <div class="bannerpane">')
		outFile.write('\n          <div class="banneritems">')

		outFile.write('\n        <h2 class="bannertitle">t u t o r i a l</h2>')

		outFile.write('\n          </div><!-- banneritems -->')
		outFile.write('\n        </div><!-- bannerpane -->')


		#--------------------
		# Print the left pane
		#--------------------
		outFile.write('\n')
		outFile.write('\n        <!-- LEFT PANE -->')
		outFile.write('\n        <div class="leftpane">')
		outFile.write('\n          <div class="leftpaneinner">')

		# SONG TITLE
		if self.Tutorials_Info['$LEFTPANEL_MAIN$\n'] != []:
			title = self.Tutorials_Info['$LEFTPANEL_MAIN$\n'][0].strip()
			outFile.write('\n        <h3>'+title+'</h3>')

		# MAIN
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
				outFile.write('\n                <a style="border-bottom:0px" href="#" class="bootstrap-popover" title="'+random.choice(titles).lower()+'" data-content="'+hintcontent+'">')
				outFile.write('\n                HINT')
				outFile.write('\n                </a>')
				outFile.write('\n              </div>')

			outFile.write('\n            </div>')
			#outFile.write('\n        <p class="small">&nbsp;</p>')

			# EDITOR
			if unicode(tutorial_num) in ['3','4','5','6', '7','8','9','10']:
				outFile.write('\n          <form align="left"> ')
				number_of_editor_rows		 = unicode(len(self.Tutorials_Info['$LEFTPANEL_EDITOR$\n'])+4)
				
				if int(number_of_editor_rows) <= 4:
					outFile.write('\n            <textarea id="textbox" name="textbox" rows="'+number_of_editor_rows+'">')
				else:
					outFile.write('\n            <textarea id="textbox" name="textbox" rows="'+number_of_editor_rows+'">')
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
				outFile.write('\n          <pre align="left" id="dynamicframe"></pre>')
				outFile.write('\n          </div><!-- editoroutput -->')
				outFile.write('\n')
				outFile.write('\n        </div><!-- editor -->')

			# Print questions for you under the "smalldevices" class
			outFile.write('\n       <div class="questions-small-devices">')
			# Print questions
			if unicode(tutorial_num) in ['7', '8', '9']:
				if len(self.Tutorials_Info['$RIGHTPANEL_QUESTIONS$\n']) not in [0]:
					outFile.write('\n          <h4 class="h4gold">Questions for You</h4>')
					for question in self.Tutorials_Info['$RIGHTPANEL_QUESTIONS$\n']:
						if '<code> or <cardcode' in question:
							outFile.write('\n              '+question.strip('\n'))
						else:
							outFile.write('\n              <p>'+question.strip('\n')+'</p>')
			outFile.write('\n       </div><!-- questions-small-devices -->')
			outFile.write('\n')


		# NAVIGATION BUTTONS
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

		outFile.write('\n        <a style="border-bottom:0px" href="'+previous_Tutorial+'">')
		if tutorial_num != 1:
			outFile.write('\n          <button>&lang; PREVIOUS</button>')
		outFile.write('\n        </a>')
		outFile.write('\n        <a style="border-bottom:0px" href="'+next_Tutorial+'">')
		if unicode(tutorial_num) == '10':
			outFile.write('\n          <button class="start">START &rang; </button>')
		else:
			outFile.write('\n          <button>NEXT &rang; </button>')
		outFile.write('\n        </a>')


		outFile.write('\n        </div><!-- leftpaneinner -->')
		outFile.write('\n        </div><!-- leftpane -->')


		#---------------------
		# Print the right pane
		#---------------------
		outFile.write('\n')
		outFile.write('\n        <!-- RIGHT PANE -->')
		outFile.write('\n       <div class="questions-large-devices">')

		# Print questions
		outFile.write('\n         <div class="rightpane">')
		if self.Tutorials_Info['$RIGHTPANEL_QUESTIONS$\n'] == ['']:
			pass
		else:
			outFile.write('\n        <div class="infocard">')
			outFile.write('\n          <h4 class="greyheading">Questions for You</h4>')
			for question in self.Tutorials_Info['$RIGHTPANEL_QUESTIONS$\n']:
				if '<code> or <cardcode' in question:
					outFile.write('\n              '+question.strip('\n'))
				else:
					outFile.write('\n              <p>'+question.strip('\n')+'</p>')
			outFile.write('\n        </div><!-- infocard -->')
		outFile.write('\n          </div><!-- rightpane -->')

		outFile.write('\n        </div><!-- questions-large-devices -->')
		outFile.write('\n')
		outFile.write('\n      </div><!-- allpanes_new -->')

		#-------------
		# Print footer
		#-------------
		outFile.write('\n')
		outFile.write('\n      <div class="footer">')
		outFile.write('\n        Copyright &copy; Pythons and Ladders 2016')
		outFile.write('\n      </div><!-- footer -->')

		outFile.write('\n')
		outFile.write('\n    </div><!-- wrapper -->')
		outFile.write('\n')




	def PAL_40_Generate_Tutorials(self):
		
		# Load the header
		self.PAL_40_Load_Header_Template()
		
		# Load the navigation
		# self.PAL_40_Load_Navigation_Template()

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
			# self.PAL_40_Print_Navigation_Template(outFile)

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
