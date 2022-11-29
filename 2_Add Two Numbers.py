class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None

class Solution:
    def __init__(self):
        self.head=None
    
    def print_LL(self):
        if self.head is None:
            print("the Node is Empty!")
        else:
            h=self.head
            while h is not None:
                print(h.data)
                h=h.nref

    def push(self,data):
        new_node=Node(data)
        new_node.nref=self.head
        self.head=new_node

    def addTwoNumbers(self,l1,l2):
        total=0
        tenths=1
        a,b=l1,l2
        while a or b:
            if a:
                total += (a.data * tenths)
                a = a.nref
            if b:
               total += (b.data * tenths)
               b = b.nref
            tenths=tenths*10
        print([int(char) for char in str(total)[::-1]])
        
l1=Solution()
l1.push(2)
l1.push(4)
l1.push(3)
print("l1 list is: " )
l1.print_LL()

l2=Solution()
l2.push(5)
l2.push(6)
l2.push(4)
print("l2 list is: " )
l2.print_LL()

new=Solution()
print("the total is")
new.addTwoNumbers(l1.head,l2.head)