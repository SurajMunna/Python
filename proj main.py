#file-output.py'
import re
import sys
import pickle
from nltk.corpus import stopwords


with open("Happy.txt",'rb')as f:
    Hap=pickle.load(f)
with open("Sad.txt",'rb')as f:
    Sa=pickle.load(f)
with open("Angry.txt",'rb')as f:
    Ang=pickle.load(f)
with open("Fear.txt",'rb')as f:
    Fea=pickle.load(f)
with open("Surprised.txt",'rb')as f:
    Sur=pickle.load(f)
with open("Positive.txt",'rb')as f:
    Pos=pickle.load(f)
with open("Alive.txt",'rb')as f:
    Ali=pickle.load(f)
with open("Affectionate.txt",'rb')as f:
    Aff=pickle.load(f)
with open("Negative.txt",'rb')as f:
    Neg=pickle.load(f)
with open("Confused.txt",'rb')as f:
    Con=pickle.load(f)

invert=["not","lack of"]

with open("input.txt","r") as f:
 f_content = f.read()    
 print(f_content)
 print("Keywords::")
 words=f_content.split()
list1=[]                
tcount=0

stop_words = set(stopwords.words('english'))
stop_words.remove("not")
stop_words.add("I")


for r in words:
    if not r in stop_words:
        list1.append(r)
print(list1)

invertcount=0
for r in list1:
    if r in invert:
        invertcount+=1  

hapcount=0
for r in list1:
    if r in Hap:
        hapcount+=1
        tcount+=1
        

Sacount=0
for r in list1:
    if r in Sa:
        Sacount+=1
        tcount+=1

    
Angcount=0
for r in list1:
    if r in Ang:
        Angcount+=1
        tcount+=1
    
Feacount=0 
for r in list1:
    if r in Fea:
        Feacount+=1
        tcount+=1
         
Surcount=0 
for r in list1:
    if r in Sur:
        Surcount+=1
        tcount+=1
        
Poscount=0
for r in list1:
    if r in Pos:
        Poscount+=1
        tcount+=1
    
alicount=0
for r in list1:
    if r in Ali:
        alicount+=1
        tcount+=1
    
affcount=0
for r in list1:
    if r in Aff:
        affcount+=1
        tcount+=1
        
Negcount=0
for r in list1:
    if r in Neg:
        Negcount+=1
        tcount+=1

       
Concount=0
for r in list1:
    if r in Con:
        Concount+=1
        tcount+=1
        
def invert():
    if invertcount>0 and Sacount>0:
     print("You are Happy ")
    if invertcount>0 and hapcount>0:
     print("You are Sad ")
    if invertcount>0 and Feacount>0:
     print("You are Positive ")
    if invertcount>0 and Poscount>0:
     print("You are Negative ")
    sys.exit()
  
  
if hapcount==0 and  Sacount==0 and Angcount==0 and Feacount==0  and affcount==0 and  Surcount==0 and Poscount==0 and alicount==0 and alicount==0 and Negcount==0 and Concount==0 :
     print("This isn't an emotion.")
     sys.exit()
     
tcount=100/tcount; 

def output():
 if Negcount>0:
    print("You are feeling",Negcount*tcount,"% 'Negative'\n")
   
 if hapcount>0:    
   print("You are feeling",hapcount*tcount, "% 'Happy' \n ")

 if Sacount>0:
    print("You are feeling",Sacount*tcount, "% 'sad' \n")

 if Angcount>0:
    print("You are feeling",Angcount*tcount, "% 'Angry'\n")

 if Feacount>0:
    print("You are feeling",Feacount*tcount,"% 'Scared'\n")

 if Surcount>0:
    print("You are feeling",Surcount*tcount,"% 'Surprised'\n")

 if Poscount>0:
    print("You are Feeling",Poscount*tcount,"% 'Positive'\n")

 if alicount>0:
    print("You are Feeling",alicount*tcount,"% 'Alive'\n")

 if affcount>0:
    print("You are feeling",affcount*tcount,"% 'Affectionate'\n")
    
 if Concount>0:
    print("You are feeling",Concount*tcount,"% 'Confused'\n")

invert()    
output()
