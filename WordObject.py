from types import *
import re
from termcolor import colored

class WordList(object):
    """Key words usable for the redaction of notes"""
    def __init__(self, List):
        self.d = {}
        for i in List:
            tmp = {"Word":i, "Verbose":False}
            self.d.update({i.__name__():tmp})
        
        
    def __repr__(self):
        return str(self.l)

    def SetVerbose(self, name, verbose):
        for i in self.d.iterkeys():
                if i == name:
                    self.d[i]["Verbose"] = verbose
                    break
                
    def Compile(self):
        for i in self.d.itervalues():
            i["Word"].Compile()
        
    def Display(self, file):
        with open(file, 'r') as Course:
            s = ""
            for i in Course:
                for j in self.d.itervalues():
                    if j["Verbose"] and j["Word"].Test(i):
                        s = s + j["Word"].Display(i)
                        break
            print s

class Word(object):
    Indent = ""
    Column = 0
    def __init__(self, re, name, List):
        self.Re = re
        self.Name = name
        List.append(self)

    def __name__(self):
        return self.Name
    
    def __repr__(self):
        return "re : ", self.Re, " Name : ", self.name
        
    def __str__(self):
        return "re : ", self.Re, " Name : ", self.name

    def Display(self, ligne):
        #default display
        return ligne
    
    def Compile(self):
        if type(self.Re) == StringType:
            self.Re = re.compile(self.Re)
        else:
            pass
        
    def Test(self, ligne):
        if self.Re.match(ligne):
            return True
        else:
            return False


    
#Specification of display for each individual words defined
ListCour = []
Chapitre = Word('\\* ', "Chapitre", ListCour)
def f(self, ligne):
    Word.Indent = " "
    ligne = ligne.replace('*', "", 1)
    ligne = ligne.replace(' ', "", 1)
    ligne = ligne.upper()
    ligne = Word.Indent + ligne
    Word.Indent = "  "
    return ligne
Chapitre.Display = MethodType(f, Chapitre)

SousChapitre = Word('\\*\\* ', "SousChapitre", ListCour)
def f(self, ligne):
    Word.Indent = "  "
    ligne = ligne.replace('*', '', 2)
    ligne = ligne.replace(' ', "", 1)
    ligne = ligne.upper()
    ligne = Word.Indent + ligne
    Word.Indent = "   "
    return ligne
SousChapitre.Display = MethodType(f, SousChapitre)

Theoreme = Word('Th ', "Theoreme", ListCour)
def f(self, ligne):
    ligne = re.sub(self.Re, "", ligne)
    Th = colored("Th  ", 'cyan')
    ligne = Word.Indent + Th + ligne
    return ligne
Theoreme.Display = MethodType(f, Theoreme)

Definition = Word('Def ', "Definition", ListCour)
def f(self, ligne):
    ligne = re.sub(self.Re, "", ligne)
    Def = colored("Def ", 'red')
    ligne = Word.Indent + Def + ligne
    return ligne
Definition.Display = MethodType(f, Definition)

Proposition = Word('Prop|Proposition', "Proposition", ListCour)
Note = Word('Note', "Note", ListCour)
Corollaire = Word('Cor', "Corollaire", ListCour)
Retour = Word('\\n', "Retour", ListCour)
Page = Word('#', "Page", ListCour)

