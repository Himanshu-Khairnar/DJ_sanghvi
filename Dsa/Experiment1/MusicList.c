#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Song {
    char title[100];
    char artist[100];
    char album[100];
    int year;
    float duration;
    struct Song* next;
};

struct Song* head = NULL;

// Function to create a new song node
struct Song* createSong(char title[], char artist[], char album[], int year, float duration) {
    struct Song* newSong = (struct Song*)malloc(sizeof(struct Song));
    strcpy(newSong->title, title);
    strcpy(newSong->artist, artist);
    strcpy(newSong->album, album);
    newSong->year = year;
    newSong->duration = duration;
    newSong->next = NULL;
    return newSong;
}

// Insert at end
void addSong(char title[], char artist[], char album[], int year, float duration) {
    struct Song* newSong = createSong(title, artist, album, year, duration);
    if (head == NULL) {
        head = newSong;
        return;
    }
    struct Song* temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newSong;
}

// Display playlist
void displaySongs() {
    struct Song* temp = head;
    if (temp == NULL) {
        printf("Playlist is empty\n");
        return;
    }
    printf("\n--- Playlist ---\n");
    while (temp != NULL) {
        printf("Title: %s | Artist: %s | Album: %s | Year: %d | Duration: %.2f\n",
               temp->title, temp->artist, temp->album, temp->year, temp->duration);
        temp = temp->next;
    }
}

// Search song by title
void searchSong(char title[]) {
    struct Song* temp = head;
    while (temp != NULL) {
        if (strcmp(temp->title, title) == 0) {
            printf("Found: %s | %s | %s | %d | %.2f\n",
                   temp->title, temp->artist, temp->album, temp->year, temp->duration);
            return;
        }
        temp = temp->next;
    }
    printf("Song not found!\n");
}

// Update song by title
void updateSong(char title[]) {
    struct Song* temp = head;
    while (temp != NULL) {
        if (strcmp(temp->title, title) == 0) {
            getchar();  // clear buffer
            printf("Enter new Artist: ");
            fgets(temp->artist, sizeof(temp->artist), stdin);
            temp->artist[strcspn(temp->artist, "\n")] = 0;

            printf("Enter new Album: ");
            fgets(temp->album, sizeof(temp->album), stdin);
            temp->album[strcspn(temp->album, "\n")] = 0;

            printf("Enter new Year: ");
            scanf("%d", &temp->year);

            printf("Enter new Duration: ");
            scanf("%f", &temp->duration);

            printf("Song updated!\n");
            return;
        }
        temp = temp->next;
    }
    printf("Song not found!\n");
}

// Delete song by title
void deleteSong(char title[]) {
    struct Song *temp = head, *prev = NULL;
    while (temp != NULL && strcmp(temp->title, title) != 0) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) {
        printf("Song not found!\n");
        return;
    }
    if (prev == NULL) {
        head = temp->next;
    } else {
        prev->next = temp->next;
    }
    free(temp);
    printf("Song deleted!\n");
}

// Count total songs
void countSongs() {
    int count = 0;
    struct Song* temp = head;
    while (temp != NULL) {
        count++;
        temp = temp->next;
    }
    printf("Total songs: %d\n", count);
}

// Count total playtime
void totalPlaytime() {
    float total = 0;
    struct Song* temp = head;
    while (temp != NULL) {
        total += temp->duration;
        temp = temp->next;
    }
    printf("Total playtime: %.2f minutes\n", total);
}

int main() {
    int choice, year;
    float duration;
    char title[100], artist[100], album[100];

    while (1) {
        printf("\n--- Music Playlist Manager ---\n");
        printf("1. Add Song\n2. Display Songs\n3. Search Song\n4. Update Song\n5. Delete Song\n6. Count Songs\n7. Total Playtime\n8. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
        case 1:
            getchar();  // clear buffer
            printf("Enter Title: ");
            fgets(title, sizeof(title), stdin);
            title[strcspn(title, "\n")] = 0;

            printf("Enter Artist: ");
            fgets(artist, sizeof(artist), stdin);
            artist[strcspn(artist, "\n")] = 0;

            printf("Enter Album: ");
            fgets(album, sizeof(album), stdin);
            album[strcspn(album, "\n")] = 0;

            printf("Enter Year: ");
            scanf("%d", &year);

            printf("Enter Duration (in minutes): ");
            scanf("%f", &duration);

            addSong(title, artist, album, year, duration);
            break;
        case 2:
            displaySongs();
            break;
        case 3:
            getchar();
            printf("Enter Title to search: ");
            fgets(title, sizeof(title), stdin);
            title[strcspn(title, "\n")] = 0;
            searchSong(title);
            break;
        case 4:
            getchar();
            printf("Enter Title to update: ");
            fgets(title, sizeof(title), stdin);
            title[strcspn(title, "\n")] = 0;
            updateSong(title);
            break;
        case 5:
            getchar();
            printf("Enter Title to delete: ");
            fgets(title, sizeof(title), stdin);
            title[strcspn(title, "\n")] = 0;
            deleteSong(title);
            break;
        case 6:
            countSongs();
            break;
        case 7:
            totalPlaytime();
            break;
        case 8:
            exit(0);
        default:
            printf("Invalid choice!\n");
        }
    }
    return 0;
}
