# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:13:05 2020

@author: Chris
"""
#function to read from file
def mutate():
    #reads from the main file and from the normal one
    File_normal = open("DNAFile.txt","r")
    File_normal_fixed = open("normalDNA.txt","w")
    #adds the main file to a string
    end = File_normal.read().replace("\n", "")
    for x in range(len(end)):
        #checks through the whole string and a is replaced with A
        if end[x] == "a":
            File_normal_fixed.writelines("A")
        else: 
            File_normal_fixed.writelines(end[x])
            
    #reads from the main file and from the normal one
    File_mutate = open("DNAFile.txt","r")
    File_mutate_fixed = open("mutatedDNA.txt","w")
    #adds the main file to a string
    end = File_mutate.read().replace("\n", "")
    for x in range(len(end)):
        #checks through the whole string and a is replaced with A
        if end[x] == "a":
            File_mutate_fixed.writelines("T")
        else: 
            File_mutate_fixed.writelines(end[x])
            
    #closes all the files
    File_normal.close()
    File_normal_fixed.close()
    File_mutate.close()
    File_mutate_fixed.close()

#reads everything from file and returns it
def readFromFile(file):
    File_object = open(file,"r")
    return File_object.read().replace("\n", "")

tfile = "DNAFile.txt"
#taking the DNA sequence from the .txt file and adding it to a string
DNAfirst = readFromFile(tfile)

#function to create a protein from the DNA sequence
def translate(DNA):
    #dictionary containing only the first 5 aminos as stated in the question
    aminoacids = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I',
        'ATG':'M',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'TTC':'F', 'TTT':'F', 
        'TTA':'L', 'TTG':'L', 
    } 
    
    aminosequence ="" 
    #runs through the DNA sequence taking strings of 3 in length
    for x in range(0, len(DNAfirst), 3): 
        #finds the 3 length codon
        codon = DNAfirst[x:x + 3] 
        #tests if the codon is in the table
        if codon in aminoacids:
            #adds the amino
            aminosequence += aminoacids[codon]
        else:
            #adds an X because it doesn't contain an amino
            aminosequence += "X"
    return aminosequence

def txtTranslate():
    mutate()
    #adds the contents of the text files to the variables "mut" and "nor"
    mut = readFromFile("mutatedDNA.txt")
    nor = readFromFile("normalDNA.txt")
    #turns them into protein strings
    mutend = translate(mut)
    norend = translate(nor)
    #prints out the finished products
    print("MutatedDNA output : " + "\n"+ mutend + "\n" + "NormalDNA output : "+ "\n" + norend)

#runs the translation
txtTranslate()