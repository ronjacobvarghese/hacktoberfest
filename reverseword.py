def findthereverseword(a):
    ans = a.split()
    print(ans)
    #for i in range(0,len(ans)):
        # t=ans[i]
        # ans[i]=t[::-1]
    re=[]
    for i in ans:
        re.append(i[::-1])
    p=' '.join(ans)
    print(p)


a = input()
findthereverseword(a)