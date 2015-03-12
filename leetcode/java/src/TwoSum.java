import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class TwoSum {

	public static void main(String[] args) {
		int[] numbers = {2, 2, 2, 7, 7, 11, 15};
		System.out.println(Arrays.toString(twoSum(numbers, 9)));
	}
	
	public static int[] twoSum(int[] numbers, int target) {
		HashMap<Integer, Integer> numsToIndices = new HashMap<Integer, Integer>();
		for (int i = 0; i < numbers.length; i++) {
			if (numsToIndices.containsKey(target - numbers[i]) && numsToIndices.get(target - numbers[i]) != i)
				return new int[] {numsToIndices.get(target - numbers[i]) + 1, i + 1};
			numsToIndices.put(numbers[i], i);
		}
		return new int[] {-1, -1};
	}
	
	public static ArrayList<int[]> twoSumWithDuplicates(int[] numbers, int target) {
		ArrayList<int[]> twoSums = new ArrayList<int[]>();
		HashMap<Integer, ArrayList<Integer>> numsToIndices = new HashMap<Integer, ArrayList<Integer>>();
		for (int i = 0; i < numbers.length; i++) {
			if (!numsToIndices.containsKey(numbers[i]))
				numsToIndices.put(numbers[i], new ArrayList<Integer>());
			numsToIndices.get(numbers[i]).add(i);
		}
		for (int i = 0; i < numbers.length; i++) {
			if (numsToIndices.containsKey(target - numbers[i])) {
				for (int index : numsToIndices.get(target - numbers[i])) {
					if (index > i)
						twoSums.add(new int[] {i, index});
				}
			}
		}
		return twoSums;
	}
	
}
