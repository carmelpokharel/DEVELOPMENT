import os

from PAL_10_Generate_GameBoard import PAL_10_Generate_GameBoard
from PAL_11_Generate_Overview import PAL_11_Generate_Overview
from PAL_12_Generate_Updates import PAL_12_Generate_Updates
from PAL_13_Generate_FAQ import PAL_13_Generate_FAQ
from PAL_20_Generate_Puzzles import PAL_20_Generate_Puzzles
from PAL_40_Generate_Tutorials import PAL_40_Generate_Tutorials
from PAL_30_Generate_PageNotFound import PAL_30_Generate_PageNotFound
from ___delete_pyc_files import cleanCompileFiles

if __name__ == '__main__':

	GameBoard = PAL_10_Generate_GameBoard()
	GameBoard.PAL_10_Generate_GameBoard()

	Overview = PAL_11_Generate_Overview()

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

	#cleanCompileFiles(os.getcwd())