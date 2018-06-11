#!/user/bin/env python

from collections import defaultdict
from PAL_90_Utilities import *

import os
import random

class PAL_40_Generate_Tutorials(object):
	
	def __init__(self):

		# Initialize utilities
		self.Utilities = PAL_90_Utilities_Class()
		self.Utilities.__init__()
		
		self.ROOT_DIR 			= os.path.dirname(os.getcwd())
		self.BACKUPS_DIR		= os.path.join(self.ROOT_DIR, 'backups')
		self.CSS_DIR			= os.path.join(self.ROOT_DIR, 'css')
		self.IMAGES_DIR			= os.path.join(self.ROOT_DIR, 'images')
		self.JAVASCRIPT_DIR		= os.path.join(self.ROOT_DIR, 'js')
		self.PYTHON_DIR			= os.getcwd()

		self.MAIN_DIR			= os.path.join(self.ROOT_DIR, 'main')
		self.CONTENTS_DIR 		= os.path.join(self.MAIN_DIR, 'data')
		self.SQUARES_DIR 		= os.path.join(self.MAIN_DIR, 'squares')
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
			if '<li' not in sentence and 'ul>' not in sentence:
				outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')
			else:
				outFile.write('\n        '+sentence.strip('\n'))

		if str(tutorial_num) in ['3','4','5','6','7','8','9']:
			
			# INSTRUCTIONS
			if str(tutorial_num) in ['5','8','9']:
				for sentence in self.Tutorials_Info['$LEFTPANEL_INSTRUCTIONSAREA$\n']:
					if '<code>' in sentence:
						outFile.write('\n        <p class="small">'+sentence.strip('\n')+'</p>')
					else:
						outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')

			# TOOLBAR
			if str(tutorial_num) in ['3','4','5','6','7','8','9']:
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
			if str(tutorial_num) in ['6','7','8','9']:
				titles = ['What gives?', 'Out of ideas?', 'Not your day?', 'Coder\'s block?', 'Dazed and confused?', 'Battered and bruised?', 'Losing hope?', 'Under the weather?', 'Need a little help?']
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
			if str(tutorial_num) in ['3','4','5','6','7','8','9']:
				outFile.write('\n          <form align="left"> ')
				number_of_editor_rows		 = str(len(self.Tutorials_Info['$LEFTPANEL_EDITOR$\n'])+4)
				
				if int(number_of_editor_rows) <= 4:
					outFile.write('\n            <textarea id="textbox" name="textbox" rows="'+number_of_editor_rows+'">')
				else:
					outFile.write('\n            <textarea id="textbox" name="textbox" rows="'+number_of_editor_rows+'">')
					for sentence in self.Tutorials_Info['$LEFTPANEL_EDITOR$\n']:
						outFile.write(sentence)
					outFile.write('\n</textarea>')
				outFile.write('\n          </form>')

			# OUTPUT
			if str(tutorial_num) in ['3','4','5','6','7','8','9']:
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
		if self.Tutorials_Info['$RIGHTPANEL_QUESTIONS$\n'] == ['']:
			pass
		elif len(self.Tutorials_Info['$RIGHTPANEL_QUESTIONS$\n']) not in [0]:
			if int(tutorial_num) == 1:
				outFile.write('\n          <h4 class="h4gold">Why Python?</h4>')
			elif int(tutorial_num) < 6 or int(tutorial_num) == 8:
				outFile.write('\n          <h4 class="h4gold">Notes</h4>')
			else:
				outFile.write('\n          <h4 class="h4gold">Questions for You</h4>')
			for question in self.Tutorials_Info['$RIGHTPANEL_QUESTIONS$\n']:
				if '<code> or <cardcode' in question:
					outFile.write('\n              '+question.strip('\n'))
				else:
					outFile.write('\n              <p>'+question.strip('\n')+'</p>')
		outFile.write('\n       </div><!-- questions-small-devices -->')
		outFile.write('\n')


		# NAVIGATION BUTTONS
		previous_Tutorial = 'tutorial_'+str(tutorial_num-1)+'.html'
		next_Tutorial 	= 'tutorial_'+str(tutorial_num+1)+'.html'

		if previous_Tutorial not in os.listdir(self.LOCAL_PAGES_DIR):
			if previous_Tutorial == 'tutorial_0.html':
				previous_Tutorial = '../../index.html'
			else:
				previous_Tutorial = '../../pagenotfound.html'

		if next_Tutorial not in os.listdir(self.LOCAL_PAGES_DIR):
			if next_Tutorial == 'tutorial_10.html':
				next_Tutorial = '../../squares/pages/square_1.html'
			else:
				next_Tutorial = '../../pagenotfound.html'

		outFile.write('\n        <a style="border-bottom:0px" href="'+previous_Tutorial+'">')
		if tutorial_num != 1:
			outFile.write('\n          <button>&lang; PREVIOUS</button>')
		outFile.write('\n        </a>')
		outFile.write('\n        <a style="border-bottom:0px" href="'+next_Tutorial+'">')
		if int(tutorial_num) == 9:
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
			if int(tutorial_num) == 1:
				outFile.write('\n          <h4 class="greyheading">Why Python?</h4>')
			elif int(tutorial_num) < 6 or int(tutorial_num) == 8:
				outFile.write('\n          <h4 class="greyheading">Notes</h4>')
			else:
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


	def PAL_40_Generate_Tutorials(self):
		
		# Load the templates
		self.Header_Data 		= self.Utilities.PAL_90_Load_Template(self.HEADER_PATH)
		self.Closing_Tags_Data 	= self.Utilities.PAL_90_Load_Template(self.CLOSING_TAGS_PATH)

		for page_num in range(1,10):
			
			# Open web page for writing
			current_html_file = self.HTML_PATHS + str(page_num) + '.html'
			outFile = open(current_html_file, 'w')

			# Load the content
			self.Tutorials_Info = self.Utilities.PAL_90_Load_Content(page_num, self.CONTENT_PATHS)
			
			# Print the header
			self.Utilities.PAL_90_Print_Template(self.Header_Data, outFile)

			# Print the body
			self.PAL_40_Print_Body(page_num, outFile)

			# Print the title
			self.Utilities.PAL_90_Print_Title('Tutorial', outFile)

			# Print closing tags
			self.Utilities.PAL_90_Print_Template(self.Closing_Tags_Data, outFile)

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
