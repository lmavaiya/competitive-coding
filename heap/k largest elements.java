
/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    public static void main(String[] args) {
        // code

        Scanner s = new Scanner(System.in);
        PriorityQueue<Integer> pQueue = new PriorityQueue<Integer>();

        int t = s.nextInt();
        while (t-- > 0) {
            int n = s.nextInt();
            int k = s.nextInt();
            for (int i = 1; i <= n; i++) {
                pQueue.add(-s.nextInt());
            }

            while (k-- > 0)
                System.out.print(-pQueue.poll() + " ");

            System.out.println("");

        }
    }
}