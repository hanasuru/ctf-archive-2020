// gcc math1.c -o math1 -no-pie -Wl,-z,relro,-z,now

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdint.h>
#include<time.h>

char *s;

void __exit(long int a, int b, char *c){
    FILE *f;
    char ch;

    f = fopen("flag.txt", "r");
    if(strcmp(c, s) == 0){
        if(b == (long int)-110){
            if(a == 0xdeeeaaadcafebeef){
                do{
                    ch = fgetc(f);
                    putchar(ch);
                }while(ch != EOF);
            }
        }
    }
}

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    srand(time(0));
    s = malloc(100);
    s[0] = 'b';
    s[1] = 'm';
    s[2] = 'l';
    s[3] = '1';
    s[4] = 'b';
    s[5] = 'm';
    s[6] = 'l';
    s[7] = '1';
    s[8] = 'b';
    s[9] = 'm';
    s[10] = 'l';
    s[11] = '1';
    s[12] = 'I';
    s[13] = 'C';
    s[14] = '0';
    s[15] = '+';
    s[16] = 'I';
    s[17] = 'G';
    s[18] = 'h';
    s[19] = '0';
    s[20] = 'd';
    s[21] = 'H';
    s[22] = 'B';
    s[23] = 'z';
    s[24] = 'O';
    s[25] = 'i';
    s[26] = '8';
    s[27] = 'v';
    s[28] = 'd';
    s[29] = '3';
    s[30] = 'd';
    s[31] = '3';
    s[32] = 'L';
    s[33] = 'n';
    s[34] = 'l';
    s[35] = 'v';
    s[36] = 'd';
    s[37] = 'X';
    s[38] = 'R';
    s[39] = '1';
    s[40] = 'Y';
    s[41] = 'm';
    s[42] = 'U';
    s[43] = 'u';
    s[44] = 'Y';
    s[45] = '2';
    s[46] = '9';
    s[47] = 't';
    s[48] = 'L';
    s[49] = '3';
    s[50] = 'd';
    s[51] = 'h';
    s[52] = 'd';
    s[53] = 'G';
    s[54] = 'N';
    s[55] = 'o';
    s[56] = 'P';
    s[57] = '3';
    s[58] = 'Y';
    s[59] = '9';
    s[60] = 'U';
    s[61] = '0';
    s[62] = 'd';
    s[63] = 'G';
    s[64] = 'X';
    s[65] = '2';
    s[66] = 'l';
    s[67] = 'U';
    s[68] = 'T';
    s[69] = 'G';
    s[70] = 'R';
    s[71] = '3';
    s[72] = 'N';
    s[73] = 'F';
    s[74] = 'U';
    s[75] = '=';
}

int main(){
    char nama[240];
    int a,b,c, ans;

    init();
    puts("Hitung semua ya :)");
    for(int i=0; i<100; i++){
        a = rand()%100;
        b = rand()%100;
        c = a+b;

        printf("%d + %d = ", a, b);
        scanf("%d", &ans);
        getchar();
        if(ans != c){
            return 1;
        }
    }

    printf("Wah pintar... siapa sih namamu? > ");
    scanf("%s", nama);
    return 1;
}