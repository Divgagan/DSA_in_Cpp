class Solution {
private:

    void remove_cycle(Node* head, Node* meetingPoint) {
        
        Node* ptr1 = head;
        Node* ptr2 = meetingPoint;

        // Step 1: Find starting point of loop
        while(ptr1 != ptr2) {
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }

        // Now ptr1 (or ptr2) is at loop start
        Node* loopStart = ptr1;

        // Step 2: Find last node of loop
        Node* temp = loopStart;
        while(temp->next != loopStart) {
            temp = temp->next;
        }

        // Step 3: Break the loop
        temp->next = NULL;
    }

public:

    void removeLoop(Node* head) {
        
        if(head == NULL || head->next == NULL) {
            return;
        }

        Node* slow = head;
        Node* fast = head;

        // Detect cycle
        while(fast != NULL && fast->next != NULL) {

            slow = slow->next;
            fast = fast->next->next;

            if(slow == fast) {   // Correct comparison
                remove_cycle(head, slow);
                return;
            }
        }
    }
};

