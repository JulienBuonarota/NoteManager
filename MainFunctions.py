import os
import re

#Path = "/home/julien/Documents/Fac/Licence_math/Organisation/Cours"
class FileList(object):
    def __init__(self, path):
        self.root = path
        self.l = tuple(os.walk(path))[0][2]
    def __str__(self):
        s = ""
        for i in self.l:
            s += re.sub(".txt", "", i) + "\n"
        return s
    
    def __iter(self):
        for i in self.l:
            yield i

#Help command display string
help_string = "Commands : \n"
help_string += "{:12} : {}\n".format("Help", "bool")
help_string += "{:12} : {}\n".format("SetVerbose", "Word, bool")
help_string += "{:12} : {}\n".format("SetPath", "Path")
help_string += "{:12} : {}\n".format("Search", "string")
help_string += "{:12}\n".format("Display")
help_string += "{:12}\n".format("Quit")
help_string += "{:12}\n".format("Words")

