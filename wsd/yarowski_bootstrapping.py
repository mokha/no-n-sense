# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 04:28:34 2015

@author: bertz
"""

#function for identification of all instances of the keyword
#in given file, output written to file

def getKwic(keyword, offset, in_filename, out_filename): #Key Word In Context
#open input file
    try:
        in_fhnd = open(in_filename)
    except:
        print "File %s cannot be opened" % in_filename
        exit()
        
    #file was opened successfully 
    #trying to open new file for writing results
    try:
        out_fhnd = open(out_filename, 'w') #I've said write        
    except:
        print "File %s cannot be opened for writing" % out_filename
        exit()
        
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
    for line in in_fhnd:
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
                        out_fhnd.write(str(review_id) + ": " + kwic + "\n") #write an entry to concordance
                        count = count + 1
     
                #clear tmp_line
                tmp_line = ""
                
            #if still reading review text    
            tmp_line = tmp_line + line #reading next line from review text

    print "%d kwic's so far" % count
        
    return 0

getKwic("game", 5, "./Data/Video_Games.txt", "./Results/kwic.txt")