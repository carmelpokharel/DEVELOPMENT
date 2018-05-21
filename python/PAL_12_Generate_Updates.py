#!/user/bin/env python

from collections import defaultdict
from datetime import datetime
from PAL_90_Utilities import *

import os


class PAL_12_Generate_Updates(object):
	
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

		self.LOCAL_ARCHIVE_DIR	= os.path.join(self.UPDATES_DIR, 'archive')
		self.LOCAL_CONTENTS_DIR	= os.path.join(self.UPDATES_DIR, 'data')
		self.LOCAL_PAGES_DIR	= os.path.join(self.UPDATES_DIR, 'pages')

		self.HEADER_PATH		= os.path.join(self.TEMPLATES_DIR, 'template_subpages_header.html')
		self.CLOSING_TAGS_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_closingtags.html')

		self.CONTENT_PATH		= os.path.join(self.LOCAL_CONTENTS_DIR, 'content_updates')
		self.HTML_PATHS			= os.path.join(self.LOCAL_PAGES_DIR, 'updates_')

		self.current_date_key	= ''

		self.Header_Data		= []
		self.Navigation_Data	= []
		self.Closing_Tags_Data	= []
		self.Updates_Info		= defaultdict(list)
		self.Split_Updates_Info = defaultdict(list)
		self.Updates_Data		= defaultdict()
		self.Updates_Dates		= defaultdict()

		self.Max_Length 		= 28


	def PAL_12_Split_Updates_Content(self):

		# Split after a max number of lines5
		input_list 	= self.Updates_Info['$LEFTPANEL_RECENTUPDATES$\n']
		new_list 	= []
		max_length	= self.Max_Length

		for element in input_list:
			while len(input_list) > 0:
				new_list.append(input_list[:max_length])
				input_list = input_list[max_length:]

		for page_num in range(len(new_list)):
			self.Split_Updates_Info[page_num] = new_list[page_num]

		num_of_pages = len(self.Split_Updates_Info)
		return num_of_pages


	def PAL_12_Print_Body(self, page_num, outFile):

		#-----------------
		# Print the banner
		#-----------------
		outFile.write('\n        <!-- BANNER -->')
		outFile.write('\n        <div class="bannerpane">')
		outFile.write('\n          <div class="banneritems">')
		outFile.write('\n            <h2 class="bannertitle">c h a n g e l o g</h2>')
		outFile.write('\n          </div><!-- banneritems -->')
		outFile.write('\n        </div><!-- bannerpane -->')
		
		#--------------------
		# Print the left pane
		#--------------------
		outFile.write('\n')
		outFile.write('\n        <!-- LEFT PANE -->')
		outFile.write('\n        <div class="leftpane">')
		outFile.write('\n        <div class="leftpaneinner">')

		current_data = self.Split_Updates_Info[page_num]
		for update in current_data:
			update = update.strip('\n')
			try: update = datetime.strptime(update, '%Y-%m-%d')
			except: pass
			if isinstance(update, datetime):
				self.current_date_key = update
				self.Updates_Data[self.current_date_key] = []
			else:
				try:
					self.Updates_Data[self.current_date_key].append(update)
				except: pass

		for date in reversed(sorted(self.Updates_Data)):
			outFile.write('\n            <p><h4 class="h4gold">'+date.strftime('%B %d, %Y')+'</h4></p>')
			outFile.write('\n            <ul>')
			for update in self.Updates_Data[date]:
				outFile.write('\n              <li>'+update+'</li>')
			outFile.write('\n            </ul>')
			outFile.write('\n            <hr>')

		prevupdatepage = 'updates_' + unicode(page_num-1) + '.html'
		nextupdatepage = 'updates_' + unicode(page_num+1) + '.html'
		if page_num != 0:
			outFile.write('\n        <a style="border-bottom:0px" href="'+prevupdatepage+'">')
			outFile.write('\n          <button>&lang; PREVIOUS</button>')
			outFile.write('\n        </a>')
		if page_num != len(self.Split_Updates_Info)-1:
			outFile.write('\n        <a style="border-bottom:0px" href="'+nextupdatepage+'">')
			outFile.write('\n          <button>NEXT &rang; </button>')
			outFile.write('\n        </a>')


		outFile.write('\n        </div><!-- leftpaneinner -->')
		outFile.write('\n        </div><!-- leftpane -->')

		#--------------------
		# Print a middle pane
		#--------------------
		outFile.write('\n      <div class="middlepane">')
		outFile.write('\n      </div>')

		#---------------------
		# Print the right pane
		#---------------------
		outFile.write('\n')
		outFile.write('\n        <!-- RIGHT PANE -->')
		outFile.write('\n        <div class="rightpane-home">')

		outFile.write('\n        </div><!-- rightpane-home -->')
		outFile.write('\n')
		outFile.write('\n      </div><!-- allpanes_new -->')


	def PAL_12_Generate_Updates(self):

		# Load the templates
		self.Header_Data 		= self.Utilities.PAL_90_Load_Template(self.HEADER_PATH)
		self.Closing_Tags_Data 	= self.Utilities.PAL_90_Load_Template(self.CLOSING_TAGS_PATH)

		# Load the content to go in this file
		self.Updates_Info = self.Utilities.PAL_90_Load_Content('', self.CONTENT_PATH)

		for page_num in range(self.PAL_12_Split_Updates_Content()):

			# Open web page for writing
			current_updates_html_file = self.HTML_PATHS + unicode(page_num) + '.html'
			outFile = open(current_updates_html_file, 'w')

			# Print the header
			self.Utilities.PAL_90_Print_Template(self.Header_Data, outFile)

			# Print the body
			self.PAL_12_Print_Body(page_num, outFile)

			# Print the title
			self.Utilities.PAL_90_Print_Title('Changelog', outFile)

			# Print closing tags
			self.Utilities.PAL_90_Print_Template(self.Closing_Tags_Data, outFile)

			# Reset variables
			self.Updates_Data = defaultdict()

			outFile.close()


	def __del__(self):
		pass


if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------
	Generate_Updates = PAL_12_Generate_Updates()
	Generate_Updates.PAL_12_Generate_Updates()
