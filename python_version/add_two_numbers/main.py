class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, retenu:int) -> ListNode:
        val = l1.val + l2.val + retenu
        retenu = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or retenu != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = Solution.addTwoNumbers(self, l1.next, l2.next, retenu)
        return ret

def main():
    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(3)
    l4 = ListNode(5)
    l5 = ListNode(6)
    l6 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l4.next = l5
    l5.next = l6
    l7 = Solution.addTwoNumbers(Solution ,l1,l4, 0)
    while (l7):
        print(l7.val)
        l7 = l7.next

if __name__ == "__main__":
    # execute only if run as a script
    main()