import copy
import random
size=int(input('please enter the size (x>7)'))
inf=input('please enter the word ')
inf_len=len(inf)
list1=[]
a=97
for i in range(1,27):
    pick=chr(a)
    a+=1
    list1.append(pick)
    
mem=[]
#print(list1)
for i in range(size):
    fin=[]
    for t in range(size):
        pick2=random.randint(0,25)
        pick_f=list1[pick2]
        fin.append(pick_f)
        fin_f=copy.deepcopy(fin)
    mem.append(fin_f)
    fin.clear()

mem2=copy.deepcopy(mem)
mem_fi=[]
mem_fi2=[]
while True:
    
    random_num=random.randint(0,size-1)
    mem_fi.append(random_num)
    random_num2=random.randint(0,size-1)
    mem_fi2.append(random_num2)
    model_chose=random.randint(1,3)
    if(model_chose==1):
        if(random_num2+inf_len<size):
            break
        
        
    elif(model_chose==2):
        if(random_num+inf_len<size):
            break
        
    else:
        if(random_num+inf_len<size and random_num2+inf_len<size):
           break 

inf_split=list(inf)
random_model=random.randint(1,2)
if(random_model==1):
    
    inf_split.reverse()
else:
    pass
    
inf_use1=copy.deepcopy(inf_split)
count=0
count1=0
count3=0
#mem_fi.reverse() 
#mem_fi2.reverse() 
#random_num_p=mem_fi[0]
#random_num_p1=mem_fi2[0]
mem_ff=copy.deepcopy(mem)
#case1    
for j in range(inf_len):
    iu=inf_use1[count3]
    mem_ff[random_num+count][random_num2+count1]=iu
    ord_mem=ord(inf_split[count3])
    ord_mem-=32
    mem2[random_num+count][random_num2+count1]=chr(ord_mem)
    
    if(model_chose==1):
        count1+=1
    elif(model_chose==2):
        count+=1
    else:
        count+=1
        count1+=1
    count3+=1
print('\n')
print('HERE IS THE LIST')
for d in mem_ff:
    for m in d:
        print('{:>5}'.format(m),end='')
            
    print('\n')    
    
        
con=input('If you want to see the answer ,enter A ,the answer will show with capital')        
print('HERE IS THE ANSWER')
for d in mem2:
    for m in d:
        print('{:>5}'.format(m),end='')
            
    print('\n')