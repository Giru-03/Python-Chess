def pawn1(x,p,pa1):
    list=[]
    if p[x[0]-1][x[1]]=='  ' or p[x[0]-1][x[1]]==' ':
        list.append((x[0],x[1]+1))
    else:
        pass
    if p[x[0]-1][x[1]-1]!='  ' and p[x[0]-1][x[1]-1]!=' ' and p[x[0]-1][x[1]-1] not in pa1:
        list.append((x[0],x[1]))
    elif x[1]!=7:
        if p[x[0]-1][x[1]+1]!='  ' and p[x[0]-1][x[1]+1]!=' ' and p[x[0]-1][x[1]+1] not in pa1:
            list.append((x[0],x[1]+2))
    else:
        pass
    if x[0]==6 and len(list)!=0:
        if p[4][x[1]]=='  ' or p[4][x[1]]==' ':
            list.append((5,x[1]+1))
    else:
        pass
    if len(list)==0:
        return None
    else:
        return list
def pawn2(b,c,p,pa):
    if p[c[0]-1][c[1]-1]!='  ' and p[c[0]-1][c[1]-1]!=' ':
        pa.append(p[c[0]-1][c[1]-1])
    else:
        pass
    p[c[0]-1][c[1]-1]=p[b[0]-1][b[1]-1]
    if b[1] in [3,6]:
        p[b[0]-1][b[1]-1]=' '
    else:
        p[b[0]-1][b[1]-1]='  '
def pawn3(x,p,pa2):
    list=[]
    if p[x[0]+1][x[1]]=='  ' or p[x[0]+1][x[1]]==' ':
        list.append((x[0]+2,x[1]+1))
    else:
        pass
    if p[x[0]+1][x[1]-1]!='  ' and p[x[0]+1][x[1]-1]!=' ' and p[x[0]+1][x[1]-1] not in pa2:
        list.append((x[0]+2,x[1]))
    elif x[1]!=7:
        if p[x[0]+1][x[1]+1]!='  ' and p[x[0]+1][x[1]+1]!=' ' and p[x[0]+1][x[1]+1] not in pa2:
            list.append((x[0]+2,x[1]+2))
    else:
        pass
    if x[0]==1 and len(list)!=0:
        if p[3][x[1]]=='  ' or p[3][x[1]]==' ':
            list.append((4,x[1]+1))
    else:
        pass
    if len(list)==0:
        return None
    else:
        return list

def knight1(x,p,pa1):
    list=[]
    list.append((x[0],x[1]+3))
    list.append((x[0]+2,x[1]+3))
    list.append((x[0],x[1]-1))
    list.append((x[0]+2,x[1]-1))
    list.append((x[0]-1,x[1]+2))
    list.append((x[0]-1,x[1]))
    list.append((x[0]+3,x[1]+2))
    list.append((x[0]+3,x[1]))
    for i in list:
        if i[0]<1:
            list[list.index(i)]=0
        elif i[0]>8:
            list[list.index(i)]=0
        elif i[1]<1:
            list[list.index(i)]=0
        elif i[1]>8:
            list[list.index(i)]=0
        elif p[i[0]-1][i[1]-1] in pa1:
            list[list.index(i)]=0
        else:
            pass
    for i in range(list.count(0)):
        list.remove(0)
    return list


def rook1(x,p,pa2,pa1):
    list=[]
    for i in range(x[0]-1,0,-1):
        list.append((i,x[1]))
        if p[i-1][x[1]-1] in pa2:
            list.pop()
            break
        elif p[i-1][x[1]-1] in pa1:
            break
        else:
            pass
    for i in range(x[0]+1,9):
        list.append((i,x[1]))
        if p[i-1][x[1]-1] in pa2:
            list.pop()
            break
        elif p[i-1][x[1]-1] in pa1:
            break
        else:
            pass
    for i in range(x[1]-1,0,-1):
        list.append((x[0],i))
        if p[x[0]-1][i-1] in pa2:
            list.pop()
            break
        elif p[x[0]-1][i-1] in pa1:
            break
        else:
            pass
    for i in range(x[1]+1,8,1):
        list.append((x[0],i))
        if p[x[0]-1][i-1] in pa2:
            list.pop()
            break
        elif p[x[0]-1][i-1] in pa1:
            break
        else:
            pass
    if len(list)==0:
        return None
    else:
        return list

