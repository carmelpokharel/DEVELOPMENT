#!/user/bin/env python

from collections import defaultdict
from PAL_90_Utilities import *

import os


class PAL_11_Generate_Overview(object):
	
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
		self.CLOSING_TAGS_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_closingtags.html')

		self.CONTENT_PATH		= os.path.join(self.CONTENTS_DIR, 'content_overview')
		self.HTML_PATH			= os.path.join(self.ROOT_DIR, 'overview.html')

		self.Header_Data		= []
		self.Navigation_Data	= []
		self.Closing_Tags_Data	= []
		self.Overview_Info		= defaultdict(list)


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
		self.Overview_Info = self.Utilities.PAL_90_Load_Content('', self.CONTENT_PATH)

		# Load and print the header
		self.Header_Data = self.Utilities.PAL_90_Load_Template(self.HEADER_PATH)
		self.Utilities.PAL_90_Print_Template(self.Header_Data, outFile)

		# Print the body
		self.PAL_11_Print_Body(outFile)

		# Print the title
		self.Utilities.PAL_90_Print_Title('Overview', outFile)

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
	Generate_Overview = PAL_11_Generate_Overview()
	Generate_Overview.PAL_11_Generate_Overview()
