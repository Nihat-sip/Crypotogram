#Nihat Najafov Python3.8
#Pyhton3.8 Encoder Decoder Program
import math
print("""


    Simple Encode Decode 

           ___
          (._.)
           <|>
          _/ \_
          



""")

#Lists
list1=['a','b','c','d','e','f','g','h','i','j',' ','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list2=['4','!','6',':','3','#','5','1','$','^','2','&','*','(','7',')','8','=','9','~','_','|','+','<','-','>','@']
list3=[]

#We try to mix list2 symbols and add it list3 thus we can make random list with key. This random list become our list which we use it make our cypher text or decode it.
def make_random_list():
    
    global list3
    key=int(input('Write key for random list[0-27]-->'))
    for i in range(0,26):
        random_number=key+i
        if random_number>26:
            random_number=random_number-26
        c=list2[random_number]
        list3+=c
    print('\nYour list created!!\n\n********************************************\n\n')
    

#Function make_random_list is running first 
make_random_list()

#User inputs
while True:
    ask=int(input('Decode(1) or Encode(2)-->'))
    if ask!=1 and ask!=2:
        print('Please write only 1 or 2 !!!!!')
    else:
        break

while True:
    key=int(input('\nWrite your key [Only number]-->'))
    if key<100:
        print('\nKey must be minimum 3 symbol!!!\n')
    if key>=100:
        break

def Encode():
    cypher=''
    text=input('Write your text -->')
    text=text.lower()
    global list3
    for i in text:
        a=list1.index(i)
        b=a+key
        while True:
            b=b-26
            if b<26:
                break
            
        c=list3[b]
        cypher+=c
    print('Your cypher text is',cypher)
    



def Decode():
    plain_text=''
    cypher=str(input('Type cypher text-->'))
    
    for i in cypher:
        a=list3.index(i)
        b=a-key
        while True:
            b=b+26
            if b>=0:
                break
        c=list1[b]
        plain_text+=c
    print('Your plain text\n',plain_text)
#We call function based on user inputs
if ask==1:
    Decode()
else:
    Encode()
