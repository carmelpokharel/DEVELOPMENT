#!/user/bin/env python

from collections import defaultdict

import os


class PAL_11_Generate_Overview(object):
	
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
		# self.NAVIGATION_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_navigation.html')
		self.CLOSING_TAGS_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_closingtags.html')

		self.CONTENT_PATH		= os.path.join(self.CONTENTS_DIR, 'content_overview.txt')
		self.HTML_PATH			= os.path.join(self.ROOT_DIR, 'overview.html')

		self.Header_Data		= []
		self.Navigation_Data	= []
		self.Closing_Tags_Data	= []
		self.Overview_Data		= []
		self.Overview_Info		= defaultdict(list)


	def PAL_11_Load_and_Print_Header_Template(self, outFile):

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


	def PAL_11_Load_and_Print_Navigation_Template(self, outFile):

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


	def PAL_11_Load_and_Print_Closing_Tags_Template(self, outFile):

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


	def PAL_11_Load_Overview_Content(self):
		
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
			self.Overview_Info[section[0]] = section[1:]

		fileStream.close()


	def PAL_11_Print_Title(self, outFile):
		outFile.write('\n    <title>Overview | Pythons and Ladders</title>')
		outFile.write('\n')


	def PAL_11_Print_Body(self, outFile):

		#-----------------
		# Print the banner
		#-----------------
		outFile.write('\n        <!-- BANNER -->')
		outFile.write('\n        <div class="bannerpane">')
		outFile.write('\n          <div class="banneritems">')
		outFile.write('\n            <h2 class="bannertitle">o v e r v i e w</h2>')
		outFile.write('\n          </div><!-- banneritems -->')
		outFile.write('\n        </div><!-- bannerpane -->')

		#--------------------
		# Print the left pane
		#--------------------
		outFile.write('\n')
		outFile.write('\n        <!-- LEFT PANE -->')
		outFile.write('\n        <div class="leftpane">')
		outFile.write('\n        <div class="leftpaneinner">')

		for sentence in self.Overview_Info['$LEFTPANEL_ABOUT$\n']:
			outFile.write('\n          <p>'+sentence.strip('\n')+'</p>')
		outFile.write('\n          <p>&nbsp;</p>')

		outFile.write('\n        <div class="questions-small-devices">')
		outFile.write('\n        <h4 class="greyheading">RESOURCES</h4>')
		for sentence in self.Overview_Info['$RIGHTPANEL_RESOURCES$\n']:
			if '<' not in sentence:
				outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')
			else: 
				outFile.write('\n       '+sentence.strip('\n'))
		outFile.write('\n        </div><!-- questions-small-devices -->')
		
		outFile.write('\n        </div><!-- leftpaneinner -->')
		outFile.write('\n        </div><!-- leftpane -->')



		#---------------------
		# Print the right pane
		#---------------------
		outFile.write('\n')
		outFile.write('\n        <!-- RIGHT PANE -->')
		outFile.write('\n        <div class="rightpane">')
		outFile.write('\n          <div class="infocard">')

		outFile.write('\n        <h4 class="greyheading">RESOURCES</h4>')
		for sentence in self.Overview_Info['$RIGHTPANEL_RESOURCES$\n']:
			if '<' not in sentence:
				outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')
			else: 
				outFile.write('\n       '+sentence.strip('\n'))

		outFile.write('\n          </div><!-- infocard -->')
		outFile.write('\n        </div><!-- rightpane -->')
		outFile.write('\n')
		outFile.write('\n      </div><!-- allpanes_new -->')



	def PAL_11_Generate_Overview(self):
		
		# Open web page for writing
		Overview = self.HTML_PATH
		outFile = open(Overview, 'w')

		# Load the content to go in this file
		self.PAL_11_Load_Overview_Content()

		# Load and print the header
		self.PAL_11_Load_and_Print_Header_Template(outFile)

		# Load and print the navigation
		# self.PAL_11_Load_and_Print_Navigation_Template(outFile)

		# Print the body
		self.PAL_11_Print_Body(outFile)

		# Print the title
		self.PAL_11_Print_Title(outFile)

		# Print closing tags
		self.PAL_11_Load_and_Print_Closing_Tags_Template(outFile)

		outFile.close()


	def __del__(self):
		pass



if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------

	Generate_Overview = PAL_11_Generate_Overview()
	Generate_Overview.PAL_11_Generate_Overview()
