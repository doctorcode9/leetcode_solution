primary = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

s= 'LVIII'




ans = 0 
char =''
for i in range(len(s)):
    if i< len(s) - 1 and primary[s[i]] < primary[s[i+1]]:
        ans -= primary[s[i]]
    else:
        ans += primary[s[i]]
    print(ans)
print(ans)

