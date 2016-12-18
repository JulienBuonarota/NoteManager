from types import *
import re

class WordList(object):
    """Key words usable for the redaction of notes"""
    def __init__(self):
        self.Woli = InstanceWord

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
    def __init__(self, re, verb):
        self.d = {"Re":re, "Verb":verb}
        
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
    
Chapitre = Word('\\*', True)
Theoreme = Word('Th', True)
SousChapitre = Word('(\\*\\*)', False)
Proposition = Word('Prop|Proposition', False)
Note = Word('Note', False)
Corollaire = Word('Cor', False)
Retour = Word('\\n', False)
Page = Word('#', False)
Definition = Word('Def', True)

InstanceWord = [Chapitre, Theoreme, SousChapitre, Proposition,
                Note, Corollaire, Retour, Page, Definition]




