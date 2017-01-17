import sys
import re
import os
from os.path import join
import WordObject as Wo
import MainFunctions as Mf


help_bool = True

#Oject with the file display methods and key words
CourseList = Wo.WordList(Wo.ListCour)
CourseList.Compile()


Path= "/home/julien/Documents/Fac/Licence_math/Organisation/Cours"
CoursePath = Mf.FileList(Path)
print CoursePath
"""
CourseName = "Topologie"
Path = join(PathBase, "CourseName" + ".txt")
"""
Soft = True
while Soft:
    if help_bool:
        print Mf.help_string
    
    s = raw_input('-->')
    s = s.split(" ")
    
    if re.match("[Hh]elp|[Hh]", s[0]):
        help_bool = eval(s[1])
    elif re.match("[Ss]et[Vv]erbose|SV", s[0]):
        CourseList.SetVerbose(s[1], eval(s[2]))
    elif re.match("[Ss]et[Pp]ath|SP", s[0]):
        Path = s[1]
    elif re.match("[Dd]isplay", s[0]):
        CourseList.Display(Path)
    elif re.match("[Qq](uit)?", s[0]):
        Soft = False
        continue
    elif re.match("[Ww]ords|W", s[0]):
        print CourseList
    elif re.match("[Dd]isplay[Ll]ast|DL", s[0]):
        CourseList.DisplayLast(Path)
    elif re.match("[Dd]isplay[Aa]ll[Ll]ast|DAL", s[0]):
        print "features to come"
    elif re.match("[Ss]earch|[Ss]", s[0]):
        CourseList.Search(Path, s[1])
