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
        return str(self.d)

    def __str__(self):
        s = ""
        for i in self.d.iteritems():
            tmp = "{:13} : {:2}".format(i[0], i[1]["Verbose"])
            s = s + tmp + "\n"
        return s

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
            for line in Course:
                for i in self.d.itervalues():
                    if i["Verbose"] and i["Word"].Test(line):
                        s = s + i["Word"].Display(line)
                        break
            print s

    def NbPages(self, file):
        with open(file, 'r') as Course:
            nb = 0
            for line in Course:
                if self.d["Page"]["Word"].Test(line):
                    nb = nb + 1
        return nb

    def DisplayDate(self, file, date):
        with open(file, 'r') as Course:
            s = ""
            tmp = False
            for line in Course:
                if self.d["Date"]["Word"].Test(line):
                    if line == (date + "\n"):
                        tmp = True
                    else:
                        tmp = False
                if tmp:
                    for i in self.d.itervalues():
                        if i["Verbose"] and i["Word"].Test(line):
                            s = s + i["Word"].Display(line)
                            break
            print s   

    def DisplayLast(self, file):
        """
        Display the last entry of the file vis-a-vis to the dates of the entries
        """
        with open(file, 'r') as Course:
            tmp = []
            for line in Course:
                if self.d["Date"]["Word"].Test(line):
                    tmp.append(line)
        #sorting the dates
        tmp = [[re.sub("\n", "", j) for j in re.split("[ \/]", i)] for i in tmp]
        top = tmp[0]
        for i in tmp[1:]:
            b1 = i[2] >= top[2]
            b2 = i[1] >= top[1]
            b3 = i[0] > top[0]
            if b1 and b2 and b3:
                top = i
        date = top[0] + "/" + top[1] + "/" + top[2]
        self.DisplayDate(file, date)

    def Search(self, file, var):
        """
        Basic search for first occurence of var in file
        """
        with open(file, 'r') as Course:
            tmpDate = ""
            tmpChapter = ""
            tmp = ""
            for line in Course:
                if self.d["Date"]["Word"].Test(line):
                    tmpDate = line
                    continue
                elif self.d["Chapitre"]["Word"].Test(line):
                    tmpChapter = line
                    continue

                #removing beginning key word from line
                line = line.split(" ")
                line.pop(0)
                if len(line) == 0:
                    continue
                s = line[0]
                for i in line[1:]:
                    s = s + " " + i

                #match
                line = s
                if re.match(var, line):
                    tmp = line
                    break
            print tmpDate + tmpChapter + tmp
                        
class Word(object):
    Indent = ""
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
        
    def Test(self, line):
        if self.Re.match(line):
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
Date = Word("[0-9]{1,2}[/ ]([0-9]{1,2}|[A-Za-z]{3,8})[/ ][0-9]{2,4}", "Date", ListCour)
