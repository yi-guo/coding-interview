import java.util.Queue;
import java.util.HashSet;
import java.util.LinkedList;

public class PossibleScores {

    /**
     * Source: VMWare Online Assessment
     *
     * There is a game where it is possible to score in different increments. Given an array input of these increments
     * (constrained from 1 to 1,000,000 inclusively) and a target score, return an integer indicating whether it is or
     * is not possible to achieve the target score utilizing a combination of multiples of the available increments.
     *
     * For example,
     *   1. given increments [2, 3, 7] and a target score of 1, your function should return 0;
     *   2. given increments [2, 3, 7] and a target score of 11, your function should return 1 since 2 + 2 + 7 = 11.
     */

    public static void main(String[] args) {
        int[] increments = {5, 9, 14};
        System.out.println(possibleScores(increments, 18));
    }

    // Similar to the subset sum problem but allowing duplicates.
    public static int possibleScores(int[] increments, int score) {
        Queue<Integer> queue = new LinkedList<Integer>();
        HashSet<Integer> visited = new HashSet<Integer>();
        queue.add(0);
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int increment : increments) {
                int newScore = curr + increment;
                if (newScore == score)
                    return 1;
                else if (newScore < score && !visited.contains(newScore)) {
                    queue.add(newScore);
                    visited.add(newScore);
                }
            }
        }
        return 0;
    }

}
