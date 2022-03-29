if __name__=='__main__':
    web_list=[]
    with open('./phishing-domains-ACTIVE.txt','r') as f:
        for line in f.readlines():
            web_list.append(str(line))
    i=int(0)
    p=0
    new=[]
    while i<len(web_list):
        new.append(web_list[i])
        i+=1
        if i-p*3000==3000 or i==len(web_list)-1:
            p=p+1
            target='phishing'+str(p)+'.txt'
            with open(target,'a') as fout:
                for t in range(0,len(new)-1):
                    fout.write(new[t])
            new=[]

