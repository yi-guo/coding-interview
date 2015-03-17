public class numOfIslands {

    public static void main(String[] args) {
        int[][] matrix = {{1, 1, 0, 0, 0},
                          {0, 1, 0, 0, 1},
                          {1, 0, 0, 1, 1},
                          {0, 0, 0, 0, 0},
                          {1, 0, 1, 0, 1}};
        System.out.println(numOfIslands(matrix));
    }

    public static int numOfIslands(int[][] matrix) {
        int count = 0;
        int[][] visited = new int[matrix.length][matrix[0].length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == 1 && getArea(matrix, visited, i, j) > 1)
                    count++;
            }
        }
        return count;
    }

    public static int getArea(int[][] matrix, int[][] visited, int i, int j) {
        if (i < 0 || j < 0 || i >= matrix.length || j >= matrix[i].length)
            return 0;
        if (matrix[i][j] == 0 || visited[i][j] == 1)
            return 0;
        visited[i][j] = 1;
        return 1 + getArea(matrix, visited, i + 1, j) + getArea(matrix, visited, i - 1, j) +
                getArea(matrix, visited, i, j + 1) + getArea(matrix, visited, i, j - 1);
    }

}
