public class Q141_LinkedListCycle {

    /**
     * Given a linked list, determine if it has a cycle in it.
     *
     * Follow up: Can you solve it without using extra space?
     *
     */

    // Two pointers move forward with the fast pointer moving two nodes at a time.
    // If at a time that the two pointers are at the same node, the list has a cycle.
    // O(n) complexity in time and O(1) complexity in space.
	public boolean hasCycle(ListNode head) {
		if (head == null)
			return false;
		ListNode slow = head, fast = head.next;
		while (fast != null && fast.next != null) {
			if (slow == fast)
				return true;
			slow = slow.next;
			fast = fast.next.next;
		}
		return false;
	}
	
}
