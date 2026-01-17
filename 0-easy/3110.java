class Solution {
    public int scoreOfString(String s) {
        int l = 0;
        int r = 1;
        int size = s.length();
        int score = 0;

        while (r < size) {
            int diff = (int)s.charAt(r) - (int)s.charAt(l);
            score += Math.abs(diff);
            r++;
            l++;
        };

        return score;
    }
}