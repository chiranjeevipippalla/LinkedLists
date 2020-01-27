class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    
    def __init__(self):
        self.head = None


    #1a. Insert a node normally
    def insert(self, data):
        new_node = Node(data)
        p = self.head
        if p is None:
            self.head = new_node
        else:
            while p.next is not None:
                p = p.next
            p.next = new_node
            new_node.next = None
        return self.head
        
    #1b. Insert a node at the beginning of the List
    def insert_at_start(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            head = new_node
            
        return self.head

    #1c. Insert a node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        p = self.head
        
        while p.next is not None:
            p = p.next
            
        p.next = new_node
        new_node.next = None
        
        return self.head

    #1d. Insert a node after a position "pos"
    def insert_at_pos(self, pos, data):
        new_node = Node(data)
        p = self.head
        
        while self.head is not None and p.data!=pos:
            p = p.next

        new_node.next = p.next
        p.next = new_node
        
        return self.head

    #2a. Print all the elements in a linked list
    def print_elements(self):
        print("The elements in the list are:")
        
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next

    #2b. Smallest element in the list
    def smallest_node(self):
        smallest = self.head.data
        p = self.head

        if p.next is None:
            return self.head.data
        else:
            while p!=None:
                if p.data < smallest:
                    smallest = p.data
                else:
                    p = p.next
        return print("Smallest number in the list is: " +str(smallest))

    #2c. Largest element in the list
    def largest_node(self):
        largest = self.head.data
        p = self.head

        if p.next is None:
            return self.head.data
        else:
            while p!=None:
                if p.data > largest:
                    largest = p.data
                else:
                    p = p.next
        return print("Largest number in the list is: " +str(largest))

            
    #3. Delete a node from the linked list
    def delete_node(self, value):
        q = self.head
        p = self.head.next

        if(q.data==value):
            self.head = p

        else:
            while p.data!=value:
                p = p.next
                q = q.next

            if p.next is None:
                q.next = None
            else:
                q.next = p.next

        return self.head

    
    #4. Insert a node in Doubly Linked List
    
    #5. Merge 2 Sorted Linked Lists
    
    
    #6. Reverse a linked list
    def reverse(self):

        if self.head is None:
            return self.head

        prev = None
        p = self.head

        while p is not None:
            temp = p.next
            p.next = prev
            prev = p
            p = temp

        self.head = prev

        return self.head
    
        #6new. Reverse a linked list
    def reverse(self, head):

        if head is None:
            return head

        prev = None
        p = head

        while p is not None:
            temp = p.next
            p.next = prev
            prev = p
            p = temp

        head = prev

        return head
    

    #7. Delete a node from Doubly Linked List
    

    #8a. Detect a loop in a Linked list
    def detect_loop(self):
        p = self.head
        q = self.head

        while p and q and q.next is not None:
            p = p.next
            q = q.next.next

            if p==q:
                return p
            else:
                return None

        return None

    #8b. Start of the loop - Floyd Cycle Detection
    def start_of_loop(self):
        p = detect_loop()
        q = self.head

        while p!=q:
            p = p.next
            q = q.next

        return p

    
    
    #9a. Palindrome Linked List or not
    def isPalindrome(self):

        p = self.head
        q = self.head

        while p is not None and p.next is not None:
            print("Above")
            p = p.next.next
            print("below")

            if p.next is None:
                start_second = q.next.next
                break
            if p is None:
                start_second = q.next
                break

            q = q.next

        q.next = None

        #Reverse the second list
        reversed_list = self.reverse(start_second)

        self.compare_2_lists(self.head, reversed_list)

    #9b. Compare two linked lists if they are same or not
    def compare_2_lists(self, head, reversed_list):
        p = self.head
        q = reversed_list

        while p is not None and q is not None:
            if p.data==q.data:
                p = p.next
                q = q.next
                print ("Pal")

            else:
                return False

            print("Palindrome")

        return True
                


    #10. Remove Duplicate nodes from Sorted list
    def remove_duplicates(self):

        return self.head

















#Test the code
list1 = SinglyLinkedList()

#Insert
list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(1)
list1.insert(2)

#Delete
#list1.delete_node(2)

#smallest
#list1.smallest_node()

#largest
#list1.largest_node()

#Merge 2 Lists
#p = [10,20,30,40,50]
#q = [60,70,80,90,100]

#merged_list = SinglyLinkedList()
#merged_list.merge2lists(p, q)



#Reverse the Linked List
#list1.reverse()
#list1.print_elements()

list1.isPalindrome()

#Print
#list1.print_elements()





        
