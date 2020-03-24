n = int(input())
dic = {}
for i in range(n):
    s = input().split(';')
    if s[0] not in dic:
        dic[s[0]] = [0,0,0,0,0]
    if s[1] not in dic:
        dic[s[1]] = [0,0,0,0,0]
    
    dic[s[0]][0] +=1
    dic[s[1]][0] +=1
#print(dic)    
    if s[2] == 'loss':
        s.insert(0,s.pop(1))
    if s[2] == 'win' or s[2] == 'loss':
        dic[s[0]][1]+=1
        dic[s[0]][4]+=3
        dic[s[1]][3]+=1
    if s[2] == 'draw':
        dic[s[0]][2]+=1
        dic[s[0]][4]+=1
        dic[s[1]][2]+=1
        dic[s[1]][4]+=1
#print(dic)            
list_1 = list(sorted(dic))
#print(list_1)
dic_1 = {i:dic[i] for i in list_1}
#print(dic_1)

for i in dic_1:
    l = sorted(dic_1,key=lambda x : dic_1 [x][4],reverse=True)

#print(l)
print("{:<23} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} |".format("Team","MP","W","D","L","P"))

for i in l:
    if i in dic_1:
        print("{:<23} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} |".format(i,dic_1[i][0],dic_1[i][1],dic_1[i][2],dic_1[i][3],dic_1[i][4]))
