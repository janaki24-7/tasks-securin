def undoom_dice(d1,d2):
    i_p=calip(d1,d2)
    new_Die_A=[]
    new_Die_B=d2.copy()
    for i in d1:
        new_Die_A.append(min(4,i))
    f_p=calip(new_Die_A,new_Die_B)
    if(i_p==f_p):
       return new_Die_A,new_Die_B

def calip(d1,d2):
    n=6
    sum=0
    p={}
    for i in range(1,len(d1)+1):
        for j in range(1,len(d2)+1):
            sum=i+j
            p[sum]=p.get(sum,0)+1
    #print(p)
    for k in p:
        p[k]=p[k]/6**2
    #print(p)
    return p
Die_A=[1,2,3,4,5,6]
Die_B=[1,2,3,4,5,6]
New_Die_A,New_Die_B=undoom_dice(Die_A,Die_B)
print(New_Die_A)
print(New_Die_B)
