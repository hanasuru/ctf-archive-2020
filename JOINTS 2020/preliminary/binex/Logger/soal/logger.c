// gcc logger.c -o logger -fstack-protector-all -pie -Wl,-z,relro,-z,now

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

char name[24];
FILE *f;

void read_str(char *var, int n){
    int nn = read(0, var, n);
    var[nn-1] = 0;
}

void create_log(){
    char n[18];
    printf("Insert log name : ");
    read_str(n, 18);
    sprintf(name, "./lg/%s", n);
    if(f = fopen(name, "r")){
        fclose(f);
        puts("File already exist!");
        exit(0);
    }
    else{
        f = fopen(name, "w");
        fclose(f);
        puts("Log created!");
    }
}

void write_log(){
    char content[160];

    puts("Insert log");
    read_str(content, 160);
    f = fopen(name, "w");
    fprintf(f, content);
    fclose(f);
    puts("");
}

void read_log(){
    char ch;
    puts("Content :");
    f = fopen(name, "r");
    do{
        ch = fgetc(f);
        putchar(ch);
    }
    while(ch != EOF);
    fclose(f);
}

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
}

void menu(){
    puts("\nMENU");
    puts("1. (Over)Write log");
    puts("2. Read log");
    puts("3. Exit");
    printf("> ");
}

int main(){
    int c = 0;
    init();
    create_log();
    while(1)
    {
        menu();
        scanf("%d", &c);
        switch (c)
        {
        case 1:
            write_log();
            break;
        
        case 2:
            read_log();
            break;
        
        case 3:
            exit(0);
        
        default:
            puts("Invalid Choice");
        }
    }
}