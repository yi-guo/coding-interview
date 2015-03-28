public class Q021_MergeTwoSortedLists {

    /**
     * Merge two sorted linked lists and return it as a new list.
     * The new list should be made by splicing together the nodes of the first two lists.
     *
     */

    // Two pointers for the two lists. Compare while moving forward.
    // O(n) complexity in time and O(1) in space.
	public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
		ListNode head = new ListNode(0), temp = head;
		while (l1 != null && l2 != null) {
			if (l1.val < l2.val) {
				temp.next = l1;
				l1 = l1.next;
			} else {
				temp.next = l2;
				l2 = l2.next;
			}
			temp = temp.next;
		}
		if (l1 != null)
			temp.next = l1;
		if (l2 != null)
			temp.next = l2;
		return head.next;
	}
	
}
