#!/user/bin/env python

from collections import defaultdict
import os

class PAL_90_Utilities(object):

    def __init__(self):

        self.ROOT_DIR           = os.path.dirname(os.getcwd())
        self.BACKUPS_DIR        = os.path.join(self.ROOT_DIR, 'backups')
        self.CSS_DIR            = os.path.join(self.ROOT_DIR, 'css')
        self.IMAGES_DIR         = os.path.join(self.ROOT_DIR, 'images')
        self.JAVASCRIPT_DIR     = os.path.join(self.ROOT_DIR, 'js')
        self.PYTHON_DIR         = os.getcwd()

        self.MAIN_DIR           = os.path.join(self.ROOT_DIR, 'main')
        self.PUZZLES_DIR        = os.path.join(self.MAIN_DIR, 'puzzles')
        self.TUTORIALS_DIR      = os.path.join(self.MAIN_DIR, 'tutorials')
        self.UPDATES_DIR        = os.path.join(self.MAIN_DIR, 'updates')

        self.PUZZLES_PAGES_DIR  = os.path.join(self.PUZZLES_DIR, 'pages')

        self.Current_HTML_Data  = []


    def PAL_90_Load_HTML_File(self, Input_HTML_File):            

        openFile = open(Input_HTML_File, 'r')
        allLines = openFile.readlines()
        for line in allLines[0:]:
            if line not in ['', None, ['']]:
                self.Current_HTML_Data.append(line)
        openFile.close()


    def PAL_90_Print_Formatted_HTML_File(self, Output_HTML_File):

            outFile = open(Output_HTML_File, 'w')

            for line in self.Current_HTML_Data:
                outFile.write(line)

            outFile.close()


    def PAL_90_Minify_HTML_File(self, Current_HTML_File):

        #----------
        # Load file
        #----------
        self.Current_HTML_Data = []
        self.PAL_90_Load_HTML_File(Current_HTML_File)

        #-------------------------------
        # HEAD
        # Remove ONLY leading whitespace
        # characters; leave trailing
        #-------------------------------

        # Locate the start and end positions
        for line in self.Current_HTML_Data:
            if '<!DOCTYPE html>' in line:
                start_position = self.Current_HTML_Data.index(line)
            if '</head>' in line:
                end_position = self.Current_HTML_Data.index(line) + 1

        # Remove all leading whitespace
        current_index = start_position
        for line in self.Current_HTML_Data[start_position:end_position]:
            self.Current_HTML_Data[current_index] = self.Current_HTML_Data[current_index].lstrip()
            current_index   += 1

        #-------------------------------
        # BODY
        # Remove BOTH leading + trailing
        # whitespace characters
        #-------------------------------

        # Locate the start and end positions
        for line in self.Current_HTML_Data:
            if '<body>' in line:
                start_position = self.Current_HTML_Data.index(line)
            if '</body>' in line:
                end_position = self.Current_HTML_Data.index(line) + 1

        # Remove all leading/trailing spaces
        ignore_line = False
        current_index = start_position
        for line in self.Current_HTML_Data[start_position:end_position]:

            # Do not remove indentation/newlines if this is the Editor
            if '<textarea' in line:
                ignore_line = True
            if '</textarea>' in line:
                ignore_line = False

            if not ignore_line:
                self.Current_HTML_Data[current_index] = self.Current_HTML_Data[current_index].lstrip().rstrip()
            current_index   += 1

        #-----------
        # Print file
        #-----------
        self.PAL_90_Print_Formatted_HTML_File(Current_HTML_File)



    def PAL_90_Pretty_Print_HTML_File(self):
        pass
    #     current_page = self.Current_HTML_Data

    #     # Locate the start and end positions of indent adjustments
    #     for line in current_page:
    #         # print line
    #         if '<body>' in line:
    #             start_position = current_page.index(line)
    #         if '</body>' in line:
    #             end_position = current_page.index(line) + 1


    #     # Remove all leading spaces
    #     current_index = start_position
    #     for line in current_page[start_position:end_position]:
    #         current_page[current_index] = current_page[current_index].lstrip()
    #         current_index += 1


        # # Correctly indent each line
        # indent_counter = 2
        # for line in current_page[start_position:end_position]:
        #     if len(line) > 0:
        #         if line[0] == '<':

        #             # Print the current line
        #             # current_index = current_page.index(line)
        #             # current_page[current_index] = ' ' * indent_counter + current_page[current_index]

        #             # If the line is a comment, don't change the indent
        #             if line[1] == '!':
        #                 current_index               = current_page.index(line)
        #                 current_page[current_index] = ' ' * indent_counter + current_page[current_index]


        #             # If the line is a closing tag, indent back
        #             elif line[1] == '/':
        #                 indent_counter -= 2
        #                 current_index               = current_page.index(line)
        #                 current_page[current_index] = ' ' * indent_counter + current_page[current_index]


        #             # If the line is a new tag
        #             else:
        #                 current_index               = current_page.index(line)
        #                 current_page[current_index] = ' ' * indent_counter + current_page[current_index]
                        
        #                 # Identify the HTML tags being used
        #                 tag_name = ''
        #                 for char in line:
        #                     if char == ' ':
        #                         break
        #                     elif char == '>':
        #                         break
        #                     else:
        #                         tag_name += char
        #                 tag_name += '>'
        #                 closing_tag = tag_name[0] + '/' + tag_name[1:]

        #                 void_elements = ['<area>', '<base>', '<br>', '<col>', '<command>', '<embed>', \
        #                 '<hr>', '<img>', '<input>', '<keygen>', '<link>', '<meta>', '<param>', '<source>', '<track>', '<wbr>']

        #                 # If the tag is a self-closing tag, don't change the indent
        #                 if tag_name in void_elements:
        #                     pass

        #                 # If the tag is opened and closed on the same line, don't change the indent
        #                 elif closing_tag in line:
        #                     pass

        #                 else:
        #                     # pass
        #                     indent_counter += 2

        #         else:
        #             current_index               = current_page.index(line)
        #             current_page[current_index] = ' ' * indent_counter + current_page[current_index]
        #             indent_counter += 2



    def PAL_90_Utilities(self):

        print 'WARNING: This program is only for use by other modules.'
        print 'Program terminated without action.\n'



    def __del__(self):
        pass


if __name__ == '__main__':

    #------------------
    # Initialize object
    #------------------

    Utilities = PAL_90_Utilities()
    Utilities.PAL_90_Utilities()