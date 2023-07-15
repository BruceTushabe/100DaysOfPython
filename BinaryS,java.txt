public static boolean binary_search(int target, int[] nums) {
    int floorIndex = -1;
    int ceilingIndex = nums.length;

    while (floorIndex < ceilingIndex - 1) {
        int distance = ceilingIndex - floorIndex;
        int halfDistance = distance / 2;
        int guessIndex = floorIndex + halfDistance;
        int guessValue = nums[guessIndex];

        if (guessValue == target) {
            return true; // Return true if target is found
        } else if (guessValue > target) {
            ceilingIndex = guessIndex;
        } else {
            floorIndex = guessIndex;
        }
    }

    return false; // Return false if target is not found
}
