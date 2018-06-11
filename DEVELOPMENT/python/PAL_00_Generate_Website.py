import os

from PAL_10_Generate_GameBoard import PAL_10_Generate_GameBoard
from PAL_11_Generate_Overview import PAL_11_Generate_Overview
from PAL_12_Generate_Updates import PAL_12_Generate_Updates
from PAL_13_Generate_FAQ import PAL_13_Generate_FAQ
from PAL_20_Generate_Squares import PAL_20_Generate_Squares
from PAL_21_Generate_Squares_Easy import PAL_21_Generate_Squares_Easy
from PAL_22_Generate_Squares_Hard import PAL_22_Generate_Squares_Hard
from PAL_40_Generate_Tutorials import PAL_40_Generate_Tutorials
from PAL_30_Generate_PageNotFound import PAL_30_Generate_PageNotFound
from PAL_90_Utilities import PAL_90_Utilities_Class
from ___delete_pyc_files import cleanCompileFiles

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

    Squares = PAL_20_Generate_Squares()
    Squares.PAL_20_Generate_Squares()

    Squares_Easy = PAL_21_Generate_Squares_Easy()
    Squares_Easy.PAL_21_Generate_Squares_Easy()

    Squares_Hard = PAL_22_Generate_Squares_Hard()
    Squares_Hard.PAL_22_Generate_Squares_Hard()

    Tutorials = PAL_40_Generate_Tutorials()
    Tutorials.PAL_40_Generate_Tutorials()

    PageNotFound = PAL_30_Generate_PageNotFound()
    PageNotFound.PAL_30_Generate_PageNotFound()

    #-------------
    # PRETTY PRINT
    #-------------

    # Set up directories
    DEV_PATH = os.path.dirname(os.getcwd())
    REL_PATH = os.path.join(os.path.dirname(
        os.path.dirname(os.getcwd())), 'DEVELOPMENT')

    MAIN_DATA = os.path.join(os.path.join(REL_PATH, 'main'), 'data')
    TUTORIAL_DATA = os.path.join(os.path.join(
        os.path.join(REL_PATH, 'main'), 'tutorials'), 'data')
    TUTORIAL_PAGES = os.path.join(os.path.join(
        os.path.join(REL_PATH, 'main'), 'tutorials'), 'pages')
    SQUARE_DATA = os.path.join(os.path.join(
        os.path.join(REL_PATH, 'main'), 'squares'), 'data')
    SQUARE_PAGES = os.path.join(os.path.join(
        os.path.join(REL_PATH, 'main'), 'squares'), 'pages')
    UPDATES_DATA = os.path.join(os.path.join(
        os.path.join(REL_PATH, 'main'), 'updates'), 'data')
    UPDATES_PAGES = os.path.join(os.path.join(
        os.path.join(REL_PATH, 'main'), 'updates'), 'pages')
    TEMPLATES_HTML = os.path.join(os.path.join(REL_PATH, 'main'), 'templates')
    PYTHON_SCRIPTS = os.path.join(REL_PATH, 'python')
    CSS_DIR = os.path.join(REL_PATH, 'css')

    Pretty_HTML_Directories = [
        REL_PATH, SQUARE_PAGES, TUTORIAL_PAGES, UPDATES_PAGES]
    Pretty_CSS_Directories = [CSS_DIR]
    Delete_Directories = [	MAIN_DATA, TUTORIAL_DATA, SQUARE_DATA, UPDATES_DATA,
                           TEMPLATES_HTML, PYTHON_SCRIPTS]

    # Pretty Print HTML
    Utilities_Class = PAL_90_Utilities_Class()
    curr_HTML_files = []

    for page_set in Pretty_HTML_Directories:
        for web_file in os.listdir(page_set):
            if '.html' in web_file:
                curr_HTML_files.append(os.path.join(page_set, web_file))

    for html_file_path in curr_HTML_files:
        if '__default.html' not in html_file_path:
            Utilities_Class.PAL_90_Pretty_Print_HTML_File(html_file_path)

    print ('Development version created successfully')
    # cleanCompileFiles(os.getcwd())
