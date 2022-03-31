if __name__=='__main__':
    web_list=[]
    time=8000
    with open('./phishing-domains-ACTIVE.txt','r') as f:
        for line in f.readlines():
            web_list.append(str(line))
    i=int(0)
    p=0
    new=[]
    while i<len(web_list):
        new.append(web_list[i])
        i+=1
        if i-p*time==time or i==len(web_list)-1:
            p=p+1
            target=str(p)+'.txt'
            with open(target,'a') as fout:
                for t in range(0,len(new)-1):
                    fout.write(new[t])
            new=[]

