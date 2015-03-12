public class ListNode {

	public int val;
	public ListNode next;
	
	public ListNode(int val) {
		this.val = val;
		this.next = null;
	}
	
	public String toString() {
		ListNode temp = next;
		StringBuilder builder = new StringBuilder("[" + val);
		while (temp != null) {
			builder.append(", " + temp.val);
			temp = temp.next;
		}
		builder.append("]");
		return builder.toString();
	}
	
}
