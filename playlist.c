// playlist.c
#include <stdio.h>
#include <string.h>

#define MAX 100

// Very simple in-memory playlist (no persistence)
char *songs[MAX];
int count = 0;

void add_song(const char *name) {
    if (count < MAX) {
        songs[count++] = strdup(name);
        printf("Added: %s\n", name);
    } else {
        printf("Playlist full\n");
    }
}

void list_songs() {
    if (count == 0) {
        printf("Playlist is empty\n");
        return;
    }
    for (int i = 0; i < count; ++i) {
        printf("%d. %s\n", i+1, songs[i]);
    }
}

void remove_song(int idx) {
    if (idx < 1 || idx > count) {
        printf("Invalid index\n");
        return;
    }
    int pos = idx - 1;
    printf("Removed: %s\n", songs[pos]);
    free(songs[pos]);
    for (int i = pos; i < count-1; ++i) songs[i] = songs[i+1];
    count--;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: playlist <cmd> [args]\n");
        printf("Commands: add <name>, list, remove <index>\n");
        return 0;
    }

    if (strcmp(argv[1], "add") == 0) {
        if (argc < 3) { printf("Usage: playlist add <song name>\n"); return 0; }
        add_song(argv[2]);
    } else if (strcmp(argv[1], "list") == 0) {
        list_songs();
    } else if (strcmp(argv[1], "remove") == 0) {
        if (argc < 3) { printf("Usage: playlist remove <index>\n"); return 0; }
        int idx = atoi(argv[2]);
        remove_song(idx);
    } else {
        printf("Unknown command: %s\n", argv[1]);
    }
    return 0;
}
