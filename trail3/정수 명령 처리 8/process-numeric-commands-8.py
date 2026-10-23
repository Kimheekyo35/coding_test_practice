# N = int(input())
# command = []
# A = []
# revers_A = []

# # 해당 코드는 알고리즘의 성능 측면엣 비효율적임
# # 리스트는 원소들이 메모리사에 연속적으로 저장되는 구조를 가짐. 따라서 pop, append는 O(1)로 처리 가능.

# for _ in range(N):
#     line = input().split()
#     command.append(line[0])

#     if line[0] =="push_front":
#         # list(reversed(A)) 를 하면 모든 원소를 순회하며 새로운 리스트를 재생성하므로 O(N)만큼이 걸림
#         revers_A = list(reversed(A))
#         revers_A.append(int(line[1]))
#         # 근데 이걸 한번 더 해주므로 또 O(N)만큼이 걸리게 됨.
#         A = list(reversed(revers_A))
#     elif line[0] == "push_back":
#         A.append(int(line[1]))
#     elif line[0] == "pop_front":
#         # 이거 역시 맨 앞 원소를 꺼내고, 뒤에 것들을 앞으로 당겨야하기때문에 O(N)이 들어감
#         print(A.pop(0))
#     elif line[0] == "pop_back":
#         print(A.pop(-1))
#     elif line[0] == "size":
#         print(len(A))
#     elif line[0] =="empty":
#         if len(A)==0:
#             print(1)
#         else:
#             print(0)
#     elif line[0] == "front":
#         print(A[0])
#     else:
#         print(A[-1])

# Node 클래스를 만들어줌
class Node:
    def __init__(self,data):
        self.data = data
        self.head = None
        self.tail = None
    

    # 이중 연결 리스트 클래스를 만들어줌.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data): #원소를 첫 번째 위치에 넣어줌
        new_node = Node(new_data) # 새로운 노드를 만들어줌
        new_node.next = self.head # 새로운 노드의 next값을 head로 바꿔줌

        if self.head != None: #만약 기존 head가 비어있지않다면
            self.head.prev = new_node #이전 head의 prev값을 바꾼뒤
            self.head = new_node #head를 new_node로 바꿈
            new_node.prev = None
        
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

        self.node_num += 1

    def push_back(self,new_data):   # 원소를 맨 끝에 넣어줌
        new_node = Node(new_data)   # 새로운 node값을 만들어줌
        new_node.prev = self.tail   # 새로운 노드의 prev값을 tail로 바꿔줌

        if self.tail != None:  # 기존 리스트가 비어있지 않다면
            self.tail.next = new_node # 기존 tail의 next값을 new_node라 지정
            self.tail = new_node  # 기존 tail의 값을 새로운 노드로 바꿔줌
            new_node.next = None  # 이제 new_node가 tail이 되었으니 그 다음값은 None으로 지정

        else:                    # 기존 리스트가 비어있다면
            self.tail = new_node    # tail, head를 새롭게 지정
            self.head = new_node
            new_node.next = None

        self.node_num += 1

    def pop_front(self):        # 첫 번째 수를 뺴면서 동시에 출력까지
        
        if self.head == None:   # 만약 처음 값이 비어있다면.. 
            print("List is empty")
        
        elif self.head.next == None: #노드가 하나 남았다면
            temp = self.head

            self.head = None # head값을 None으로 바꿔주고
            self.tail = None # tail값을 None으로 바꿔주고
            self.node_num = 0 # 원소의 수도 0개로 변경해줌
            
            return temp.data
#[10]-[20]-[30] 이라는 가정하에
        else:
            temp = self.head
            temp.next.prev = None   # 새로 head가 될 노드의 prev값 지워줌, 안 끊으면 temp.next.prev 은 head값이 계속 나옴
            self.head = temp.next   # head값을 새로 갱신해줌
            temp.next = None # 이전 head의 next값을 지워줌, temp의 다음값도 끊는 것

            self.node_num -= 1
            return temp.data

    def pop_back(self):
        if self.tail == None:
            print("List is empty")
        elif self.tail.prev == None: # 노드가 하나 남았다면, pop하고 다 없애줘야하니까 head,tail을 None으로 둠
            temp = self.tail

            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        else:
            temp = self.tail
            temp.prev.next = None # -> 이방향 끊음
            self.tail = temp.prev
            temp.prev = None # <- 이 방향 끊음

            self.node_num -= 1
            return temp.data

    def size(self):
        return self.node_num

    def empty(self):
        return self.node_num == 0


    # 맨앞 숫자 갖고 오는 것
    def front(self):
        if self.head == None:
            print("List is empty")
        else:
            return self.head.data

    # 맨 뒤의 값 가져오는 것
    def back(self):
        if self.tail == None:
            print("Lit is empty")
        else:
            return self.tail.data

n = int(input())
l = DoublyLinkedList()

for _ in range(n):
    command = input()
    if command.startswith("push_front"):
        x = int(command.split()[1])
        l.push_front(x)
    elif command.startswith("push_back"):
        x = int(command.split()[1])
        l.push_back(x)
    elif command == "pop_front":
        print(l.pop_front())
    elif command == "pop_back":
        print(l.pop_back())
    elif command == "size":
        print(l.size())
    elif command == "empty":
        print(1 if l.empty() else 0)
    elif command == "front":
        print(l.front())
    else:
        print(l.back())
