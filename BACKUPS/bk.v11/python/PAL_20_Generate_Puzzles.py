#!/user/bin/env python

from collections import defaultdict
from PAL_10_Generate_GameBoard import PAL_10_Generate_GameBoard

import os
import random


class PAL_20_Generate_Puzzles(object):
	
	def __init__(self):

		self.PAL_10_Generate_GameBoard = PAL_10_Generate_GameBoard()
		
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
		self.Submit_Cases		= []

		self.Hint_Titles		= [ 'What gives?', 'Out of ideas?', 'Not your day?', \
									'Coder\'s block?', 'Puzzled?', 'Fate fell short this time?', \
									'Feeling blue?', 'Dazed and confused?', 'Battered and bruised?', \
									'Losing hope?', 'Under the weather?', 'Need a little help?']

		self.Numbers_to_Words	= { 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
									6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
									11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
									15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
									19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
									50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
									90: 'Ninety', 0: 'Zero', 100: 'One Hundred'}

		self.Python_Squares		= [4,8]
		self.Ladder_Squares		= [2,6,10]

		self.Keywords_Delimiter = '$%$%'

		self.Keywords_Formats	= { 'int': "<span class=keyword-teal>int</span>", \
									'str': "<span class=keyword-teal>str</span>", \
									'bool': "<span class=keyword-teal>bool</span>", \
									'list': "<span class=keyword-teal>list</span>", \
									'dict': "<span class=keyword-teal>dict</span>", \
									'escape': "<span class=keyword-purple>\\</span>", \
									'newline': "<span class=keyword-purple>\\n</span>", \
									'tab': "<span class=keyword-purple>\\t</span>", \
									'type': "<span class=keyword-green>type</span>", \
									'print': "<span class=keyword-orange>print</span>", \
									'is': "<span class=keyword-orange>is</span>", \
									'float': "<span class=keyword-teal>float</span>", \
									'in': "<span class=keyword-orange>in</span>", \
									'not': "<span class=keyword-orange>not</span>", \
									'if': "<span class=keyword-orange>if</span>", \
									'else': "<span class=keyword-orange>else</span>", \
									'elif': "<span class=keyword-orange>elif</span>", \
									'for': "<span class=keyword-orange>for</span>", \
									'range': "<span class=keyword-green>range</span>", \
									'#': "<span class=keyword-green>#</span>", \
									'True': "<span class=keyword-purple>True</span>", \
									'False': "<span class=keyword-purple>False</span>", \
									'len': "<span class=keyword-green>len</span>", \
									'append': "<span class=keyword-green>append</span>", \
									'extend': "<span class=keyword-green>extend</span>", \
									'return': "<span class=keyword-orange>return</span>", \
									'def': "<span class=keyword-orange>def</span>", \
									'max': "<span class=keyword-green>max</span>", \
									'min': "<span class=keyword-green>min</span>", \
									'capitalize': "<span class=keyword-green>capitalize</span>", \
									'upper': "<span class=keyword-green>upper</span>", \
									'lower': "<span class=keyword-green>lower</span>", \
									'reversed': "<span class=keyword-green>reversed</span>", \
									'pop': "<span class=keyword-green>pop</span>", \
									'rstrip': "<span class=keyword-green>rstrip</span>", \
									'choice': "<span class=keyword-green>choice</span>", \
									'import': "<span class=keyword-orange>import</span>", \
									'random': "<span class=keyword-purple>random</span>", \
									'split': "<span class=keyword-green>split</span>", \

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

		# Populate test cases for SUBMIT button
		for key in self.Puzzle_Info:
			if key == '$ALLPANES_SUBMITCASES$\n':
				self.Submit_Cases = self.Puzzle_Info[key]
		for case in self.Submit_Cases:
			self.Submit_Cases[self.Submit_Cases.index(case)] = case\
			.replace('PASSED!', '<span class=keyword-green>PASSED!</span>')\
			.replace('FAILED', '<span class=keyword-red>FAILED</span>')\
			.replace('\'', '\\\'')
		for case in self.Submit_Cases:
			self.Submit_Cases[self.Submit_Cases.index(case)] = '    ' + self.Submit_Cases[self.Submit_Cases.index(case)]

		# Process content to format colours of new/key terms
		for heading in self.Puzzle_Info:
			current_section = self.Puzzle_Info[heading]
			tempString = self.Keywords_Delimiter.join(self.Puzzle_Info[heading])
			tempString = tempString.replace('^int^', self.Keywords_Formats['int'])
			tempString = tempString.replace('^str^', self.Keywords_Formats['str'])
			tempString = tempString.replace('^float^', self.Keywords_Formats['float'])
			tempString = tempString.replace('^bool^', self.Keywords_Formats['bool'])
			tempString = tempString.replace('^list^', self.Keywords_Formats['list'])
			tempString = tempString.replace('^dict^', self.Keywords_Formats['dict'])

			tempString = tempString.replace('^print^', self.Keywords_Formats['print'])
			tempString = tempString.replace('^is^', self.Keywords_Formats['is'])
			tempString = tempString.replace('^in^', self.Keywords_Formats['in'])
			tempString = tempString.replace('^not^', self.Keywords_Formats['not'])
			tempString = tempString.replace('^if^', self.Keywords_Formats['if'])
			tempString = tempString.replace('^else^', self.Keywords_Formats['else'])
			tempString = tempString.replace('^elif^', self.Keywords_Formats['elif'])
			tempString = tempString.replace('^for^', self.Keywords_Formats['for'])
			tempString = tempString.replace('^return^', self.Keywords_Formats['return'])
			tempString = tempString.replace('^import^', self.Keywords_Formats['import'])

			tempString = tempString.replace('^\\n^', self.Keywords_Formats['newline'])
			tempString = tempString.replace('^\\t^', self.Keywords_Formats['tab'])
			tempString = tempString.replace('^\\^', self.Keywords_Formats['escape'])
			tempString = tempString.replace('^True^', self.Keywords_Formats['True'])
			tempString = tempString.replace('^False^', self.Keywords_Formats['False'])
			tempString = tempString.replace('^random^', self.Keywords_Formats['random'])

			tempString = tempString.replace('^type^', self.Keywords_Formats['type'])
			tempString = tempString.replace('^range^', self.Keywords_Formats['range'])
			tempString = tempString.replace('^append^', self.Keywords_Formats['append'])
			tempString = tempString.replace('^extend^', self.Keywords_Formats['extend'])
			tempString = tempString.replace('^#^', self.Keywords_Formats['#'])
			tempString = tempString.replace('^len^', self.Keywords_Formats['len'])
			tempString = tempString.replace('^max^', self.Keywords_Formats['max'])
			tempString = tempString.replace('^min^', self.Keywords_Formats['min'])
			tempString = tempString.replace('^capitalize^', self.Keywords_Formats['capitalize'])
			tempString = tempString.replace('^upper^', self.Keywords_Formats['upper'])
			tempString = tempString.replace('^lower^', self.Keywords_Formats['lower'])
			tempString = tempString.replace('^reversed^', self.Keywords_Formats['reversed'])
			tempString = tempString.replace('^pop^', self.Keywords_Formats['pop'])
			tempString = tempString.replace('^rstrip^', self.Keywords_Formats['rstrip'])
			tempString = tempString.replace('^choice^', self.Keywords_Formats['choice'])
			tempString = tempString.replace('^split^', self.Keywords_Formats['split'])

			tempString = tempString.replace('^def^', self.Keywords_Formats['def'])

			tempString = tempString.replace('--', '&#8212;')
			tempString = tempString.replace('<linespace>', '<p class="small">&nbsp;</p>')
			tempString = tempString.replace('<codespace>', '<p class="small">&nbsp;</p>')
			tempString = tempString.replace('<tab>', '&nbsp;&nbsp;&nbsp;&nbsp;')
			tempString = tempString.replace('<3sp>', '&nbsp;&nbsp;&nbsp;')
			tempString = tempString.replace('<2sp>', '&nbsp;&nbsp;')
			tempString = tempString.replace('<1sp>', '&nbsp;')

			tempString = tempString.replace('<outputcodeline>', '<table class="codeline"><tr><td class="output">')
			tempString = tempString.replace('</outputcodeline>', '</td></tr></table>')

			tempString = tempString.replace('<outputcodeblock>', '<table class="output"><tr><td>')
			tempString = tempString.replace('</outputcodeblock>', '</td></tr></table><p></p>')

			tempString = tempString.replace('<democodeline>', '<table class="codeline"><tr><td class="demo">')
			tempString = tempString.replace('</democodeline>', '</td></tr></table>')
			
			tempString = tempString.replace('<democodeblock>', '<table class="demo"><tr><td>')
			tempString = tempString.replace('</democodeblock>', '</td></tr></table><p></p>')

			tempString = tempString.replace('<cardcodeline>', '<table class="codeline"><tr><td class="card">')
			tempString = tempString.replace('</cardcodeline>', '</td></tr></table>')
			
			tempString = tempString.replace('<cardcodeblock>', '<table class="card"><tr><td>')
			tempString = tempString.replace('</cardcodeblock>', '</td></tr></table><p></p>')

			tempString = tempString.replace('<mathexp>', '<p class="mathexp">')
			tempString = tempString.replace('</mathexp>', '</p')

			tempString = tempString.replace('<mathexpblock>', '<table class="mathexp"><tr><td>')
			tempString = tempString.replace('</mathexpblock>', '</td></tr></table><p></p>')

			tempString = tempString.replace('<comment>', '<span class="keyword-green">')
			tempString = tempString.replace('</comment>', '</span>')

			tempString = tempString.replace('<def>', '<span class=\'keyword-pink\'>')
			tempString = tempString.replace('</def>', '</span>')

			tempString = tempString.replace('<var>', '<span class=\'keyword-var\'>')
			tempString = tempString.replace('</var>', '</span>')

			self.Puzzle_Info[heading] = tempString.split(self.Keywords_Delimiter)

		fileStream.close()


	def PAL_20_Print_Mini_Row(self, outFile):

		outFile.write('\n            <div>')

		end_puzzle = 0
		for id_num in range(1,6):
			id_num = unicode(id_num)

			start_puzzle 	= end_puzzle + 1
			end_puzzle 		= start_puzzle + 19

			puzzle_string	= unicode(start_puzzle) + ' to ' + unicode(end_puzzle)

			outFile.write('\n          <label class="minigameboard-row" for="_'+id_num+'">Puzzles '+puzzle_string+'</label>')
			outFile.write('\n          <input id="_'+id_num+'" type="checkbox">')
			outFile.write('\n          <div class="minigameboard-box-contain">')
			
			for square in range (int(start_puzzle), int(end_puzzle)+1):
				square = unicode(square)
				puzzle_link = 'puzzle_' + square + '.html'

				if puzzle_link in os.listdir(self.LOCAL_PAGES_DIR):
					if square == '1':
						outFile.write('\n          <a href="./main/puzzles/pages/puzzle_'+square+'.html"><div class="minigameboard-box-start" onclick="">'+'GO'+'</div></a>')
					else:
						outFile.write('\n          <a href="./main/puzzles/pages/puzzle_'+square+'.html"><div class="minigameboard-box" onclick="">'+square+'</div></a>')
				else: 
					outFile.write('\n          <a href="../../../pagenotfound.html"><div class="minigameboard-box" onclick="">'+square+'</div></a>')

			outFile.write('\n          </div><!-- minigameboard-box-contain -->')
		outFile.write('\n            </div><!-- anonymous div -->')


	def PAL_20_Print_Title(self, puzzle_num, outFile):
		outFile.write('\n    <title>Puzzle '+unicode(puzzle_num)+' | Pythons and Ladders</title>\n')
		outFile.write('\n')


	def PAL_20_Print_Body(self, puzzle_num, outFile):

		#-----------------
		# Print the banner
		#-----------------
		outFile.write('\n        <!-- BANNER -->')
		outFile.write('\n        <div class="bannerpane">')
		outFile.write('\n          <div class="banneritems">')

		previous_puzzle = 'puzzle_'+unicode(puzzle_num-1)+'.html'
		next_puzzle 	= 'puzzle_'+unicode(puzzle_num+1)+'.html'

		if previous_puzzle not in os.listdir(self.LOCAL_PAGES_DIR):
			if previous_puzzle == 'puzzle_0.html':
				previous_puzzle = '../../../index.html'
			else:
				previous_puzzle = '../../../pagenotfound.html'

		if next_puzzle not in os.listdir(self.LOCAL_PAGES_DIR):
			if next_puzzle == 'puzzle_101.html':
				next_puzzle = '../../../index.html'
			else:
				next_puzzle = '../../../pagenotfound.html'

		outFile.write('\n      <div class="puzzlenav2">')
		outFile.write('\n        <a href="puzzle_'+unicode(puzzle_num)+'.html"><div class="box-puzz2"><div class="box-puzzle-number2" onclick="">'+unicode(puzzle_num)+'</div></div></a>')
		if unicode(puzzle_num) != '1':
			outFile.write('\n        <a href="'+previous_puzzle+'"><div class="box-puzz2"><div class="box-puzzle-arrows2" onclick="">&lang;</div></div></a>')
		if unicode(puzzle_num) != '100':
			outFile.write('\n        <a href="'+next_puzzle+'"><div class="box-puzz2"><div class="box-puzzle-arrows2" onclick="">&rang;</div></div></a>')
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
		if self.Puzzle_Info['$LEFTPANEL_HEADING$\n'] != []:
			songtitle = self.Puzzle_Info['$LEFTPANEL_HEADING$\n'][0].strip()
			songlink  = self.Puzzle_Info['$LEFTPANEL_HEADING$\n'][1].strip()
			outFile.write('\n        <a class="songheading" target="_blank" href="'+songlink+'"">')
			outFile.write('\n        <h3>'+songtitle+'</h3>')
			outFile.write('\n        </a>')

		# Print instructions
		for sentence in self.Puzzle_Info['$LEFTPANEL_INSTRUCTIONS$\n']:
			if '<code>' in sentence:
				outFile.write('\n        <p class="small">'+sentence.strip('\n')+'</p>')
			else:
				outFile.write('\n        <p>'+sentence.strip('\n')+'</p>')
		
		# Print question
		alphanum = self.PAL_20_Spell_Number(puzzle_num)
		outFile.write('\n          <h4 class="h4gold">Task '+alphanum+'</h4>')
		for sentence in self.Puzzle_Info['$LEFTPANEL_QUESTION$\n']:
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
		for sentence in self.Puzzle_Info['$LEFTPANEL_HINTS$\n']:
			hintcontent += '<p>' + sentence + '</p>'
		outFile.write('\n                <a href="#" style="border-bottom:0px" class="bootstrap-popover" title="'+random.choice(self.Hint_Titles).lower()+'" data-content="'+hintcontent+'">')
		outFile.write('\n                HINT')
		outFile.write('\n                </a>')
		outFile.write('\n              </div><!-- editortoolbaritems -->')
		if int(puzzle_num) > 42 and int(puzzle_num) not in [65,66,67,70,75,76,89,96,97,98]:
			outFile.write('\n                <div class="editortoolbaritems-submit" onclick="testit()">SUBMIT</div>')
		outFile.write('\n            </div><!-- editortoolbar -->')

		# Print editor content
		outFile.write('\n          <form> ')
		number_of_editor_rows		 = unicode(len(self.Puzzle_Info['$LEFTPANEL_EDITOR$\n'])+4)
		
		if int(number_of_editor_rows) <= 4:
			outFile.write('\n            <textarea id="textbox" name="textbox" rows="'+number_of_editor_rows+'">')
		else:
			outFile.write('\n            <textarea id="textbox" name="textbox" rows="'+number_of_editor_rows+'">')

			aggregated_sentence = ''
			for sentence in self.Puzzle_Info['$LEFTPANEL_EDITOR$\n']:
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
		if self.Puzzle_Info['$RIGHTPANEL_QUESTIONS$\n'] == ['']:
			pass
		elif len(self.Puzzle_Info['$RIGHTPANEL_QUESTIONS$\n']) not in [0]:
			outFile.write('\n          <h4 class="h4gold">Questions for You</h4>')
			for question in self.Puzzle_Info['$RIGHTPANEL_QUESTIONS$\n']:
				if '<code> or <cardcode' in question:
					outFile.write('\n              '+question.strip('\n'))
				else:
					outFile.write('\n              <p>'+question.strip('\n')+'</p>')

		# Print notes
		if self.Puzzle_Info['$RIGHTPANEL_TESTCASES$\n'] == ['']:
			pass
		elif len(self.Puzzle_Info['$RIGHTPANEL_TESTCASES$\n']) not in [0]:
			outFile.write('\n          <h4 class="h4gold">Notes</h4>')
			for testcase in self.Puzzle_Info['$RIGHTPANEL_TESTCASES$\n']:
				if '<code> or <cardcode' in testcase:
					outFile.write('\n              '+testcase.strip('\n'))
				else:
					outFile.write('\n              <p>'+testcase.strip('\n')+'</p>')
		
		outFile.write('\n       </div><!-- questions-small-devices -->')
		outFile.write('\n')

		# NAVIGATION BUTTONS
		outFile.write('\n        <a style="border-bottom:0px" href="'+previous_puzzle+'">')
		if puzzle_num != 1:
			outFile.write('\n          <button>&lang; PREVIOUS</button>')
		outFile.write('\n        </a>')
		outFile.write('\n        <a style="border-bottom:0px" href="'+next_puzzle+'">')
		if unicode(puzzle_num) == '100':
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
		if self.Puzzle_Info['$RIGHTPANEL_QUESTIONS$\n'] == ['']:
			pass
		else:
			outFile.write('\n        <div class="infocard">')
			outFile.write('\n          <h4 class="greyheading">Questions for You</h4>')
			for question in self.Puzzle_Info['$RIGHTPANEL_QUESTIONS$\n']:
				if '<code> or <cardcode' in question:
					outFile.write('\n              '+question.strip('\n'))
				else:
					outFile.write('\n              <p>'+question.strip('\n')+'</p>')
			outFile.write('\n        </div><!-- infocard -->')
		outFile.write('\n          </div><!-- rightpane -->')

		# Print notes
		outFile.write('\n         	<div class="rightpane">')
		if self.Puzzle_Info['$RIGHTPANEL_TESTCASES$\n'] == ['']:
			pass
		else:
			outFile.write('\n         <div class="infocard">')
			outFile.write('\n          <h4 class="greyheading">NOTES</h4>')
			for testcase in self.Puzzle_Info['$RIGHTPANEL_TESTCASES$\n']:
				if '<code> or <cardcode' in testcase:
					outFile.write('\n              '+testcase.strip('\n'))
				else:
					outFile.write('\n              <p>'+testcase.strip('\n')+'</p>')
			outFile.write('\n        </div><!-- infocard -->')
		outFile.write('\n          </div><!-- rightpane -->')


		outFile.write('\n        </div><!-- questions-large-devices -->')
		outFile.write('\n')
		outFile.write('\n      </div><!-- allpanes_new -->')



	def PAL_20_Generate_Puzzles(self):
		
		# Load the header
		self.PAL_20_Load_Header_Template()
		
		# Load the navigation
		# self.PAL_20_Load_Navigation_Template()

		# Load the closing tags
		self.PAL_20_Load_Closing_Tags_Template()

		for page_num in range(1,101):
			
			# Open web page for writing
			current_puzzle_html_file = self.HTML_PATHS + unicode(page_num) + '.html'
			outFile = open(current_puzzle_html_file, 'w')

			# Load the content to go in this file
			self.PAL_20_Load_Puzzle_Content(page_num)
			
			# Print the header
			self.PAL_20_Print_Header_Template(outFile)
			
			# Print the navigation
			# self.PAL_20_Print_Navigation_Template(outFile)

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
