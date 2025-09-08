    #include <stdio.h>
    #include <stdlib.h>

    // Node structure
    struct Node {
        int data;
        struct Node* next;
    };

    // Function to create a new node
    struct Node* createNode(int data) {
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = data;
        newNode->next = NULL;
        return newNode;
    }

    // Function to insert node at end
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

    // Function to print the linked list
    void printList(struct Node* head) {
        struct Node* temp = head;
        while (temp != NULL) {
            printf("%d ", temp->data);
            temp = temp->next;
        }
        printf("\n");
    }

    // Function to delete Nth node from end
    void deleteNthFromEnd(struct Node** head, int N) {
        struct Node* temp = *head;
        int len = 0;

        // Find length
        while (temp != NULL) {
            len++;
            temp = temp->next;
        }

        // If N is greater than length
        if (N > len) {
            printf("N is greater than length of linked list!\n");
            return;
        }

        // Position from start = len - N + 1
        int pos = len - N + 1;

        temp = *head;

        // If head needs to be deleted
        if (pos == 1) {
            *head = temp->next;
            free(temp);
            return;
        }

        // Traverse to (pos-1)th node
        for (int i = 1; i < pos - 1; i++)
            temp = temp->next;

        // Delete node at pos
        struct Node* delNode = temp->next;
        temp->next = delNode->next;
        free(delNode);
    }

    // Main function
    int main() {
        struct Node* head = NULL;

        // Creating linked list: 10 -> 20 -> 30 -> 40 -> 50
        insertEnd(&head, 10);
        insertEnd(&head, 20);
        insertEnd(&head, 30);
        insertEnd(&head, 40);
        insertEnd(&head, 50);

        printf("Original Linked List: ");
        printList(head);

        int N;
        printf("Enter N (node from end to delete): ");
        scanf("%d", &N);

        deleteNthFromEnd(&head, N);

        printf("Updated Linked List: ");
        printList(head);

        return 0;
    }
