# Node 클래스를 만들어줌.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# 이중 연결 리스트 클래스를 만들어줌
class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)     # 구현의 편의를 위해 dummy값 넣어줌
        self.head = self.END
        self.tail = self.END

    def push_front(self, new_data):     #원소의 첫 번째 위치에 넣어줌
        new_node = Node(new_data)       # 새로운 노드를 만들어줌
        new_node.next = self.head       # 새로운 노드의 next값을 head로 바꿔줌

        self.head.prev = new_node   #이전 head의 prev값을 바꿈
        self.head = new_node    # head값 바꿔줌
        new_node.prev = None

    def push_back(self, new_data):  #원소를 끝 위치에 넣어줌
        if self.begin() == self.end():  #만약 원소가 비어있다면
            self.push_front(new_data) # 맨 앞에 원소를 넣어주는 것과 로직이 같음.
        
        else:
            # 여기서 tail은 dummy
            new_node = Node(new_data)   #새로운 노드를 만들어줌
            new_node.prev = self.tail.prev  # 새로운 노드의 prev 값을 맨 끝 dummy의 prev로 변경해준 뒤
            self.tail.prev.next = new_node  # 맨 끝 dummy의 next로 새로운 노드를 연결햊고
            new_node.next = self.tail       # 새로운 노드의 next값을 맨 끝 dummy값으로 바꿔주고
            self.tail.prev = new_node       # 맨 끝 dummy의 prev값을 새로운 노드로 변경해줌.

    def erase(self,node):
        next_node = node.next

        if node == self.begin():    # 만약 head가 삭제되어야한다면
            temp = self.head    # temp에 head값 넣음
            temp.next.prev = None   # 새로 head가 될 노드의 prev값 없애줌
            self.head = temp.next   # head값을 새로 갱신해주고
            temp.next = None        # 이전 head의 next값 지워줌

        else:                               # head가 삭제되는 것이 아니라면
            node.prev.next = node.next      # 바로 전 노드의 next값을 바꿔주고
            node.next.prev = node.prev      # 바로 다음 노드의 prev값을 바꿔주고
            node.prev = None            # node.prev 연결고리 끊기
            node.next = None            # node.next 연결고리 끊기

        return next_node # 근데 위에서 node.next를 끊어버려서 literator로 next로 찾기 위해 next_node를 저장해두는 것
    
    def insert(self, node, new_data):
        if node == self.end():      # node가 맨 끝 위치에 있다면
            self.push_back(new_data)    # 맨 뒤에 원소 추가
        
        elif node == self.begin():      # node가 맨 앞 위치에 있다면
            self.push_front(new_data)   # 맨 앞에 원소 추가
        
        else:
            new_node = Node(new_data)   # 새로운 노드 데이터 만들어줌
            new_node.prev = node.prev   # 새로운 노드의 prev값을 node의 prev값으로 하고
            new_node.next = node        # 새로운 노드의 next값을 node로 하고
            node.prev.next = new_node   # node의 prev의 next값을 새로운 노드로 변경하고
            node.prev = new_node # node의 prev값을 새로운 노드로 변경함.

    def begin(self):
        return self.head
    
    def end(self):
        return self.tail

# 우선 내가 문제보면서 몰랐던 것. 화살표를 어떻게 지정해주는지, 그리고 각 함수에 변수를 어떻게 넣어야하는지

# 변수 선언 및 입력
n, m = tuple(map(int,input().split()))
s = input() # codet

l = DoublyLinkedList() # l은 빈 값으로 지정해줌
for c in s:
    l.push_back(c) #빈 리스트이기 때문에 c를 넣어줌
# [c,o,d,e,t]

# iterator 정의 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
it = l.end() # 맨 끝 값을 it로 정의해줌

# 이제 명령어 넣음 . L,R,D,P 같은 거
for _ in range(m):
    command = input()

    if command.startswith("L"):
        if it != l.begin(): # 빵들의 맨 앞이 아니라면
            it = it.prev    # 앞으로 이동
    
    elif command.startswith("R"):
        if it != l.end(): # 빵들의 맨 끝이 아니라면 
            it = it.next    # 뒤로 이동
    
    elif command.startswith("D"):
        if it == l.end():
            pass
        else:
            it = l.erase(it) # 우선 오른쪽에 있는 걸 없앰
    else:
        _, c = command.split() 
        l.insert(it,c)      # 가르키는 위치에 문자 c를 ㅊㄱ

# 출력
it = l.begin()
while it != l.end():
    print(it.data,end="")
    it = it.next





