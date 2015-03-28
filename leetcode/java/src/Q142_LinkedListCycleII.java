public class Q142_LinkedListCycleII {

    /**
     * Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
     *
     * Follow up: Can you solve it without using extra space?
     *
     */

    // Two pointers move forward with the fast pointer moving two nodes at a time.
    // If at a time that the two pointers are at the same node, replace the fast
    // pointer at the head and move it one node at a time.
    // The cycle begins when the they meet again.
    // O(n) complexity in time and O(1) complexity in space.
	public ListNode detectCycle(ListNode head) {
		if (head == null)
			return null;
		ListNode slow = head, fast = head;
		while (fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
			if (fast == slow) {
				fast = head;
				while (fast != slow) {
					slow = slow.next;
					fast = fast.next;
				}
				return fast;
			}
		}
		return null;
	}
	
}
