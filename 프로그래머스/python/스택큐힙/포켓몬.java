import java.util.*;


class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length / 2;
        List<Integer> list = new ArrayList<Integer>();
        for (int num : nums){
            list.add(num);
        }
        Set<Integer> set = new HashSet<Integer>(list);
        
        if(set.size() >= n){
            answer = n;
        }else{
            answer = set.size();
        }
        
        return answer;
    }
}