#!/user/bin/env python

from collections import defaultdict
import os
import re

class PAL_90_Utilities_Class(object):

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
        ignore_line     = False
        current_index   = start_position
        for line in self.Current_HTML_Data[start_position:end_position]:

            # Do not remove indentation/newlines if this is the Editor
            if '<textarea' in line:
                ignore_line = True
            if '</textarea>' in line:
                ignore_line = False

            if not ignore_line:
                self.Current_HTML_Data[current_index] = self.Current_HTML_Data[current_index].lstrip().rstrip()
            current_index   += 1

        #-------------------------------
        # HEAD + BODY
        # Remove all comments
        # '// ', '<!-- ' and ' -->'
        #-------------------------------

        current_index = 0
        for line in self.Current_HTML_Data:
            comment_text = ''
            if '<!-- ' in line:
                comment_start   = line.index('<!-- ')
                comment_end     = line.index(' -->') + 4
                comment_text    = line[comment_start:comment_end]
                self.Current_HTML_Data[current_index] = self.Current_HTML_Data[current_index].replace(comment_text, '').rstrip()
            elif '// ' in line:
                comment_start   = line.index('// ')
                comment_text    = line[comment_start:]
                self.Current_HTML_Data[current_index] = self.Current_HTML_Data[current_index].replace(comment_text, '').rstrip()
            current_index += 1

        #-----------
        # Print file
        #-----------
        self.PAL_90_Print_Formatted_HTML_File(Current_HTML_File)


    def PAL_90_Pretty_Print_HTML_File(self, Current_HTML_File):
        
        #----------
        # Load file
        #----------
        self.Current_HTML_Data = []
        self.PAL_90_Load_HTML_File(Current_HTML_File)

        #------------------------------
        # BODY
        # Format the indents correctly
        #------------------------------

        # Locate the start and end positions of indent adjustments
        for line in self.Current_HTML_Data:
            if '<body>' in line:
                start_position = self.Current_HTML_Data.index(line)
            if '</body>' in line:
                end_position = self.Current_HTML_Data.index(line) + 1

        # Remove all leading/trailing spaces
        ignore_line     = False
        current_index   = start_position
        for line in self.Current_HTML_Data[start_position:end_position]:

            # Do not remove indentation/newlines if this is the Editor
            if '<textarea' in line:
                ignore_line = True
            if '</textarea>' in line:
                ignore_line = False

            if not ignore_line:
                self.Current_HTML_Data[current_index] = self.Current_HTML_Data[current_index].lstrip()
            current_index   += 1

        # # Remove all leading spaces
        # current_index = start_position
        # for line in self.Current_HTML_Data[start_position:end_position]:
        #     self.Current_HTML_Data[current_index] = self.Current_HTML_Data[current_index].lstrip()
        #     current_index += 1


        # Correctly indent each line
        indent_counter  = 0
        ignore_line     = False
        div_class_list  = []
        div_anon_list   = []
        for line in self.Current_HTML_Data[start_position:end_position]:
            if '<textarea' in line:
                ignore_line = True
            if not ignore_line:
                if len(line) > 0:
                    if line[0] == '<':

                        # If the line is a comment, don't change the indent
                        if line[1] == '!':
                            current_index               = self.Current_HTML_Data.index(line)
                            self.Current_HTML_Data[current_index] = ' ' * indent_counter + self.Current_HTML_Data[current_index]


                        # If the line is a closing tag, indent back
                        elif line[1] == '/':
                            indent_counter -= 2
                            current_index               = self.Current_HTML_Data.index(line)
                            self.Current_HTML_Data[current_index] = ' ' * indent_counter + self.Current_HTML_Data[current_index]


                        # If the line is a new tag
                        else:
                            current_index               = self.Current_HTML_Data.index(line)
                            self.Current_HTML_Data[current_index] = ' ' * indent_counter + self.Current_HTML_Data[current_index]
                            
                            # Identify the HTML tags being used
                            tag_name = ''
                            for char in line:
                                if char == ' ':
                                    break
                                elif char == '>':
                                    break
                                else:
                                    tag_name += char
                            tag_name    += '>'
                            closing_tag = tag_name[0] + '/' + tag_name[1:]

                            void_elements = ['<area>', '<base>', '<br>', '<col>', '<command>', '<embed>', \
                            '<hr>', '<img>', '<input>', '<keygen>', '<link>', '<meta>', '<param>', '<source>', '<track>', '<wbr>']

                            # If the tag is a self-closing tag, don't change the indent
                            if tag_name in void_elements:
                                pass

                            # If the tag is opened and closed on the same line, don't change the indent
                            elif closing_tag in line:
                                pass

                            else:
                                indent_counter += 2

                    else:
                        current_index               = self.Current_HTML_Data.index(line)
                        self.Current_HTML_Data[current_index] = ' ' * indent_counter + self.Current_HTML_Data[current_index]
                        if '</' not in line:
                            indent_counter += 2

            if '</textarea>' in line:
                ignore_line = False

        #------------------------------
        # BODY
        # Add closing tags to all divs
        #------------------------------

        # Make a list of all (line, index) pairs where '<div' occurs
        class_list = ['']
        current_index = start_position

        for line in self.Current_HTML_Data[start_position:end_position]:
            new_div_indexes     = []
            anon_div_counter    = line.count('<div>')
            class_div_counter   = line.count('<div class')
            new_div_counter     = anon_div_counter + class_div_counter
            if new_div_counter > 1:
                for open_tag in re.finditer('<div', line):
                    new_div_indexes.append(open_tag.end())
            elif new_div_counter == 1:
                new_div_indexes.append(line.index('<div')+4)

            for tag_pos in new_div_indexes:
                class_name = 'anonymous div'
                if line[tag_pos] == ' ':
                    class_name = ''
                    for char in line[tag_pos+8:]:
                        if char == '"':
                            break
                        else:
                            class_name += char
                
                class_list.append(class_name)

            temp_close_tags     = []
            close_div_indexes   = []
            close_div_counter   = line.count('</div>')

            # If there is more than one </div> in the same line
            if close_div_counter > 1:
                for close_tag in re.finditer('</div>', line):
                    close_div_indexes.append(close_tag.end())

            # If there is only one </div> on the line
            elif close_div_counter == 1:
                close_div_indexes.append(line.index('</div>')+6)

            # print self.Current_HTML_Data[current_index]
            # print '\n'
            # print line
            # print class_list
            # print close_div_indexes

            for tag_pos in reversed(close_div_indexes):
                # print line == '</div>'
                if '</div>' in line:
                    #print self.Current_HTML_Data[current_index]
                    if self.Current_HTML_Data[current_index][tag_pos:tag_pos+4] != '<!--':
                        self.Current_HTML_Data[current_index] = self.Current_HTML_Data[current_index][:tag_pos] + '<!-- ' + class_list[-1] + ' -->' + self.Current_HTML_Data[current_index][tag_pos:]
                    #print self.Current_HTML_Data[current_index]
                class_list = class_list[:-1]

            # print self.Current_HTML_Data[current_index]

            current_index += 1

        #-----------
        # Print file
        #-----------
        self.PAL_90_Print_Formatted_HTML_File(Current_HTML_File)


    def PAL_90_Utilities_Internal(self):

        print 'WARNING: This program is only for use by other modules.'
        print 'Program terminated without action.\n'



    def __del__(self):
        pass


if __name__ == '__main__':

    #------------------
    # Initialize object
    #------------------

    Utilities_Class = PAL_90_Utilities_Class()
    Utilities_Class.PAL_90_Utilities_Internal()