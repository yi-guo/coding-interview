import java.util.Arrays;
import java.util.HashMap;

public class Q001_TwoSum {

    /**
     * Given an array of integers, find two numbers such that they add up to a specific target number.
     * The function twoSum should return indices of the two numbers such that they add up to the target, where index1
     * must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
     *
     * You may assume that each input would have exactly one solution.
     *
     * Input: num = [2, 7, 11, 15], target = 9
     * Output: (1, 2)
     *
     */

	public static void main(String[] args) {
		int[] numbers = {2, 2, 2, 7, 7, 11, 15};
		System.out.println(Arrays.toString(twoSum(numbers, 9)));
	}

    // Use hash table to map all elements to their indices and for each element, check if target - element exists.
    // Exactly one pass, thus O(n) complexity in both time and space.
	public static int[] twoSum(int[] numbers, int target) {
		HashMap<Integer, Integer> indices = new HashMap<Integer, Integer>();
		for (int i = 0; i < numbers.length; i++) {
			if (indices.containsKey(target - numbers[i]) && indices.get(target - numbers[i]) != i)
				return new int[] {indices.get(target - numbers[i]) + 1, i + 1};
			indices.put(numbers[i], i);
		}
		return new int[] {-1, -1};
	}

}