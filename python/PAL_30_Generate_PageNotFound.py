#!/user/bin/env python

from collections import defaultdict
from PAL_90_Utilities import *

import os


class PAL_30_Generate_PageNotFound(object):
	
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

		self.HEADER_PATH		= os.path.join(self.TEMPLATES_DIR, 'template_header.html')
		self.NAVIGATION_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_navigation.html')
		self.CLOSING_TAGS_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_closingtags.html')

		self.HTML_PATH			= os.path.join(self.ROOT_DIR, 'pagenotfound.html')

		self.Header_Data		= []
		self.Navigation_Data	= []
		self.Closing_Tags_Data	= []


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


	def PAL_30_Generate_PageNotFound(self):
		
		# Open web page for writing
		PageNotFound = self.HTML_PATH
		outFile = open(PageNotFound, 'w')

		# Load and print the header
		self.Header_Data = self.Utilities.PAL_90_Load_Template(self.HEADER_PATH)
		self.Utilities.PAL_90_Print_Template(self.Header_Data, outFile)

		# Print the body
		self.PAL_30_Print_Body(outFile)

		# Print the title
		self.Utilities.PAL_90_Print_Title('Oops!', outFile)

		# Print closing tags
		self.Closing_Tags_Data = self.Utilities.PAL_90_Load_Template(self.CLOSING_TAGS_PATH)
		self.Utilities.PAL_90_Print_Template(self.Closing_Tags_Data, outFile)

		outFile.close()


	def __del__(self):
		pass


if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------
	PageNotFound = PAL_30_Generate_PageNotFound()
	PageNotFound.PAL_30_Generate_PageNotFound()
