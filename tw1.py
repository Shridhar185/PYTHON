""" #implement a queue using a list and functions
#1.add to queue
#2.delete item in queue
#3.display front and rear
#4.display the queue


def enq(Q):
    item=input("enter value: ")
    Q.append(item)
def deq(Q):
     x=Q.pop(0)   #remove first element and returns 
     print("the pop ele is: ",x) 
def qfront(Q):
     a=Q[0]
     print("the front ele:",a)
def qrear(Q):
    z=Q[len(Q)-1]
    print("the rear ele: ",z)
def disp(Q):
    if(len(Q)==0):
        print("queue is empty ")
    else:
        print("the queue is: ",Q)
def main():
    Q=[]
    while(1):
        print("1.enque\n2.deque\n3.qfront\n4.qrear\n5.display\n6.exit")
        opt=int(input("enter your option "))
        if opt==1:
            enq(Q)
        elif opt==2:
            deq(Q)
        elif opt==3:
            qrear(Q)
        elif opt==4:
            qfront(Q)
        elif opt==5:
            disp(Q)
        else:
            print("invalid option ")
            break
 
if __name__=='__main__':
    main()
         """








from collections import defaultdict
graph = defaultdict(list)

def addEdge(u, v):
    graph[u].append(v)

def dfs(start, goal, depth):
    print(start, end=" -> ")
    if start == goal:
        return True
    if depth <= 0:
        return False
    for i in graph[start]:
        if dfs(i,  goal, depth-1):
            return True
    return False


def dfid(start, goal, maxDepth):
    #print("Start node : ", start, " Goal node : ", goal)
    for i in range(maxDepth):
        print("\nDFS at level : ", i+1)
        print("Path : ", end='')
        isPathFound = dfs(start, goal, i)
    if isPathFound:
        print("\nGoal node found!")
        return
    else:
        print("\nGoal node not found!")

 
addEdge('A', 'B')
addEdge('A', 'C')
addEdge('B', 'D')
addEdge('B', 'E')
addEdge('C', 'F')
addEdge('C', 'G')
dfid('A', 'G', 3)