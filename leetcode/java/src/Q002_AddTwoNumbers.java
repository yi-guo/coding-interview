public class Q002_AddTwoNumbers {

    /**
     * You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order
     * and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
     *
     * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
     * Output: 7 -> 0 -> 8
     */

    public static void main(String[] args) {
        LinkedList l1 = new LinkedList(new int[] {9, 9});
        LinkedList l2 = new LinkedList(new int[] {1});
        System.out.println(addTwoNumbers(l1.head, l2.head));
    }

    // Add each digit from left to right.
    // Exactly one pass, thus O(n) complexity in time and O(1) in space.
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode head = new ListNode(0);
        ListNode temp = head;
        while (l1 != null || l2 != null || carry != 0) {
            if (l1 != null) {
                temp.val = temp.val + l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                temp.val = temp.val + l2.val;
                l2 = l2.next;
            }
            carry = temp.val / 10;
            temp.val = temp.val % 10;
            if (l1 != null || l2 != null || carry != 0)
                temp.next = new ListNode(carry);
                temp = temp.next;
        }
        return head;
    }

}
