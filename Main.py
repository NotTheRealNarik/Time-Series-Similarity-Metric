
# coding: utf-8

# In[2]:


import string
import numpy as np
import igraph
import pandas as pd
import csv
import random
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import distance #for lev, hamming , jaccard

#import sys
#np.set_printoptions(threshold=sys.maxsize)

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[66]:


order1 = ["A", "R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"] #RANDOM SAMPLE ORDERING
order2 = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"] #Alphabetical SAMPLE ORDERING, USE YOUR OWN
order3 = ["V", "Y", "T", "W", "P", "E", "C", "G", "R", "L", "I", "N", "M", "S", "H", "F", "K", "D", "Q", "A"] #RANDOM SAMPLE ORDERING

order1_groEL = ["a", "r", "n", "d", "c", "e", "q", "g", "h", "i", "l", "k", "m", "f", "p", "s", "t", "w", "y", "v","x"] #Random sample
order2_groEL = ["a", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y"] #Alphabetical SAMPLE ORDERING
order3_groEL = ["v", "y", "t", "w", "p", "e", "c", "g","x", "r", "l", "i", "n", "m", "s", "h", "f", "k", "d", "q", "a"] #RANDOM SAMPLE ORDERING


# In[67]:


vals1= {' ':0} #assign an incremement or decrement to each alphabet letter
id1=-((len(order1)+1)/2)
vals2= {' ':0} #assign an incremement or decrement to each alphabet letter
id2=-((len(order2)+1)/2)
vals3= {' ':0} #assign an incremement or decrement to each alphabet letter
id3=-((len(order3)+1)/2)

vals1_groEL= {' ':0} #assign an incremement or decrement to each alphabet letter
id1_groEL=-((len(order1_groEL)+1)/2)
vals2_groEL= {' ':0} #assign an incremement or decrement to each alphabet letter
id2_groEL=-((len(order2_groEL)+1)/2)
vals3_groEL= {' ':0} #assign an incremement or decrement to each alphabet letter
id3_groEL=-((len(order3_groEL)+1)/2)

vals1


# In[141]:


# Order 1 Values
for i in order1:    
    if id1 == 0:
        #print ("entered this loop")
        vals1[" "]=id1
        id1+=1
        #print("exiting")
    vals1[i]=id1
    #print (id1)
    id1+=1  
#print (vals1)

    
# Order 2 Values
for i in order2:    
    if id2 == 0:
        #print ("entered this loop")
        vals2[" "]=id2
        id2+=1
        #print("exiting")
    vals2[i]=id2
    #print (id2)
    id2+=1   
#print (vals2)

# Order 3 Values
for i in order3:    
    if id3 == 0:
        #print ("entered this loop")
        vals3[" "]=id3
        id3+=1
        #print("exiting")
    vals3[i]=id3
    #print (id3)
    id3+=1   
#print (vals3)


# In[144]:


# Order 1 Values
for i in order1_groEL:    
    if id1_groEL == 0:
        #print ("entered this loop")
        vals1_groEL[" "]=id1_groEL
        id1_groEL+=1
        #print("exiting")
    vals1_groEL[i]=id1_groEL
    #print (id1_groEL)
    id1_groEL+=1  
#print (vals1_groEL)

    
# Order 2 Values
for i in order2_groEL:    
    if id2_groEL == 0:
        #print ("entered this loop")
        vals2_groEL[" "]=id2_groEL
        id2_groEL+=1
        #print("exiting")
    vals2_groEL[i]=id2_groEL
    #print (id2_groEL)
    id2_groEL+=1   
#print (vals2_groEL)

# Order 3 Values
for i in order3_groEL:    
    if id3_groEL == 0:
        #print ("entered this loop")
        vals3_groEL[" "]=id3_groEL
        id3_groEL+=1
        #print("exiting")
    vals3_groEL[i]=id3_groEL
    #print (id3_groEL)
    id3_groEL+=1   
#print (vals3_groEL)


# In[145]:



#Dump code to declare row

start=0

f = open('data1.csv')
csv_f = csv.reader(f)
with open("dump.txt",'w') as WF:
    for row in csv_f:
        #print (row[1])
        for x in row[1]:
            #print ('x=',x) #printing one letter one by one
            if x in vals1:
                    #print (vals[x]) # converting only the capital letters of the word to a number
                    #print (vals[x],"+",start,"=",start+vals[x]) #printing the added values
                    start+=vals1[x] #adding the converted numbers
            else:
                    #print (start)
                    #print ("entered else:",start ,"+", vals[" "],"=",start+vals[" "]) # handling encounter of other letters 
                    start+=vals1[" "]
            WF.write(str(start)+" ")


# ### DATA 1 - Converting to time series 1 

# In[147]:


#DATA 1 Order 1 Time series 1

f = open('data1.csv')
csv_f = csv.reader(f)

a = []
with open('data1TS1order1.csv','w',newline='') as cf:  #newline='' lets us write without adding an extra line betweeen rows
    for row[1] in csv_f:
        #print (row[1])
        for col in csv_f:
                #print (col[1])
                d = []
                d.append(0)
                #print (d[0])
                count=0
                for x in col[1]:
                    #print (x) # letter
                    c = vals1[x]
                    #print(c) #vals of letter x
                    a=c+d[count]
                    d.append(a)
                    count+=1
                    
                    #print(a)
                #print (d)
                wr = csv.writer(cf,lineterminator='\r')
                wr.writerow(d)


# In[148]:


##DATA 1 Order 1 Time series 1
# converting to array of list
length = 0
mlist1 = []
for line in open("data1TS1order1.csv"):
        reader_file = csv.reader(open("data1TS1order1.csv"))
        length_of_file = len(list(reader_file))
        x = line.split(',')
        y = []
        for i in range(len(x)):
            y.append(float(x[i]))
            #mlist.append(float(x[i]))
        mlist1.append(y)
        length = max(length, len(y))
        arr1_Order1_TS1 = np.array(mlist1)
        


# In[149]:


##DATA 1 Order 1 Time series 1
#padding
pad_arr1_Order1_TS1 = []
for i in range(0,len(arr1_Order1_TS1)):
    abc = np.array(mlist1[i])
    a_padded = np.pad(abc,(0,length-len(mlist1[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr1_Order1_TS1.append(a_padded)

    
#print (pad_arr1_Order1_TS1) 


# In[150]:


#DATA 1 Order 2 Time series 1

f = open('data1.csv')
csv_f = csv.reader(f)

a = []
with open('data1TS1order2.csv','w',newline='') as cf:  #newline='' lets us write without adding an extra line betweeen rows
    for row[1] in csv_f:
        #print (row[1])
        for col in csv_f:
                #print (col[1])
                d = []
                d.append(0)
                #print (d[0])
                count=0
                for x in col[1]:
                    #print (x) # letter
                    c = vals2[x]
                    #print(c) #vals of letter x
                    a=c+d[count]
                    d.append(a)
                    count+=1
                    
                    #print(a)
                #print (d)
                wr = csv.writer(cf,lineterminator='\r')
                wr.writerow(d)


# In[13]:


# converting to array of list
length = 0
mlist1 = []
for line in open("data1TS1order2.csv"):
        reader_file = csv.reader(open("data1TS1order2.csv"))
        length_of_file = len(list(reader_file))
        x = line.split(',')
        y = []
        for i in range(len(x)):
            y.append(float(x[i]))
            #mlist.append(float(x[i]))
        mlist1.append(y)
        length = max(length, len(y))
        arr1_Order2_TS1 = np.array(mlist1)


# In[14]:


##DATA 1 Order 2 Time series 1
#padding
pad_arr1_Order2_TS1 = []
for i in range(0,len(arr1_Order2_TS1)):
    abc = np.array(mlist1[i])
    a_padded = np.pad(abc,(0,length-len(mlist1[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr1_Order2_TS1.append(a_padded)

    
print (pad_arr1_Order2_TS1) 


# In[15]:


pad_arr1_Order2_TS1


# In[16]:


#DATA 1 Order 3 Time series 1

f = open('data1.csv')
csv_f = csv.reader(f)

a = []
with open('data1TS1order3.csv','w',newline='') as cf:  #newline='' lets us write without adding an extra line betweeen rows
    for row[1] in csv_f:
        print (row[1])
        for col in csv_f:
                print (col[1])
                d = []
                d.append(0)
                print (d[0])
                count=0
                for x in col[1]:
                    print (x) # letter
                    c = vals3[x]
                    print(c) #vals of letter x
                    a=c+d[count]
                    d.append(a)
                    count+=1
                    
                    #print(a)
                print (d)
                wr = csv.writer(cf,lineterminator='\r')
                wr.writerow(d)


# In[17]:


# converting to array of list
length = 0
mlist1 = []
for line in open("data1TS1order3.csv"):
        reader_file = csv.reader(open("data1TS1order3.csv"))
        length_of_file = len(list(reader_file))
        x = line.split(',')
        y = []
        for i in range(len(x)):
            y.append(float(x[i]))
            #mlist.append(float(x[i]))
        mlist1.append(y)
        length = max(length, len(y))
        arr1_Order3_TS1 = np.array(mlist1)


# In[18]:


##DATA 1 Order 3 Time series 1
#padding
pad_arr1_Order3_TS1 = []
for i in range(0,len(arr1_Order3_TS1)):
    abc = np.array(mlist1[i])
    a_padded = np.pad(abc,(0,length-len(mlist1[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr1_Order3_TS1.append(a_padded)

    
print (pad_arr1_Order3_TS1) 


# In[19]:


pad_arr1_Order3_TS1


# ### DATA 1 - Converting to time series 2 (Experimental) (our conversion)
# 

# In[20]:


#DATA 1 Order 1 to TIme series 2

f = open('data1.csv')
csv_f = csv.reader(f)

a = []
with open('data1TS2Order1.csv','w',newline='') as cf:  #newline='' lets us write without adding an extra line betweeen rows
    for row[1] in csv_f:
        print (row[1])
        for col in csv_f:
                print (col[1])
                d = []
                
                for x in col[1]:
                    print (x)
                    c = vals1[x]
                    a =d.append(c)
                print (d)
                wr = csv.writer(cf,lineterminator='\r')
                wr.writerow(d)


# In[21]:


# converting to array of list
length = 0
mlist1 = []
for line in open("data1TS2Order1.csv"):
        reader_file = csv.reader(open("data1TS2Order1.csv"))
        length_of_file = len(list(reader_file))
        x = line.split(',')
        y = []
        for i in range(len(x)):
            y.append(float(x[i]))
            #mlist.append(float(x[i]))
        mlist1.append(y)
        length = max(length, len(y))
        arr1_Order1_TS2 = np.array(mlist1)


# In[22]:


##DATA 1 Order 1 Time series 2
#padding
pad_arr1_Order1_TS2 = []
for i in range(0,len(arr1_Order1_TS2)):
    abc = np.array(mlist1[i])
    a_padded = np.pad(abc,(0,length-len(mlist1[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr1_Order1_TS2.append(a_padded)

    
print (pad_arr1_Order1_TS2) 


# In[23]:


pad_arr1_Order1_TS2


# In[24]:


#DATA 1 Order 2 to Time series 2

f = open('data1.csv')
csv_f = csv.reader(f)

a = []
with open('data1TS2Order2.csv','w',newline='') as cf:  #newline='' lets us write without adding an extra line betweeen rows
    for row[1] in csv_f:
        print (row[1])
        for col in csv_f:
                print (col[1])
                d = []
                
                for x in col[1]:
                    print (x)
                    c = vals2[x]
                    a = d.append(c)
                print (d)
                wr = csv.writer(cf,lineterminator='\r')
                wr.writerow(d)


# In[25]:


# converting to array of list
length = 0
mlist1 = []
for line in open("data1TS2Order2.csv"):
        reader_file = csv.reader(open("data1TS2Order2.csv"))
        length_of_file = len(list(reader_file))
        x = line.split(',')
        y = []
        for i in range(len(x)):
            y.append(float(x[i]))
            #mlist.append(float(x[i]))
        mlist1.append(y)
        length = max(length, len(y))
        arr1_Order2_TS2 = np.array(mlist1)


# In[26]:


##DATA 1 Order 2 Time series 2
#padding
pad_arr1_Order2_TS2 = []
for i in range(0,len(arr1_Order2_TS2)):
    abc = np.array(mlist1[i])
    a_padded = np.pad(abc,(0,length-len(mlist1[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr1_Order2_TS2.append(a_padded)

    
print (pad_arr1_Order2_TS2) 


# In[27]:


pad_arr1_Order2_TS2


# In[28]:


#DATA 1 Order 3 to Time series 2

f = open('data1.csv')
csv_f = csv.reader(f)

a = []
with open('data1TS2Order3.csv','w',newline='') as cf:  #newline='' lets us write without adding an extra line betweeen rows
    for row[1] in csv_f:
        print (row[1])
        for col in csv_f:
                print (col[1])
                d = []
                
                for x in col[1]:
                    print (x)
                    c = vals3[x]
                    a = d.append(c)
                print (d)
                wr = csv.writer(cf,lineterminator='\r')
                wr.writerow(d)


# In[29]:


# converting to array of list
length = 0
mlist1 = []
for line in open("data1TS2Order3.csv"):
        reader_file = csv.reader(open("data1TS2Order3.csv"))
        length_of_file = len(list(reader_file))
        x = line.split(',')
        y = []
        for i in range(len(x)):
            y.append(float(x[i]))
            #mlist.append(float(x[i]))
        mlist1.append(y)
        length = max(length, len(y))
        arr1_Order3_TS2 = np.array(mlist1)


# In[30]:


##DATA 1 Order 3 Time series 2
#padding
pad_arr1_Order3_TS2 = []
for i in range(0,len(arr1_Order3_TS2)):
    abc = np.array(mlist1[i])
    a_padded = np.pad(abc,(0,length-len(mlist1[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr1_Order3_TS2.append(a_padded)

    
print (pad_arr1_Order3_TS2) 


# In[31]:


pad_arr1_Order3_TS2


# ### DATA 2 - Converting to time series 1 

# In[32]:


# DATA 2 order 1 Time series 1

f = open('data2.csv')
csv_f = csv.reader(f)
a = []
with open('data2TS1Order1.csv','w',newline='') as cf:  #newline='' lets us write without adding an extra line betweeen rows
    for row[1] in csv_f:
        print (row[1])
        for col in csv_f:
                print (col[1])
                d = []
                d.append(0)
                print (d[0])
                count=0
                for x in col[1]:
                    print (x) # letter
                    c = vals1[x]
                    print(c) #vals of letter x
                    a=c+d[count]
                    d.append(a)
                    count+=1
                    
                    #print(a)
                print (d)
                wr = csv.writer(cf,lineterminator='\r')
                wr.writerow(d)                        


# In[33]:


# Data 2 order 1 TS 1 
# coverting to array of list

length2 = 0
mlist2 = []
for line in open("data2TS1Order1.csv"):
        reader_file2 = csv.reader(open("data2TS1Order1.csv"))
        length_of_file2 = len(list(reader_file2))
        x2 = line.split(',')
        y2 = []
        for i in range(len(x2)):
            y2.append(float(x2[i]))
            #mlist.append(float(x[i]))
        mlist2.append(y2)
        length2 = max(length2, len(y2))
        arr2_Order1_TS1 = np.array(mlist2)
        #print (len(mlist2))


# In[34]:


#padding

pad_arr2_Order1_TS1 = []
for i in range(0,len(arr2_Order1_TS1)):
    abc2 = np.array(mlist2[i])
    a_padded2 = np.pad(abc2,(0,length2-len(mlist2[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr2_Order1_TS1.append(a_padded2)

    


# In[35]:


pad_arr2_Order1_TS1


# In[36]:


# DATA 2 order 2 Time series 1

f = open('data2.csv')
csv_f = csv.reader(f)
a = []
with open('data2TS1Order2.csv','w',newline='') as cf:  #newline='' lets us write without adding an extra line betweeen rows
    for row[1] in csv_f:
        print (row[1])
        for col in csv_f:
                print (col[1])
                d = []
                d.append(0)
                print (d[0])
                count=0
                for x in col[1]:
                    print (x) # letter
                    c = vals2[x]
                    print(c) #vals of letter x
                    a=c+d[count]
                    d.append(a)
                    count+=1
                    
                    #print(a)
                print (d)
                wr = csv.writer(cf,lineterminator='\r')
                wr.writerow(d)    


# In[37]:


# Data 2 order 2 TS 1 
# coverting to array of list

length2 = 0
mlist2 = []
for line in open("data2TS1Order2.csv"):
        reader_file2 = csv.reader(open("data2TS1Order2.csv"))
        length_of_file2 = len(list(reader_file2))
        x2 = line.split(',')
        y2 = []
        for i in range(len(x2)):
            y2.append(float(x2[i]))
            #mlist.append(float(x[i]))
        mlist2.append(y2)
        length2 = max(length2, len(y2))
        arr2_Order2_TS1 = np.array(mlist2)
        #print (len(mlist2))


# In[38]:


#padding

pad_arr2_Order2_TS1 = []
for i in range(0,len(arr2_Order2_TS1)):
    abc2 = np.array(mlist2[i])
    a_padded2 = np.pad(abc2,(0,length2-len(mlist2[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr2_Order2_TS1.append(a_padded2)

    


# In[39]:


pad_arr2_Order2_TS1


# In[40]:


# DATA 2 order 3 Time series 1

f = open('data2.csv')
csv_f = csv.reader(f)
a = []
with open('data2TS1Order3.csv','w',newline='') as cf:  #newline='' lets us write without adding an extra line betweeen rows
    for row[1] in csv_f:
        print (row[1])
        for col in csv_f:
                print (col[1])
                d = []
                d.append(0)
                print (d[0])
                count=0
                for x in col[1]:
                    print (x) # letter
                    c = vals3[x]
                    print(c) #vals of letter x
                    a=c+d[count]
                    d.append(a)
                    count+=1
                    
                    #print(a)
                print (d)
                wr = csv.writer(cf,lineterminator='\r')
                wr.writerow(d)    


# In[41]:


# Data 2 order 3 TS 1 
# coverting to array of list

length2 = 0
mlist2 = []
for line in open("data2TS1Order3.csv"):
        reader_file2 = csv.reader(open("data2TS1Order3.csv"))
        length_of_file2 = len(list(reader_file2))
        x2 = line.split(',')
        y2 = []
        for i in range(len(x2)):
            y2.append(float(x2[i]))
            #mlist.append(float(x[i]))
        mlist2.append(y2)
        length2 = max(length2, len(y2))
        arr2_Order3_TS1 = np.array(mlist2)
        #print (len(mlist2))


# In[42]:


#padding

pad_arr2_Order3_TS1 = []
for i in range(0,len(arr2_Order3_TS1)):
    abc2 = np.array(mlist2[i])
    a_padded2 = np.pad(abc2,(0,length2-len(mlist2[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr2_Order3_TS1.append(a_padded2)

    


# In[43]:


pad_arr2_Order3_TS1


# ### DATA 2 - Converting to time series 2 (Experimental) (our conversion)
# 

# In[44]:


# DATA 2 order 1 time series 2

f = open('data2.csv')
csv_f = csv.reader(f)
a = []
with open('data2TS2Order1.csv','w',newline='') as cf:  #newline='' lets us write without adding an extra line betweeen rows
    for row[1] in csv_f:
        print (row[1])
        for col in csv_f:
                print (col[1])
                d = []
                
                for x in col[1]:
                    print (x)
                    c = vals1[x]
                    a =d.append(c)
                print (d)
                wr = csv.writer(cf)
                wr.writerow(d)                          


# In[45]:


length2 = 0
mlist2 = []
for line in open("data2TS2Order1.csv"):
        reader_file2 = csv.reader(open("data2TS2Order1.csv"))
        length_of_file2 = len(list(reader_file2))
        x2 = line.split(',')
        y2 = []
        for i in range(len(x2)):
            y2.append(float(x2[i]))
            #mlist.append(float(x[i]))
        mlist2.append(y2)
        length2 = max(length2, len(y2))
        arr2_Order1_TS2 = np.array(mlist2)
        #print (len(mlist2))


# In[46]:


#padding

pad_arr2_Order1_TS2 = []
for i in range(0,len(arr2_Order1_TS2)):
    abc2 = np.array(mlist2[i])
    a_padded2 = np.pad(abc2,(0,length2-len(mlist2[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr2_Order1_TS2.append(a_padded2)

    


# In[47]:


pad_arr2_Order1_TS2


# In[48]:


# DATA 2 order 2 time series 2

f = open('data2.csv')
csv_f = csv.reader(f)
a = []
with open('data2TS2Order2.csv','w',newline='') as cf:  #newline='' lets us write without adding an extra line betweeen rows
    for row[1] in csv_f:
        print (row[1])
        for col in csv_f:
                print (col[1])
                d = []
                
                for x in col[1]:
                    print (x)
                    c = vals2[x]
                    a =d.append(c)
                print (d)
                wr = csv.writer(cf)
                wr.writerow(d)                          


# In[49]:


length2 = 0
mlist2 = []
for line in open("data2TS2Order2.csv"):
        reader_file2 = csv.reader(open("data2TS2Order2.csv"))
        length_of_file2 = len(list(reader_file2))
        x2 = line.split(',')
        y2 = []
        for i in range(len(x2)):
            y2.append(float(x2[i]))
            #mlist.append(float(x[i]))
        mlist2.append(y2)
        length2 = max(length2, len(y2))
        arr2_Order2_TS2 = np.array(mlist2)
        #print (len(mlist2))


# In[50]:


#padding

pad_arr2_Order2_TS2 = []
for i in range(0,len(arr2_Order2_TS2)):
    abc2 = np.array(mlist2[i])
    a_padded2 = np.pad(abc2,(0,length2-len(mlist2[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr2_Order2_TS2.append(a_padded2)

    


# In[51]:


pad_arr2_Order2_TS2


# In[52]:


# DATA 2 order 3 time series 2

f = open('data2.csv')
csv_f = csv.reader(f)
a = []
with open('data2TS2Order3.csv','w',newline='') as cf:  #newline='' lets us write without adding an extra line betweeen rows
    for row[1] in csv_f:
        print (row[1])
        for col in csv_f:
                print (col[1])
                d = []
                
                for x in col[1]:
                    print (x)
                    c = vals3[x]
                    a =d.append(c)
                print (d)
                wr = csv.writer(cf)
                wr.writerow(d)                          


# In[53]:


length2 = 0
mlist2 = []
for line in open("data2TS2Order2.csv"):
        reader_file2 = csv.reader(open("data2TS2Order2.csv"))
        length_of_file2 = len(list(reader_file2))
        x2 = line.split(',')
        y2 = []
        for i in range(len(x2)):
            y2.append(float(x2[i]))
            #mlist.append(float(x[i]))
        mlist2.append(y2)
        length2 = max(length2, len(y2))
        arr2_Order3_TS2 = np.array(mlist2)
        #print (len(mlist2))


# In[54]:


#padding

pad_arr2_Order3_TS2 = []
for i in range(0,len(arr2_Order3_TS2)):
    abc2 = np.array(mlist2[i])
    a_padded2 = np.pad(abc2,(0,length2-len(mlist2[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr2_Order3_TS2.append(a_padded2)


# In[55]:


pad_arr2_Order3_TS2


# # Data 3

# In[56]:


from Bio import SeqIO
records_groEL = list(SeqIO.parse("groEL.fasta", "fasta"))
#print(len(records_groEL[0].seq)) # first seq
#print(records_groEL[-2].seq)  # last record
#print(records_groEL[0].seq)


# ## Data 3 Time Series 1

# In[57]:


#Data 3 Order 1 TS 1 
with open('data3TS1Order1.csv','w',newline='') as cf:  
    for i in range(0,100):
        print(records_groEL[i].seq)
        d=[]
        d.append(0)
        count= 0
        for x in records_groEL[i].seq:
            print(x)
            c= vals1_groEL[x]
            a=c+d[count]
            d.append(a)
            count+=1
        print (d)
        wr = csv.writer(cf,lineterminator='\r')
        wr.writerow(d)


# In[58]:


length_groEL = 0
mlist_groEL = []
for line in open("data3TS1Order1.csv"):
        reader_file = csv.reader(open("data3TS1Order1.csv"))
        length_of_file = len(list(reader_file))
        x = line.split(',')
        y = []
        for i in range(len(x)):
            y.append(float(x[i]))
            #mlist.append(float(x[i]))
        mlist_groEL.append(y)
        length_groEL = max(length_groEL, len(y))
        arr3_Order1_TS1 = np.array(mlist_groEL)
        


# In[59]:


pad_arr3_Order1_TS1 = []
for i in range(0,len(arr3_Order1_TS1)):
    abc = np.array(mlist_groEL[i])
    a_padded = np.pad(abc,(0,length_groEL-len(mlist_groEL[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr3_Order1_TS1.append(a_padded)

    
print ((pad_arr3_Order1_TS1)) 


# In[60]:


pad_arr3_Order1_TS1


# In[76]:


#Data 3 Order 2 TS 1 
with open('data3TS1Order2.csv','w',newline='') as cf:  
    for i in range(0,100):
        print(records_groEL[i].seq)
        d=[]
        d.append(0)
        count= 0
        for x in records_groEL[i].seq:
            print(x)
            c= vals2_groEL[x]
            a=c+d[count]
            d.append(a)
            count+=1
        print (d)
        wr = csv.writer(cf,lineterminator='\r')
        wr.writerow(d)


# In[77]:



length_groEL = 0
mlist_groEL = []
for line in open("data3TS1Order2.csv"):
        reader_file = csv.reader(open("data3TS1Order2.csv"))
        length_of_file = len(list(reader_file))
        x = line.split(',')
        y = []
        for i in range(len(x)):
            y.append(float(x[i]))
            #mlist.append(float(x[i]))
        mlist_groEL.append(y)
        length_groEL = max(length_groEL, len(y))
        arr3_Order2_TS1 = np.array(mlist_groEL)
        


# In[78]:


pad_arr3_Order2_TS1 = []
for i in range(0,len(arr3_Order2_TS1)):
    abc = np.array(mlist_groEL[i])
    a_padded = np.pad(abc,(0,length_groEL-len(mlist_groEL[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr3_Order2_TS1.append(a_padded)

    
print ((pad_arr3_Order2_TS1)) 


# In[79]:


pad_arr3_Order2_TS1


# In[80]:


#Data 3 Order 3 TS 1 
with open('data3TS1Order3.csv','w',newline='') as cf:  
    for i in range(0,100):
        print(records_groEL[i].seq)
        d=[]
        d.append(0)
        count= 0
        for x in records_groEL[i].seq:
            print(x)
            c= vals3_groEL[x]
            a=c+d[count]
            d.append(a)
            count+=1
        print (d)
        wr = csv.writer(cf,lineterminator='\r')
        wr.writerow(d)


# In[81]:



length_groEL = 0
mlist_groEL = []
for line in open("data3TS1Order3.csv"):
        reader_file = csv.reader(open("data3TS1Order3.csv"))
        length_of_file = len(list(reader_file))
        x = line.split(',')
        y = []
        for i in range(len(x)):
            y.append(float(x[i]))
            #mlist.append(float(x[i]))
        mlist_groEL.append(y)
        length_groEL = max(length_groEL, len(y))
        arr3_Order3_TS1 = np.array(mlist_groEL)
        


# In[82]:


pad_arr3_Order3_TS1 = []
for i in range(0,len(arr3_Order3_TS1)):
    abc = np.array(mlist_groEL[i])
    a_padded = np.pad(abc,(0,length_groEL-len(mlist_groEL[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr3_Order3_TS1.append(a_padded)

    


# In[83]:


pad_arr3_Order3_TS1


# ### DATA 3 - Converting to time series 2 (Experimental) (our conversion)

# In[84]:


#Data 3 Order 1 TS 2 
with open('data3TS2Order1.csv','w',newline='') as cf:  
    for i in range(0,100):
        print(records_groEL[i].seq)
        d=[]
        for x in records_groEL[i].seq:
            print(x)
            c= vals1_groEL[x]
            a=d.append(c)
        print (d)
        wr = csv.writer(cf,lineterminator='\r')
        wr.writerow(d)
        


# In[85]:


length_groEL = 0
mlist_groEL = []
for line in open("data3TS2Order1.csv"):
        reader_file = csv.reader(open("data3TS2Order1.csv"))
        length_of_file = len(list(reader_file))
        x = line.split(',')
        y = []
        for i in range(len(x)):
            y.append(float(x[i]))
            #mlist.append(float(x[i]))
        mlist_groEL.append(y)
        length_groEL = max(length_groEL, len(y))
        arr3_Order1_TS2 = np.array(mlist_groEL)
        


# In[86]:


pad_arr3_Order1_TS2 = []
for i in range(0,len(arr3_Order1_TS2)):
    abc = np.array(mlist_groEL[i])
    a_padded = np.pad(abc,(0,length_groEL-len(mlist_groEL[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr3_Order1_TS2.append(a_padded)

    
print ((pad_arr3_Order1_TS2)) 


# In[87]:


pad_arr3_Order1_TS2


# In[88]:


#Data 3 Order 2 TS 2 
with open('data3TS2Order2.csv','w',newline='') as cf:  
    for i in range(0,100):
        print(records_groEL[i].seq)
        d=[]
        for x in records_groEL[i].seq:
            print(x)
            c= vals2_groEL[x]
            a=d.append(c)
        print (d)
        wr = csv.writer(cf,lineterminator='\r')
        wr.writerow(d)
        


# In[89]:


length_groEL = 0
mlist_groEL = []
for line in open("data3TS2Order2.csv"):
        reader_file = csv.reader(open("data3TS2Order2.csv"))
        length_of_file = len(list(reader_file))
        x = line.split(',')
        y = []
        for i in range(len(x)):
            y.append(float(x[i]))
            #mlist.append(float(x[i]))
        mlist_groEL.append(y)
        length_groEL = max(length_groEL, len(y))
        arr3_Order2_TS2 = np.array(mlist_groEL)
        


# In[90]:


pad_arr3_Order2_TS2 = []
for i in range(0,len(arr3_Order2_TS2)):
    abc = np.array(mlist_groEL[i])
    a_padded = np.pad(abc,(0,length_groEL-len(mlist_groEL[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr3_Order2_TS2.append(a_padded)

    
print ((pad_arr3_Order2_TS2)) 


# In[91]:


pad_arr3_Order2_TS2


# In[92]:


#Data 3 Order 3 TS 2 
with open('data3TS2Order3.csv','w',newline='') as cf:  
    for i in range(0,100):
        print(records_groEL[i].seq)
        d=[]
        for x in records_groEL[i].seq:
            print(x)
            c= vals3_groEL[x]
            a=d.append(c)
        print (d)
        wr = csv.writer(cf,lineterminator='\r')
        wr.writerow(d)
        


# In[93]:


length_groEL = 0
mlist_groEL = []
for line in open("data3TS2Order3.csv"):
        reader_file = csv.reader(open("data3TS2Order3.csv"))
        length_of_file = len(list(reader_file))
        x = line.split(',')
        y = []
        for i in range(len(x)):
            y.append(float(x[i]))
            #mlist.append(float(x[i]))
        mlist_groEL.append(y)
        length_groEL = max(length_groEL, len(y))
        arr3_Order3_TS2 = np.array(mlist_groEL)
        


# In[94]:


pad_arr3_Order3_TS2 = []
for i in range(0,len(arr3_Order3_TS2)):
    abc = np.array(mlist_groEL[i])
    a_padded = np.pad(abc,(0,length_groEL-len(mlist_groEL[i])),'constant')
    #a_stack = np.stack(a_padded, axis=0)
    #arr_of_arr = np.append(arr_of_arr,a_padded,axis = 0) # contains a 1D array with all the values.
    #ar_splited = np.split(arr_of_arr,[length]*i)
    pad_arr3_Order3_TS2.append(a_padded)

    
print ((pad_arr3_Order3_TS2)) 


# In[95]:


pad_arr3_Order3_TS2


# # plots

# In[96]:


pad_arr2_Order1_TS1[0][1:]


# In[97]:



plt.plot(pad_arr2_Order1_TS1[0][1:])
plt.xlabel('Index position of the sequence')
plt.ylabel('Time series Values')


# In[98]:



plt.plot(pad_arr2_Order1_TS2[0])
plt.xlabel('Index position of the sequence')
plt.ylabel('Numeric converted Values')


# ## Distance

# ### Euclidean

# In[113]:


get_ipython().run_cell_magic('time', '', '#DATA1 order1 TS 1  FAST DTW\n\ncurrent_row= 0\ncompare_row= 0\neucl1_order1_ts1 = []\nfor current_row in range(0,21):\n    dist_values = []\n    for comapre_row in range(0,21):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        distance,path = fastdtw(pad_arr1_Order1_TS1[current_row],pad_arr1_Order1_TS1[compare_row],dist=euclidean) \n        #print(distance)\n        dist_values.append(distance)\n        compare_row=compare_row+1\n    eucl1_order1_ts1.append(dist_values)\n    current_row=current_row+1\n    compare_row=0\n    \n\ndf_eucl1_order1_ts1 =  pd.DataFrame(eucl1_order1_ts1)\nprint(df_eucl1_order1_ts1)')


# In[115]:


get_ipython().run_cell_magic('time', '', '#DATA1 order2 TS 1  FAST DTW\n\ncurrent_row= 0\ncompare_row= 0\neucl1_order2_ts1 = []\nfor current_row in range(0,21): #only considering 21 sequences, since it takes time to compute\n    dist_values = []\n    for comapre_row in range(0,21):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        distance,path = fastdtw(pad_arr1_Order2_TS1[current_row],pad_arr1_Order2_TS1[compare_row],dist=euclidean) \n        #print(distance)\n        dist_values.append(distance)\n        compare_row=compare_row+1\n    eucl1_order2_ts1.append(dist_values)\n    current_row=current_row+1\n    compare_row=0\n    \n\ndf_eucl1_order2_ts1 =  pd.DataFrame(eucl1_order2_ts1)\nprint(df_eucl1_order2_ts1)')


# In[137]:


get_ipython().run_cell_magic('time', '', '#DATA1 order3 TS 1  FAST DTW\n\ncurrent_row= 0\ncompare_row= 0\neucl1_order3_ts1 = []\nfor current_row in range(0,21):\n    dist_values = []\n    for comapre_row in range(0,21):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        distance,path = fastdtw(pad_arr1_Order3_TS1[current_row],pad_arr1_Order3_TS1[compare_row],dist=euclidean) \n        #print(distance)\n        dist_values.append(distance)\n        compare_row=compare_row+1\n    eucl1_order3_ts1.append(dist_values)\n    current_row=current_row+1\n    compare_row=0\n    \n\ndf_eucl1_order3_ts1 =  pd.DataFrame(eucl1_order3_ts1)\nprint(df_eucl1_order3_ts1)')


# In[117]:


get_ipython().run_cell_magic('time', '', '#DATA1 order1 TS 2  FAST DTW\n\ncurrent_row= 0\ncompare_row= 0\neucl1_order1_ts2 = []\nfor current_row in range(0,21):\n    dist_values = []\n    for comapre_row in range(0,21):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        distance,path = fastdtw(pad_arr1_Order1_TS2[current_row],pad_arr1_Order1_TS2[compare_row],dist=euclidean) \n        #print(distance)\n        dist_values.append(distance)\n        compare_row=compare_row+1\n    eucl1_order1_ts2.append(dist_values)\n    current_row=current_row+1\n    compare_row=0\n    \n\ndf_eucl1_order1_ts2 =  pd.DataFrame(eucl1_order1_ts2)\nprint(df_eucl1_order1_ts2)')


# In[118]:


get_ipython().run_cell_magic('time', '', '#DATA1 order2 TS 2  FAST DTW\n\ncurrent_row= 0\ncompare_row= 0\neucl1_order2_ts2 = []\nfor current_row in range(0,21):\n    dist_values = []\n    for comapre_row in range(0,21):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        distance,path = fastdtw(pad_arr1_Order2_TS2[current_row],pad_arr1_Order2_TS2[compare_row],dist=euclidean) \n        #print(distance)\n        dist_values.append(distance)\n        compare_row=compare_row+1\n    eucl1_order2_ts2.append(dist_values)\n    current_row=current_row+1\n    compare_row=0\n    \n\ndf_eucl1_order2_ts2 =  pd.DataFrame(eucl1_order2_ts2)\nprint(df_eucl1_order2_ts2)')


# In[119]:


get_ipython().run_cell_magic('time', '', '#DATA1 order3 TS 2  FAST DTW\n\ncurrent_row= 0\ncompare_row= 0\neucl1_order3_ts2 = []\nfor current_row in range(0,21):\n    dist_values = []\n    for comapre_row in range(0,21):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        distance,path = fastdtw(pad_arr1_Order3_TS2[current_row],pad_arr1_Order3_TS2[compare_row],dist=euclidean) \n        #print(distance)\n        dist_values.append(distance)\n        compare_row=compare_row+1\n    eucl1_order3_ts2.append(dist_values)\n    current_row=current_row+1\n    compare_row=0\n    \n\ndf_eucl1_order3_ts2 =  pd.DataFrame(eucl1_order3_ts2)\nprint(df_eucl1_order3_ts2)')


# In[120]:


get_ipython().run_cell_magic('time', '', '#DATA2 order1 TS 1  FAST DTW\n\ncurrent_row= 0\ncompare_row= 0\neucl2_order1_ts1 = []\nfor current_row in range(0,len(pad_arr2_Order1_TS1)):\n    dist_values = []\n    for comapre_row in range(0,len(pad_arr2_Order1_TS1)):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        distance,path = fastdtw(pad_arr2_Order1_TS1[current_row],pad_arr2_Order1_TS1[compare_row],dist=euclidean) \n        #print(distance)\n        dist_values.append(distance)\n        compare_row=compare_row+1\n    eucl2_order1_ts1.append(dist_values)\n    current_row=current_row+1\n    compare_row=0\n    \n\ndf_eucl2_order1_ts1 =  pd.DataFrame(eucl2_order1_ts1)\nprint(df_eucl2_order1_ts1)')


# In[114]:


get_ipython().run_cell_magic('time', '', '#DATA2 order2 TS 1  FAST DTW\n\ncurrent_row= 0\ncompare_row= 0\neucl2_order2_ts1 = []\nfor current_row in range(0,len(pad_arr2_Order2_TS1)):\n    dist_values = []\n    for comapre_row in range(0,len(pad_arr2_Order2_TS1)):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        distance,path = fastdtw(pad_arr2_Order2_TS1[current_row],pad_arr2_Order2_TS1[compare_row],dist=euclidean) \n        #print(distance)\n        dist_values.append(distance)\n        compare_row=compare_row+1\n    eucl2_order2_ts1.append(dist_values)\n    current_row=current_row+1\n    compare_row=0\n    \n\ndf_eucl2_order2_ts1 =  pd.DataFrame(eucl2_order2_ts1)\nprint(df_eucl2_order2_ts1)')


# In[101]:


get_ipython().run_cell_magic('time', '', '#DATA2 order3 TS 1  FAST DTW\n\ncurrent_row= 0\ncompare_row= 0\neucl2_order3_ts1 = []\nfor current_row in range(0,len(pad_arr2_Order3_TS1)):\n    dist_values = []\n    for comapre_row in range(0,len(pad_arr2_Order3_TS1)):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        distance,path = fastdtw(pad_arr2_Order3_TS1[current_row],pad_arr2_Order3_TS1[compare_row],dist=euclidean) \n        #print(distance)\n        dist_values.append(distance)\n        compare_row=compare_row+1\n    eucl2_order3_ts1.append(dist_values)\n    current_row=current_row+1\n    compare_row=0\n    \n\ndf_eucl2_order3_ts1 =  pd.DataFrame(eucl2_order3_ts1)\nprint(df_eucl2_order3_ts1)')


# In[102]:


get_ipython().run_cell_magic('time', '', '#DATA2 order1 TS 2  FAST DTW\n\ncurrent_row= 0\ncompare_row= 0\neucl2_order1_ts2 = []\nfor current_row in range(0,len(pad_arr2_Order1_TS2)):\n    dist_values = []\n    for comapre_row in range(0,len(pad_arr2_Order1_TS2)):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        distance,path = fastdtw(pad_arr2_Order1_TS2[current_row],pad_arr2_Order1_TS2[compare_row],dist=euclidean) \n        #print(distance)\n        dist_values.append(distance)\n        compare_row=compare_row+1\n    eucl2_order1_ts2.append(dist_values)\n    current_row=current_row+1\n    compare_row=0\n    \n\ndf_eucl2_order1_ts2 =  pd.DataFrame(eucl2_order1_ts2)\nprint(df_eucl2_order1_ts2)')


# In[104]:


get_ipython().run_cell_magic('time', '', '#DATA2 order2 TS 2  FAST DTW\n\ncurrent_row= 0\ncompare_row= 0\neucl2_order2_ts2 = []\nfor current_row in range(0,len(pad_arr2_Order2_TS2)):\n    dist_values = []\n    for comapre_row in range(0,len(pad_arr2_Order2_TS2)):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        distance,path = fastdtw(pad_arr2_Order2_TS2[current_row],pad_arr2_Order2_TS2[compare_row],dist=euclidean) \n        #print(distance)\n        dist_values.append(distance)\n        compare_row=compare_row+1\n    eucl2_order2_ts2.append(dist_values)\n    current_row=current_row+1\n    compare_row=0\n    \n\ndf_eucl2_order2_ts2 =  pd.DataFrame(eucl2_order2_ts2)\nprint(df_eucl2_order2_ts2)')


# In[105]:


get_ipython().run_cell_magic('time', '', '#DATA2 order3 TS 2  FAST DTW\n\ncurrent_row= 0\ncompare_row= 0\neucl2_order3_ts2 = []\nfor current_row in range(0,len(pad_arr2_Order3_TS2)):\n    dist_values = []\n    for comapre_row in range(0,len(pad_arr2_Order3_TS2)):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        distance,path = fastdtw(pad_arr2_Order3_TS2[current_row],pad_arr2_Order3_TS2[compare_row],dist=euclidean) \n        #print(distance)\n        dist_values.append(distance)\n        compare_row=compare_row+1\n    eucl2_order3_ts2.append(dist_values)\n    current_row=current_row+1\n    compare_row=0\n    \n\ndf_eucl2_order3_ts2 =  pd.DataFrame(eucl2_order3_ts2)\nprint(df_eucl2_order3_ts2)')


# ### EDIT DISTANCE

# In[106]:


data1csv = pd.read_csv('data1.csv',header=None,usecols=[1])
data2csv = pd.read_csv('data2.csv',header=None,usecols=[1])


# In[136]:


get_ipython().run_cell_magic('time', '', '#DATA1\ncurrent_row= 1\ncompare_row= 1\nleven1_order1_ts1 = []\nfor current_row in range(1,len(pad_arr1_Order1_TS1)+1):\n    dist_values = []\n    for comapre_row in range(1,len(pad_arr1_Order1_TS1)+1):\n        #print ("current",current_row)\n        #print ("comapre",compare_row)\n        levin_distance = distance.levenshtein(data1csv[1].iloc[current_row],data1csv[1].iloc[compare_row]) \n        #print(levin_distance)\n        dist_values.append(levin_distance)\n        compare_row=compare_row+1\n    leven1_order1_ts1.append(dist_values)\n    current_row=current_row+1\n    compare_row=1\n    \ndf_leven1 =  pd.DataFrame(leven1_order1_ts1)\nprint (df_leven1)')


# In[110]:


#DATA2
current_row= 1
compare_row= 1
leven2_order1_ts1 = []
for current_row in range(1,len(pad_arr2_Order1_TS1)+1):
    dist_values = []
    for comapre_row in range(1,len(pad_arr2_Order1_TS1)+1):
        #print ("current",current_row)
        #print ("comapre",compare_row)
        levin_distance = distance.levenshtein(data2csv[1].iloc[current_row],data2csv[1].iloc[compare_row]) 
        #print(levin_distance)
        dist_values.append(levin_distance)
        compare_row=compare_row+1
    leven2_order1_ts1.append(dist_values)
    current_row=current_row+1
    compare_row=1

    
df_leven2_order1_ts1 =  pd.DataFrame(leven2_order1_ts1)
df_leven2_order1_ts1


# ## Sequence matcher

# In[121]:


from difflib import SequenceMatcher


# In[128]:


print(pad_arr1_Order1_TS1[0][1:])
print(pad_arr1_Order1_TS1[1][1:])
sm_data1_test1 = SequenceMatcher(None,pad_arr1_Order1_TS1[0][1:],pad_arr1_Order1_TS1[1][1:])
sm_data1_test1.ratio()*100


# In[129]:


print(pad_arr1_Order2_TS1[0][1:])
print(pad_arr1_Order2_TS1[1][1:])
sm_data1_test1 = SequenceMatcher(None,pad_arr1_Order2_TS1[0][1:],pad_arr1_Order2_TS1[1][1:])
sm_data1_test1.ratio()*100


# In[130]:


print(pad_arr1_Order3_TS1[0][1:])
print(pad_arr1_Order3_TS1[1][1:])
sm_data1_test1 = SequenceMatcher(None,pad_arr1_Order3_TS1[0][1:],pad_arr1_Order3_TS1[1][1:])
sm_data1_test1.ratio()*100


# # Plots for distance comaprision

# In[140]:


# plot for comapring Seq 0 distance values of order 3 with Edit distance values of the same sequence 
'''
fig, ax = plt.subplots()
x = df_eucl1_order3_ts1[0]
ax.plot(x, 'b')
ax.set_xlabel('Sequence 0')
ax.set_ylabel('Euclidean Distance')
plt.legend('Eucl')
ax2 = ax.twinx()

ax2.plot(df_leven1[0], 'g')
plt.legend('Leven')
ax2.set_ylabel('Levenshtein Distance')

fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.show()
'''


# In[139]:


# plot for comapring Seq 1 distance values of order 3 with Edit distance values of the same sequence  
'''
fig, ax = plt.subplots()
x = df_eucl1_order3_ts1[1]
ax.plot(x, 'b')
ax.set_xlabel('Sequence 0')
ax.set_ylabel('Euclidean Distance')
plt.legend('Eucl')
ax2 = ax.twinx()

ax2.plot(df_leven1[1], 'g')
plt.legend('Leven')
ax2.set_ylabel('Levenshtein Distance')

fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.show()
'''

