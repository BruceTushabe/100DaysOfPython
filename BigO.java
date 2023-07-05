public class BigO{

    public static boolean binarySearch (int[] arr, int target) {

        int low = 0;
        int high = arr.length - 1;

        while (low  <= high){
            int mid = low + (high - low)/ 2;

            int guess = arr[mid];

            if (guess == target) {
                return  true;


            } else if (guess < target) {
                low = mid + 1;


            } else {
                high  = mid - 1;

            }

            }

        return false;

        }

    public static void main (String[] args){
        int[] myArray = {1,3,5,7,9};

            System.out.println(binarySearch(myArray, 3));   // Output: true
            System.out.println(binarySearch(myArray, -1));  // Output: false
            System.out.println(binarySearch(myArray, 9));   // Output: true
            System.out.println(binarySearch(myArray, 4));   // Output: false
    }    
}
