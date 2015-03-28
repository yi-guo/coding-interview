import java.util.Stack;

public class TreeHeight {

    /**
     * Source: VMWare Online Assessment
     *
     * Given the preorder traversal of a binary tree, write a function that returns the height of the tree.
     *
     * For exmaple, given a binary tree
     *       1
     *    2     3
     *         4
     * the preorder traversal is represented as a string "1 2 3 * * 4 *", where '*' indicates a null.
     *
     * Your function should return 3, which is the height of the given tree.
     */

    public static void main(String[] args) {
        String preorder = "1 2 3 * * 4 *";
        System.out.println(treeHeight(preorder));
    }

    // Split the string by spaces and traverse the preorder array backward. If
    //   1. '*', push 0 to stack;
    //   2. otherwise, pop twice and push whichever is greater plus 1.
    // Every node will be accessed once, thus O(n) complexity in both time and space.
    public static int treeHeight(String preorder) {
        if (preorder == null || preorder.length() == 0)
            return -1;
        String[] nodes = preorder.split(" ");
        Stack<Integer> height = new Stack<Integer>();
        for (int i = nodes.length - 1; i >= 0; i--) {
            if (nodes[i].equals("*"))
                height.push(0);
            else {
                if (height.size() < 2)
                    return -1;
                height.push(Math.max(height.pop(), height.pop()) + 1);
            }
        }
        return height.size() == 1 ? height.pop() : -1;
    }

}