def bishop1(x,p,pa2,pa1):
    list=[]
    count=x[1]
    for i in range(x[0]-1,0,-1):
        list.append((i,count-1))
        if count-2>=0:
            if p[i-1][count-2] in pa2:
                list.pop()
                break
            elif p[i-1][count-2] in pa1:
                break
            else:
                pass
        else:
            list.pop()
            break
        count-=1
    count=x[1]
    for i in range(x[0]+1,9):
        list.append((i,count-1))
        if count-2>=0:
            if p[i-1][count-2] in pa2:
                list.pop()
                break
            elif p[i-1][count-2] in pa1:
                break
            else:
                pass
        else:
            list.pop()
            break
        count-=1
    count=x[1]
    for i in range(x[0]-1,0,-1):
        list.append((i,count+1))
        if count<=7:
            if p[i-1][count] in pa2:
                list.pop()
                break
            elif p[i-1][count] in pa1:
                break
            else:
                pass
        else:
            list.pop()
            break
        count+=1
    count=x[1]
    for i in range(x[0]+1,9):
        list.append((i,count+1))
        if count<=7:
            if p[i-1][count] in pa2:
                list.pop()
                break
            elif p[i-1][count] in pa1:
                break
            else:
                pass
        else:
            list.pop()
            break
        count+=1
    if len(list)==0:
        return None
    else:
        return list

def king1(x,p,pa1):
    list=[]
    list.append((x[0]-1,x[1]))
    list.append((x[0]+1,x[1]))
    list.append((x[0],x[1]-1))
    list.append((x[0],x[1]+1))
    list.append((x[0]-1,x[1]-1))
    list.append((x[0]-1,x[1]+1))
    list.append((x[0]+1,x[1]-1))
    list.append((x[0]+1,x[1]+1))
    for i in list:
        if i[0]<1:
            list[list.index(i)]=0
        elif i[0]>8:
            list[list.index(i)]=0
        elif i[1]<1:
            list[list.index(i)]=0
        elif i[1]>8:
            list[list.index(i)]=0
        elif p[i[0]-1][i[1]-1] in pa1:
            list[list.index(i)]=0
        else:
            pass
    for i in range(list.count(0)):
        list.remove(0)
    if len(list)==0:
        return None
    else:
        return list
    
def display(a,b,c,d,e,f,g,h):
    print('\t\t'+'\u0332'+('\t\t'+'\u0332'*16)*2+('      '+'\u0332'*8))
    for j in [a,b,c,d,e,f,g,h]:
        print('\t\t',end='|')
        for k in range(8):
            print('\u0332'+' '+'\u0332'+str(j[k])+'\u0332'+' ',end='|'+'\u0332'*5)
        print()
