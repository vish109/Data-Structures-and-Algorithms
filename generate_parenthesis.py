
result = []
def back_track(n,o,c,temp):
    if(o==n and c==n):
        result.append(temp)
    if(o<n):
        back_track(n,o+1,c,temp+"(")
    if(c<o):
        back_track(n,o,c+1,temp+")")


n=3
back_track(n,0,0,"")
print(result)