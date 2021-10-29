xc=int(input("Enter the capacity of x"))
yc=int(input("Enter the capacity of y"))
xg=int(input("Enter the goal state of x"))
yg=int(input("Enter the goal state of y"))

bfs_tree={}

ol,cl=[(0,0)],[]

while((xg,yg) not in cl and len(ol)!=0):
    x,y=ol.pop()
    l,l1=[],[]
    if(x==xg and y==yg):
        cl.append((x,y))
        break
    bfs_tree[(x,y)]=[]
    if(x<xc):
        l1.append((xc,y))
    if(y<yc):
        l1.append((xc,yc))
    if(x>0):
        l1.append((0,y))
    if(y>0):
        l1.append((x,0))
    if(x>0 and y<yc):
        if(x+y>yc):
            l1.append((x+y-yc,yc))
        else:
            l1.append((0,x+y))
    if(y>0 and x<xc):
        if(x+y>xc):
            l1.append((xc,x+y-xc))
        else:
            l1.append((x+y,0))
    for i in l1:
        if (i not in ol) and (i not in cl):
            l.append(i)
            ol.append(i)
    cl.append((x,y))
    print('open nodes are ', ol)
    print("closed nodes are ", cl)
    print()
