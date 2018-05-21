#!/user/bin/env python

from collections import defaultdict
from PAL_90_Utilities import *

import os
import random

class PAL_20_Generate_Squares(object):
	
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

		self.LOCAL_ARCHIVE_DIR	= os.path.join(self.SQUARES_DIR, 'archive')
		self.LOCAL_CONTENTS_DIR	= os.path.join(self.SQUARES_DIR, 'data')
		self.LOCAL_PAGES_DIR	= os.path.join(self.SQUARES_DIR, 'pages')
		
		self.HEADER_PATH		= os.path.join(self.TEMPLATES_DIR, 'template_subpages_header.html')
		self.NAVIGATION_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_subpages_navigation.html')
		self.CLOSING_TAGS_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_closingtags.html')

		self.CONTENT_PATHS		= os.path.join(self.LOCAL_CONTENTS_DIR, 'content_square_')
		self.HTML_PATHS			= os.path.join(self.LOCAL_PAGES_DIR, 'square_')

		self.Header_Data		= []
		self.Navigation_Data	= []
		self.Closing_Tags_Data	= []
		self.Square_Data		= []
		self.Square_Info		= defaultdict(list)
		self.Submit_Cases		= []

		self.Easy_Alt_Exists	= False
		self.Hard_Alt_Exists 	= False


	def PAL_20_Print_Header_Template(self, outFile):
		for header_line in self.Header_Data:

			if '</head>' in header_line:

				outFile.write('\n    <script>')
				outFile.write('\n      function testit() {')

				error_string  = '"<span class=keyword-error>SemanticError: invalid logic encountered</span>"'
				concat_string = '\\ntry:\\n' + (''.join(self.Submit_Cases)).replace('\n', '\\n') + 'except:\\n\\tprint ' + error_string

				outFile.write('\n        var prog = editor.getDoc().getValue().concat(\''+'\\nprint "<b>TEST RESULTS</b>:"'+concat_string+'\');')
				outFile.write('\n        var mypre = document.getElementById("dynamicframe");')
				#outFile.write('\n        window.alert(prog);')
				outFile.write('\n        mypre.innerHTML = \'\';')
				outFile.write('\n        Sk.pre = "dynamicframe";')
				outFile.write('\n        Sk.configure({')
				outFile.write('\n            output: outf,')
				outFile.write('\n            read: builtinRead')
				outFile.write('\n        });')
				outFile.write('\n        var myPromise = Sk.misceval.asyncToPromise(function() {')
				outFile.write('\n            return Sk.importMainWithBody("<stdin>", false, prog, true);')
				outFile.write('\n        });')
				outFile.write('\n        myPromise.then(function(mod) {')
				outFile.write('\n                console.log(\'success\');')
				outFile.write('\n            },')
				outFile.write('\n            function(err) {')
				outFile.write('\n                console.log(err.toString());')
				outFile.write('\n            });')
				outFile.write('\n      }')
				outFile.write('\n    </script>')
				outFile.write('\n  </head>')

			else:
				outFile.write(header_line)


	def PAL_20_Load_Square_Content(self, square_num):
		
		current_content_file 	= self.CONTENT_PATHS + unicode(square_num) + '.txt'
		easy_content_file 		= self.CONTENT_PATHS + unicode(square_num) + '_easy.txt'
		hard_content_file 		= self.CONTENT_PATHS + unicode(square_num) + '_hard.txt'

		if os.path.exists(easy_content_file):
			self.Easy_Alt_Exists = True
		if os.path.exists(hard_content_file):
			self.Hard_Alt_Exists = True

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
			self.Square_Info[section[0]] = section[1:]

		# Populate test cases for SUBMIT button
		for key in self.Square_Info:
			if key == '$ALLPANES_SUBMITCASES$\n':
				self.Submit_Cases = self.Square_Info[key]
		for case in self.Submit_Cases:
			self.Submit_Cases[self.Submit_Cases.index(case)] = case\
			.replace('PASSED!', '<span class=keyword-green>PASSED!</span>')\
			.replace('FAILED', '<span class=keyword-red>FAILED</span>')\
			.replace('\'', '\\\'')
		for case in self.Submit_Cases:
			self.Submit_Cases[self.Submit_Cases.index(case)] = '    ' + self.Submit_Cases[self.Submit_Cases.index(case)]

		# Process content to format colours of new/key terms
		for heading in self.Square_Info:
			current_section = self.Square_Info[heading]
			tempString = self.Utilities.Keywords_Delimiter.join(self.Square_Info[heading])

			# Format special characters
			tempString = self.Utilities.PAL_90_Format_Special_Characters(tempString)

			self.Square_Info[heading] = tempString.split(self.Utilities.Keywords_Delimiter)

		fileStream.close()


	# def PAL_20_Print_Mini_Row(self, outFile):

	# 	outFile.write('\n            <div>')

	# 	end_square = 0
	# 	for id_num in range(1,6):
	# 		id_num = unicode(id_num)

	# 		start_square 	= end_square + 1
	# 		end_square 		= start_square + 19

	# 		square_string	= unicode(start_square) + ' to ' + unicode(end_square)

	# 		outFile.write('\n          <label class="minigameboard-row" for="_'+id_num+'">Squares '+square_string+'</label>')
	# 		outFile.write('\n          <input id="_'+id_num+'" type="checkbox">')
	# 		outFile.write('\n          <div class="minigameboard-box-contain">')
			
	# 		for square in range (int(start_square), int(end_square)+1):
	# 			square = unicode(square)
	# 			square_link = 'square_' + square + '.html'

	# 			if square_link in os.listdir(self.LOCAL_PAGES_DIR):
	# 				if square == '1':
	# 					outFile.write('\n          <a href="./main/squares/pages/square_'+square+'.html"><div class="minigameboard-box-start" onclick="">'+'GO'+'</div></a>')
	# 				else:
	# 					outFile.write('\n          <a href="./main/squares/pages/square_'+square+'.html"><div class="minigameboard-box" onclick="">'+square+'</div></a>')
	# 			else: 
	# 				outFile.write('\n          <a href="../../../pagenotfound.html"><div class="minigameboard-box" onclick="">'+square+'</div></a>')

	# 		outFile.write('\n          </div><!-- minigameboard-box-contain -->')
	# 	outFile.write('\n            </div><!-- anonymous div -->')


	def PAL_20_Print_Body(self, square_num, outFile):

		#-----------------
		# Print the banner
		#-----------------
		outFile.write('\n        <!-- BANNER -->')
		outFile.write('\n        <div class="bannerpane">')
		outFile.write('\n          <div class="banneritems">')

		easy_square 	= 'square_'+unicode(square_num)+'_easy.html'
		hard_square 	= 'square_'+unicode(square_num)+'_hard.html'
		previous_square = 'square_'+unicode(square_num-1)+'.html'
		next_square 	= 'square_'+unicode(square_num+1)+'.html'

		if previous_square not in os.listdir(self.LOCAL_PAGES_DIR):
			if previous_square == 'square_0.html':
				previous_square = '../../../index.html'
			else:
				previous_square = '../../../pagenotfound.html'

		if next_square not in os.listdir(self.LOCAL_PAGES_DIR):
			if next_square == 'square_101.html':
				next_square = '../../../index.html'
			else:
				next_square = '../../../pagenotfound.html'

		outFile.write('\n      <div class="squarenav2">')
		outFile.write('\n        <a href="square_'+unicode(square_num)+'.html"><div class="box-square2"><div class="box-square-number2" onclick="">'+unicode(square_num)+'</div></div></a>')

		if unicode(square_num) != '1':
			outFile.write('\n        <a href="'+previous_square+'"><div class="box-square2"><div class="box-square-arrows2" onclick="">&lang;</div></div></a>')
		if unicode(square_num) != '100':
			outFile.write('\n        <a href="'+next_square+'"><div class="box-square2"><div class="box-square-arrows2" onclick="">&rang;</div></div></a>')

		# Print link to easy/hard if available
		if self.Easy_Alt_Exists:
			outFile.write('\n        <a href="'+easy_square+'"><div class="box-square2"><div class="box-square-arrows2" onclick=""><img style="width:80%;height:100%;max-width:47px" src="../../../images/snake.png"></div></div></a>')
		self.Easy_Alt_Exists = False
		if self.Hard_Alt_Exists:
			outFile.write('\n        <a href="'+hard_square+'"><div class="box-square2"><div class="box-square-arrows2" onclick=""><img style="width:80%;height:100%;max-width:47px" src="../../../images/ladder.png"></div></div></a>')
		self.Hard_Alt_Exists = False

		outFile.write('\n      </div>')

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
		if self.Square_Info['$LEFTPANEL_HEADING$\n'] != []:
			songtitle = self.Square_Info['$LEFTPANEL_HEADING$\n'][0].strip()
			songlink  = self.Square_Info['$LEFTPANEL_HEADING$\n'][1].strip()
			outFile.write('\n        <a class="songheading" target="_blank" href="'+songlink+'"">')
			outFile.write('\n        <h3>'+songtitle+'</h3>')
			outFile.write('\n        </a>')

		# Print instructions
		for sentence in self.Square_Info['$LEFTPANEL_INSTRUCTIONS$\n']:
			if '<code>' in sentence:
				outFile.write('\n        <p class="small">'+sentence.strip('\n')+'</p>')
			else:
				outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')
		
		# Print question
		alphanum = self.Utilities.PAL_90_Spell_Number(square_num)
		outFile.write('\n          <h4 class="h4gold">Task '+alphanum+'</h4>')
		for sentence in self.Square_Info['$LEFTPANEL_QUESTION$\n']:
			if '<code>' in sentence:
				outFile.write('\n        <p class="small">'+sentence.strip('\n')+'</p>')
			else:
				outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')

		# Print editor toolbar
		outFile.write('\n          <div class="editor">')
		outFile.write('\n            <div class="editortoolbar">')
		outFile.write('\n              <div class="editortoolbaritems" onclick="runit()">RUN</div>')
		outFile.write('\n              <div class="editortoolbaritems" onclick="clearBox()">CLEAR</div>')
		
		outFile.write('\n              <div class="editortoolbarsave">')
		outFile.write('\n                <div class="editortoolbaritems" id="save" onclick="saveTextAsFile()">SAVE</div>')
		outFile.write('\n              </div><!-- editortoolbarsave -->')
		
		# Print hint
		outFile.write('\n              <div class="editortoolbaritems">')
		hintcontent = ''
		for sentence in self.Square_Info['$LEFTPANEL_HINTS$\n']:
			hintcontent += '<p>' + sentence + '</p>'
		outFile.write('\n                <a href="#" style="border-bottom:0px" class="bootstrap-popover" title="'+random.choice(self.Utilities.Hint_Titles).lower()+'" data-content="'+hintcontent+'">')
		outFile.write('\n                HINT')
		outFile.write('\n                </a>')
		outFile.write('\n              </div><!-- editortoolbaritems -->')
		if self.Utilities.PAL_90_Eligible_For_Submit_Button(square_num):
			outFile.write('\n                <div class="editortoolbaritems-submit" onclick="testit()">SUBMIT</div>')
		outFile.write('\n            </div><!-- editortoolbar -->')

		# Print editor content
		outFile.write('\n          <form> ')
		number_of_editor_rows		 = unicode(len(self.Square_Info['$LEFTPANEL_EDITOR$\n'])+4)
		
		if int(number_of_editor_rows) <= 4:
			outFile.write('\n            <textarea id="textbox" name="textbox" rows="'+number_of_editor_rows+'">')
		else:
			outFile.write('\n            <textarea id="textbox" name="textbox" rows="'+number_of_editor_rows+'">')

			aggregated_sentence = ''
			for sentence in self.Square_Info['$LEFTPANEL_EDITOR$\n']:
				aggregated_sentence += sentence
			outFile.write(aggregated_sentence[:-1])
			outFile.write('\n</textarea>')
		outFile.write('\n          </form>')

		outFile.write('\n          <div class="editoroutput">')
		outFile.write('\n          <pre align="left" id="dynamicframe"></pre>')
		outFile.write('\n          </div><!-- editoroutput -->')
		outFile.write('\n')
		outFile.write('\n        </div><!-- editor -->')


		# Print questions for you under the "smalldevices" class
		outFile.write('\n       <div class="questions-small-devices">')


		# Print questions
		if self.Square_Info['$RIGHTPANEL_QUESTIONS$\n'] == ['']:
			pass
		elif len(self.Square_Info['$RIGHTPANEL_QUESTIONS$\n']) not in [0]:
			outFile.write('\n          <h4 class="h4gold">Questions for You</h4>')
			for question in self.Square_Info['$RIGHTPANEL_QUESTIONS$\n']:
				if '<code> or <cardcode' in question:
					outFile.write('\n              '+question.strip('\n'))
				else:
					outFile.write('\n              <p>'+question.strip('\n')+'</p>')

		# Print notes
		if self.Square_Info['$RIGHTPANEL_TESTCASES$\n'] == ['']:
			pass
		elif len(self.Square_Info['$RIGHTPANEL_TESTCASES$\n']) not in [0]:
			outFile.write('\n          <h4 class="h4gold">Notes</h4>')
			for testcase in self.Square_Info['$RIGHTPANEL_TESTCASES$\n']:
				if '<code> or <cardcode' in testcase:
					outFile.write('\n              '+testcase.strip('\n'))
				else:
					outFile.write('\n              <p>'+testcase.strip('\n')+'</p>')
		
		outFile.write('\n       </div><!-- questions-small-devices -->')
		outFile.write('\n')

		# NAVIGATION BUTTONS
		outFile.write('\n        <a style="border-bottom:0px" href="'+previous_square+'">')
		if square_num != 1:
			outFile.write('\n          <button>&lang; PREVIOUS</button>')
		outFile.write('\n        </a>')
		outFile.write('\n        <a style="border-bottom:0px" href="'+next_square+'">')
		if unicode(square_num) == '100':
			outFile.write('\n          <button class="start">FINISH!</button>')
		else:
			outFile.write('\n          <button>NEXT &rang; </button>')
		outFile.write('\n        </a>')


		outFile.write('\n          </div><!-- leftpaneinner -->')
		outFile.write('\n        </div><!-- leftpane -->')



		#---------------------
		# Print the right pane
		#---------------------
		outFile.write('\n')
		outFile.write('\n        <!-- RIGHT PANE -->')
		outFile.write('\n       <div class="questions-large-devices">')

		# Print questions
		outFile.write('\n         <div class="rightpane">')
		if self.Square_Info['$RIGHTPANEL_QUESTIONS$\n'] == ['']:
			pass
		else:
			outFile.write('\n        <div class="infocard">')
			outFile.write('\n          <h4 class="greyheading">Questions for You</h4>')
			for question in self.Square_Info['$RIGHTPANEL_QUESTIONS$\n']:
				if '<code> or <cardcode' in question:
					outFile.write('\n              '+question.strip('\n'))
				else:
					outFile.write('\n              <p>'+question.strip('\n')+'</p>')
			outFile.write('\n        </div><!-- infocard -->')
		outFile.write('\n          </div><!-- rightpane -->')

		# Print notes
		outFile.write('\n         	<div class="rightpane">')
		if self.Square_Info['$RIGHTPANEL_TESTCASES$\n'] == ['']:
			pass
		else:
			outFile.write('\n         <div class="infocard">')
			outFile.write('\n          <h4 class="greyheading">NOTES</h4>')
			for testcase in self.Square_Info['$RIGHTPANEL_TESTCASES$\n']:
				if '<code> or <cardcode' in testcase:
					outFile.write('\n              '+testcase.strip('\n'))
				else:
					outFile.write('\n              <p>'+testcase.strip('\n')+'</p>')
			outFile.write('\n        </div><!-- infocard -->')
		outFile.write('\n          </div><!-- rightpane -->')


		outFile.write('\n        </div><!-- questions-large-devices -->')
		outFile.write('\n')
		outFile.write('\n      </div><!-- allpanes_new -->')


	def PAL_20_Generate_Squares(self):
		
		# Load the templates
		self.Header_Data 		= self.Utilities.PAL_90_Load_Template(self.HEADER_PATH)
		self.Closing_Tags_Data 	= self.Utilities.PAL_90_Load_Template(self.CLOSING_TAGS_PATH)

		for page_num in range(1,101):
			
			# Open web page for writing
			current_square_html_file = self.HTML_PATHS + unicode(page_num) + '.html'
			outFile = open(current_square_html_file, 'w')

			# Load the content to go in this file
			self.PAL_20_Load_Square_Content(page_num)
			
			# Print the header
			self.PAL_20_Print_Header_Template(outFile)

			# Print the body
			self.PAL_20_Print_Body(page_num, outFile)

			# Print the title
			self.Utilities.PAL_90_Print_Title('Square ' + unicode(page_num), outFile)

			# Print closing tags
			self.Utilities.PAL_90_Print_Template(self.Closing_Tags_Data, outFile)

			outFile.close()

			# Reset variables
			self.Template_Data		= []
			self.Square_Data		= []
			self.Square_Info		= defaultdict(list)


	def __del__(self):
		pass


if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------
	Generate_Squares = PAL_20_Generate_Squares()
	Generate_Squares.PAL_20_Generate_Squares()
