#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insertEnd(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node* temp = *head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newNode;
}

void printList(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

struct Node* findMiddle(struct Node* head) {
    struct Node* slow = head;
    struct Node* fast = head;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;  // slow will be middle (second middle if even length)
}

struct Node* segregateEvenOdd(struct Node* head) {
    struct Node *evenStart = NULL, *evenEnd = NULL;
    struct Node *oddStart = NULL, *oddEnd = NULL;
    struct Node* curr = head;

    while (curr != NULL) {
        int val = curr->data;
        if (val % 2 == 0) { // Even node
            if (evenStart == NULL) {
                evenStart = evenEnd = curr;
            } else {
                evenEnd->next = curr;
                evenEnd = evenEnd->next;
            }
        } else { // Odd node
            if (oddStart == NULL) {
                oddStart = oddEnd = curr;
            } else {
                oddEnd->next = curr;
                oddEnd = oddEnd->next;
            }
        }
        curr = curr->next;
    }

    if (evenStart == NULL || oddStart == NULL)
        return head;

    evenEnd->next = oddStart;
    oddEnd->next = NULL;

    return evenStart;
}

int main() {
    struct Node* head = NULL;

    insertEnd(&head, 1);
    insertEnd(&head, 2);
    insertEnd(&head, 3);
    insertEnd(&head, 4);
    insertEnd(&head, 5);
    insertEnd(&head, 6);
    insertEnd(&head, 7);

    printf("Original List: ");
    printList(head);

    // Problem 1: Find middle
    struct Node* middle = findMiddle(head);
    printf("Middle Node: %d\n", middle->data);

    // Problem 2: Segregate even and odd
    head = segregateEvenOdd(head);
    printf("Modified List (Even before Odd): ");
    printList(head);

    return 0;
}
