import sys
from WordObject import *

WL = WordList(ListCour)
WL.Compile()
WL.SetVerbose("Definition", True)
WL.SetVerbose("Theoreme", True)
WL.SetVerbose("Chapitre", True)
WL.SetVerbose("SousChapitre", True)
WL.SetVerbose("Date", True)
cour = "../Cours/Topologie.txt"
cour2 = "../Cours/Test.txt"
#WL.Display(cour)
print "----------"
#WL.DisplayDate(cour, "29/09/2016")
#WL.DisplayLast(cour)
WL.Search(cour, "Boule")
