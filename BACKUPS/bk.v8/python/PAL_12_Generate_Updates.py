#!/user/bin/env python

from collections import defaultdict
from datetime import datetime

import os


class PAL_12_Generate_Updates(object):
	
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

		self.LOCAL_ARCHIVE_DIR	= os.path.join(self.UPDATES_DIR, 'archive')
		self.LOCAL_CONTENTS_DIR	= os.path.join(self.UPDATES_DIR, 'data')
		self.LOCAL_PAGES_DIR	= os.path.join(self.UPDATES_DIR, 'pages')

		self.HEADER_PATH		= os.path.join(self.TEMPLATES_DIR, 'template_subpages_header.html')
		self.NAVIGATION_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_subpages_navigation.html')
		self.CLOSING_TAGS_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_closingtags.html')

		self.CONTENT_PATH		= os.path.join(self.LOCAL_CONTENTS_DIR, 'content_updates.txt')
		self.HTML_PATHS			= os.path.join(self.LOCAL_PAGES_DIR, 'updates_')

		self.current_date_key	= ''

		self.Header_Data		= []
		self.Navigation_Data	= []
		self.Closing_Tags_Data	= []
		self.Updates_Info		= defaultdict(list)
		self.Split_Updates_Info = defaultdict(list)
		self.Updates_Data		= defaultdict()
		self.Updates_Dates		= defaultdict()


	def PAL_12_Load_Header_Template(self):

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


	def PAL_12_Print_Header_Template(self, outFile):
		for header_line in self.Header_Data:
			outFile.write(header_line)


	def PAL_12_Load_Navigation_Template(self):

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


	def PAL_12_Print_Navigation_Template(self, outFile):
		for navigation_line in self.Navigation_Data:
			outFile.write(navigation_line)


	def PAL_12_Load_Closing_Tags_Template(self):

		if not os.path.isfile(self.CLOSING_TAGS_PATH):
			print "ERROR: CLOSING TAGS TEMPLATE FILE NOT FOUND"

		fileStream = open(self.CLOSING_TAGS_PATH, 'r')
		allLines = fileStream.readlines()

		for line in allLines[0:]:
			line_list = line
			if line_list != ['']:
				self.Closing_Tags_Data.append(line_list)
		fileStream.close()


	def PAL_12_Print_Closing_Tags_Template(self, outFile):
		for closing_tag in self.Closing_Tags_Data:
			outFile.write(closing_tag)


	def PAL_12_Load_Updates_Content(self):
		
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
			self.Updates_Info[section[0]] = section[1:]

		fileStream.close()


	def PAL_12_Split_Updates_Content(self):

		# Split after a max number of lines5
		input_list 	= self.Updates_Info['$LEFTPANEL_RECENTUPDATES$\n']
		new_list 	= []
		max_length	= 16

		for element in input_list:
			while len(input_list) > 0:
				new_list.append(input_list[:max_length])
				input_list = input_list[max_length:]

		for page_num in range(len(new_list)):
			self.Split_Updates_Info[page_num] = new_list[page_num]

		num_of_pages = len(self.Split_Updates_Info)
		return num_of_pages


	def PAL_12_Print_Title(self, outFile):
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--       TITLE      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <title>Updates & Change Log | Pythons and Ladders</title>\n')
		outFile.write('\n')


	def PAL_12_Print_Body(self, page_num, outFile):

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
		outFile.write('\n    <div class="welcomehome2"></div>')
		outFile.write('\n      <div class="leftpane">')
		
		# Print heading
		outFile.write('\n        <h2>Updates and Change Log</h2>')

		# Process recent updates
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

		# Print recent updates
		for date in reversed(sorted(self.Updates_Data)):
			outFile.write('\n            <h4 class="h4goldsmall">'+date.strftime('%B %d, %Y')+'</h4>')
			outFile.write('\n            <ul>')
			for update in self.Updates_Data[date]:
				outFile.write('\n              <li>'+update+'</li>')
			outFile.write('\n            </ul>')
			outFile.write('\n            <hr>')

		prevupdatepage = 'updates_' + unicode(page_num-1) + '.html'
		nextupdatepage = 'updates_' + unicode(page_num+1) + '.html'
		if page_num != 0:
			outFile.write('\n        <a href="'+prevupdatepage+'">')
			outFile.write('\n          <div class="box-nav-buttons"><div class="box-nav-orange-empty">&lang; PREVIOUS</div></div>')
			outFile.write('\n        </a>')
		if page_num != len(self.Split_Updates_Info)-1:
			outFile.write('\n        <a href="'+nextupdatepage+'">')
			outFile.write('\n          <div class="box-nav-buttons"><div class="box-nav-orange-empty">NEXT &rang; </div></div>')
			outFile.write('\n        </a>')

		outFile.write('\n      <br>')
		outFile.write('\n      <br>')
		outFile.write('\n      <br>')
		outFile.write('\n      <br>')
		outFile.write('\n      </div>')

		#--------------------
		# Print a middle pane
		#--------------------
		outFile.write('\n      <div class="middlepane">')
		outFile.write('\n      </div>')

		#---------------------
		# Print the right pane
		#---------------------
		outFile.write('\n      <!-- RIGHT PANEL -->')
		# outFile.write('\n      <div class="rightpane">')
		
		# outFile.write('\n        <h4 class="greyheading">SPONSORED</h4>')
		# outFile.write('\n          <ul>')
		# for reading in self.Updates_Info['$RIGHTPANEL_SPONSORED$\n']:
		# 	reading = reading.strip('\n').split(' $LINK$ ')
		# 	outFile.write('\n            <a href="'+reading[1]+'" target="_blank"><li class="small">'+reading[0].strip('\n')+'</li></a>')
		# outFile.write('\n          </ul>')
		# outFile.write('\n          <br>')
		# outFile.write('\n      </div>')

		#--------------------
		# Print a middle pane
		#--------------------
		outFile.write('\n    <div class="middlepane">')
		outFile.write('\n    </div>')

		outFile.write('\n    </div>')
		outFile.write('\n')


	def PAL_12_Generate_Updates(self):

		# Load the header
		self.PAL_12_Load_Header_Template()
		
		# Load the navigation
		self.PAL_12_Load_Navigation_Template()

		# Load the closing tags
		self.PAL_12_Load_Closing_Tags_Template()

		# Load the content to go in this file
		self.PAL_12_Load_Updates_Content()

		for page_num in range(self.PAL_12_Split_Updates_Content()):

			# Open web page for writing
			current_updates_html_file = self.HTML_PATHS + unicode(page_num) + '.html'
			outFile = open(current_updates_html_file, 'w')

			# Print the header
			self.PAL_12_Print_Header_Template(outFile)
			
			# Print the navigation
			self.PAL_12_Print_Navigation_Template(outFile)

			# Print the body
			self.PAL_12_Print_Body(page_num, outFile)

			# Print the title
			self.PAL_12_Print_Title(outFile)

			# Print closing tags
			self.PAL_12_Print_Closing_Tags_Template(outFile)

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
