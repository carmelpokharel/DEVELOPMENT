#!/user/bin/env python

from collections import defaultdict
from datetime import datetime

import os


class PAL_10_Generate_GameBoard(object):
	
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

		self.PUZZLE_PAGES_DIR	= os.path.join(self.PUZZLES_DIR, 'pages')
		self.TUTORIAL_PAGES_DIR	= os.path.join(self.TEMPLATES_DIR, 'pages')
		self.UPDATES_PAGES_DIR	= os.path.join(self.UPDATES_DIR, 'pages')
		self.UPDATES_DATA_DIR 	= os.path.join(self.UPDATES_DIR, 'data')

		self.HEADER_PATH		= os.path.join(self.TEMPLATES_DIR, 'template_header.html')
		self.NAVIGATION_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_navigation.html')
		self.CLOSING_TAGS_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_closingtags.html')

		self.GAMEBOARD_PATH		= os.path.join(self.CONTENTS_DIR, 'content_gameboard.txt')
		self.UPDATES_DATA_PATH	= os.path.join(self.UPDATES_DATA_DIR, 'content_updates.txt')
		self.HTML_PATH			= os.path.join(self.ROOT_DIR, 'index.html')

		self.current_date_key	= ''

		self.Header_Data		= []
		self.Navigation_Data	= []
		self.Closing_Tags_Data	= []
		self.Updates_Info		= defaultdict(list)
		self.Updates_Dates		= defaultdict()
		self.GameBoard_Info		= defaultdict(list)
		self.Build_No			= defaultdict()

		self.Number_of_Update_Lines = 12


	def PAL_10_Load_and_Print_Header_Template(self, outFile):

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


	def PAL_10_Load_and_Print_Navigation_Template(self, outFile):

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


	def PAL_10_Load_and_Print_Closing_Tags_Template(self, outFile):

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


	def PAL_10_Load_GameBoard_Content(self):
		
		current_content_file = self.GAMEBOARD_PATH

		fileStream = open(current_content_file, 'r')
		allLines = fileStream.readlines()

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
			self.GameBoard_Info[section[0]] = section[1:]

		fileStream.close()


	def PAL_10_Load_Updates_Content(self):
		
		current_content_file = self.UPDATES_DATA_PATH

		fileStream = open(current_content_file, 'r')
		allLines = fileStream.readlines()

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


	def PAL_10_Determine_Build_Number(self):
		for update in self.Updates_Info['$LEFTPANEL_RECENTUPDATES$\n']:
			update = update.strip('\n')
			try: update = datetime.strptime(update, '%Y-%m-%d')
			except: pass
			if isinstance(update, datetime):
				self.current_date_key = update
				self.Build_No[self.current_date_key] = []
			else:
				self.Build_No[self.current_date_key].append(update)
		return unicode(len(self.Build_No)-25)


	def PAL_10_Print_Title(self, outFile):
		outFile.write('\n    <title>Welcome! | Pythons and Ladders</title>')
		outFile.write('\n')


	def PAL_10_Print_Mini_Row(self, outFile):

		outFile.write('\n            <div>')

		end_puzzle = 0
		for id_num in range(1,6):
			id_num = unicode(id_num)

			start_puzzle 	= end_puzzle + 1
			end_puzzle 		= start_puzzle + 19

			puzzle_string	= unicode(start_puzzle) + ' to ' + unicode(end_puzzle)

			outFile.write('\n          <label class="minigameboard-home-row" for="_'+id_num+'">Puzzles '+puzzle_string+'</label>')
			outFile.write('\n          <input id="_'+id_num+'" type="checkbox">')
			outFile.write('\n          <div class="minigameboard-home-box-contain">')
			
			for square in range (int(start_puzzle), int(end_puzzle)+1):
				square = unicode(square)
				puzzle_link = 'puzzle_' + square + '.html'
				if puzzle_link in os.listdir(self.PUZZLE_PAGES_DIR):
					if square == '1':
						outFile.write('\n          <a href="./main/puzzles/pages/puzzle_'+square+'.html"><div class="minigameboard-home-box-start" onclick="">'+'GO'+'</div></a>')
					else:
						outFile.write('\n          <a href="./main/puzzles/pages/puzzle_'+square+'.html"><div class="minigameboard-home-box" onclick="">'+square+'</div></a>')
				else:
						outFile.write('\n          <a href="./pagenotfound.html"><div class="minigameboard-home-box" onclick="">'+square+'</div></a>')

			outFile.write('\n          </div><!-- minigameboard-home-box-contain -->')

		outFile.write('\n            </div><!-- anonymous div -->')


	def PAL_10_Print_Backward_Row(self, start, end, outFile):
		
		outFile.write('\n            <div>')
		boxnum = 3
		for square in reversed(range(start, end+1)):
			if boxnum == 0:
				boxnum = 3
			if square == 100:
				square = '100'
			puzzle_link = 'puzzle_' + unicode(square) + '.html'
			
			if puzzle_link in os.listdir(self.PUZZLE_PAGES_DIR):
				if square == '100':
					outFile.write('\n              <a href="./main/puzzles/pages/'+puzzle_link+'" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home" onclick="">'+unicode(square)+'</div></div></a>')
				else:
					outFile.write('\n              <a href="./main/puzzles/pages/'+puzzle_link+'" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home" onclick="">'+unicode(square)+'</div></div></a>')
			else:
				if square == '100':
					outFile.write('\n              <a href="pagenotfound.html" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home" onclick="">'+unicode(square)+'</div></div></a>')
				else:
					outFile.write('\n              <a href="pagenotfound.html" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home" onclick="">'+unicode(square)+'</div></div></a>')
			
			boxnum -=1
		outFile.write('\n            </div><!-- anonymous div -->')


	def PAL_10_Print_Forward_Row(self, start, end, outFile):

		outFile.write('\n            <div>')
		boxnum = 2
		for square in range(start, end+1):
			
			if boxnum == 2: curr_boxnum = 1
			if boxnum == 1: curr_boxnum = 3
			if boxnum == 3: curr_boxnum = 2

			if square == 1:
				puzzle_link = 'puzzle_' + '1' + '.html'
				square_print = 'GO'
			else:
				puzzle_link = 'puzzle_' + unicode(square) + '.html'
				square_print = unicode(square)

			if puzzle_link in os.listdir(self.PUZZLE_PAGES_DIR):
				if square_print=='GO':
					outFile.write('\n              <a href="./main/puzzles/pages/'+puzzle_link+'" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home-start" onclick="">'+unicode(square_print)+'</div></div></a>')
				else:
					outFile.write('\n              <a href="./main/puzzles/pages/'+puzzle_link+'" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home" onclick="">'+unicode(square_print)+'</div></div></a>')
			else: 
				outFile.write('\n              <a href="pagenotfound.html" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home" onclick="">'+unicode(square_print)+'</div></div></a>')

			if curr_boxnum == 1: boxnum = 1
			if curr_boxnum == 3: boxnum = 3
			if curr_boxnum == 2: boxnum = 2

		outFile.write('\n            </div><!-- anonymous div -->')


	def PAL_10_Print_Body(self, outFile):

		#-----------------
		# Print the banner
		#-----------------
		outFile.write('\n        <!-- BANNER -->')
		outFile.write('\n        <div class="bannerpane-home">')
		outFile.write('\n          <div class="banneritems-home">')
		outFile.write('\n            <h2 class="bannertitle-home">w e l c o m e</h2>')

		for sentence in self.GameBoard_Info['$LEFTPANEL_WELCOME$\n']:
			outFile.write('\n            <p class="bannertext-home">'+sentence.strip('\n')+'</p>')

		outFile.write('\n            <!-- Boxes: Take the tutorial and Learn more -->')
		outFile.write('\n            <a href="./main/tutorials/pages/tutorial_1.html">')
		outFile.write('\n              <button class="red" onclick="">Take the tutorial &rang;</button>')
		outFile.write('\n            </a>')

		outFile.write('\n            <a href="overview.html">')
		outFile.write('\n              <button class="clear" onclick="">Learn more</button>')
		outFile.write('\n            </a>')

		outFile.write('\n          </div><!-- banneritems-home -->')
		outFile.write('\n        </div><!-- bannerpane-home -->')

		#--------------------
		# Print the left pane
		#--------------------
		outFile.write('\n')
		outFile.write('\n        <!-- LEFT PANE -->')
		outFile.write('\n        <div class="leftpane-home">')
		outFile.write('\n          <div class="gameboard">')
		# Squares
		self.PAL_10_Print_Forward_Row (1,  10,  outFile)
		self.PAL_10_Print_Backward_Row(11, 20,  outFile)
		self.PAL_10_Print_Forward_Row (21, 30,  outFile)
		self.PAL_10_Print_Backward_Row(31, 40,  outFile)
		self.PAL_10_Print_Forward_Row (41, 50,  outFile)
		self.PAL_10_Print_Backward_Row(51, 60,  outFile)
		self.PAL_10_Print_Forward_Row (61, 70,  outFile)
		self.PAL_10_Print_Backward_Row(71, 80,  outFile)
		self.PAL_10_Print_Forward_Row (81, 90,  outFile)
		self.PAL_10_Print_Backward_Row(91, 100, outFile)
		outFile.write('\n          </div><!-- gameboard -->')

		# Mini-squares
		outFile.write('\n          <div class="minigameboard-home">')
		self.PAL_10_Print_Mini_Row (outFile)
		outFile.write('\n          </div><!-- minigameboard-home -->')

		outFile.write('\n        </div><!-- leftpane-home -->')

		#---------------------
		# Print the right pane
		#---------------------
		outFile.write('\n')
		outFile.write('\n        <!-- RIGHT PANE -->')
		outFile.write('\n        <div class="rightpane-home">')
		outFile.write('\n          <div class="infocard-home">')


		outFile.write('\n            <h4 class="greyheading">VERSION</h4>')
		for sentence in self.Updates_Info['$VERSION$\n']:
			Build_No = self.PAL_10_Determine_Build_Number() + ' (BETA)'
			outFile.write('\n            <p>'+sentence.strip('\n')+Build_No+'</p>')
		outFile.write('\n            <hr>')

		# Print recent updates
		line_number = 0
		for update in self.Updates_Info['$LEFTPANEL_RECENTUPDATES$\n']:
			if line_number < self.Number_of_Update_Lines:
				line_number += 1
				update = update.strip('\n')
				try: update = datetime.strptime(update, '%Y-%m-%d')
				except: pass
				if isinstance(update, datetime):
					self.current_date_key = update
					self.Updates_Dates[self.current_date_key] = []
				else:
					self.Updates_Dates[self.current_date_key].append(update)
		outFile.write('\n            <h4 class="greyheading">RECENT UPDATES</h4>')
		for date in reversed(sorted(self.Updates_Dates)):
			outFile.write('\n            <h4 class="h4goldsmall">'+date.strftime('%B %d, %Y')+'</h4>')
			outFile.write('\n            <ul>')
			for update in self.Updates_Dates[date]:
				outFile.write('\n              <li class="small">'+update+'</li>')
			outFile.write('\n            </ul>')
		outFile.write('\n          </div><!-- infocard-home -->')
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



	def PAL_10_Generate_GameBoard(self):
		
		# Open web page for writing
		GameBoard = self.HTML_PATH
		outFile = open(GameBoard, 'w')

		# Load the content to go in this file
		self.PAL_10_Load_GameBoard_Content()

		# Load the updates section
		self.PAL_10_Load_Updates_Content()

		# Load and print the header
		self.PAL_10_Load_and_Print_Header_Template(outFile)

		# Load and print the navigation
		# self.PAL_10_Load_and_Print_Navigation_Template(outFile)

		# Print the body
		self.PAL_10_Print_Body(outFile)

		# Print the title
		self.PAL_10_Print_Title(outFile)

		# Print closing tags
		self.PAL_10_Load_and_Print_Closing_Tags_Template(outFile)

		outFile.close()


	def __del__(self):
		pass



if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------

	Generate_GameBoard = PAL_10_Generate_GameBoard()
	Generate_GameBoard.PAL_10_Generate_GameBoard()
