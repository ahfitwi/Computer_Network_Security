#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""======================================================================"""
"""IDE used: Spyder
   Python 3.6.4 on Anaconda3"""
#============================================================================
"""
Created on Sat Jan 27 05:13:02 2018

Due Date: Friday Feb 09 23:59 2018

@author: Alem Haddush Fitwi
Email:afitwi1@binghamton.edu
Network Computer Security - EECE580F
Department of Electrical & Computer Engineering
Watson Graduate School of Engineering & Applied Science
The State University of New York @ Binghamton
"""
#============================================================================
"""
Terse Project Description:
Write a python program that does the following
1) Read in a text named "text.txt", a long book titled "War and Peace"
2) Print total number of words and sentences onto screen.
3) save the list of words along with their count & frequency as result.csv
4) print the overall number & frequency of sentences that begin with 'T/the' 
"""
#============================================================================
"""
Step_0: Laconic Description of the solution Program Organization
It comprises four classes, namely
  1) Class FileInput: handles file reading & preliminary string processing
  2) Class Words: handles word processing, counting, listing, & sorting
  3) Class Sentences: handles sentence processing, listing, and counting
  4) Class Testing: handles the calling and testing of all other classes
"""
#============================================================================
#----------------------------------------------------------------------------
"""
Step_1: Importing Required Packages or modules:
~importing re for string regular expressions handling
"""
#----------------------------------------------------------------------------
import re

#============================================================================
#----------------------------------------------------------------------------
"""
Step_2: Constructing the Class InputFile: """        
#----------------------------------------------------------------------------    
class FileInput:
    """This class does the following tasks:
        ~reads a file, named "text.txt
        ~returns a string of the whole file using the inputFile() function
        ~processes string, like case lowering, using processString() function
        """
    #------------------------------------------------------------------------
    def inputFile(self,file_path):
        """This function reads in a the text file
           Input@rgument: file_path
           Output:file_string
        """   
        self.file_path=file_path
        f_name = open(self.file_path, 'r')               
        file_string= f_name.read()                
        f_name.close()             
        return file_string         
    #------------------------------------------------------------------------
    def processString(self,string_in):
        """This function performs preliminary string operations like case
           lowering, handling apostrophes, and outputs the filtered words.
           Input@rgument: string_in
           Output:filtered_words           
        """
        self.string_in=string_in
        str_to_lower=self.string_in.lower()        
        st_re=r'([\w]+[\'|\-|\--]*[a-zA-Z]+|[\w]+)'       
        #This is the re formula according which words are extracted.        
        filtered_words= re.findall(st_re, str_to_lower, re.M)        
        return filtered_words         
