import errno
import os
import shutil

from PAL_10_Generate_GameBoard import PAL_10_Generate_GameBoard
from PAL_11_Generate_Overview import PAL_11_Generate_Overview
from PAL_12_Generate_Updates import PAL_12_Generate_Updates
from PAL_13_Generate_FAQ import PAL_13_Generate_FAQ
from PAL_20_Generate_Puzzles import PAL_20_Generate_Puzzles
from PAL_40_Generate_Tutorials import PAL_40_Generate_Tutorials
from PAL_30_Generate_PageNotFound import PAL_30_Generate_PageNotFound

if __name__ == '__main__':

	#---------------------
	# GENERATE DEVELOPMENT
	#---------------------

	GameBoard = PAL_10_Generate_GameBoard()
	GameBoard.PAL_10_Generate_GameBoard()

	Overview = PAL_11_Generate_Overview()
	Overview.PAL_11_Generate_Overview()

	Updates = PAL_12_Generate_Updates()
	Updates.PAL_12_Generate_Updates()

	FAQ = PAL_13_Generate_FAQ()
	FAQ.PAL_13_Generate_FAQ()

	Puzzles = PAL_20_Generate_Puzzles()
	Puzzles.PAL_20_Generate_Puzzles()

	Tutorials = PAL_40_Generate_Tutorials()
	Tutorials.PAL_40_Generate_Tutorials()

	PageNotFound = PAL_30_Generate_PageNotFound()
	PageNotFound.PAL_30_Generate_PageNotFound()


	#-----------------
	# GENERATE RELEASE
	#-----------------

	DEV_PATH = os.path.dirname(os.getcwd())
	REL_PATH = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'RELEASE')

	# Delete existing configuration
	if os.path.exists(REL_PATH):
		shutil.rmtree(REL_PATH)

	# Create new release folder & copy all files
	try:
		shutil.copytree(DEV_PATH, REL_PATH)
	except OSError as exc:
		if exc.errno == errno.ENOTDIR:
			shutil.copy(DEV_PATH, REL_PATH)
		else: raise

	# Perform directory deletions
	MAIN_DATA			= os.path.join(REL_PATH, 'main/data')
	TUTORIAL_DATA		= os.path.join(REL_PATH, 'main/tutorials/data')
	PUZZLE_DATA 		= os.path.join(REL_PATH, 'main/puzzles/data')
	UPDATES_DATA		= os.path.join(REL_PATH, 'main/updates/data')
	TEMPLATES_HTML		= os.path.join(REL_PATH, 'main/templates')
	PYTHON_SCRIPTS		= os.path.join(REL_PATH, 'python')

	Delete_Directories 	= [	MAIN_DATA, TUTORIAL_DATA, PUZZLE_DATA, UPDATES_DATA, \
							TEMPLATES_HTML, PYTHON_SCRIPTS]

	for directory in Delete_Directories:
		if os.path.exists(directory):
			shutil.rmtree(directory)

	# Perform image directory deletions
	IMAGE_DIR			= os.path.join(REL_PATH, 'images')
	Approved_Images 	= [ 'facebook_icon.png', \
							'headingtitle_snake.png',
							'headingtitle.png', \
							'search.png', \
							'spacing_icon.png', \
							'twitter_icon.png' ]

	for image in os.listdir(IMAGE_DIR):
		if image not in Approved_Images:
			image_path = os.path.join(IMAGE_DIR, image)
			os.remove(image_path)

	ds_store = os.path.join(REL_PATH, '.DS_Store')
	os.remove(ds_store)


	print 'Release version created successfully'


