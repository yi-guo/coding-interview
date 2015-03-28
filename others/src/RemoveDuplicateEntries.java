import java.util.HashSet;

public class RemoveDuplicateEntries {

    /**
     * Given a singly linked list, write a function to remove all duplicate entries in place. The returned linked list
     * should maintain ordering such that only the duplicates of a previous node are removed.
     */

    public static void main(String[] args) {
        LinkedList list = new LinkedList(new int[] {1, 2, 4, 2, 3, 2, 31, 1});
        System.out.println(removeDuplicateEntries(list.head).toString());
    }

    // Use hash set to keep track of existing values.
    public static ListNode removeDuplicateEntries(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode curr = head;
        HashSet<Integer> visited = new HashSet<Integer>();
        visited.add(curr.val);
        while (curr.next != null) {
            if (visited.contains(curr.next.val))
                curr.next = curr.next.next;
            else {
                visited.add(curr.next.val);
                curr = curr.next;
            }
        }
        return head;
    }

}