a=['♜','♞','♝','♛','♚','♝','♞','♜']
b=['♟','♟','♟','♟','♟','♟','♟','♟']
c=['  ','  ',' ','  ','  ',' ','  ','  ']
d=['  ','  ',' ','  ','  ',' ','  ','  ']
e=['  ','  ',' ','  ','  ',' ','  ','  ']
f=['  ','  ',' ','  ','  ',' ','  ','  ']
g=['♙','♙','♙','♙','♙','♙','♙','♙']
h=['♖','♘','♗','♕','♔','♗','♘','♖']
display(a,b,c,d,e,f,g,h)
p=[a,b,c,d,e,f,g,h]
print("  ")
p1=input("Enter the name of first player:")
p2=input("Enter the name of second player:")
pa1=['♙','♔','♕','♗','♘','♖']
pa2=['♟','♚','♛','♝','♞','♜']
pa3=[]
pa4=[]
z1=True
while z1==True:
    z2=True
    while z2==True:
        x=input(f"{p1}, Enten your chance (King, Queen, Rook, Bishop, Knight, or Pawn):")
        y=list(map(int,input("Enter the position (r,c):").split(',')))
        if x.lower()=='pawn' and p[y[0]-1][y[1]-1]=='♙':
            a1=pawn1([y[0]-1,y[1]-1],p,pa1)
            print("The possible options are:",a1)
        elif x.lower()=='knight' and p[y[0]-1][y[1]-1]=='♘':
            a1=knight1([y[0]-1,y[1]-1],p,pa1)
            print("The possible options are:",a1)
        elif x.lower()=='rook' and p[y[0]-1][y[1]-1]=='♖':
            a1=rook1([y[0],y[1]],p,pa1,pa2)
            print("The possible options are:",a1)
        elif x.lower()=='bishop' and p[y[0]-1][y[1]-1]=='♗':
            a1=bishop1([y[0],y[1]],p,pa1,pa2)
            print("The possible options are:",a1)
        elif x.lower()=='queen' and p[y[0]-1][y[1]-1]=='♕':
            a1=bishop1([y[0],y[1]],p,pa1,pa2)+rook1([y[0],y[1]],p,pa1,pa2)
            print("The possible options are:",a1)
        elif x.lower()=='king' and p[y[0]-1][y[1]-1]=='♔':
            a1=king1([y[0],y[1]],p,pa1)
            print("The possible options are:",a1)
        else:
            print("wrong input")
            continue
        if a1 is None:
            continue
        z=tuple(map(int,input("Enter the position you want to move (r,c):").split(',')))
        if z in a1:
            pawn2(y,z,p,pa4)
            if x.lower()=='pawn' and z[0]==1:
                m=True
                while m==True:
                    z12=input("Enten your choice (Queen, Rook, Bishop, or Knight):")
                    if z12.lower()=='queen':
                        p[z[0]-1][z[1]-1]='♕'
                        m=False
                    elif z12.lower()=='rook':
                        p[z[0]-1][z[1]-1]='♖'
                        m=False
                    elif z12.lower()=='knight':
                        p[z[0]-1][z[1]-1]='♘'
                        m=False
                    elif z12.lower()=='bishop':
                        p[z[0]-1][z[1]-1]='♗'
                        m=False
                    else:
                        print('Wrong input')
            else:
                pass
            display(a,b,c,d,e,f,g,h)
            print(p1,pa3)
            print(p2,pa4)
            z2=False

    if '♔' in pa3:
        print(p2,"Wins")
        break
    elif '♚' in pa4:
        print(p1,"Wins")
        break
    elif len(pa4)==15 and len(pa3)==15:
        print("Tie")
        break
    else:
        pass
    print('  ')
    z3=True
    while z3==True:
        q=input(f"{p2}, Enten your chance (King, Queen, Rook, Bishop, Knight, or Pawn):")
        r=list(map(int,input("Enter the position (r,c):").split(',')))
        if q.lower()=='pawn' and p[r[0]-1][r[1]-1]=='♟':
            a1=pawn3([r[0]-1,r[1]-1],p,pa2)
            print("The possible options are:",a1)
        elif q.lower()=='knight' and p[r[0]-1][r[1]-1]=='♞':
            a1=knight1([r[0]-1,r[1]-1],p,pa2)
            print("The possible options are:",a1)
        elif q.lower()=='rook' and p[r[0]-1][r[1]-1]=='♜':
            a1=rook1([r[0],r[1]],p,pa2,pa1)
            print("The possible options are:",a1)
        elif q.lower()=='bishop' and p[r[0]-1][r[1]-1]=='♝':
            a1=bishop1([r[0],r[1]],p,pa2,pa1)
            print("The possible options are:",a1)
        elif q.lower()=='queen' and p[r[0]-1][r[1]-1]=='♛':
            a1=bishop1([r[0],r[1]],p,pa2,pa1)+rook1([r[0],r[1]],p,pa2,pa1)
            print("The possible options are:",a1)
        elif q.lower()=='king' and p[r[0]-1][r[1]-1]=='♚':
            a1=king1([r[0],r[1]],p,pa2)
            print("The possible options are:",a1)
        else:
            print("Wrong input")
            continue
        if a1 is None:
            continue
        s=tuple(map(int,input("Enter the position you want to move (r,c):").split(',')))
        if s in a1:
            pawn2(r,s,p,pa3)
            if x.lower()=='pawn' and z[0]==8:
                m=True
                while m==True:
                    z12=input("Enten your choice (Queen, Rook, Bishop, or Knight):")
                    if z12.lower()=='queen':
                        p[z[0]-1][z[1]-1]='♛'
                        m=False
                    elif z12.lower()=='rook':
                        p[z[0]-1][z[1]-1]='♜'
                        m=False
                    elif z12.lower()=='knight':
                        p[z[0]-1][z[1]-1]='♞'
                        m=False
                    elif z12.lower()=='bishop':
                        p[z[0]-1][z[1]-1]='♝'
                        m=False
                    else:
                        print('Wrong input')
            else:
                pass
            display(a,b,c,d,e,f,g,h)
            print(p1,pa4)
            print(p2,pa3)
            z3=False
    if '♔' in pa3:
        print(p2,"Wins")
        break
    elif '♚' in pa4:
        print(p1,"Wins")
        break
    elif len(pa4)==15 and len(pa3)==15:
        print("Tie")
        break
    else:
        pass







        
    
