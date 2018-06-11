#!/user/bin/env python

from collections import defaultdict

import os


class PAL_20_Generate_Puzzles(object):
	
	def __init__(self):
		
		self.ROOT_DIR 			= os.path.dirname(os.getcwd())
		self.BACKUPS_DIR		= os.path.join(self.ROOT_DIR, 'backups')
		self.CONTENTS_DIR 		= os.path.join(self.ROOT_DIR, 'content')
		self.CSS_DIR			= os.path.join(self.ROOT_DIR, 'css')
		self.IMAGES_DIR			= os.path.join(self.ROOT_DIR, 'images')
		self.JAVASCRIPT_DIR		= os.path.join(self.ROOT_DIR, 'js')
		self.PYTHON_DIR			= os.getcwd()

		self.TEMPLATE_PATH		= os.path.join(self.CONTENTS_DIR, 'emptytemplate.html')
		self.CONTENT_PATHS		= os.path.join(self.CONTENTS_DIR, 'content_puzzle_')
		self.HTML_PATHS			= os.path.join(self.ROOT_DIR, 'puzzle_')

		self.Template_Data		= []
		self.Puzzle_Data		= []
		self.Puzzle_Info		= defaultdict(list)


	def PAL_20_Load_Template(self):

		if not os.path.isfile(self.TEMPLATE_PATH):
			print "ERROR: EMPTY TEMPLATE FILE NOT FOUND"

		fileStream = open(self.TEMPLATE_PATH, 'r')
		allLines = fileStream.readlines()

		for line in allLines[0:]:
			line_list = line
			if line_list != ['']:
				self.Template_Data.append(line_list)

		fileStream.close()


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

		fileStream.close()


	def PAL_20_Print_Template(self, outFile):

		for template_line in self.Template_Data:
			outFile.write(template_line)


	def PAL_20_Print_Title(self, puzzle_num, outFile):
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--       TITLE      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <title>Puzzle '+unicode(puzzle_num)+'</title')
		outFile.write('\n    <div align="center">')


	def PAL_20_Print_Header(self, puzzle_num, outFile):
		previous_puzzle = 'puzzle_'+unicode(puzzle_num-1)+'.html'
		next_puzzle 	= 'puzzle_'+unicode(puzzle_num+1)+'.html'

		if previous_puzzle == 'puzzle_0.html':
			previous_puzzle = 'index.html'
		if next_puzzle == 'puzzle_101.html':
			next_puzzle = 'index.html'

		if previous_puzzle not in os.listdir(self.ROOT_DIR):
			previous_puzzle = 'pagenotfound.html'
		if next_puzzle not in os.listdir(self.ROOT_DIR):
			next_puzzle = 'pagenotfound.html'

		outFile.write('\n')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--      HEADER      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n      <br><br>')
		outFile.write('\n      <table align="center" style="width:1200px" cellspacing="0px" border="0">')
		outFile.write('\n        <tr>')
		outFile.write('\n          <!-- LEFT: EMPTY PADDING COLUMN -->')
		outFile.write('\n          <td valign="top" width="20px">')
		outFile.write('\n          </td>')
		outFile.write('\n          <!-- CURRENT PAGE IMAGE -->')
		outFile.write('\n          <td valign="top" width="90px">')
		outFile.write('\n            <a href="puzzle_'+unicode(puzzle_num)+'.html">')
		outFile.write('\n              <img src="./images/'+unicode(puzzle_num)+'.png" alt="INIT">')
		outFile.write('\n            </a>')
		outFile.write('\n          </td>')
		outFile.write('\n          <!-- NAVIGATION IMAGES -->')
		outFile.write('\n          <td valign="top" width="50px">')
		outFile.write('\n            <a href="'+previous_puzzle+'">')
		outFile.write('\n              <img align="top" src="./images/back.png" alt="2" style="width:90%;height:48%">')
		outFile.write('\n            </a>')
		outFile.write('\n            <a href="'+next_puzzle+'">')
		outFile.write('\n              <img align="top" src="./images/next.png" alt="3" style="width:90%;height:48%">')
		outFile.write('\n            </a>')
		outFile.write('\n          </td>')
		outFile.write('\n          <!-- RIGHT: EMPTY PADDING COLUMN -->')
		outFile.write('\n          <td valign="bottom">')
		#outFile.write('\n            <a href="#">')
		#outFile.write('\n              <img align="right" src="./images/feedback.png" alt="3" style="width:10%;height:48%">')
		#outFile.write('\n            </a>')
		outFile.write('\n          </td>')
		outFile.write('\n        </tr>')
		outFile.write('\n      </table>')
		outFile.write('\n      <!-- LINE BREAK -->')
		outFile.write('\n      <br>')
		outFile.write('\n      <hr>')


	def PAL_20_Print_Body(self, puzzle_num, outFile):
		outFile.write('\n')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--        BODY      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n      <table align="center" style="width:1200px" cellspacing="20px" border="0">')
		outFile.write('\n        <tr>')
		
		# Print the left panel
		outFile.write('\n        <!-- LEFT: QUESTION AND EDITOR -->')
		outFile.write('\n          <td align="left" valign="top" width="600px">')
		outFile.write('\n            <h3>SQ. '+unicode(puzzle_num)+'</h3>')

		for sentence in self.Puzzle_Info['$LEFTPANEL_INSTRUCTIONS$\n']:
			if sentence == '\n':
				outFile.write('\n            <p class="small">&nbsp;</p>')
			else:
				outFile.write('\n            <p class="small">'+sentence.strip('\n')+'</p>')

		outFile.write('\n            <p class="small">&nbsp;</p>')
		outFile.write('\n            <form align="left"> ')
		number_of_editor_rows		 = unicode(len(self.Puzzle_Info['$LEFTPANEL_EDITOR$\n'])+4)
		outFile.write('\n            <textarea id="yourcode" cols="80" rows="'+number_of_editor_rows+'">')
		outFile.write('\n')

		for sentence in self.Puzzle_Info['$LEFTPANEL_EDITOR$\n']:
			outFile.write(sentence)

		outFile.write('\n            </textarea>')
		outFile.write('\n            <br>')
		outFile.write('\n            <br>')
		outFile.write('\n            <button type="button" onclick="runit()">Run</button>')
		outFile.write('\n            <button type="button" onclick="sendEmail()">Feedback</button>')
		outFile.write('\n            </form>')
		outFile.write('\n          </td>')

		# Print the right panel
		outFile.write('\n        <!-- RIGHT: TIMES, QUESTIONS, AND SPONSORED -->')
		outFile.write('\n          <td align="left"  valign="top">')
		
		outFile.write('\n          <h3>Approximate learning time</h3>')
		outFile.write('\n          <p>'+self.Puzzle_Info['$RIGHTPANEL_TIME$\n'][0].strip('\n')+'</p>')
		outFile.write('\n          <button type="button" onclick="requestSolution()">Request solution</button>')

		outFile.write('\n          <h3><br>Questions for you</h3>')
		outFile.write('\n          <ol>')
		for question in self.Puzzle_Info['$RIGHTPANEL_QUESTIONS$\n']:
			outFile.write('\n            <li>'+question.strip('\n')+'</li><br>')
		outFile.write('\n          </ol>')

		outFile.write('\n          <h3>Sponsored</h3>')
		outFile.write('\n          <ol>')
		for reading in self.Puzzle_Info['$RIGHTPANEL_SPONSORED$\n']:
			reading = reading.strip('\n').split(' $LINK$ ')
			outFile.write('\n            <a href="'+reading[1]+'" target="_blank"><li>'+reading[0].strip('\n')+'</li></a>')
		outFile.write('\n          </ol>')
		outFile.write('\n          </td>')

		outFile.write('\n        </tr>')
		outFile.write('\n      </table>')


	def PAL_20_Print_Console(self, outFile):
		
		outFile.write('\n')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--     CONSOLE      -->')
		outFile.write('\n    <!-- **************** -->')
 		outFile.write('\n     <table align="center" style="width:1200px;" cellspacing="20px" border="0s">')
		outFile.write('\n      <tr>')
		outFile.write('\n      <td>')
		outFile.write('\n      <pre align="left" id="output"></pre>')
		outFile.write('\n      </td>')
		outFile.write('\n      </tr>')
		outFile.write('\n      </table>')


	def PAL_20_Print_Closing_Tags(self, outFile):
		outFile.write('\n    </div>')
		outFile.write('\n  </body>')
		outFile.write('\n  <footer align="center"><br>Copyright &copy; Shamil Pokharel 2016</footer>')
		outFile.write('\n</html>')


	def PAL_20_Print_HTML_WebPage(self, puzzle_num):
		
		# Open web page for writing
		current_puzzle_html_file = self.HTML_PATHS + unicode(puzzle_num) + '.html'
		outFile = open(current_puzzle_html_file, 'w')

		# Print the template
		self.PAL_20_Print_Template(outFile)

		# Print the title
		self.PAL_20_Print_Title(puzzle_num, outFile)

		# Print the header
		self.PAL_20_Print_Header(puzzle_num, outFile)

		# Print the body
		self.PAL_20_Print_Body(puzzle_num, outFile)

		# Print the console
		self.PAL_20_Print_Console(outFile)

		# Print closing tags
		self.PAL_20_Print_Closing_Tags(outFile)

		outFile.close()


	def PAL_20_Generate_Puzzles(self):
		
		for page_num in range(1,10):
			self.PAL_20_Load_Template()
			self.PAL_20_Load_Puzzle_Content(page_num)
			self.PAL_20_Print_HTML_WebPage(page_num)

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
