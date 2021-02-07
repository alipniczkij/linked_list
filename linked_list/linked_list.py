import copy
import pdb

class Node(object):
    """
    LinkedList is full of Nodes
    """
    def __init__(self, el, next=None):
        self.el = el
        self.next = next

    def __str__(self):
        return str(self.el)

    def __repr__(self):
        return str(self.el)

    def __eq__(self, other):
        if type(other) is Node:
            return self.el == other.el
        return self.el == other

    def __ne__(self, other):
        return not self == other


class LinkedList(object):
    """
    Implementation of Linked List
    """
    def __init__(self, elems=None):
        """
        Can read LinkedList() without parameters or LinkedList([1, 2, 3, 4]) with list of elements
        """
        self.head = None
        self.end = None

        if elems:
            for el in elems:
                self.append(el)

    def __str__(self):
        return "[{}]".format(", ".join(str(node) for node in self))

    def __len__(self):
        """
        Returns lenght of LinkedList by len() func
        """
        return self.count()

    def __iter__(self):
        """
        Returns generator through the LinkedList
        """
        point = self.head
        while point:
            yield point
            point = point.next

    def __getitem__(self, index):
        """
        Returns the node by index in LinkedList
        l[1]
        """
        if not 0 <= index < len(self):
            raise IndexError
        for pos, node in enumerate(self):
            if pos == index:
                return node

    def __add__(self, other):
        """
        Adds one list for another. [1, 2, 3, 4, 5, 6] = [1, 2, 3] + [4, 5, 6]
        """
        left_list = copy.deepcopy(self)
        right_list = copy.deepcopy(other)

        if left_list.head is None:
            return left_list
        if right_list.head is None:
            return right_list

        left_list.end.next = right_list.head
        left_list.end = right_list.end
        return left_list

    def __contains__(self, elem):
        """
        Check if there is a value (via "in")
        """
        return elem in [node.el for node in self]

    def __iadd__(self, other):
        """
        [1, 2, 3] += [4, 5, 6]. Returns [1, 2, 3, 4, 5, 6]
        """
        self = self + other
        return self

    def __eq__(self, other):
        """
        Compare 2 LinkedLists. True if same lenght and nodes elems have same order and value 
        """
        if len(self) != len(other):
            return False

        for ind in range(len(self)):
            if self[ind] != other[ind]:
                return False
        return True

    def append(self, element):
        """
        Append new node with element to the end of LinkedList
        """
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            self.end.next = new_node
        self.end = new_node

    def count(self):
        """
        Returns lenght of LinkedList
        """
        return sum(1 for _ in self)

    def pop(self, index=None):
        """
        Deletes and returns node from LinkedList by index (Without index it would be last node)
        """
        list_length = len(self)

        if index is None:
            index = list_length - 1

        if not 0 <= index < list_length:
            raise IndexError
        
        node_to_remove = self[index]

        if index == 0:
            if list_length == 1:
                self.head = None
                self.end = None
            else:
                self.head = self[1]
        elif index == list_length - 1:
            prev_node = self[index - 1]
            prev_node.next = None
            self.end = prev_node
        else:
            prev_node = self[index - 1]
            next_node = self[index + 1]
            prev_node.next = next_node
        
        return node_to_remove