#!/usr/bin/python

# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

from cStringIO import StringIO

class Node:

	def __init__(self, key, next = None):
		self.key = key
		self.next = next

class LinkedList:

	def __init__(self, head = None):
		if type(head) == int:
			self.head = Node(head)
		elif type(head) == list:
			self.head = None
			for key in head:
				self.insert(key)
		else:
			self.head = None

	def insert(self, key):
		if self.isEmpty():
			self.head = Node(key)
		else:
			temp = self.head
			while temp.next is not None:
				temp = temp.next
			temp.next = Node(key)

	def isEmpty(self):
		return self.head is None

	def toString(self):
		temp = self.head
		output = StringIO()
		output.write('[')
		while temp is not None:
			output.write(str(temp.key))
			if temp.next is not None:
				output.write(', ')
			temp = temp.next
		output.write(']')
		return output.getvalue()

def addTwoNumbers(l1, l2):
	flag = 0
	l = LinkedList()
	temp1, temp2 = l1.head, l2.head
	while temp1 is not None and temp2 is not None:
		addition = temp1.key + temp2.key + flag
		if addition > 9:
			flag = 1
			addition = addition - 10
		else:
			flag = 0
		l.insert(addition)
		temp1 = temp1.next
		temp2 = temp2.next
	while temp1 is not None:
		addition = temp1.key + flag
		if addition  > 9:
			flag = 1
			addition = addition - 10
		else:
			flag = 0
		l.insert(addition)
		temp1 = temp1.next
	while temp2 is not None:
		addition = temp2.key + flag
		if addition > 0:
			flag = 1
			addition = addition - 10
		else:
			flag = 0
		l.insert(addition)
		temp2 = temp2.next
	if flag == 1:
		l.insert(flag)
	return l.toString()






def main():
	l1 = LinkedList([8, 6, 9, 9])
	l2 = LinkedList([5, 6, 4])
	print addTwoNumbers(l1, l2)

main()