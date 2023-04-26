class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode *slow = head, *fast = head->next, *firstHalf, *secondHalf, *previous, *temp, *temp2;
        
        while (fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }

        secondHalf = slow->next;
        slow->next = previous = NULL;
    }
};
