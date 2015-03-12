public class RemoveNthNodeFromEndOfList {

	public static void main(String[] args) {
		LinkedList list = new LinkedList(new int[] {2, 4, 5, 7, 8, 11, 12, 14, 18});
		System.out.println(removeNthFromEnd(list.head, 3));
	}
	
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
