#!/user/bin/env python

from collections import defaultdict
from datetime import datetime

import os


class PAL_13_Generate_FAQ(object):
	
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

		self.HEADER_PATH		= os.path.join(self.TEMPLATES_DIR, 'template_header.html')
		self.NAVIGATION_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_navigation.html')
		self.CLOSING_TAGS_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_closingtags.html')
		
		self.CONTENT_PATH		= os.path.join(self.CONTENTS_DIR, 'content_faq.txt')
		self.HTML_PATH			= os.path.join(self.ROOT_DIR, 'faq.html')

		self.current_date_key	= ''

		self.Header_Data		= []
		self.Navigation_Data	= []
		self.Closing_Tags_Data	= []
		self.FAQ_Info			= defaultdict(list)
		self.FAQ_Data			= defaultdict()


	def PAL_13_Load_and_Print_Header_Template(self, outFile):

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

		# Print Header
		for header_line in self.Header_Data:
			outFile.write(header_line)


	def PAL_13_Load_and_Print_Navigation_Template(self, outFile):

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

		# Print Navigation
		for navigation_line in self.Navigation_Data:
			outFile.write(navigation_line)


	def PAL_13_Load_and_Print_Closing_Tags_Template(self, outFile):

		if not os.path.isfile(self.CLOSING_TAGS_PATH):
			print "ERROR: CLOSING TAGS TEMPLATE FILE NOT FOUND"

		fileStream = open(self.CLOSING_TAGS_PATH, 'r')
		allLines = fileStream.readlines()

		for line in allLines[0:]:
			line_list = line
			if line_list != ['']:
				self.Closing_Tags_Data.append(line_list)
		fileStream.close()

		for closing_tag in self.Closing_Tags_Data:
			outFile.write(closing_tag)


	def PAL_13_Load_FAQ_Content(self):
		
		current_content_file = self.CONTENT_PATH

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
			self.FAQ_Info[section[0]] = section[1:]

		fileStream.close()


	def PAL_13_Print_Title(self, outFile):
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--       TITLE      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <title>FAQ | Pythons and Ladders</title>')
		outFile.write('\n')


	def PAL_13_Print_Body(self, outFile):

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
		outFile.write('\n      <!-- LEFT PANEL -->')
		outFile.write('\n      <div class="leftpane">')
		
		# Print heading
		outFile.write('\n        <h2>Frequently Asked Questions</h2>')
		outFile.write('\n        <p class="small">&nbsp;</p>')

		# Process content
		for faq in self.FAQ_Info['$LEFTPANEL_FAQs$\n']:
			if '&#9656;' in faq:
				outFile.write('\n              <p>'+faq+'</p>')
			else:
				outFile.write('\n              <p>'+faq+'</p>')
				outFile.write('\n              <br><hr>')
		outFile.write('\n      </div>')

		#--------------------
		# Print a middle pane
		#--------------------
		outFile.write('\n      <div class="middlepane">')
		outFile.write('\n      </div>')

		#---------------------
		# Print the right pane
		#---------------------
		# outFile.write('\n      <!-- RIGHT PANEL -->')
		# outFile.write('\n      <div class="rightpane">')
		
		# outFile.write('\n        <h4 class="greyheading">SPONSORED</h4>')
		# outFile.write('\n          <ul>')
		# for reading in self.FAQ_Info['$RIGHTPANEL_SPONSORED$\n']:
		# 	reading = reading.strip('\n').split(' $LINK$ ')
		# 	outFile.write('\n            <a href="'+reading[1]+'" target="_blank"><li class="small">'+reading[0].strip('\n')+'</li></a>')
		# outFile.write('\n          </ul><br>')
		# outFile.write('\n      </div>')

		#--------------------
		# Print a middle pane
		#--------------------
		outFile.write('\n    <div class="middlepane">')
		outFile.write('\n    </div>')

		outFile.write('\n    </div>')
		outFile.write('\n')


	def PAL_13_Generate_FAQ(self):
		
		# Open web page for writing
		faq = self.HTML_PATH
		outFile = open(faq, 'w')

		# Load the content to go in this file
		self.PAL_13_Load_FAQ_Content()

		# Load and print the header
		self.PAL_13_Load_and_Print_Header_Template(outFile)

		# Load and print the navigation
		self.PAL_13_Load_and_Print_Navigation_Template(outFile)

		# Print the body
		self.PAL_13_Print_Body(outFile)

		# Print the title
		self.PAL_13_Print_Title(outFile)

		# Print closing tags
		self.PAL_13_Load_and_Print_Closing_Tags_Template(outFile)

		outFile.close()


	def __del__(self):
		pass



if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------

	Generate_FAQ = PAL_13_Generate_FAQ()
	Generate_FAQ.PAL_13_Generate_FAQ()
