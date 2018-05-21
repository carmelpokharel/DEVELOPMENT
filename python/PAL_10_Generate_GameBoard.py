#!/user/bin/env python

from collections import defaultdict
from datetime import datetime
from PAL_90_Utilities import *

import os


class PAL_10_Generate_GameBoard(object):
	
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

		self.SQUARE_DATA_DIR 	= os.path.join(self.SQUARES_DIR, 'data')
		self.SQUARE_PAGES_DIR	= os.path.join(self.SQUARES_DIR, 'pages')
		self.TUTORIAL_PAGES_DIR	= os.path.join(self.TEMPLATES_DIR, 'pages')
		self.UPDATES_PAGES_DIR	= os.path.join(self.UPDATES_DIR, 'pages')
		self.UPDATES_DATA_DIR 	= os.path.join(self.UPDATES_DIR, 'data')

		self.HEADER_PATH		= os.path.join(self.TEMPLATES_DIR, 'template_header.html')
		self.CLOSING_TAGS_PATH	= os.path.join(self.TEMPLATES_DIR, 'template_closingtags.html')

		self.GAMEBOARD_PATH		= os.path.join(self.CONTENTS_DIR, 'content_gameboard')
		self.UPDATES_DATA_PATH	= os.path.join(self.UPDATES_DATA_DIR, 'content_updates')
		self.HTML_PATH			= os.path.join(self.ROOT_DIR, 'index.html')

		self.current_date_key	= ''

		self.Header_Data		= []
		self.Navigation_Data	= []
		self.Closing_Tags_Data	= []
		self.Updates_Info		= defaultdict(list)
		self.Updates_Dates		= defaultdict()
		self.GameBoard_Info		= defaultdict(list)
		self.Build_No			= defaultdict()

		self.list_of_easy_squares 	= defaultdict()
		self.list_of_hard_squares 	= defaultdict()

		self.Number_of_Update_Lines = 12


	# def PAL_10_Determine_Build_Number(self):
	# 	for update in self.Updates_Info['$LEFTPANEL_RECENTUPDATES$\n']:
	# 		update = update.strip('\n')
	# 		try: update = datetime.strptime(update, '%Y-%m-%d')
	# 		except: pass
	# 		if isinstance(update, datetime):
	# 			self.current_date_key = update
	# 			self.Build_No[self.current_date_key] = []
	# 		else:
	# 			self.Build_No[self.current_date_key].append(update)
	# 	return unicode(len(self.Build_No)-25-1)


	def PAL_10_Print_Mini_Row(self, outFile):

		outFile.write('\n            <div>')

		end_square = 0
		for id_num in range(1,6):
			id_num = unicode(id_num)

			start_square 	= end_square + 1
			end_square 		= start_square + 19

			square_string	= unicode(start_square) + ' to ' + unicode(end_square)

			outFile.write('\n          <label class="minigameboard-home-row" for="_'+id_num+'">Squares '+square_string+'</label>')
			outFile.write('\n          <input id="_'+id_num+'" type="checkbox">')
			outFile.write('\n          <div class="minigameboard-home-box-contain">')
			
			for square in range (int(start_square), int(end_square)+1):
				square = unicode(square)
				square_link = 'square_' + square + '.html'
				if square_link in os.listdir(self.SQUARE_PAGES_DIR):
					if square == '1':
						outFile.write('\n          <a href="./main/squares/pages/square_'+square+'.html"><div class="minigameboard-home-box-start" onclick="">'+'GO'+'</div></a>')
					else:
						if int(square) in self.list_of_easy_squares:
							outFile.write('\n          <a href="./main/squares/pages/square_'+square+'.html"><div class="minigameboard-home-box-easy" onclick="">'+square+'</div></a>')
						elif int(square) in self.list_of_hard_squares:
							outFile.write('\n          <a href="./main/squares/pages/square_'+square+'.html"><div class="minigameboard-home-box-hard" onclick="">'+square+'</div></a>')
						else:
							outFile.write('\n          <a href="./main/squares/pages/square_'+square+'.html"><div class="minigameboard-home-box" onclick="">'+square+'</div></a>')
				else:
						outFile.write('\n          <a href="./pagenotfound.html"><div class="minigameboard-home-box" onclick="">'+square+'</div></a>')

			outFile.write('\n          </div><!-- minigameboard-home-box-contain -->')

		outFile.write('\n            </div><!-- anonymous div -->')


	def PAL_10_Print_Forward_Row(self, start, end, outFile):

		for square in range(start, end+1):
			if 'content_square_' + unicode(square) + '_easy.txt' in os.listdir(self.SQUARE_DATA_DIR):
				self.list_of_easy_squares[square] = None
			elif 'content_square_' + unicode(square) + '_hard.txt' in os.listdir(self.SQUARE_DATA_DIR):
				self.list_of_hard_squares[square] = None

		outFile.write('\n            <div>')
		boxnum = 2
		for square in range(start, end+1):
			
			if boxnum == 2: curr_boxnum = 1
			if boxnum == 1: curr_boxnum = 3
			if boxnum == 3: curr_boxnum = 2

			if square == 1:
				square_link = 'square_' + '1' + '.html'
				square_print = 'GO'
			else:
				square_link = 'square_' + unicode(square) + '.html'
				square_print = unicode(square)

			if square_link in os.listdir(self.SQUARE_PAGES_DIR):
				if square_print=='GO':
					outFile.write('\n              <a href="./main/squares/pages/'+square_link+'" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home-start" onclick="">'+unicode(square_print)+'</div></div></a>')
				else:
					if square in self.list_of_easy_squares:
						outFile.write('\n              <a href="./main/squares/pages/'+square_link+'" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home-easy" onclick="">'+unicode(square_print)+'</div></div></a>')
					elif square in self.list_of_hard_squares:
						outFile.write('\n              <a href="./main/squares/pages/'+square_link+'" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home-hard" onclick="">'+unicode(square_print)+'</div></div></a>')
					else:
						outFile.write('\n              <a href="./main/squares/pages/'+square_link+'" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home" onclick="">'+unicode(square_print)+'</div></div></a>')
			else: 
				outFile.write('\n              <a href="pagenotfound.html" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home" onclick="">'+unicode(square_print)+'</div></div></a>')

			if curr_boxnum == 1: boxnum = 1
			if curr_boxnum == 3: boxnum = 3
			if curr_boxnum == 2: boxnum = 2

		outFile.write('\n            </div><!-- anonymous div -->')


	def PAL_10_Print_Backward_Row(self, start, end, outFile):

		for square in range(start, end+1):
			if 'content_square_' + unicode(square) + '_easy.txt' in os.listdir(self.SQUARE_DATA_DIR):
				self.list_of_easy_squares[square] = None
			elif 'content_square_' + unicode(square) + '_hard.txt' in os.listdir(self.SQUARE_DATA_DIR):
				self.list_of_hard_squares[square] = None
		
		outFile.write('\n            <div>')
		boxnum = 3
		for square in reversed(range(start, end+1)):
			if boxnum == 0:
				boxnum = 3
			if square == 100:
				square = '100'
			square_link = 'square_' + unicode(square) + '.html'
			
			if square_link in os.listdir(self.SQUARE_PAGES_DIR):
				if square == '100':
					outFile.write('\n              <a href="./main/squares/pages/'+square_link+'" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home" onclick="">'+unicode(square)+'</div></div></a>')
				else:
					if square in self.list_of_easy_squares:
						outFile.write('\n              <a href="./main/squares/pages/'+square_link+'" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home-easy" onclick="">'+unicode(square)+'</div></div></a>')
					elif square in self.list_of_hard_squares:
						outFile.write('\n              <a href="./main/squares/pages/'+square_link+'" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home-hard" onclick="">'+unicode(square)+'</div></div></a>')
					else:
						outFile.write('\n              <a href="./main/squares/pages/'+square_link+'" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home" onclick="">'+unicode(square)+'</div></div></a>')
			else:
				if square == '100':
					outFile.write('\n              <a href="pagenotfound.html" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home" onclick="">'+unicode(square)+'</div></div></a>')
				else:
					outFile.write('\n              <a href="pagenotfound.html" alt="'+unicode(square)+'"><div class="box"><div class="box-grid-home" onclick="">'+unicode(square)+'</div></div></a>')
			
			boxnum -=1
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

		for sentence in self.Updates_Info['$VERSION$\n']:
			# Build_No = self.PAL_10_Determine_Build_Number() + ''
			outFile.write('\n            <a href="./main/updates/pages/updates_0.html"><h4 class="greyheading">VERSION '+sentence.strip('\n')+'</h4></a>')
		outFile.write('\n            <p></p>')
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


	def PAL_10_Generate_GameBoard(self):
		
		# Open web page for writing
		GameBoard = self.HTML_PATH
		outFile = open(GameBoard, 'w')

		# Load the content to go in this file
		self.GameBoard_Info = self.Utilities.PAL_90_Load_Content('', self.GAMEBOARD_PATH)

		# Load the updates section
		self.Updates_Info = self.Utilities.PAL_90_Load_Content('', self.UPDATES_DATA_PATH)

		# Load and print the header
		self.Header_Data = self.Utilities.PAL_90_Load_Template(self.HEADER_PATH)
		self.Utilities.PAL_90_Print_Template(self.Header_Data, outFile)

		# Print the body
		self.PAL_10_Print_Body(outFile)

		# Print the title
		self.Utilities.PAL_90_Print_Title('Welcome!', outFile)

		# Print closing tags
		self.Closing_Tags_Data = self.Utilities.PAL_90_Load_Template(self.CLOSING_TAGS_PATH)
		self.Utilities.PAL_90_Print_Template(self.Closing_Tags_Data, outFile)

		outFile.close()


	def __del__(self):
		pass


if __name__ == '__main__':

	#-----------------
	# Initialize class
	#-----------------
	Generate_GameBoard = PAL_10_Generate_GameBoard()
	Generate_GameBoard.PAL_10_Generate_GameBoard()
