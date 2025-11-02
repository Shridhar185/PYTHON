stack=[]
top=-1
def push(data):
    global top
    top+=1
    print("the pushed element",data)
    stack.append(data)
def pop():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        print("the popped element",stack[top])
        top-=1
def displayStack():
    print("the elements in stack are: ")
    for i in range(top+1):
        print(stack[i],end=' ')
def main():
    while True:
        print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter number to push: ")
            push(data)
        elif choice == 2:
            pop()
        elif choice == 3:
            displayStack()
        elif choice == 4:
            break
        else:
            print("Invalid choice")
if __name__=='__main__':
    main()
 