#============================================================================
#----------------------------------------------------------------------------
"""
Step_3: Constructing the Class Words. 
Please  kindly note that in-depth analysis was made on the words. I formulated
the regular expression: st_re=r'([\w]+[\'|\-|\--]*[a-zA-Z]+|[\w]+)' to extract
the words exhaustively. Here are my considerations:
    ***********************************************************************
    *1. Tolstoy and Tolstoi are considered as two d/t words               *
    *2. Numbers like 1805, 7, etc are counted as words                    *
    *3. Single lettered words like I, a, etc are counted                  *
    *4. Two lettered words like an, la (French) are  counted              *
    *5. Contracted words like don't, that's, etc are handled              *
    *6. Double hyphenated words like Antichrist--I & you--sit are handled *
    *7. Single hyphenated words like well-known are handled               *
    *8. Alphanumeric words like 10--Annette are handled                   *
    ***********************************************************************
"""        
#----------------------------------------------------------------------------
class Words:
    """This class counts words, and returns total number of words, list of 
       words, and the count of each word in the created list!
    """
    #------------------------------------------------------------------------   
    def processWords(self,words_in):
        """This function computes total number of words and the count of 
           each word given in the list of the words.
           Input@rgument: words_in
           Output:word_list, word_count, total_words          
        """
        self.words_in=words_in
        word_list=self.words_in
        #list of words processed by class FileInput's processString function
        words_count={}
        #a dinctionary that will hold words as key, and counts as values
        total_words=len(words_in)
        #len computes the total number of words and is saved to total_words        
        for word in words_in:
            #Computes the total count of words             
            if word not in words_count:
                words_count[word] = 1                
            else:                
                words_count[word] += 1                  
        word_count=sorted(words_count.items(), key=lambda i: i[1],reverse=True)
        #sorts the word list in descending order based on their count  
        return word_list,word_count,total_words  
    #------------------------------------------------------------------------  
    def computeTwoWordsFreq(self,word_list,word_count):
        """ This function computes the most frequent two-word combination
            in the provided file named text.txt, and returns the results.
            Input@rgument: word_list,word_count computed by processWords()
            Output:high_freq_comb, high_freq_value   
        """
        self.word_list=word_list
        self.word_count=word_count
        high_freq_comb="" #stores the high frequency words    
        high_freq_dict={} # stores word combinations & their frequencies
        word_aggregate="" # stores aggregate of the words in word_list
        high_freq_value=0 #stores the highest frequency value        
        for word in self.word_list:
            #This foor loop aggregates the words
            word_aggregate += word
            word_aggregate +=" " #Space is used as word-split marker
        for key_1,value_1 in self.word_count:
            """These nested for loops computes the highest frequency 
               two-word combination in the given file.
            """
            for key_2,value_2 in self.word_count:  
                if ((high_freq_value>value_1) or (high_freq_value>value_2)):
                    break                    
                joint_key=key_1+" "+key_2 #stores the combined keys or words
                freq_wrd=len(re.findall(joint_key, word_aggregate, re.M))
                #computes frequency of joint_keys from words_aggregate
                if (high_freq_value<freq_wrd):
                    """updates two-word combinations, their frequencies,
                       and stores them on a dictionary, declared above!
                    """
                    high_freq_comb=joint_key
                    high_freq_value=freq_wrd 
                    high_freq_dict[joint_key] = freq_wrd           
        t={} #Temporary dictionary storage for space mgt
        t=sorted(high_freq_dict.items(), key=lambda i: i[1],reverse=True)
        #sorts the two words combination in descending order
        high_freq_dict=t #the dictionary is updated 
        return high_freq_comb, high_freq_value
    #------------------------------------------------------------------------
    def saveWordStatistics(self, word_count, total_words):
        """ This function saves the statistics of words as result.csv  
            Input@rgument: word_count tuple and total_words count
            Output:writes out statistics of words named result.csv
        """
        self.word_count=word_count
        self.total_words=total_words
        open_file = open("result.csv", "w")
        open_file.write("Word, Count, Frequency(%)\n") 
        for k,v in self.word_count: #word_count is a tuple of words & counts
            freq=(v*100.0/(self.total_words))            
            open_file.write("%s, %s, %2.7f\n" %(k,v,freq))
        open_file.close()        
        
