// gcc ez.c -o ez -s -no-pie -Wl,-z,norelro -fstack-protector-all

#include<stdio.h>
#include<stdlib.h>

void shell(){
    system("/bin/sh");
}

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
}

int main(){
    long int c[10], cc;
    init();
    printf("Bonus for you :) - %p\n", &cc);
    printf("> ");
    scanf("%ld", &cc);
    printf("> ");
    scanf("%hhd", &c[cc]);
    exit(0);
}
