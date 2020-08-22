// gcc math2.c -o math2 -fstack-protector-all -no-pie -Wl,-z,relro,-z,now -lm

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

char *s;
int *num_arr;
FILE *fp;

void win(){
    int c;
    puts("Terima kasih sudah bermain :)");
    puts("Pilih hadiahmu :");
    puts("[1] ?");
    puts("[2] ??");
    puts("[3] ???");
    puts("[4] ????");
    puts("[5] ?????");
    printf("> ");
    scanf("%d", &c);
    switch (c)
    {
    case 1:
        system("cat A");
        break;
    
    case 2:
        system("cat B");
        break;
        
    case 3:
        system("cat C");
        break;
        
    case 4:
        system("cat D");
        break;
        
    case 5:
        system("cat E");
        break;

    default:
        puts(":(");
        break;
    }
}

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    s = malloc(0x400);
    num_arr = malloc(64);
    fp = fopen("/dev/random", "r");
}

void read_int_arr(){
    char *n;
    int i=0;
    memset(s, 0, 0x400);
    memset(num_arr, 0, 64);
    fgets(s, 0x400, stdin);

    n = strtok(s, " ");
    while(n)
    {
        num_arr[i++] = atoi(n);
        n = strtok(NULL, " ");
    }
}

void getPrimeFactors(int *num, int n){
    int i=0;
    while(n%2 == 0){
        num[i++] = 2;
        n /= 2;
    }
    for(int k=3; k<=(int)sqrt(n); k += 2){
        while(n%k == 0){
            num[i++] = k;
            n /= k;
        }
    }
    if(n > 2){
        num[i++] = n;
    }
}

int checkPrimeFactors(int *num, int fc){
    int numCk[50];
    memset(numCk, 0, 50*4);
    getPrimeFactors(numCk, fc);
    for(int i=0; numCk[i] != 0; i++){
        if(numCk[i] != num[i]){
            return 1;
        }
    }
    return 0;
}

int main(){
    int strn;
    int n[50];
    init();
    puts("Masukkan semua faktor prima dari bilangan yang diberikan!");
    for(int i=0; i<100; i++){
        strn = getc(fp);
        while (strn < 2)
        {
            strn = getc(fp);
        }
        
        printf("%d\n> ", strn);
        memset(n, 0, 50*4);
        read_int_arr();
        if(checkPrimeFactors(num_arr, strn)){
            puts("Salah!");
            exit(1);
        }
    }
    win();
    fclose(fp);
    exit(0);
}