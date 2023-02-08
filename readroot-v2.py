#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Takes in the PhysVolName string (volline) and Returns the indices SAno, DUno
# Index Extractor Function
def indext(volline):
    DAind = volline.index("DetectorArray_") + len("DetectorArray_")
    DAno = int(volline[DAind :DAind + 3])
    SAind = volline.index("StringAssembly_") + len("StringAssembly_")
    SAno = int(volline[SAind:SAind + 3])
    DUind = volline.index("DetUnit_") + len("DetUnit_")
    DUno = int(volline[DUind:DUind + 3])
    ADind = volline.index("ActiveDet_") + len("ActiveDet_")
    ADno = int(volline[ADind:ADind + 3])
    return SAno, DUno


# In[5]:


import uproot
import numpy
import pandas as pd
# Reading the input file
file = uproot.open(inpath)


# In[6]:


# Examining the rootfile
file["fTree"].values()


# In[7]:


# Each event contains a series of energy deposited in each step
Edep=file["fTree"]["fSteps.fEdep"].array(library="numpy")
#print(Edep)


# In[8]:


# The associated active volume in which the energy is deposited
PhysVolName=file["fTree"]["fSteps.fPhysVolName"].array(library="numpy")
#print(PhysVolName)


# In[9]:


# The cood [i,j,k] : i = the row number is the evtid; j= det unit; k= string assembly
# No. of Strings = 12, No of Det per string = 8
#
# 'etab' is the table of energy deposited
etab=numpy.zeros([PhysVolName.size,8,12], dtype=object)# index runs from 0 to 196378
#print(etab)
#
# 'hits' is the table of hits in the region of interest )(defined below)
hits=numpy.zeros([8,12], dtype=object)# index runs from 0 to 196378
#print(hits)
#
# Defining the energy ROI, by defining the centroid and half-window
centE = 2.6145
deltaE = 0.0001
minE = centE - deltaE
maxE = centE + deltaE


# In[10]:


# Looping over the events, extracting the energy deposited detector by detector and appropriately summing
# This takes care of possible scatters between detectors in a single event
for i in range(len(Edep)):
    for (E,volline) in zip(Edep[i],PhysVolName[i]):
        SAno,DUno=indext(volline)
        etab[i, DUno-1, SAno-1]=etab[i, DUno-1, SAno-1] + E


# In[11]:


# Now that the total energy deposited in each event and in each detector has been computed,
# extracting the hits in the region of interest
for i in range(len(Edep)):
    for j in range(0,8):
        for k in range(0,12):
            if ((minE<= etab[i,j,k]) & (etab[i,j,k] <= maxE)):
                hits[j, k] = hits[j, k] + 1


# In[12]:


print(hits)


# In[25]:


# Setting the output file
start = inpath.find('LGND_200')
end = inpath.find('.root')
outpath="./fresults/" + inpath[start:end] + ".txt"
print(outpath)


# In[26]:


outfile = open(outpath,'w')
outfile.write("String assembly on the columns and detector units on the rows\n")
outfile.write("infile: ")
outfile.write(inpath)
outfile.write("\n")
numpy.savetxt(outfile, hits, fmt = "%4.0f") 
outfile.close()


# In[ ]:




