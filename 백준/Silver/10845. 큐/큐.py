from collections import deque
import sys

dq = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        dq.append(command[1])
        
    elif command[0] == 'pop':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(len(dq))
    
    elif command[0] == 'empty':
        print(0 if dq else 1)
    
    elif command[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    
    elif command[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)