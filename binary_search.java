public class binary_search {

    public static int binarySearch(int[] nums, int target) {
        int low = 0;

        int high = nums.length - 1;

        while (low <= high) {
            
            int mid = (high + low) / 2;
            
            
            if (nums[mid] == target) {
            return mid;}
            
            
            if (target < nums[mid]){
            high = mid - 1;
        
        } else {
            low = mid + 1;
        }

    }

    return -1;
}

public static void main(String[] args){
    int [] nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int target = 5;
    int result = binarySearch(nums, target);
    System.out.println(result);
}

}
