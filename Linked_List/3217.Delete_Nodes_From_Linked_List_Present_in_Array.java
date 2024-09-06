/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        Set<Integer> valuesToRemove = new HashSet<>();
        for (int num: nums){
            valuesToRemove.add(num);
        }

        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode res = dummy;
        while (dummy.next != null){
            if (valuesToRemove.contains(dummy.next.val)){
                ListNode tmp = dummy.next.next;
                dummy.next.next = null;
                dummy.next = tmp;
            } else {
                dummy = dummy.next;
            }          
        }
        return res.next;
    }
}
