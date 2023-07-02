public class BinarySearch {
    public static Integer binarySearch(int[] arr, int item) {

        int low = 0;
        int high = arr.length - 1;

        while (low <=  high) {
            int mid = (low + high) / 2;
            int guess = arr[mid];

            if (guess == item) {

                return mid;

            } else if (guess > item) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return null; 
    }

    public static void main (String[] args) {
        int[] myArray = {1, 3, 5, 7, 9};

        System.out.println(binarySearch(myArray, 3));
        System.out.println(binarySearch(myArray, -1));
}

}