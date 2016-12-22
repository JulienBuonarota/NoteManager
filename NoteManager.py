import sys
from WordObject import *

WL = WordList(ListCour)
WL.Compile()
WL.SetVerbose("Definition", True)
WL.SetVerbose("Chapitre", True)
WL.SetVerbose("SousChapitre", True)
WL.Display("../Cours/Topologie.txt")

