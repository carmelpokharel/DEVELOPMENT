#!/user/bin/env python

from collections import defaultdict

import os


class PAL_11_Generate_Manual(object):
	
	def __init__(self):
		
		self.ROOT_DIR 			= os.path.dirname(os.getcwd())
		self.BACKUPS_DIR		= os.path.join(self.ROOT_DIR, 'backups')
		self.CONTENTS_DIR 		= os.path.join(self.ROOT_DIR, 'content')
		self.CSS_DIR			= os.path.join(self.ROOT_DIR, 'css')
		self.IMAGES_DIR			= os.path.join(self.ROOT_DIR, 'images')
		self.JAVASCRIPT_DIR		= os.path.join(self.ROOT_DIR, 'js')
		self.PYTHON_DIR			= os.getcwd()

		self.TEMPLATE_PATH		= os.path.join(self.CONTENTS_DIR, 'emptytemplate.html')
		self.CONTENT_PATH		= os.path.join(self.CONTENTS_DIR, 'content_manual.txt')
		self.HTML_PATH			= os.path.join(self.ROOT_DIR, 'manual.html')

		self.Template_Data		= []
		self.Manual_Data		= []
		self.Manual_Info		= defaultdict(list)


	def PAL_11_Load_Template(self):

		if not os.path.isfile(self.TEMPLATE_PATH):
			print "ERROR: EMPTY TEMPLATE FILE NOT FOUND"

		fileStream = open(self.TEMPLATE_PATH, 'r')
		allLines = fileStream.readlines()

		for line in allLines[0:]:
			line_list = line
			if line_list != ['']:
				self.Template_Data.append(line_list)

		fileStream.close()


	def PAL_11_Load_Manual_Content(self):
		
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
			self.Manual_Info[section[0]] = section[1:]

		fileStream.close()


	def PAL_11_Print_Template(self, outFile):

		for template_line in self.Template_Data:
			outFile.write(template_line)


	def PAL_11_Print_Title(self, outFile):
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--       TITLE      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <title>Manual</title')
		outFile.write('\n    <div align="center">')


	def PAL_11_Print_Header(self, outFile):

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
		outFile.write('\n          <!-- MANUAL TITLE -->')
		outFile.write('\n          <td valign="bottom" width="140">')
		outFile.write('\n            <h2 align="left">Manual</h2>')
		outFile.write('\n          </td>')
		outFile.write('\n          <!-- RIGHT: EMPTY PADDING COLUMN -->')
		outFile.write('\n          <td valign="bottom">')
		outFile.write('\n          </td>')
		outFile.write('\n        </tr>')
		outFile.write('\n      </table>')
		outFile.write('\n      <!-- LINE BREAK -->')
		outFile.write('\n      <br>')
		outFile.write('\n      <hr>')


	def PAL_11_Print_Body(self, outFile):
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
		outFile.write('\n          <td width="20">')
		outFile.write('\n          </td>')
		outFile.write('\n          <td align="left" valign="top" width="600px">')
		
		# Print About Pythons and Ladders
		outFile.write('\n            <h3>About Pythons and Ladders</h3>')
		for sentence in self.Manual_Info['$LEFTPANEL_ABOUT$\n']:
			if sentence == '\n':
				outFile.write('\n            <p class="small">&nbsp;</p>')
			else:
				outFile.write('\n            <p class="small">'+sentence.strip('\n')+'</p>')
		outFile.write('\n            <p class="small">&nbsp;</p>')

		# Print objectives
		outFile.write('\n            <h3>Objective</h3>')
		for sentence in self.Manual_Info['$LEFTPANEL_OBJECTIVE$\n']:
			if sentence == '\n':
				outFile.write('\n            <p class="small">&nbsp;</p>')
			else:
				outFile.write('\n            <p class="small">'+sentence.strip('\n')+'</p>')
		outFile.write('\n            <p class="small">&nbsp;</p>')
		
		outFile.write('\n          </td>')

		#---------------------
		# Print a middle panel
		#---------------------
		outFile.write('\n          <td width="100px"></td>')

		#----------------------
		# Print the right panel
		#----------------------
		outFile.write('\n          <!-- RIGHT PANEL -->')
		outFile.write('\n          <td align="left"  valign="top">')
		
		# Print setup information
		outFile.write('\n            <h3>Setting up Python</h3>')
		for sentence in self.Manual_Info['$LEFTPANEL_SETUP$\n']:
			if sentence == '\n':
				outFile.write('\n            <p class="small">&nbsp;</p>')
			else:
				outFile.write('\n            <p class="small">'+sentence.strip('\n')+'</p>')
		outFile.write('\n            <p class="small">&nbsp;</p>')
		
		# Print terminology
		outFile.write('\n          <h3>Terminology</h3>')
		outFile.write('\n          <ol>')
		for term in self.Manual_Info['$RIGHTPANEL_TERMINOLOGY$\n']:
			outFile.write('\n            <li>'+term.strip('\n')+'</li>')
		outFile.write('\n          </ol>')

		# Print resources
		outFile.write('\n          <h3>Resources</h3>')
		for sentence in self.Manual_Info['$RIGHTPANEL_RESOURCES$\n']:
			if sentence == '\n':
				outFile.write('\n            <p class="small">&nbsp;</p>')
			else:
				outFile.write('\n            <p class="small">'+sentence.strip('\n')+'</p>')
		outFile.write('\n            <p class="small">&nbsp;</p>')

		#------------------------
		# Print closing HTML tags
		#------------------------
		outFile.write('\n          </td>')
		outFile.write('\n        </tr>')
		outFile.write('\n      </table>')


	def PAL_11_Print_Closing_Tags(self, outFile):
		outFile.write('\n    </div>')
		outFile.write('\n  </body>')
		outFile.write('\n  <footer align="center"><br>Copyright &copy; Shamil Pokharel 2016</footer>')
		outFile.write('\n</html>')


	def PAL_11_Print_HTML_WebPage(self):
		
		# Open web page for writing
		manual = self.HTML_PATH
		outFile = open(manual, 'w')

		# Print the template
		self.PAL_11_Print_Template(outFile)

		# Print the title
		self.PAL_11_Print_Title(outFile)

		# Print the header
		self.PAL_11_Print_Header(outFile)

		# Print the body
		self.PAL_11_Print_Body( outFile)

		# Print closing tags
		self.PAL_11_Print_Closing_Tags(outFile)

		outFile.close()


	def PAL_11_Generate_Manual(self):
		
		self.PAL_11_Load_Template()
		self.PAL_11_Load_Manual_Content()
		self.PAL_11_Print_HTML_WebPage()


	def __del__(self):
		pass



if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------

	Generate_Manual = PAL_11_Generate_Manual()
	Generate_Manual.PAL_11_Generate_Manual()
