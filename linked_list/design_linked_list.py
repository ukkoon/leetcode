class MyLinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index>self.size-1:
            return -1

        cur = self.head
        for _ in range(index):        
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)        

    def addAtTail(self, val: int) -> None:
       self.addAtIndex(self.size,val)        

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return

        if index==0:
            self.head=ListNode(val,self.head)
            
        dummy = ListNode(None,self.head)
        for _ in range(index):
            dummy = dummy.next
        dummy.next=ListNode(val,dummy.next)
        self.size+=1        

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size-1:
            return

        if index==0:
            self.head=self.head.next

        dummy = ListNode(None,self.head)
        for _ in range(index):        
            dummy = dummy.next
        dummy.next = dummy.next.next if dummy.next else None
        self.size-=1

    def printAll(self)->None:
        cur = self.head
        while cur:
            print(cur.val)
            cur=cur.next
        print("---")

obj = MyLinkedList()
obj.addAtHead(7)
obj.printAll()
obj.addAtHead(2)
obj.printAll()
obj.addAtHead(1)
obj.printAll()
obj.addAtIndex(3,1)
obj.printAll()
obj.deleteAtIndex(2)
obj.printAll()
obj.addAtHead(6)
obj.printAll()
obj.addAtTail(4)
obj.printAll()
obj.get(4)
obj.printAll()
obj.addAtHead(4)
obj.printAll()
obj.addAtIndex(5,0)
obj.printAll()
obj.addAtHead(6)
obj.printAll()