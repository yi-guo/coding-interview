public class Q019_RemoveNthNodeFromEndOfList {

    /**
     * Given a linked list, remove the nth node from the end of list and return its head.
     *
     * For example, given linked list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, after removing the second node from the end,
     * the linked list becomes 1 -> 2 -> 3 -> 5.
     *
     * Note: Given n will always be valid, try to do this in one pass.
     *
     */

	public static void main(String[] args) {
		LinkedList list = new LinkedList(new int[] {2, 4, 5, 7, 8, 11, 12, 14, 18});
		System.out.println(removeNthFromEnd(list.head, 3));
	}

    // Two pointers moving forward. The second one starts when the first one passes n nodes.
    // O(n) complexity in time and O(1) complexity in space.
	public static ListNode removeNthFromEnd(ListNode head, int n) {
		if (n < 1)
			return head;
		ListNode slow = head, fast = head;
		for (int i = 0; i < n; i++) {
			fast = fast.next;
			if (fast == null)
				return i == n - 1 ? head.next : head;
		}
		while (fast.next != null) {
			fast = fast.next;
			slow = slow.next;
		}
		slow.next = slow.next.next;
		return head;
	}

    // Return the nth node from the end of list.
	public static ListNode findNthFromEnd(ListNode head, int n) {
		if (n < 1)
			return null;
		ListNode slow = head, fast = head;
		for (int i = 0; i < n; i++) {
			fast = fast.next;
			if (fast == null)
				return i == n - 1 ? head : null;
		}
		while (fast != null) {
			fast = fast.next;
			slow = slow.next;
		}
		return slow;
	}
	
}
