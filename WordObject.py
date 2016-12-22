from types import *
import re
from termcolor import colored

class WordList(object):
    """Key words usable for the redaction of notes"""
    def __init__(self):
        self.Woli = Word.List

    def __repr__(self):
        return str(self.Woli)
                
    def Compile(self):
        for i in self.Woli:
            i.Compile()
        
    def Display(self, file):
        with open(file, 'r') as Course:
            s = ""
            for i in Course:
                a, b = self.Test(i)
                if a:
                    s = s + b.Display(i)
            print s

    def Test(self, ligne):
        for i in self.Woli:
            if i.Test(ligne):
                return [True, i]
            else:
                pass
        return [False, 0]


class Word(object):
    List = []
    Indent = ""
    Column = 0
    def __init__(self, re, verb):
        self.d = {"Re":re, "Verb":verb}
        Word.List.append(self)
        
    def __getitem__(self, key):
        return self.d[key]
    
    def __setitem__(self, key, value):
        self.d[key] = value

    def __repr__(self):
        return str(self.d)
        
    def __str__(self):
        return str(self.d)

    def Display(self, ligne):
        #default display
        return ligne
    
    def Compile(self):
        if type(self.d["Re"]) == StringType:
            self.d["Re"] = re.compile(self.d["Re"])
        else:
            pass
        
    def Test(self, ligne):
        if self.d["Verb"] and self.d["Re"].match(ligne):
            return True
        else:
            pass
        return False

    
#Specification of display for each individual words defined

Chapitre = Word('\\* ', True)
def f(self, ligne):
    Word.Indent = " "
    ligne = ligne.replace('*', "", 1)
    ligne = ligne.replace(' ', "", 1)
    ligne = ligne.upper()
    ligne = Word.Indent + ligne
    Word.Indent = "  "
    return ligne
Chapitre.Display = MethodType(f, Chapitre)

SousChapitre = Word('\\*\\* ', True)
def f(self, ligne):
    Word.Indent = "  "
    ligne = ligne.replace('*', '', 2)
    ligne = ligne.replace(' ', "", 1)
    ligne = ligne.upper()
    ligne = Word.Indent + ligne
    Word.Indent = "   "
    return ligne
SousChapitre.Display = MethodType(f, SousChapitre)

Theoreme = Word('Th ', True)
def f(self, ligne):
    ligne = re.sub(self.d["Re"], "", ligne)
    Th = colored("Th  ", 'cyan')
    ligne = Word.Indent + Th + ligne
    return ligne
Theoreme.Display = MethodType(f, Theoreme)

Definition = Word('Def ', True)
def f(self, ligne):
    ligne = re.sub(self.d["Re"], "", ligne)
    Def = colored("Def ", 'red')
    ligne = Word.Indent + Def + ligne
    return ligne
Definition.Display = MethodType(f, Definition)

Proposition = Word('Prop|Proposition', False)
Note = Word('Note', False)
Corollaire = Word('Cor', False)
Retour = Word('\\n', False)
Page = Word('#', False)

