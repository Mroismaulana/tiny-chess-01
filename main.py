import sys
A="PNBRQKpnbrqk";V=[100,320,330,500,900,50000];H={}
B=[13]*120
for i in range(64):B[21+i%8+(i//8)*12]=12
for f,pc in enumerate([9,7,8,10,11,8,7,9]):B[105+f]=pc
for f in range(8):B[93+f]=6;B[33+f]=0
for f,pc in enumerate([3,1,2,4,5,2,1,3]):B[21+f]=pc
def G(b,p):
 c=[];q=[]
 for s in range(120):
  x=b[s]
  if x<12 and x//6==p:
   t=x%6
   if t==0:
    d=12 if p==0 else -12
    if 0<=s+d<120 and b[s+d]==12:
     q.append((s,s+d))
     if (p==0 and 33<=s<=40)or(p==1 and 93<=s<=100):
      if 0<=s+2*d<120 and b[s+2*d]==12:q.append((s,s+2*d))
    for cd in(11,13)if p==0 else(-11,-13):
     z=s+cd
     if 0<=z<120 and b[z]<12 and b[z]//6!=p:c.append((s,z))
   elif t==1:
    for d in(-25,-23,-14,-10,10,14,23,25):
     z=s+d
     if 0<=z<120:
      if b[z]==12:q.append((s,z))
      elif b[z]<12 and b[z]//6!=p:c.append((s,z))
   elif t in(2,3,4):
    ds=(-13,-11,11,13)if t==2 else(-12,-1,1,12)if t==3 else(-13,-12,-11,-1,1,11,12,13)
    for d in ds:
     z=s+d
     while 0<=z<120 and b[z]==12:q.append((s,z));z+=d
     if 0<=z<120 and b[z]<12 and b[z]//6!=p:c.append((s,z))
   elif t==5:
    for d in(-13,-12,-11,-1,1,11,12,13):
     z=s+d
     if 0<=z<120:
      if b[z]==12:q.append((s,z))
      elif b[z]<12 and b[z]//6!=p:c.append((s,z))
 return c+q
def Mk(b,p,m):
 s,z=m;r=b[:];r[z]=r[s];r[s]=12
 if r[z]%6==0:
  if p==0 and z>=105:r[z]=4
  if p==1 and z<=28:r[z]=10
 return r
def Ev(b,p):
 mk=4 if p==0 else 10;ok=10 if p==0 else 4
 if mk not in b:return -999999
 if ok not in b:return 999999
 return sum(V[b[s]%6]*(1 if b[s]//6==p else -1) for s in range(120) if b[s]<12)
def S(b,p,d,a=-999999,z=999999):
 k=(tuple(b),p,d)
 if k in H:return H[k]
 if d<=0:return Ev(b,p)
 ms=G(b,p)
 if not ms:return -999999 if p==0 else 999999
 v=-999999
 for m in ms:
  v=max(v,-S(Mk(b,p,m),1-p,d-1,-z,-a))
  if v>=z:break
  a=max(a,v)
 H[k]=v;return v
def Bf(b,p,dp=5):
 bm=None;bs=-999999
 for d in range(2,dp+1):
  for m in G(b,p):
   v=-S(Mk(b,p,m),1-p,d-1)
   if v>bs:bs=v;bm=m
 return bm
def U():
 b=B[:];p=0
 while 1:
  try:l=input()
  except:break
  if l=="quit":break
  if l=="uci":print("id name TinyChess\nauthor AI\nuciok")
  elif l=="isready":print("readyok")
  elif l=="ucinewgame":b=B[:];p=0;H.clear()
  elif l.startswith("position"):
   b=B[:];p=0
   if"moves"in l:
    for mv in l.split("moves")[1].split():
     s=21+(ord(mv[0])-97)+(ord(mv[1])-49)*12;z=21+(ord(mv[2])-97)+(ord(mv[3])-49)*12
     b=Mk(b,p,(s,z));p=1-p
  elif l.startswith("go"):
   dp=5
   if"depth"in l:dp=int(l.split("depth")[1].split()[0])
   m=Bf(b,p,dp)
   if m:
    a=(m[0]-21)%12;r=(m[0]-21)//12;c=(m[1]-21)%12;k=(m[1]-21)//12
    print(f"bestmove {chr(97+a)}{chr(49+r)}{chr(97+c)}{chr(49+k)}")
   else:print("bestmove 0000")
U()