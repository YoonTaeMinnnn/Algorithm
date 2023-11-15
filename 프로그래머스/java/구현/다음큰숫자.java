import java.util.*;


class Solution {

    int cnt = 0;

    public int count(int n){
        if(n == 0){
            return 0;
        }else{
            if (n % 2 == 1){
                this.cnt += 1;
            }
            count(n / 2);
        }
        return this.cnt;
    }

    public int solution(int n) {
        int answer = 0;
        int sol;
        Solution s = new Solution();
        int com = s.count(n);
        s.cnt = 0;

        while(true){
            n += 1;
            if (s.count(n) == com){
                sol = n;
                break;
            }
            s.cnt = 0;
        }
        return sol;
    }
}