#============================================================================
#----------------------------------------------------------------------------
"""
Step_4: Constructing the Class Sentences. 
Please note that I used the Period or full-stop, Question mark,  Exclamation 
mark, Colon, and Semicolon as markers of the end of a sentence.Here are the 
regular expressions that I formulated to extract the required sentences:
    1. sen_re = r'([\w][^\.!?:;]*[\.!?:;])'") for all sentences
    2. the_re = r'([T|t]he\b)'") for sentences that begin with 'T/the'
NB: No nested sentences! The nest is stripped off! Only the above markers are
used!                                         
""" 
#----------------------------------------------------------------------------
class Sentences: 
    """This class counts sentences, and returns total number of sentences, 
       number and frequency of sentences that start with T/the!
    """
    def processSentences(self, text):
        """This function takes the text as input, removes special characters
           in the text, and then computes total number of sentences! 
           Input@rgument: text, from class InputFile
           Output:sentences,total_sen         
        """
        self.text=text
        buffer_strg=self.text.replace('"' , "")
        buffer_strg=buffer_strg.replace('\r' , "")
        buffer_strg=buffer_strg.replace('\n' , " ") 
        #The above 3 statements remove the special characters specified         
        sen_re = r'([\w][^\.!?:;]*[\.!?:;])'
        """This regular expression is defined to extract the list of sentences
        ending with Period, exclamation & question marks, colon, & semicoln"""
        sentences= re.findall(sen_re, buffer_strg, re.M)  
        #sentences is a list that contains all the extracted sentences
        total_sen=len(sentences)  # stores the count of sentences
        return sentences,total_sen
    #------------------------------------------------------------------------
    def filterTheSen(self,sentences):
        """This function handles sentences that start with "T/the", and 
           computes their total number and overall frequency.
           Input@rgument: sentences from processSentences()
           Output:sen_cnt,the_cnt,the_sen         
        """        
        self.sentences=sentences        
        the_cnt={} # a dictionary to hold the_sentences and their counts
        sen_cnt={} # a dictionary to hold any unique sentences       
        the_re = r'([T|t]he\b)' # filters sentences that begin with 'T/the'
        the_sen=0 # variable to hold the list of the_sentences
        for sentence in self.sentences:
            """This for loop computes the list the_sentences, each sentence's
               count, total count, and the unique sentences in the whole text
            """
            if sentence not in sen_cnt:
                sen_cnt[sentence] = 1            
            else:
                sen_cnt[sentence] += 1            
            isMatch=re.match(the_re, sentence, re.M) #filters matches
            if isMatch:
                the_sen+=1
                if sentence not in the_cnt:  
                    the_cnt[sentence] = 1
                else:
                    the_cnt[sentence] += 1        
        sen_cnt=sorted(sen_cnt.items(), key=lambda d: d[1],reverse=True)
        # A lambda function that sorts unique sentences dict by count
        the_cnt=sorted(the_cnt.items(), key=lambda d: d[1],reverse=True)
        # A lambda function that sorts unique the_sentences dict by count
        return sen_cnt,the_cnt,the_sen
    #------------------------------------------------------------------------   
    
#============================================================================
#----------------------------------------------------------------------------
class Test:
    """This class calls all other classes, execute them, prints out all
       desired outputs onto the screen, and saves words as result.csv
    """
    class_input_object_1=FileInput() # Instantiating Class FileInput
    class_input_object_2=FileInput()
    temp_str=class_input_object_1.inputFile("text.txt")
    filtered_words=class_input_object_2.processString(temp_str)
    C_W_1=Words() # creating instantiates of Class Words
    C_W_2=Words()
    C_W_3=Words()
    (word_list,word_count,total_words)=C_W_1.processWords(filtered_words)    
    (two_words, counts)=C_W_2.computeTwoWordsFreq(word_list,word_count)    
    result_csv=C_W_2.saveWordStatistics(word_count, total_words) 
    print("-------------------****************-------------------------")
    print("Statistics of words in the given text, 'War and Peace:'")    
    print("************************************************************")
    print("Here comes the words' statistics")
    print("      1. Total number of words = %s" %(total_words))
    print("      2. Number of Distinct words = %s" %(len(word_count)))
    print("      3. Most frequent two-word combination = \'%s\'" %(two_words))
    print("         and its count = %s" %(counts))
    print("      NB: Detailed list of words is saved in result.csv")     
    print("-------------------****************-------------------------")   
    #------------------------------------------------
    sen_obj_1=Sentences() # creating instantiates of Class Sentences
    sen_obj_2=Sentences()
    (sen_string,total_sen)=sen_obj_1.processSentences(temp_str)    
    (distinct_sen, distict_the,count_the)=sen_obj_2.filterTheSen(sen_string)    
    print("Statistics of sentences in the given text, 'War and Peace:'")      
    print("************************************************************")
    print("Here comes the sentences' statistics")
    print("1. Total number of sentences = %s" %(total_sen))
    print("2. # of Distinct sentences = %s" %(len(distinct_sen)))
    print("3. # of sentences that start with 'T/the' = %s" %(count_the))
    print("     and their frequency = %2.3f" %(count_the*100.0/total_sen)+"%")
    print("4. # of Distinct T/the_sentences = %s" %(len(distict_the)))
    print("************************************************************")
    print("---------------End of Program!------------------------------")   
#============================================================================
"""                          End of Program!                               """
#----------------------------------------------------------------------------
