d={}
print('wellcome to the 高手系統')
while True:
    print('1.creat new')
    print('2.print out all word')
    print('3.translate e to c')
    print('4.translate c to e')
    print('5.test')
    print('6.leave')
    op=input('type in the choice("number")')
    if op=='6':
        break
    elif op=='1':
        while True:
            voc=input('type in english word("press 0 to leave")')
            if voc=='0':
                break
            if voc not in d:
                vocc=input('type in chinese')
                d[voc]=vocc
            else:
                print('it is here')
    
    
    
    
    elif op=='2':
        #s=sorted(d)
        for i in d:
            print(i,":",d[i])
    
    
    
    
    
    elif op=='3':
        while True:
            voc=input('type in english word("press 0 to leave")')
            if voc=='0':
                break
            if voc in d:
                print(voc,'chinese is:',d[voc])
            else:
                print('no word...')
    
    
    
    
    
    
    
    
    
    elif op=='4':
        
        while True:
            got=True
            ch=input('enter chinese word:')
            for k,v in d.items():
                if ch=='0':
                    break
                if ch in v:
                    print(ch,'english is:',k)
                    got=True
            if got==False:
                print('no word')
    elif op=='5':
        score=0
        for k,v in d.items():
            print(v,':')
            ans=input('enter in english:')
            if ans==k:
                score+=1
                print('good')
            else:
                print('wrong')
        print(score)























