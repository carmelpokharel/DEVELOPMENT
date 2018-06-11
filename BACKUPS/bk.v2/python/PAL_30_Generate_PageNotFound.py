#!/user/bin/env python

from collections import defaultdict

import os


class PAL_30_Generate_PageNotFound(object):
	
	def __init__(self):
		
		self.ROOT_DIR 			= os.path.dirname(os.getcwd())
		self.BACKUPS_DIR		= os.path.join(self.ROOT_DIR, 'backups')
		self.CONTENTS_DIR 		= os.path.join(self.ROOT_DIR, 'content')
		self.CSS_DIR			= os.path.join(self.ROOT_DIR, 'css')
		self.IMAGES_DIR			= os.path.join(self.ROOT_DIR, 'images')
		self.JAVASCRIPT_DIR		= os.path.join(self.ROOT_DIR, 'js')
		self.PYTHON_DIR			= os.getcwd()

		self.TEMPLATE_PATH		= os.path.join(self.CONTENTS_DIR, 'emptytemplate.html')
		self.HTML_PATH			= os.path.join(self.ROOT_DIR, 'pagenotfound.html')

		self.Template_Data		= []


	def PAL_30_Load_Template(self):

		if not os.path.isfile(self.TEMPLATE_PATH):
			print "ERROR: EMPTY TEMPLATE FILE NOT FOUND"

		fileStream = open(self.TEMPLATE_PATH, 'r')
		allLines = fileStream.readlines()

		for line in allLines[0:]:
			line_list = line
			if line_list != ['']:
				self.Template_Data.append(line_list)

		fileStream.close()


	def PAL_30_Print_Template(self, outFile):

		for template_line in self.Template_Data:
			outFile.write(template_line)


	def PAL_30_Print_Title(self, outFile):
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--       TITLE      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <title>Oops!</title')
		outFile.write('\n    <div align="center">')


	def PAL_30_Print_Header(self, outFile):

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
		outFile.write('\n          <td valign="bottom" width="500">')
		outFile.write('\n            <h2 align="left">Oops! We couldn\'t find that page.</h2>')
		outFile.write('\n          </td>')
		outFile.write('\n          <!-- RIGHT: EMPTY PADDING COLUMN -->')
		outFile.write('\n          <td valign="bottom">')
		outFile.write('\n          </td>')
		outFile.write('\n        </tr>')
		outFile.write('\n      </table>')
		outFile.write('\n      <!-- LINE BREAK -->')
		outFile.write('\n      <br>')
		outFile.write('\n      <hr>')
		outFile.write('\n      <br>')


	def PAL_30_Print_Body(self, outFile):
		outFile.write('\n')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--        BODY      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n      <table align="center" style="width:1200px" cellspacing="20px" border="0">')
		outFile.write('\n        <tr>')
		
		#---------------------
		# Print the left panel
		#---------------------
		outFile.write('\n        <!-- LEFT PANEL -->')
		outFile.write('\n          <td align="left" valign="top" width="550px">')

		outFile.write('\n            <p>Looks like you\'ve stumbled upon a page that doesn\'t (yet) exist.</p>')
		outFile.write('\n            <p>That could mean a couple of things:</p>')
		outFile.write('\n            <ol>')
		outFile.write('\n            <li>We\'re still working on it... it\'ll be up soon!</li>')
		outFile.write('\n            <li>We never intended for this page to exist in the first place -- you found a bug!</li>')
		outFile.write('\n            </ol>')
		outFile.write('\n            <p>If this feels like unexpected behaviour, please call it to our attention below.</p>')
		outFile.write('\n            <br>')
		outFile.write('\n            <button type="button" onclick="window.location.href=\'index.html\'">Return home</button>')
		outFile.write('\n            <button type="button" onclick="reportBug()">Report bug</button>')
		
		outFile.write('\n          </td>')

		#---------------------
		# Print a middle panel
		#---------------------
		#outFile.write('\n          <td width="10px"></td>')

		#----------------------
		# Print the right panel
		#----------------------
		outFile.write('\n          <!-- RIGHT PANEL -->')
		outFile.write('\n          <td align="left"  valign="top">')

		#------------------------
		# Print closing HTML tags
		#------------------------
		outFile.write('\n        </td>')
		outFile.write('\n      </tr>')
		outFile.write('\n    </table>')


	def PAL_30_Print_Closing_Tags(self, outFile):
		outFile.write('\n    </div>')
		outFile.write('\n  </body>')
		outFile.write('\n  <footer align="center"><br>Copyright &copy; Shamil Pokharel 2016</footer>')

		outFile.write('\n</html>')


	def PAL_30_Print_HTML_WebPage(self):
		
		# Open web page for writing
		PageNotFound = self.HTML_PATH
		outFile = open(PageNotFound, 'w')

		# Print the template
		self.PAL_30_Print_Template(outFile)

		# Print the title
		self.PAL_30_Print_Title(outFile)

		# Print the header
		self.PAL_30_Print_Header(outFile)

		# Print the body
		self.PAL_30_Print_Body(outFile)

		# Print closing tags
		self.PAL_30_Print_Closing_Tags(outFile)

		outFile.close()


	def PAL_30_Generate_PageNotFound(self):
		
		self.PAL_30_Load_Template()
		self.PAL_30_Print_HTML_WebPage()


	def __del__(self):
		pass



if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------

	PageNotFound = PAL_30_Generate_PageNotFound()
	PageNotFound.PAL_30_Generate_PageNotFound()
