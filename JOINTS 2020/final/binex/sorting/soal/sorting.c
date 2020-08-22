// gcc sorting.c -o sorting -fno-stack-protector -no-pie -z execstack

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

char nama[64];
int counter = 0;
char arr[100];

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
}

void set_array(){
    srand(time(0));
    for(int i=0; i<100; i++){
        arr[i] = rand()%0x100;
    }
}

void print_array(){
    for(int i=0; i<100; i++){
        printf("%d ", arr[i]);
    }
    puts("");
}

int check(){
    for(int i=0; i<99; i++){
        if(arr[i] > arr[i+1]){
            return 1;
        }
    }
    return 0;
}

int main(){
    int a,b;
    char temp;
    init();
    puts("Latihan mengurutkan bilangan");
    
    set_array();
    while(check()){
        counter++;
        printf("\nIterasi Ke - %d\n", counter);
        print_array();
        printf("Masukkan index yang mau ditukar (0-99) : ");
        scanf("%d %d", &a, &b);
        if(a > 99 || b > 99){
            puts("OUT OF BOUND!");
            exit(0);
        }
        else
        {
            temp = arr[a];
            arr[a] = arr[b];
            arr[b] = temp;
        }
    }
    puts("\nCongratulation!");
    printf("Total iterasi - %d\n", counter);
}