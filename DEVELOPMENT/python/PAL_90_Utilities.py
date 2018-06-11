#!/user/bin/env python

from collections import defaultdict
import os
import re

class PAL_90_Utilities_Class(object):

    def __init__(self):

        self.ROOT_DIR                   = os.path.dirname(os.getcwd())
        self.BACKUPS_DIR                = os.path.join(self.ROOT_DIR, 'backups')
        self.CSS_DIR                    = os.path.join(self.ROOT_DIR, 'css')
        self.IMAGES_DIR                 = os.path.join(self.ROOT_DIR, 'images')
        self.JAVASCRIPT_DIR             = os.path.join(self.ROOT_DIR, 'js')
        self.PYTHON_DIR                 = os.getcwd()

        self.MAIN_DIR                   = os.path.join(self.ROOT_DIR, 'main')
        self.SQUARES_DIR                = os.path.join(self.MAIN_DIR, 'squares')
        self.TUTORIALS_DIR              = os.path.join(self.MAIN_DIR, 'tutorials')
        self.UPDATES_DIR                = os.path.join(self.MAIN_DIR, 'updates')

        self.SQUARES_PAGES_DIR          = os.path.join(self.SQUARES_DIR, 'pages')

        self.Current_HTML_Data          = []
        self.Current_CSS_Data           = []
        self.Current_CSS_Variables_Data = []

        self.Hint_Titles                = [ 'What gives?', 'Out of ideas?', 'Not your day?', \
                                            'Coder\'s block?', 'Fate fell short this time?', \
                                            'Feeling blue?', 'Dazed and confused?', 'Battered and bruised?', \
                                            'Losing hope?', 'Under the weather?', 'Need a little help?']

        self.Numbers_to_Words           = { 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
                                            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
                                            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
                                            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
                                            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
                                            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
                                            90: 'Ninety', 0: 'Zero', 100: 'One Hundred'}
        
        self.Keywords_Delimiter         = '$%$%'
        
        self.Keywords_Formats           = { 'int': "<span class=keyword-teal>int</span>", \
                                            'str': "<span class=keyword-teal>str</span>", \
                                            'bool': "<span class=keyword-teal>bool</span>", \
                                            'list': "<span class=keyword-teal>list</span>", \
                                            'dict': "<span class=keyword-teal>dict</span>", \
                                            'escape': "<span class=keyword-purple>\\</span>", \
                                            'newline': "<span class=keyword-purple>\\n</span>", \
                                            'tab': "<span class=keyword-purple>\\t</span>", \
                                            'type': "<span class=keyword-green>type</span>", \
                                            'print': "<span class=keyword-orange>print</span>", \
                                            'is': "<span class=keyword-orange>is</span>", \
                                            'float': "<span class=keyword-teal>float</span>", \
                                            'in': "<span class=keyword-orange>in</span>", \
                                            'not': "<span class=keyword-orange>not</span>", \
                                            'if': "<span class=keyword-orange>if</span>", \
                                            'else': "<span class=keyword-orange>else</span>", \
                                            'elif': "<span class=keyword-orange>elif</span>", \
                                            'for': "<span class=keyword-orange>for</span>", \
                                            'range': "<span class=keyword-green>range</span>", \
                                            '#': "<span class=keyword-green>#</span>", \
                                            'True': "<span class=keyword-purple>True</span>", \
                                            'False': "<span class=keyword-purple>False</span>", \
                                            'len': "<span class=keyword-green>len</span>", \
                                            'append': "<span class=keyword-green>append</span>", \
                                            'extend': "<span class=keyword-green>extend</span>", \
                                            'return': "<span class=keyword-orange>return</span>", \
                                            'def': "<span class=keyword-orange>def</span>", \
                                            'max': "<span class=keyword-green>max</span>", \
                                            'min': "<span class=keyword-green>min</span>", \
                                            'capitalize': "<span class=keyword-green>capitalize</span>", \
                                            'upper': "<span class=keyword-green>upper</span>", \
                                            'lower': "<span class=keyword-green>lower</span>", \
                                            'reversed': "<span class=keyword-green>reversed</span>", \
                                            'pop': "<span class=keyword-green>pop</span>", \
                                            'rstrip': "<span class=keyword-green>rstrip</span>", \
                                            'choice': "<span class=keyword-green>choice</span>", \
                                            'import': "<span class=keyword-orange>import</span>", \
                                            'random': "<span class=keyword-purple>random</span>", \
                                            'split': "<span class=keyword-green>split</span>", \
                                            'replace': "<span class=keyword-green>replace</span>"

                                            }

        self.Easy_Version_Text          = 'This square is an easier version of Square $#$.\nIn Pythons \
                                            and Ladders, some concepts we introduce are multi-faceted, \
                                            and require breaking down into smaller pieces. In such \
                                            instances, you\'ll find pages such as this one, containing \
                                            easier prerequisites to your current task.\nOnce you\'re \
                                            comfortable with the content here, click \'Done\' at the \
                                            bottom of this page to go back and re-attempt Square $#$!'

        self.Hard_Version_Text          = 'This square is a harder version of Square $#$.\nIn Pythons \
                                            and Ladders, some concepts we introduce benefit from \
                                            repetition and memorization, and consequently may feel \
                                            "too easy." In such instances, you\'ll find \
                                            pages such as this one, which challenge you to complete \
                                            harder versions of your current square.\nOnce you\'ve \
                                            completed the task on this page, celebrate and carry on!'


    # =================
    # UTILITY FUNCTIONS
    # =================

    def PAL_90_Utilities_Internal(self):
        print ('WARNING: This program is only for use by other modules.')
        print ('Program terminated without action.\n')


    def PAL_90_Spell_Number(self, n):
        try:
            return self.Numbers_to_Words[n]
        except KeyError:
            try:
                return self.Numbers_to_Words[n-n%10] + '-' + self.Numbers_to_Words[n%10]
            except KeyError:
                return 'Number out of range'


    def PAL_90_Format_Special_Characters(self, Format_String=''):

            # tempString = tempString.replace("'", '&apos;')
            # tempString = tempString.replace('"', '&quot;')
            
            Format_String = Format_String.replace('^int^', self.Keywords_Formats['int'])
            Format_String = Format_String.replace('^str^', self.Keywords_Formats['str'])
            Format_String = Format_String.replace('^float^', self.Keywords_Formats['float'])
            Format_String = Format_String.replace('^bool^', self.Keywords_Formats['bool'])
            Format_String = Format_String.replace('^list^', self.Keywords_Formats['list'])
            Format_String = Format_String.replace('^dict^', self.Keywords_Formats['dict'])

            Format_String = Format_String.replace('^print^', self.Keywords_Formats['print'])
            Format_String = Format_String.replace('^is^', self.Keywords_Formats['is'])
            Format_String = Format_String.replace('^in^', self.Keywords_Formats['in'])
            Format_String = Format_String.replace('^not^', self.Keywords_Formats['not'])
            Format_String = Format_String.replace('^if^', self.Keywords_Formats['if'])
            Format_String = Format_String.replace('^else^', self.Keywords_Formats['else'])
            Format_String = Format_String.replace('^elif^', self.Keywords_Formats['elif'])
            Format_String = Format_String.replace('^for^', self.Keywords_Formats['for'])
            Format_String = Format_String.replace('^return^', self.Keywords_Formats['return'])
            Format_String = Format_String.replace('^import^', self.Keywords_Formats['import'])

            Format_String = Format_String.replace('^\\n^', self.Keywords_Formats['newline'])
            Format_String = Format_String.replace('^\\t^', self.Keywords_Formats['tab'])
            Format_String = Format_String.replace('^\\^', self.Keywords_Formats['escape'])
            Format_String = Format_String.replace('^True^', self.Keywords_Formats['True'])
            Format_String = Format_String.replace('^False^', self.Keywords_Formats['False'])
            Format_String = Format_String.replace('^random^', self.Keywords_Formats['random'])

            Format_String = Format_String.replace('^type^', self.Keywords_Formats['type'])
            Format_String = Format_String.replace('^range^', self.Keywords_Formats['range'])
            Format_String = Format_String.replace('^append^', self.Keywords_Formats['append'])
            Format_String = Format_String.replace('^extend^', self.Keywords_Formats['extend'])
            Format_String = Format_String.replace('^#^', self.Keywords_Formats['#'])
            Format_String = Format_String.replace('^len^', self.Keywords_Formats['len'])
            Format_String = Format_String.replace('^max^', self.Keywords_Formats['max'])
            Format_String = Format_String.replace('^min^', self.Keywords_Formats['min'])
            Format_String = Format_String.replace('^capitalize^', self.Keywords_Formats['capitalize'])
            Format_String = Format_String.replace('^upper^', self.Keywords_Formats['upper'])
            Format_String = Format_String.replace('^lower^', self.Keywords_Formats['lower'])
            Format_String = Format_String.replace('^reversed^', self.Keywords_Formats['reversed'])
            Format_String = Format_String.replace('^pop^', self.Keywords_Formats['pop'])
            Format_String = Format_String.replace('^rstrip^', self.Keywords_Formats['rstrip'])
            Format_String = Format_String.replace('^choice^', self.Keywords_Formats['choice'])
            Format_String = Format_String.replace('^split^', self.Keywords_Formats['split'])
            Format_String = Format_String.replace('^replace^', self.Keywords_Formats['replace'])

            Format_String = Format_String.replace('^def^', self.Keywords_Formats['def'])

            Format_String = Format_String.replace('--', '&#8212;')
            Format_String = Format_String.replace('<linespace>', '<p class="small">&nbsp;</p>')
            Format_String = Format_String.replace('<codespace>', '<p class="small">&nbsp;</p>')
            Format_String = Format_String.replace('<tab>', '&nbsp;&nbsp;&nbsp;&nbsp;')
            Format_String = Format_String.replace('<3sp>', '&nbsp;&nbsp;&nbsp;')
            Format_String = Format_String.replace('<2sp>', '&nbsp;&nbsp;')
            Format_String = Format_String.replace('<1sp>', '&nbsp;')

            Format_String = Format_String.replace('<outputcodeline>', '<table class="codeline"><tr><td class="output">')
            Format_String = Format_String.replace('</outputcodeline>', '</td></tr></table>')

            Format_String = Format_String.replace('<outputcodeblock>', '<table class="output"><tr><td>')
            Format_String = Format_String.replace('</outputcodeblock>', '</td></tr></table><p></p>')

            Format_String = Format_String.replace('<democodeline>', '<table class="codeline"><tr><td class="demo">')
            Format_String = Format_String.replace('</democodeline>', '</td></tr></table>')
            
            Format_String = Format_String.replace('<democodeblock>', '<table class="demo"><tr><td>')
            Format_String = Format_String.replace('</democodeblock>', '</td></tr></table><p></p>')

            Format_String = Format_String.replace('<cardcodeline>', '<table class="codeline"><tr><td class="card">')
            Format_String = Format_String.replace('</cardcodeline>', '</td></tr></table>')
            
            Format_String = Format_String.replace('<cardcodeblock>', '<table class="card"><tr><td>')
            Format_String = Format_String.replace('</cardcodeblock>', '</td></tr></table><p></p>')

            Format_String = Format_String.replace('<mathexp>', '<p class="mathexp">')
            Format_String = Format_String.replace('</mathexp>', '</p')

            Format_String = Format_String.replace('<mathexpblock>', '<table class="mathexp"><tr><td>')
            Format_String = Format_String.replace('</mathexpblock>', '</td></tr></table><p></p>')

            Format_String = Format_String.replace('<comment>', '<span class="keyword-green">')
            Format_String = Format_String.replace('</comment>', '</span>')

            Format_String = Format_String.replace('<def>', '<span class=\'keyword-pink\'>')
            Format_String = Format_String.replace('</def>', '</span>')

            Format_String = Format_String.replace('<var>', '<span class=\'keyword-var\'>')
            Format_String = Format_String.replace('</var>', '</span>')

            return Format_String


    def PAL_90_Eligible_For_Submit_Button(self, Square_Num):
        if int(Square_Num) > 42 and int(Square_Num) not in [65,66,67,70,75,89,96,97,98]:
            return True
        else:
            return False


    # ======================
    # FLATFILE CONTENT LOADS
    # ======================

    def PAL_90_Print_Title(self, text, outFile):
        outFile.write('\n    <title>'+text+' | Pythons and Ladders</title>\n')
        outFile.write('\n')


    def PAL_90_Load_Template(self, GIVEN_PATH):

        Template_Data = []

        if not os.path.isfile(GIVEN_PATH):
            print ("ERROR: TEMPLATE FILE NOT FOUND")

        fileStream = open(GIVEN_PATH, 'r')
        allLines = fileStream.readlines()

        for line in allLines[0:]:
            line_list = line
            if line_list != ['']:
                Template_Data.append(line_list)
        fileStream.close()
        return Template_Data


    def PAL_90_Print_Template(self, Given_Data, outFile):
        for line in Given_Data:
            outFile.write(line)


    def PAL_90_Load_Content(self, tutorial_num, GIVEN_PATH):

        Content_Info = defaultdict(list)

        current_content_file = GIVEN_PATH + str(tutorial_num) + '.txt'

        fileStream = open(current_content_file, 'r')
        allLines = fileStream.readlines()

        # Create sections of content
        SECTIONS    = []
        TEMP        = []
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
            Content_Info[section[0]] = section[1:]

        # Process content to format colours of new/key terms
        for heading in Content_Info:
            current_section = Content_Info[heading]
            tempString = self.Keywords_Delimiter.join(Content_Info[heading])

            # Format special characters
            tempString = self.PAL_90_Format_Special_Characters(tempString)

            Content_Info[heading] = tempString.split(self.Keywords_Delimiter)

        fileStream.close()
        return Content_Info


    # =======================
    # MINIFY AND PRETTY PRINT
    # =======================

    def PAL_90_Load_File(self, FileType, Input_File):            

        openFile = open(Input_File, 'r')
        allLines = openFile.readlines()
        for line in allLines[0:]:
            if line not in ['', None, ['']]:
                if FileType == 'HTML':
                    self.Current_HTML_Data.append(line)
                elif FileType == 'CSS':
                    self.Current_CSS_Data.append(line)
                elif FileType == 'Variables':
                    self.Current_CSS_Variables_Data.append(line)
        openFile.close()


    def PAL_90_Print_Formatted_File(self, FileType, Output_File):

        outFile = open(Output_File, 'w')

        if FileType == 'HTML':
            Data_Source = self.Current_HTML_Data
        elif FileType == 'CSS':
            Data_Source = self.Current_CSS_Data

        for line in Data_Source:
            outFile.write(line)

        outFile.close()


    def PAL_90_Minify_HTML_File(self, Current_HTML_File):

        #----------
        # Load file
        #----------
        self.Current_HTML_Data = []
        self.PAL_90_Load_File('HTML', Current_HTML_File)

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
                # Remove newline between </head> and <body>
                self.Current_HTML_Data[self.Current_HTML_Data.index(line)] = line.strip()

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
        self.PAL_90_Print_Formatted_File('HTML', Current_HTML_File)


    def PAL_90_Minify_CSS_File(self, Current_CSS_File):

        #----------
        # Load file
        #----------
        self.Current_CSS_Data = []
        self.PAL_90_Load_File('CSS', Current_CSS_File)

        #----------------------
        # Remove all whitespace
        #----------------------
        current_index = 0
        for line in self.Current_CSS_Data:
            # Remove all leading whitespace
            self.Current_CSS_Data[current_index] = line.lstrip()
            # Remove trailing characters, but add a space to make sure characters on two separate lines never touch
            # For instance, we want to see 'red; --background-color: ' instead of 'red;--background-color: '
            self.Current_CSS_Data[current_index] = line.lstrip().rstrip() + ' '
            current_index += 1

        #-----------------------
        # Replace variable names
        #-----------------------
        if 'variables' not in Current_CSS_File:
            Variables_Data         = {}
            variables_file_path    = os.path.join(os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'RELEASE'), 'css'), 'variables.css')
            self.PAL_90_Load_File('Variables', variables_file_path)
            
            # Create a variable:value mapping dictionary
            for line in self.Current_CSS_Variables_Data:
                if line[:2] == '--' and line[:3] != '---':
                    line = line.split(':')
                    Variables_Data[line[0]] = line[1].lstrip().rstrip().replace(';', '')

            # Replace variable names
            for variable in Variables_Data:
                variable_value = Variables_Data[variable]
                current_index = 0
                for line in self.Current_CSS_Data:
                    if variable in line:
                        full_variable_name = 'var(' + variable + ')'
                        line = line.replace(full_variable_name, variable_value)
                        self.Current_CSS_Data[current_index] = line
                    current_index += 1

        #-----------
        # Print file
        #-----------
        self.PAL_90_Print_Formatted_File('CSS', Current_CSS_File)

        #----------------------------------------
        # Load and print again to delete comments
        #----------------------------------------
        self.Current_CSS_Data = []
        self.PAL_90_Load_File('CSS', Current_CSS_File)
        current_index = 0
        for line in self.Current_CSS_Data:
            # Remove all characters between /* and */
            self.Current_CSS_Data[current_index] = re.sub(r'\/\*.*?\*\/', '', line)
            # Remove all extra whitespace in file
            self.Current_CSS_Data[current_index] = re.sub(' +', ' ', self.Current_CSS_Data[current_index])
            current_index += 1
        self.PAL_90_Print_Formatted_File('CSS', Current_CSS_File)


    def PAL_90_Pretty_Print_HTML_File(self, Current_HTML_File):
        
        #----------
        # Load file
        #----------
        self.Current_HTML_Data = []
        self.PAL_90_Load_File('HTML', Current_HTML_File)

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

        # Correctly indent each line
        indent_counter  = 2
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

            for tag_pos in reversed(close_div_indexes):
                if '</div>' in line:
                    if self.Current_HTML_Data[current_index][tag_pos:tag_pos+4] != '<!--':
                        self.Current_HTML_Data[current_index] = self.Current_HTML_Data[current_index][:tag_pos] + '<!-- ' + class_list[-1] + ' -->' + self.Current_HTML_Data[current_index][tag_pos:]
                class_list = class_list[:-1]

            current_index += 1

        #-----------
        # Print file
        #-----------
        self.PAL_90_Print_Formatted_File('HTML', Current_HTML_File)


    def PAL_90_Pretty_Print_CSS_File(self, Current_CSS_File):
        #----------
        # Load file
        #----------
        self.Current_CSS_Data = []
        self.PAL_90_Load_File('CSS', Current_CSS_File)

        #--------------------------------
        # Perform Pretty Print operations
        #--------------------------------

        # Remove all extra whitespace in file
        current_index = 0
        for line in self.Current_CSS_Data:
            self.Current_CSS_Data[current_index] = re.sub(' +', ' ', self.Current_CSS_Data[current_index])
            current_index += 1

        # Left justify everything
        current_index = 0
        for line in self.Current_CSS_Data:
            self.Current_CSS_Data[current_index] = line.lstrip()
            current_index += 1

        # Tab attributes 
        current_index = 0
        for line in self.Current_CSS_Data:
            if (';' in line) and ('}' not in line):
                self.Current_CSS_Data[current_index] = '  ' + line
            current_index += 1

        #-----------
        # Print file
        #-----------
        self.PAL_90_Print_Formatted_File('CSS', Current_CSS_File.replace('.css', '_NEW.css'))



    def __del__(self):
        pass


if __name__ == '__main__':

    #------------------
    # Initialize object
    #------------------
    Utilities_Class = PAL_90_Utilities_Class()
    Utilities_Class.PAL_90_Utilities_Internal()
