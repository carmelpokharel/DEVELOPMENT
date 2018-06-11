#!/user/bin/env python

from collections import defaultdict

import os
import random


class PAL_20_Generate_Puzzles(object):
	
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

		self.LOCAL_ARCHIVE_DIR	= os.path.join(self.PUZZLES_DIR, 'archive')
		self.LOCAL_CONTENTS_DIR	= os.path.join(self.PUZZLES_DIR, 'data')
		self.LOCAL_PAGES_DIR	= os.path.join(self.PUZZLES_DIR, 'pages')
		
		self.HEADER_PATH		= os.path.join(self.TEMPLATES_DIR, 'template_subpages_header.html')
		self.NAVIGATION_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_subpages_navigation.html')
		self.CLOSING_TAGS_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_closingtags.html')

		self.CONTENT_PATHS		= os.path.join(self.LOCAL_CONTENTS_DIR, 'content_puzzle_')
		self.HTML_PATHS			= os.path.join(self.LOCAL_PAGES_DIR, 'puzzle_')

		self.Header_Data		= []
		self.Navigation_Data	= []
		self.Closing_Tags_Data	= []
		self.Puzzle_Data		= []
		self.Puzzle_Info		= defaultdict(list)

		self.Numbers_to_Words	= { 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
									6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
									11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
									15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
									19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
									50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
									90: 'Ninety', 0: 'Zero'}

		self.Keywords_Delimiter = '$%$%'

		self.Keywords_Formats	= { 'int': "<span class=keyword-teal>int</span>", \
									'str': "<span class=keyword-teal>str</span>", \
									'newline': "<span class=keyword-purple>\\n</span>", \
									 }


	def PAL_20_Spell_Number(self, n):
		try:
			return self.Numbers_to_Words[n]
		except KeyError:
			try:
				return self.Numbers_to_Words[n-n%10] + '-' + self.Numbers_to_Words[n%10]
			except KeyError:
				return 'Number out of range'


	def PAL_20_Load_Header_Template(self):

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


	def PAL_20_Print_Header_Template(self, outFile):
		for header_line in self.Header_Data:
			outFile.write(header_line)


	def PAL_20_Load_Navigation_Template(self):

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


	def PAL_20_Print_Navigation_Template(self, outFile):
		for navigation_line in self.Navigation_Data:
			outFile.write(navigation_line)


	def PAL_20_Load_Closing_Tags_Template(self):

		if not os.path.isfile(self.CLOSING_TAGS_PATH):
			print "ERROR: CLOSING TAGS TEMPLATE FILE NOT FOUND"

		fileStream = open(self.CLOSING_TAGS_PATH, 'r')
		allLines = fileStream.readlines()

		for line in allLines[0:]:
			line_list = line
			if line_list != ['']:
				self.Closing_Tags_Data.append(line_list)
		fileStream.close()


	def PAL_20_Print_Closing_Tags_Template(self, outFile):
		for closing_tag in self.Closing_Tags_Data:
			outFile.write(closing_tag)


	def PAL_20_Load_Puzzle_Content(self, puzzle_num):
		
		current_content_file = self.CONTENT_PATHS + unicode(puzzle_num) + '.txt'

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
			self.Puzzle_Info[section[0]] = section[1:]

		# Process content to format colours of new/key terms
		for heading in self.Puzzle_Info:
			current_section = self.Puzzle_Info[heading]
			tempString = self.Keywords_Delimiter.join(self.Puzzle_Info[heading])
			tempString = tempString.replace('^keyword^int', self.Keywords_Formats['int'])
			tempString = tempString.replace('^keyword^str', self.Keywords_Formats['str'])
			tempString = tempString.replace('^keyword^\\n', self.Keywords_Formats['newline'])

			self.Puzzle_Info[heading] = tempString.split(self.Keywords_Delimiter)

		fileStream.close()


	def PAL_20_Print_Title(self, puzzle_num, outFile):
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--       TITLE      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <title>Puzzle '+unicode(puzzle_num)+' | Pythons and Ladders</title>\n')
		outFile.write('\n')


	def PAL_20_Print_Body(self, puzzle_num, outFile):

		previous_puzzle = 'puzzle_'+unicode(puzzle_num-1)+'.html'
		next_puzzle 	= 'puzzle_'+unicode(puzzle_num+1)+'.html'

		if previous_puzzle not in os.listdir(self.LOCAL_PAGES_DIR):
			if previous_puzzle == 'puzzle_0.html':
				previous_puzzle = '../../../index.html'
			else:
				previous_puzzle = '../../pagenotfound.html'

		if next_puzzle not in os.listdir(self.LOCAL_PAGES_DIR):
			if next_puzzle == 'puzzle_101.html':
				next_puzzle = '../../index.html'
			else:
				next_puzzle = '../../pagenotfound.html'

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
		outFile.write('\n    <div class="leftpane">')
		
		# Print navigation
		outFile.write('\n      <div class="puzzlenav">')
		outFile.write('\n        <a href="puzzle_'+unicode(puzzle_num)+'.html"><div class="box"><div class="box-puzzle-number">'+unicode(puzzle_num)+'</div></div></a>')
		if unicode(puzzle_num) != '1':
			outFile.write('\n        <a href="'+previous_puzzle+'"><div class="box"><div class="box-puzzle-arrows">&lang;</div></div></a>')
		if unicode(puzzle_num) != '100':
			outFile.write('\n        <a href="'+next_puzzle+'"><div class="box"><div class="box-puzzle-arrows">&rang;</div></div></a>')
		outFile.write('\n      </div>')

		outFile.write('\n        <!-- LEFT: QUESTION AND EDITOR -->')
		outFile.write('\n        <br><br><br>')
		
		# Print heading
		if self.Puzzle_Info['$LEFTPANEL_HEADING$\n'] != []:
			songtitle = self.Puzzle_Info['$LEFTPANEL_HEADING$\n'][0].strip()
			songlink  = self.Puzzle_Info['$LEFTPANEL_HEADING$\n'][1].strip()
			outFile.write('\n        <a class="songheading" target="_blank" href="'+songlink+'"">')
			outFile.write('\n        <h3>'+songtitle+'</h3>')
			outFile.write('\n        </a>')

		# Print instructions
		for sentence in self.Puzzle_Info['$LEFTPANEL_INSTRUCTIONS$\n']:
			if '<code>' in sentence:
				outFile.write('\n        <p class="small">'+sentence.strip('\n'))
			elif '<code class="demo">' in sentence:
				outFile.write('\n        <div class="codedemo">'+sentence.strip('\n')+'</div>')
			elif '<code class="demoblock">' in sentence:
				outFile.write('\n        <div class="codedemo">')
				sentence = sentence.split('~')
				for codeline in sentence:
					outFile.write('\n        <p class="medium">'+codeline+'</p>')
				outFile.write('\n        </div>')
			else:
				outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')
		
		# Print question
		alphanum = self.PAL_20_Spell_Number(puzzle_num)
		outFile.write('\n          <h4 class="h4gold">Task '+alphanum+'</h4>')
		for sentence in self.Puzzle_Info['$LEFTPANEL_QUESTION$\n']:
			if '<code>' in sentence:
				outFile.write('\n        <p class="small">'+sentence.strip('\n'))
			else:
				outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')

		# Print editor toolbar
		outFile.write('\n          <div class="editor">')
		outFile.write('\n            <div class="editortoolbar">')
		outFile.write('\n              <div class="editortoolbaritems" onclick="runit()">RUN</div>')
		outFile.write('\n              <div class="editortoolbaritems" onclick="clearBox()">CLEAR</div>')
		outFile.write('\n              <div class="editortoolbarsave">')
		outFile.write('\n                <div class="editortoolbaritems" id="save" onclick="saveTextAsFile()">SAVE</div>')
		outFile.write('\n              </div>')
		outFile.write('\n              <div class="editortoolbaritems">')
		
		# Print hint
		titles = ['What gives?', 'Out of ideas?', 'Not your day?', 'Coder\'s block?', 'Puzzled?', 'Dazed and confused?', 'Battered and bruised?', 'Losing hope?', 'Under the weather?', 'Need a little help?']
		hintcontent = ''
		for sentence in self.Puzzle_Info['$LEFTPANEL_HINTS$\n']:
			hintcontent += '<p>' + sentence + '</p>'
		outFile.write('\n                <a href="#" class="bootstrap-popover" title="'+random.choice(titles).lower()+'" data-content="'+hintcontent+'">')
		outFile.write('\n                HINT')
		outFile.write('\n                </a>')
		outFile.write('\n              </div>')
		
		outFile.write('\n            </div>')

		# Print editor content
		outFile.write('\n          <form align="left"> ')
		number_of_editor_rows		 = unicode(len(self.Puzzle_Info['$LEFTPANEL_EDITOR$\n'])+4)
		
		if int(number_of_editor_rows) <= 4:
			outFile.write('\n            <textarea id="yourcode" class="editortextarea" rows="'+number_of_editor_rows+'"></textarea>')
		else:
			outFile.write('\n            <textarea id="yourcode" class="editortextarea" rows="'+number_of_editor_rows+'">')
			for sentence in self.Puzzle_Info['$LEFTPANEL_EDITOR$\n']:
				outFile.write(sentence)
			outFile.write('\n</textarea>')
		outFile.write('\n          </form>')

		# Print the output box
		outFile.write('\n          <!-- **************** -->')
		outFile.write('\n          <!--     OUTPUT       -->')
		outFile.write('\n          <!-- **************** -->')
		outFile.write('\n          <div class="editoroutput">')
		outFile.write('\n          <pre align="left" id="output"></pre>')
		#outFile.write('\n          <input type="hidden" id="myInput1" value="print SHAMIL(1,2)">')
		#outFile.write('\n          <input type="hidden" id="myInput2" value="print SHAMIL(2,2)">')
		outFile.write('\n          </div>')
		outFile.write('\n')
		outFile.write('\n        </div>')

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
		outFile.write('\n      <div class="rightpane">')
		
		# Print Python shell
		outFile.write('\n            <div class="pythonshell">')
		outFile.write('\n            <h4 class="greyheading">Python Shell</h4>')
		outFile.write('\n            <div class="pythonshellbox">')
		outFile.write('\n            <textarea id="interactive" cols="85" rows="1" style="display: none;">')
		outFile.write('\n            </textarea>')
		outFile.write('\n            </div>')
		outFile.write('\n            </div>')


		# Print questions

		if len(self.Puzzle_Info['$RIGHTPANEL_QUESTIONS$\n']) <= 1: 
			outFile.write('\n          <h4 class="greyheading">Question for You</h4>')
			outFile.write('\n          <div class="questionsforyou">')
			for question in self.Puzzle_Info['$RIGHTPANEL_QUESTIONS$\n']:
				outFile.write('\n            <p>'+question.strip('\n')+'</p>')
			outFile.write('\n          <div>')
		else:
			outFile.write('\n          <h4 class="greyheading">Questions for You</h4>')
			outFile.write('\n          <div class="questionsforyou">')
			outFile.write('\n            <ol>')
			for question in self.Puzzle_Info['$RIGHTPANEL_QUESTIONS$\n']:
				outFile.write('\n              <li>'+question.strip('\n'))
			outFile.write('\n            </ol')
			outFile.write('\n          <div>')
		outFile.write('\n        <p class="small">&nbsp;</p>')

		# outFile.write('\n          </ol>')
		# outFile.write('\n          <h4 class="greyheading">SPONSORED</h4>')
		# outFile.write('\n          <ol>')
		# for reading in self.Puzzle_Info['$RIGHTPANEL_SPONSORED$\n']:
		# 	reading = reading.strip('\n').split(' $LINK$ ')
		# 	outFile.write('\n            <a href="'+reading[1]+'" target="_blank"><li class="small">'+reading[0].strip('\n')+'</li></a>')

		outFile.write('\n        <p class="small">&nbsp;</p>')

		outFile.write('\n      </div>')
		outFile.write('\n    </div>')
		outFile.write('\n')


	def PAL_20_Generate_Puzzles(self):
		
		# Load the header
		self.PAL_20_Load_Header_Template()
		
		# Load the navigation
		self.PAL_20_Load_Navigation_Template()

		# Load the closing tags
		self.PAL_20_Load_Closing_Tags_Template()

		for page_num in range(1,31):
			
			# Open web page for writing
			current_puzzle_html_file = self.HTML_PATHS + unicode(page_num) + '.html'
			outFile = open(current_puzzle_html_file, 'w')

			# Load the content to go in this file
			self.PAL_20_Load_Puzzle_Content(page_num)
			
			# Print the header
			self.PAL_20_Print_Header_Template(outFile)
			
			# Print the navigation
			self.PAL_20_Print_Navigation_Template(outFile)

			# Print the body
			self.PAL_20_Print_Body(page_num, outFile)

			# Print the title
			self.PAL_20_Print_Title(page_num, outFile)

			# Print closing tags
			self.PAL_20_Print_Closing_Tags_Template(outFile)

			outFile.close()

			# Reset variables
			self.Template_Data		= []
			self.Puzzle_Data		= []
			self.Puzzle_Info		= defaultdict(list)


	def __del__(self):
		pass



if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------

	Generate_Puzzles = PAL_20_Generate_Puzzles()
	Generate_Puzzles.PAL_20_Generate_Puzzles()
