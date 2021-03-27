import json

from unidecode import unidecode

### PUT SOURCE FILE PATH HERE
SOURCE_PATH = ""
###

class TextFile():
    """class with words loaded from specified, prepared file. 
    Works similarly to list. Aimed to be read-only"""

    def __init__(self, path = "", normalizeChars = False):
        """import words from wordfile in path.
        Object made without path given will be empty"""

        self._file_lines = []
        self._converted_dict = {}
        self.normalize = normalizeChars
        
        if len(path):
            self._import_file(path)
            self._convert_to_dict()
    
    def _import_file(self, path=""):
        """import given textfile. Clears existing import."""
        self.clear()

        try:
            with open(path) as import_file:
                self._file_lines = import_file.read().splitlines()
        except FileNotFoundError:
            print("ERROR: file not found, sorry!")
            raise SystemExit()

    def _convert_to_dict(self):
        """converting imported file lines into python dictionary."""

        is_in_converting_block = False
        current_key = ""
        value_index = 0

        for line in self._file_lines:
            # main loop for converting text to dictionary
            if line[0] == "{":
                is_in_converting_block = True
                continue # go to next line to start converting
            if line[0] == "}":
                is_in_converting_block = False
                break # end sign occured, stop converting
            
            if is_in_converting_block:
                if line[0] == "#":
                    value_index = 0
                    current_key = line[1:].strip() # save the key without "#" char
                    continue # got the key, start doing the values
                else:
                    pushed_value = unidecode(line.strip()) if self.normalize else line.strip()
                    
                    if value_index == 0:
                        # it's the first value for that key
                        self._converted_dict[current_key] = pushed_value
                    if value_index == 1:
                        # it's the second value -> convert string to list and append new value
                        self._converted_dict[current_key] = [self._converted_dict[current_key]]
                        self._converted_dict[current_key].append(pushed_value)
                    if value_index > 1:
                        # it's the third+ value -> just append to list 
                        self._converted_dict[current_key].append(pushed_value)
                    value_index += 1
    
    def dump_json(self, json_path):
        with open(json_path, "w") as json_output:
            json.dump(self._converted_dict, json_output, indent=4)

    def clear(self):
        """clears/resets the container"""
        self._file_lines.clear()
    
##########

if (SOURCE_PATH == ""):
    print("no path given!")
    raise SystemExit

text = TextFile(path=SOURCE_PATH)
text.dump_json(json_path=str(SOURCE_PATH + ".json"))
print("ok")
