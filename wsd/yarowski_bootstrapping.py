# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 04:28:34 2015

@author: bertz
"""

#function for identification of all instances of the keyword
#in given file, output written to file

def getKwic(keyword, offset, in_filename, out_filename): #Key Word In Context
    #open files for inpurt/output, fhnd[0] - in, fhnd[1 ]- out
    fhnd = open_files(in_filename, out_filename)
        
    #anchors, depend on dataset format
    rev_start = "review/text: "
    rev_props = "review" #additional review data marker
    prod_props = "product" #product properties
    
    #files are ready, getting instances of keyword and it's contexts
    review_id = 0 #for one-sense-per-discourse assumption, just unique number
    tmp_line = "" #line for storing review text
    rev_found = None #boolean flage to indicate review text reading
    count = 0 #kwic lines count
    
    #processing input file
    for line in fhnd[0]:
        if line.startswith(rev_start) :
            review_id = review_id + 1 #update id, we've got new review to do
            #get entire review to a single line
            tmp_line = line[len(rev_start):] #line with rev_start anchor
            rev_found = True #now reading lines from review text
            continue #nothing more to do on this iteration
            
        if rev_found: #now processing review text            
            #review text comes to an end eventually
            if line.startswith(rev_props) or line.startswith(prod_props):
                rev_found = False #not a line from review text, write results
                #strip line from whitespaces at both ends
                tmp_line = tmp_line.strip()        
                #process line
                word_list = tmp_line.split() #line to list
                inds = [i for i, x in enumerate(word_list) if x == keyword] #indices of all keyword occurences
                for val in inds:
                    if val > (offset - 1) and val < (len(word_list) - offset): #if have enough words on both ends
                        seq = word_list[val-offset : val+(offset+1)] #list range to sequence
                        seq = [word + "\t" for word in seq] #add tabs to each word in sequence
                        kwic = "".join(seq) #sequence to string
                        fhnd[1].write("sense: unknown\t" + kwic + "\n") #write an entry to concordance
                        count = count + 1
     
                #clear tmp_line
                tmp_line = ""
                
            #if still reading review text    
            tmp_line = tmp_line + line #reading next line from review text

    print "%d kwic's so far" % count
        
    return 0

#collocation checks    
#literal:
def open_files(in_filename, out_filename):
    #open input file    
    try:
        in_fhnd = open(in_filename) #read     
    except:
        print "File %s cannot be opened for reading" % out_filename
        exit()
        
    #trying to open new file for writing results
    try:
        out_fhnd = open(out_filename, 'w') #write        
    except:
        print "File %s cannot be opened for writing" % out_filename
        exit()
        
    return (in_fhnd, out_fhnd)
    
def get_clc(keyword, in_fhnd, out_fhnd, begin, end):
    count = 0   
    for line in in_fhnd:
        #strip line from whitespaces at both ends
        line = line.strip()
        #line to list
        word_list = line.split()
        inds = [i for i, x in enumerate(word_list) if x == keyword] #indices of all keyword occurences
        for val in inds:
            seq = word_list[val+begin : val+end] #list range to sequence
            seq = [word + "\t" for word in seq] #add spaces to each word in sequence
                                                #to split by them later
            clc = "".join(seq) #sequence to string
            out_fhnd.write(str(count) + ": " + clc + "\n") #write an entry to concordance
            count = count + 1
    return 0

def getRightBigrams(keyword, in_filename, out_filename):   
    #open files for inpurt/output, fhnd[0] - in, fhnd[1 ]- out
    fhnd = open_files(in_filename, out_filename)
    
    #get right bigram collocations, offset: from keyword+0 to keyword+2
    get_clc(keyword, fhnd[0], fhnd[1], 0, 2)    

    return 0
        
def getLeftBigrams(keyword, in_filename, out_filename):
    #open files for inpurt/output, fhnd[0] - in, fhnd[1 ]- out
    fhnd = open_files(in_filename, out_filename)
    
    #get left bigram collocations, offset: from keyword-1 to keyword+1
    get_clc(keyword, fhnd[0], fhnd[1], -1, 1)  
    return 0
    
def getLeftTrigrams(keyword, in_filename, out_filename):
    #open files for inpurt/output, fhnd[0] - in, fhnd[1 ]- out
    fhnd = open_files(in_filename, out_filename)
    
    #get left trigram collocations, offset: from keyword-2 to keyword+1
    get_clc(keyword, fhnd[0], fhnd[1], -2, 1)  
    return 0
    
def getCenterTrigrams(keyword, in_filename, out_filename):
    #open files for inpurt/output, fhnd[0] - in, fhnd[1 ]- out
    fhnd = open_files(in_filename, out_filename)
    
    #get center trigram collocations, offset: from keyword-1 to keyword+2
    get_clc(keyword, fhnd[0], fhnd[1], -1, 2)  
    return 0
    
def getRightTrigrams(keyword, in_filename, out_filename):
    #open files for inpurt/output, fhnd[0] - in, fhnd[1 ]- out
    fhnd = open_files(in_filename, out_filename)
    
    #get rigth trigram collocations, offset: from keyword+0 to keyword+3
    get_clc(keyword, fhnd[0], fhnd[1], 0, 3)  
    return 0
    
#class-based: POS within the window
def adjInWindow():
    return 0   
    
def verbInWindow():
    return 0 
    
#process collocation file to get most frequent collocations
def getFreqClc(in_filename, out_filename, amount):    
     #open files for inpurt/output, fhnd[0] - in, fhnd[1 ]- out
    fhnd = open_files(in_filename, out_filename)
    
    import collections, re    
    list = [line.split(':')[1].strip()  for line in fhnd[0]]
    
    counter = collections.Counter(list)
    out =  counter.most_common(amount)   
    for item in out:
        print item
        clc_str = re.search("'.+'", str(item)).group()
        clc_freq = re.search("(\d+)\)", str(item)).group().strip(')')
        clc_str = clc_str.strip("'")
        word_list = re.split(r'\\t', clc_str)
        seq = word_list[:]
        
        seq = [word + "\t" for word in word_list]
        clc = "".join(seq) #sequence to string
        fhnd[1].write(clc + clc_freq +  "\n")
        
    return 0
    
#part-of-speech tagging
def getPosTag(in_filename, out_filename):    
     #open files for inpurt/output, fhnd[0] - in, fhnd[1 ]- out
    fhnd = open_files(in_filename, out_filename)
    
    tagged_line = ""
    
    from pattern.en import parse
    
    for line in fhnd[0]:
        word_list = line.split() #line to list
        for word in word_list:
            tagged_line += " " + parse(word, Relations = False, lemmata = False)
        
        fhnd[1].write(tagged_line + "\n")
        tagged_line = ""
        
        
      
    return 0
    
def getRightBigramsPOS(keyword, in_filename, out_filename, POS_a, POS_b):   
    #open files for inpurt/output, fhnd[0] - in, fhnd[1 ]- out
    fhnd = open_files(in_filename, out_filename)
    
    #get right bigram collocations, offset: from keyword+0 to keyword+2
    get_clcPOS(keyword, fhnd[0], fhnd[1], 0, 2, POS_a, POS_b)    

    return 0
    
def getLeftTrigramsPOS(keyword, in_filename, out_filename, POS_a, POS_b):
    #open files for inpurt/output, fhnd[0] - in, fhnd[1 ]- out
    fhnd = open_files(in_filename, out_filename)
    
    #get left trigram collocations, offset: from keyword-2 to keyword+1
    get_clcPOS(keyword, fhnd[0], fhnd[1], -2, 1, POS_a, POS_b)  
    return 0
    
def getCenterTrigramsPOS(keyword, in_filename, out_filename, POS_a, POS_b):
    #open files for inpurt/output, fhnd[0] - in, fhnd[1 ]- out
    fhnd = open_files(in_filename, out_filename)
    
    #get center trigram collocations, offset: from keyword-1 to keyword+2
    get_clcPOS(keyword, fhnd[0], fhnd[1], -1, 2, POS_a, POS_b)  
    return 0
    
def get_clcPOS(keyword, in_fhnd, out_fhnd, begin, end, POS_a, POS_b):
    count = 0   
    for line in in_fhnd:
        #strip line from whitespaces at both ends
        line = line.strip()
        #line to list
        word_list = line.split()
        inds = [i for i, x in enumerate(word_list) if x == keyword] #indices of all keyword occurences
        for val in inds:
            seq = word_list[val+begin : val+end] #list range to sequence
            seq = [word + "\t" for word in seq if POS_a in word or POS_b in word] #add spaces to each word in sequence
                                               #to split by them later
            if len(seq) == (abs(end - begin)): 
                clc = "".join(seq) #sequence to string
                out_fhnd.write(str(count) + ": " + clc + "\n") #write an entry to concordance
                count = count + 1
    return 0
    
#function calls
    
#process keywords
getKwic("game", 5, "./Data/Video_Games.txt", "./Results/kwic.txt")
getPosTag("./Results/kwic.txt", "./Results/kwic_tag.txt")

#extract collocations
getRightBigrams("game", "./Results/kwic.txt", "./Results/r_bgr.txt")
getFreqClc("./Results/r_bgr.txt", "./Results/freq_r_bgr.txt", 5)
getLeftBigrams("game", "./Results/kwic.txt", "./Results/l_bgr.txt")
getFreqClc("./Results/l_bgr.txt", "./Results/freq_l_bgr.txt", 5)
getLeftTrigrams("game", "./Results/kwic.txt", "./Results/l_tgr.txt")
getFreqClc("./Results/l_tgr.txt", "./Results/freq_l_tgr.txt", 5)
getCenterTrigrams("game", "./Results/kwic.txt", "./Results/c_tgr.txt")
getFreqClc("./Results/c_tgr.txt", "./Results/freq_c_tgr.txt", 5)
getRightTrigrams("game", "./Results/kwic.txt", "./Results/r_tgr.txt")
getFreqClc("./Results/r_tgr.txt", "./Results/freq_r_tgr.txt", 5)

#extract pos-tagged collocations
getRightBigramsPOS("game/NN/B-NP/O", "./Results/kwic_tag.txt", "./Results/r_bgr_pos.txt", "JJ", "NN")
getFreqClc("./Results/r_bgr_pos.txt", "./Results/freq_r_bgr_pos.txt", 5)

getLeftTrigramsPOS("game/NN/B-NP/O", "./Results/kwic_tag.txt", "./Results/l_tgr_pos.txt", "JJ", "NN")
getFreqClc("./Results/l_tgr_pos.txt", "./Results/freq_l_tgr_pos.txt", 5)

getCenterTrigramsPOS("game/NN/B-NP/O", "./Results/kwic_tag.txt", "./Results/c_tgr_pos.txt", "JJ", "NN")
getFreqClc("./Results/c_tgr_pos.txt", "./Results/freq_c_tgr_pos.txt", 5)