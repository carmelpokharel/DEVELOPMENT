#!/user/bin/env python

from collections import defaultdict
from datetime import datetime

import os


class PAL_13_Generate_FAQ(object):
	
	def __init__(self):
		
		self.ROOT_DIR 			= os.path.dirname(os.getcwd())
		self.BACKUPS_DIR		= os.path.join(self.ROOT_DIR, 'backups')
		self.CONTENTS_DIR 		= os.path.join(self.ROOT_DIR, 'content')
		self.CSS_DIR			= os.path.join(self.ROOT_DIR, 'css')
		self.IMAGES_DIR			= os.path.join(self.ROOT_DIR, 'images')
		self.JAVASCRIPT_DIR		= os.path.join(self.ROOT_DIR, 'js')
		self.PYTHON_DIR			= os.getcwd()

		self.TEMPLATE_PATH		= os.path.join(self.CONTENTS_DIR, 'emptytemplate.html')
		self.CONTENT_PATH		= os.path.join(self.CONTENTS_DIR, 'content_faq.txt')
		self.HTML_PATH			= os.path.join(self.ROOT_DIR, 'faq.html')

		self.current_date_key	= ''

		self.Template_Data		= []
		self.FAQ_Info			= defaultdict(list)
		self.FAQ_Data			= defaultdict()


	def PAL_13_Load_Template(self):

		if not os.path.isfile(self.TEMPLATE_PATH):
			print "ERROR: EMPTY TEMPLATE FILE NOT FOUND"

		fileStream = open(self.TEMPLATE_PATH, 'r')
		allLines = fileStream.readlines()

		for line in allLines[0:]:
			line_list = line
			if line_list != ['']:
				self.Template_Data.append(line_list)

		fileStream.close()


	def PAL_13_Load_FAQ_Content(self):
		
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
			self.FAQ_Info[section[0]] = section[1:]

		fileStream.close()


	def PAL_13_Print_Template(self, outFile):

		for template_line in self.Template_Data:
			outFile.write(template_line)


	def PAL_13_Print_Title(self, outFile):
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--       TITLE      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <title>FAQ</title')
		outFile.write('\n    <div align="center">')


	def PAL_13_Print_Header(self, outFile):

		outFile.write('\n')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--      HEADER      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n      <br><br>')
		outFile.write('\n      <table align="center" style="width:1200px" cellspacing="0px" border="0">')
		outFile.write('\n        <tr>')
		outFile.write('\n          <!-- LEFT: EMPTY PADDING COLUMN -->')
		outFile.write('\n          <td valign="bottom" width="20px">')
		outFile.write('\n          </td>')
		outFile.write('\n          <!-- TITLE -->')
		outFile.write('\n          <td valign="bottom" width="400">')
		outFile.write('\n            <h2 align="left">Frequently Asked Questions</h2>')
		outFile.write('\n          </td>')
		outFile.write('\n          <!-- RIGHT: EMPTY PADDING COLUMN -->')
		outFile.write('\n          <td valign="bottom">')
		outFile.write('\n          </td>')
		outFile.write('\n        </tr>')
		outFile.write('\n      </table>')
		outFile.write('\n      <!-- LINE BREAK -->')
		outFile.write('\n      <br>')
		outFile.write('\n      <hr>')


	def PAL_13_Print_Body(self, outFile):
		
		outFile.write('\n')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--        BODY      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n      <table align="center" style="width:1200px" cellspacing="0px" border="0">')
		outFile.write('\n        <tr>')
		
		#---------------------
		# Print the left panel
		#---------------------
		outFile.write('\n        <!-- LEFT PANEL -->')
		outFile.write('\n          <td width="20px"></td>')
		outFile.write('\n          <td align="left" valign="top" width="610px">')

		# Process recent FAQ
		for faq in self.FAQ_Info['$LEFTPANEL_FAQs$\n']:
			outFile.write('\n              <p>'+faq+'</p>')
			outFile.write('\n            <br><hr>')

		outFile.write('\n          </td>')


		#---------------------
		# Print a middle panel
		#---------------------
		outFile.write('\n          <td width="100px"></td>')

		#----------------------
		# Print the right panel
		#----------------------
		outFile.write('\n          <!-- RIGHT PANEL -->')
		outFile.write('\n          <td align="left" valign="top">')
		outFile.write('\n          <h3>Sponsored</h3>')
		outFile.write('\n          <ol>')
		for reading in self.FAQ_Info['$RIGHTPANEL_SPONSORED$\n']:
			reading = reading.strip('\n').split(' $LINK$ ')
			outFile.write('\n            <a href="'+reading[1]+'" target="_blank"><li>'+reading[0].strip('\n')+'</li></a>')
		outFile.write('\n          </ol>')

		#------------------------
		# Print closing HTML tags
		#------------------------
		outFile.write('\n        </td>')
		outFile.write('\n      </tr>')
		outFile.write('\n    </table>')


	def PAL_13_Print_Closing_Tags(self, outFile):
		outFile.write('\n    </div>')
		outFile.write('\n  </body>')
		outFile.write('\n  <footer align="center"><br>Copyright &copy; Shamil Pokharel 2016</footer>')
		outFile.write('\n</html>')


	def PAL_13_Print_HTML_WebPage(self):
		
		# Open web page for writing
		FAQ = self.HTML_PATH
		outFile = open(FAQ, 'w')

		# Print the template
		self.PAL_13_Print_Template(outFile)

		# Print the title
		self.PAL_13_Print_Title(outFile)

		# Print the header
		self.PAL_13_Print_Header(outFile)

		# Print the body
		self.PAL_13_Print_Body(outFile)

		# Print closing tags
		self.PAL_13_Print_Closing_Tags(outFile)

		outFile.close()


	def PAL_13_Generate_FAQ(self):
		
		self.PAL_13_Load_Template()
		self.PAL_13_Load_FAQ_Content()
		self.PAL_13_Print_HTML_WebPage()


	def __del__(self):
		pass



if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------

	Generate_FAQ = PAL_13_Generate_FAQ()
	Generate_FAQ.PAL_13_Generate_FAQ()
