import random
poker=[]
for t in[chr(9824),chr(9825),chr(9826),chr(9827)]:
    for e in['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
        result=t+e
        poker.append(result)
        
poker2=poker.copy()
poker.insert(0,'0')
turn_list=['c1']
turn=random.randint(0,1)
print("YOUR order is '{}'".format(turn+1))
print('\n')
turn_list.insert(turn,'p')
#print(turn_list)
mem=[]
mem2=[]
mem3=[]

counter=0

rounder=0
for y in range(5):
    pick=random.randint(0,len(poker2))
    mem.append(poker2.pop(pick-1))
    
for y in range(5):
    pick=random.randint(0,len(poker2))
    mem2.append(poker2.pop(pick-1))
#for y in range(5):
    #pick=random.randint(0,len(poker2))
    #mem3.append(poker2.pop(pick))  
    
ii=0    
while True:
    if(counter>99 or ii>=1):
        break
    for i in turn_list:
        rounder+=1
        mem_comm=[]
        mem_use=[]
        mem_c=[]
        if(i=='c1'):
            for yy in mem2:
                index_yy=poker.index(yy)
                index_f=int(index_yy%13)
                mem_c.append(index_f)
            cou=99-counter
            for tt in mem_c:
                if(tt==4 or tt==5 or tt==10 or tt==11 or tt==12 or tt==13):
                    mem_comm.append(tt)
                elif(tt<=cou):
                    mem_use.append(tt)
            #use common
            #common funtion
            mem_comm.sort(reverse=True)
            mem_use.sort(reverse=True)    
            mem_use.extend(mem_comm)
            ##print(mem2)
           
            if(len(mem_use)==0 and len(mem_comm)==0):
                ii+=1
                break
            fin_c=mem_use.pop(0)
            com_index=mem_c.index(fin_c)
            computer_pick=mem2.pop(com_index)
            #index_pick_f=com_index
            index_pick_f=fin_c
            poker2.append(computer_pick)
            mem_comm.clear()
            mem_use.clear()
            mem_c.clear()
            
            index_pick=poker.index(computer_pick)  
            #print(index_pick)
            #index_pick standard
            
            
        else:    
            print('YOUR CARD {}'.format(mem))
            inf=int(input('please play poker,(enter the location,count from 1)'))
            print('\n')
            inf-=1
            pick2=mem.pop(inf)
            index_pick=poker.index(pick2)
            index_pick_f=index_pick%13
            poker2.append(pick2)
        
            
        
        #print('index',index_pick)
        if(index_pick==1):
            counter=0
            print('RESET TO ZERO')
        elif(index_pick_f==11):
            print('PASS')
        elif(index_pick_f==0):
            counter=99
        elif(index_pick_f==10 or index_pick_f==12):
            if(i=='p'):
                
                model=input('plus enter P ,minus enter M ')
                
            else:
                compare=99-counter
                if(index_pick_f==10):
                    if(compare>=10):
                        model='P'
                    else:
                        model='M'
                        
                else:
                    if(compare>=20):
                        model='P'
                        
                    else:
                        model='M'
            #check            
            if(model=='P'):
                if(index_pick_f==10):
                    counter+=10
                else:
                    counter+=20
            else:
                if(index_pick_f==12):
                    counter-=20
                else:
                    counter-=10
        elif(index_pick_f==4):
            #turn_list.reverse()
            print('TURN')
        elif(index_pick_f==5):
            #change=input('please enter the object you want to specify,computer1 enter c1 or computer2 enter c2')
            #change_index=turn_list.index(change)
            #turn_list.pop(change_index)
            #turn_list.insert(change,0)
            print('DESIGNATION')
        #elif(index_pick_f==2):
            #counter=0
        else:
            counter+=index_pick_f
            
            
        print('ROUND:{}'.format(rounder))
        
        if(counter>99):
            print('\n')
            if(i=='c1'):
                print('COMPUTER IS LOSER')
                break
            else:
                print('PLAYER IS LOSER')
                break
        random_num=random.randint(0,20)
        random.shuffle(poker2)
        pick4=poker2.pop(random_num)
        poker
        if(i=='c1'):
            mem2.append(pick4)
        else:
            mem.append(pick4)
            
            
            
            
        
        if(i=='c1'):
            print('Computer play poker {}'.format(computer_pick))
        else:
            print('Player play poker {}'.format(pick2))
        if(counter==99):
            
            print("THE TOTAL NUMBER : '{}' ".format(counter))
        else:
            print('THE TOTAL NUMBER : {}'.format(counter))
            
        print('\n')