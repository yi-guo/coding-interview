import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;

public class MergeKLists {

	public static void main(String[] args) {
		List<ListNode> lists = new ArrayList<ListNode>();
		lists.add(new LinkedList(new int[] {2, 3, 5, 8, 10}).head);
		lists.add(new LinkedList(new int[] {4}).head);
		lists.add(new LinkedList(new int[] {5, 7, 8, 9, 10, 13, 15}).head);
		System.out.println(mergeKLists(lists));
	}
	
	public static ListNode mergeKLists(List<ListNode> lists) {
		if (lists ==  null || lists.size() < 1)
			return null;
		PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>(lists.size(),
				new Comparator<ListNode>() {
			public int compare(ListNode n1, ListNode n2) {
				return n1.val - n2.val;
			}
		});
		for (ListNode head : lists) {
			if (head != null)
				queue.add(head);
		}
		ListNode head = new ListNode(0), temp = head;
		while (!queue.isEmpty()) {
			ListNode min = queue.poll();
			temp.next = min;
			temp = temp.next;
			if (min.next != null)
				queue.add(min.next);
		}
		return head.next;
	}
	
}

