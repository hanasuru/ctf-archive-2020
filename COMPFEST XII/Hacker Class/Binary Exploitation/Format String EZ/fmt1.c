#include <stdio.h>

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);

    int target = 0;
    char name[20];

    printf("What's your name?\n");
    scanf("%s", name);
    printf("Hello, ");
    printf(name, &target);
    printf("!\n");

    if(target == 1337) {
        system("cat flag.txt");
    }
}
