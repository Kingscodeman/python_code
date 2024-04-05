import csv
import datetime
import copy
count=1
with open('C:/python/out_put text/lock.csv')as ff:
    obj1=csv.reader(ff)
    datalis=list(obj1)
print('It will be save to: {}'.format(datalis[0][0]))
change=input('if you want to change the postion, enter c:')
if(change=='c'):
    file=input('enter here:')
    temp=[file]
    with open('C:/python/out_put text/lock.csv','w')as f:
        obj=csv.writer(f)
        obj.writerow(temp)
else:
    
    file=datalis[0][0]  #revise
mem=['NO','Date','Subject','Item','Amount']
date=datetime.datetime.now().strftime('%Y%m%d')
fin=[]
add=input('if it is a new file ,please enter n:')
if(add=='n'):
    fin.append(mem)
   
        
else:
    with open(file)as wte:
        re1=csv.reader(wte)
        data1=list(re1)
    data_len=len(data1)-1
    count=int(data1[data_len][0])+1
   

amount_i=0
amount_s=0


while True:
    mem2=[]
    while True:
        print('\n')
        print('please enter your subject:')
        model=input('Income plaese enter 1 , Expense please enter 2:')
        item=input('please enter your item:')
        money=int(input('please enter your amount:'))
        
        if(model=='1'):
            pr='Income'
            money=money
        else:
            pr='Expense'
            money=-money
        print('\n')
        print('Subject:{}  ,Item:{}  ,Amount:{}'.format(pr,item,money))
        judge=input('if it is correct,please enter y, not enter n:')
        if(judge=='y'):
            print('ADD!')
            break
        else:
            continue
        
    mem2.append(count)
    mem2.append(date)
    mem2.append(pr)
    mem2.append(item)
    mem2.append(money)
    mem3=copy.deepcopy(mem2)
    fin.append(mem3)
    mem2.clear()
    
    stop=input('if you want to stop,enter s:')
    if(stop=='s'):
        break
    count+=1
    
if(add=='n'):
    use='w'
else:
    use='a'
    
with open (file,use,newline='')  as r:
    csvobj=csv.writer(r)
    csvobj.writerows(fin)

#print(fin)

with open(file)as we:
    re=csv.reader(we)
    data=list(re)

print('\n')
print('INCOME  EXPENSE  LIST :')
it=0
it2=0
b=1
for d in data:
    for m in d:
        if(m=='Income'):
            pick11=data[b][4]
            amount_i+=int(pick11)
            it+=1
            b+=1
        elif(m=='Expense'):
            pick22=int(data[b][4])
            amount_s+=pick22
            it2+=1
            b+=1
        else:
            pass
    
            
        print('{:<14}'.format(m),end='')
          
    print('\n') 
    
for y in range(64):
    print('_',end='')
print('\n')
print('Total Income : {:>12} , it has {:>8} item'.format(amount_i,it))
print('Total Expense : {:>12} , it has {:>8} item'.format(amount_s,it2))
print('Fin Total : {:>12}'.format(amount_i+amount_s))