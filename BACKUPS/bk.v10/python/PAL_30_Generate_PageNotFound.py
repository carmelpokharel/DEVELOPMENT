#!/user/bin/env python

from collections import defaultdict

import os


class PAL_30_Generate_PageNotFound(object):
	
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

		self.HTML_PATH			= os.path.join(self.ROOT_DIR, 'pagenotfound.html')

		self.Header_Data		= []
		self.Navigation_Data	= []
		self.Closing_Tags_Data	= []


	def PAL_30_Load_and_Print_Header_Template(self, outFile):

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


	def PAL_30_Load_and_Print_Navigation_Template(self, outFile):

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


	def PAL_30_Load_and_Print_Closing_Tags_Template(self, outFile):

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


	def PAL_30_Print_Title(self, outFile):
		outFile.write('\n    <title>Oops!</title')
		outFile.write('\n')


	def PAL_30_Print_Body(self, outFile):

		#-----------------
		# Print the banner 
		#-----------------
		outFile.write('\n        <!-- BANNER -->')
		outFile.write('\n        <div class="bannerpane">')
		outFile.write('\n          <div class="banneritems">')
		outFile.write('\n            <h2 class="bannertitle">e r r o r</h2>')
		outFile.write('\n          </div><!-- banneritems -->')
		outFile.write('\n        </div><!-- bannerpane -->')

		#--------------------
		# Print the left pane
		#--------------------
		outFile.write('\n')
		outFile.write('\n        <!-- LEFT PANE -->')
		outFile.write('\n        <div class="leftpane">')
		outFile.write('\n        <div class="leftpaneinner">')
		
		# Print message
		outFile.write('\n        <h3>Oops! There\'s nothing here.</h3>')
		outFile.write('\n            <p>Looks like you\'ve stumbled upon a page that doesn\'t (yet) exist.</p>')
		outFile.write('\n            <p>That could mean a couple of things:</p>')
		outFile.write('\n            <ol>')
		outFile.write('\n            <li>We\'re still working on it... it\'ll be up soon!</li>')
		outFile.write('\n            <li>We never intended for this page to exist in the first place -- you found a bug!</li>')
		outFile.write('\n            </ol>')
		outFile.write('\n            <p>If this feels like unexpected behaviour, please call it to our attention below.</p>')
		outFile.write('\n            <button type="button" onclick="window.location.href=\'./index.html\'">Return home</button>')
		outFile.write('\n            <button type="button" onclick="reportBug()">Report bug</button>')

		outFile.write('\n        </div><!-- leftpaneinner -->')
		outFile.write('\n        </div><!-- leftpane -->')

		#---------------------
		# Print the right pane
		#---------------------
		outFile.write('\n')
		outFile.write('\n        <!-- RIGHT PANE -->')
		outFile.write('\n        <div class="rightpane-home">')

		outFile.write('\n        </div><!-- rightpane-home -->')
		outFile.write('\n')
		outFile.write('\n      </div><!-- allpanes_new -->')

		#--------------------
		# Print mobile footer
		#--------------------
		outFile.write('\n')
		outFile.write('\n      <div class="footer">')
		outFile.write('\n        Copyright &copy; Pythons and Ladders 2016')
		outFile.write('\n      </div><!-- footer -->')

		outFile.write('\n')
		outFile.write('\n    </div><!-- wrapper -->')
		outFile.write('\n')


	def PAL_30_Generate_PageNotFound(self):
		
		# Open web page for writing
		PageNotFound = self.HTML_PATH
		outFile = open(PageNotFound, 'w')

		# Load and print the header
		self.PAL_30_Load_and_Print_Header_Template(outFile)

		# Load and print the navigation
		# self.PAL_30_Load_and_Print_Navigation_Template(outFile)

		# Print the body
		self.PAL_30_Print_Body(outFile)

		# Print the title
		self.PAL_30_Print_Title(outFile)

		# Print closing tags
		self.PAL_30_Load_and_Print_Closing_Tags_Template(outFile)

		outFile.close()


	def __del__(self):
		pass



if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------

	PageNotFound = PAL_30_Generate_PageNotFound()
	PageNotFound.PAL_30_Generate_PageNotFound()
