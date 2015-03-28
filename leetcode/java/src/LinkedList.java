public class LinkedList {

    public ListNode head;
    
    public LinkedList() {
        head = null;
    }
    
    public LinkedList(int val) {
        head = new ListNode(val);
    }
    
    public LinkedList(int[] nums) {
        if (nums == null || nums.length == 0)
            head = null;
        else {
            head = new ListNode(nums[0]);
            ListNode temp = head;
            for (int i = 1; i < nums.length; i++) {
                temp.next = new ListNode(nums[i]);
                temp = temp.next;
            }
        }
    }
    
    public String toString() {
        return head == null ? null : head.toString();
    }
    
}
