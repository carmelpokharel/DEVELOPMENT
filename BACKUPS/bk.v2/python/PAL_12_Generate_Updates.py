#!/user/bin/env python

from collections import defaultdict
from datetime import datetime

import os


class PAL_12_Generate_Updates(object):
	
	def __init__(self):
		
		self.ROOT_DIR 			= os.path.dirname(os.getcwd())
		self.BACKUPS_DIR		= os.path.join(self.ROOT_DIR, 'backups')
		self.CONTENTS_DIR 		= os.path.join(self.ROOT_DIR, 'content')
		self.CSS_DIR			= os.path.join(self.ROOT_DIR, 'css')
		self.IMAGES_DIR			= os.path.join(self.ROOT_DIR, 'images')
		self.JAVASCRIPT_DIR		= os.path.join(self.ROOT_DIR, 'js')
		self.PYTHON_DIR			= os.getcwd()

		self.TEMPLATE_PATH		= os.path.join(self.CONTENTS_DIR, 'emptytemplate.html')
		self.CONTENT_PATH		= os.path.join(self.CONTENTS_DIR, 'content_updates.txt')
		self.HTML_PATH			= os.path.join(self.ROOT_DIR, 'updates.html')

		self.current_date_key	= ''

		self.Template_Data		= []
		self.Updates_Info		= defaultdict(list)
		self.Updates_Data		= defaultdict()


	def PAL_12_Load_Template(self):

		if not os.path.isfile(self.TEMPLATE_PATH):
			print "ERROR: EMPTY TEMPLATE FILE NOT FOUND"

		fileStream = open(self.TEMPLATE_PATH, 'r')
		allLines = fileStream.readlines()

		for line in allLines[0:]:
			line_list = line
			if line_list != ['']:
				self.Template_Data.append(line_list)

		fileStream.close()


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


	def PAL_12_Print_Template(self, outFile):

		for template_line in self.Template_Data:
			outFile.write(template_line)


	def PAL_12_Print_Title(self, outFile):
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <!--       TITLE      -->')
		outFile.write('\n    <!-- **************** -->')
		outFile.write('\n    <title>Updates</title')
		outFile.write('\n    <div align="center">')


	def PAL_12_Print_Header(self, outFile):

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
		outFile.write('\n            <h2 align="left">Updates & Change Log</h2>')
		outFile.write('\n          </td>')
		outFile.write('\n          <!-- RIGHT: EMPTY PADDING COLUMN -->')
		outFile.write('\n          <td valign="bottom">')
		outFile.write('\n          </td>')
		outFile.write('\n        </tr>')
		outFile.write('\n      </table>')
		outFile.write('\n      <!-- LINE BREAK -->')
		outFile.write('\n      <br>')
		outFile.write('\n      <hr>')


	def PAL_12_Print_Body(self, outFile):
		
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

		# Process recent updates
		for update in self.Updates_Info['$RIGHTPANEL_RECENTUPDATES$\n']:
			update = update.strip('\n')
			try: update = datetime.strptime(update, '%Y-%m-%d')
			except: pass
			if isinstance(update, datetime):
				self.current_date_key = update
				self.Updates_Data[self.current_date_key] = []
			else:
				self.Updates_Data[self.current_date_key].append(update)

		# Print recent updates
		for date in reversed(sorted(self.Updates_Data)):
			outFile.write('\n            <h4>'+date.strftime('%B %d, %Y')+'</h4>')
			outFile.write('\n            <ol>')
			for update in self.Updates_Data[date]:
				outFile.write('\n              <li>'+update+'</li>')
			outFile.write('\n            </ol>')
			outFile.write('\n            <br><hr>')	

		outFile.write('\n            <br>')
		outFile.write('\n            <button type="button" onclick="featureRequest()">Request a feature</button>')
		outFile.write('\n            <br><br>')
		outFile.write('\n          </td>')


		#---------------------
		# Print a middle panel
		#---------------------
		outFile.write('\n          <td width="100px"></td>')

		#----------------------
		# Print the right panel
		#----------------------
		outFile.write('\n          <!-- RIGHT PANEL -->')
		outFile.write('\n          <!-- RIGHT PANEL -->')
		outFile.write('\n          <td align="left" valign="top">')
		outFile.write('\n          <h3>Sponsored</h3>')
		outFile.write('\n          <ol>')
		for reading in self.Updates_Info['$RIGHTPANEL_SPONSORED$\n']:
			reading = reading.strip('\n').split(' $LINK$ ')
			outFile.write('\n            <a href="'+reading[1]+'" target="_blank"><li>'+reading[0].strip('\n')+'</li></a>')
		outFile.write('\n          </ol>')

		#------------------------
		# Print closing HTML tags
		#------------------------
		outFile.write('\n        </td>')
		outFile.write('\n      </tr>')
		outFile.write('\n    </table>')


	def PAL_12_Print_Closing_Tags(self, outFile):
		outFile.write('\n    </div>')
		outFile.write('\n  </body>')
		outFile.write('\n  <footer align="center"><br>Copyright &copy; Shamil Pokharel 2016</footer>')
		outFile.write('\n</html>')


	def PAL_12_Print_HTML_WebPage(self):
		
		# Open web page for writing
		Updates = self.HTML_PATH
		outFile = open(Updates, 'w')

		# Print the template
		self.PAL_12_Print_Template(outFile)

		# Print the title
		self.PAL_12_Print_Title(outFile)

		# Print the header
		self.PAL_12_Print_Header(outFile)

		# Print the body
		self.PAL_12_Print_Body(outFile)

		# Print closing tags
		self.PAL_12_Print_Closing_Tags(outFile)

		outFile.close()


	def PAL_12_Generate_Updates(self):
		
		self.PAL_12_Load_Template()
		self.PAL_12_Load_Updates_Content()
		self.PAL_12_Print_HTML_WebPage()


	def __del__(self):
		pass



if __name__ == '__main__':

	#------------------
	# Initialize object
	#------------------

	Generate_Updates = PAL_12_Generate_Updates()
	Generate_Updates.PAL_12_Generate_Updates()
