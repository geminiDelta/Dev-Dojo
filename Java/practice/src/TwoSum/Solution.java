package TwoSum;

class Solution {
   public static int[] twoSum(int[] nums, int target) {
      for(int i = 0; i < nums.length; i++)
         for(int j = i+1; j < nums.length; j++)
            if(nums[i] + nums[j] == target)
               return new int[]{i, j};
      return new int[0];
    }
    
    public static void main(String[] args) {
      int[] nums = new int[]{0,4,7,11};
      int target = 11;
      int[] result = twoSum(nums, target);
      if(result.length > 0)
         System.out.println(nums[result[0]] + " + " + 
            nums[result[1]] + " = " + (nums[result[0]] + nums[result[1]]));
      else
         System.out.println("No solution...");
    }
}