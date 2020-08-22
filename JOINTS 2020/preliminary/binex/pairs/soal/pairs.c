// gcc pairs.c -o pairs -fstack-protector-all -pie -Wl,-z,relro,-z,now

#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

char card[6][9] = {
    {'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'},
    {'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I'},
    {'J', 'J', 'K', 'K', 'L', 'L', 'M', 'M', 'N'},
    {'N', 'O', 'O', 'P', 'P', 'Q', 'Q', 'R', 'R'},
    {'S', 'S', 'T', 'T', 'U', 'U', 'X', 'X', 'Y'},
    {'Y', 'Z', 'Z', '0', '0', '1', '1', '2', '2'}
};
int playerScore, computerScore, coor[2][2] = {{-1,-1},{-1,-1}}, match;

void init(){
    int a1,a2,b1,b2;
    char t;
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    srand(time(0));
    for(int i=0; i<1000; i++){
        a1 = rand()%6;
        a2 = rand()%6;
        b1 = rand()%9;
        b2 = rand()%9;
        t = card[a1][b1];
        card[a1][b1] = card[a2][b2];
        card[a2][b2] = t;
    }
}

void win(char *fl){
    FILE *f;
    char ch;
    f = fopen(fl, "r");
    do
    {
        ch = getc(f);
        putchar(ch);
    }while(ch != EOF);
    fclose(f);
}

int read_arr(){
    char s[16], *ss;
    int i=0, valid = 0;
    fgets(s, 16, stdin);
    ss = strtok(s, " ");
    while(ss){
        coor[i/2][i%2] = atoi(ss);
        i++;
        ss = strtok(NULL, " ");
        if(i > 3){
            break;
        }
    }
    if(coor[0][0] > -1 && coor[0][0] < 6 && coor[0][1] > -1 && coor[0][1] < 9){
        if(coor[1][0] > -1 && coor[1][0] < 6 && coor[1][1] > -1 && coor[1][1] < 9){
            if(coor[0][0] != coor[1][0] || coor[0][1] != coor[1][1]){
                valid = 1;
            }
        }
    }
    return valid;
}

int read_int(){
    char s[16];
    fgets(s, 16, stdin);
    return atoi(s);
}

void print_card(){
    for(int i=0; i<6; i++)
    {
        for(int j=0; j<9; j++)
        {
            if(card[i][j] == '-')
            {
                printf("[-] ");
            }
            else if(i == coor[0][0] && j == coor[0][1]){
                printf("[%c] ", card[coor[0][0]][coor[0][1]]);
            }
            else if(i == coor[1][0] && j == coor[1][1]){
                printf("[%c] ", card[coor[1][0]][coor[1][1]]);
            }
            else
            {
                printf("[#] ");
                // printf("[%c] ", card[i][j]);
            }
        }
        puts("");
    }
}

int is_game_end(){
    for(int i=0; i<54; i++){
        if(card[i/9][i%9] != '-'){
            return 0;
        }
    }
    return 1;
}

int computer_logic(){
    char x = '$';
    for(int i=0; i<54; i++){
        if(card[i/9][i%9] != '-' && x == '$'){
            x = card[i/9][i%9];
            coor[0][0] = i/9;
            coor[0][1] = i%9;
        }
        else if(card[i/9][i%9] == x){
            coor[1][0] = i/9;
            coor[1][1] = i%9;
            break;
        }
    }
    computerScore += 100;
    match = 1;
    sleep(1);
    return 1;
}

int player_logic(){
    int v = 0;
    do{
        printf("> Coordinate (c1 c2 c3 c4) : ");
        v = read_arr();
    }while (!v);
    
    if(card[coor[0][0]][coor[0][1]] == '-' || card[coor[1][0]][coor[1][1]] == '-'){
        puts("Invalid card!");
        match = 0;
        return 1;
    }
    else if (card[coor[0][0]][coor[0][1]] != card[coor[1][0]][coor[1][1]])
    {
        match = 0;
        return 1;
    }
    else
    {
        playerScore += 100;
        match = 1;
        return 0;
    }
}

void game_logic(){
    int turn=0;
    printf("\nComputer score : %d\n", computerScore);
    printf("Player score   : %d\n", playerScore);
    print_card();
    while (!is_game_end())
    {
        if(turn == 0){
            turn = player_logic();
            puts("");
            printf("Computer score : %d\n", computerScore);
            printf("Player score   : %d\n", playerScore);
            print_card();
        }
        else if (turn == 1)
        {
            puts("");
            turn = computer_logic();
            printf("Computer score : %d\n", computerScore);
            printf("Player score   : %d\n", playerScore);
            print_card();
            printf("> Computer : %d %d & %d %d\n", coor[0][0], coor[0][1], coor[1][0], coor[1][1]);
        }
        if(match){
            card[coor[0][0]][coor[0][1]] = '-';
            card[coor[1][0]][coor[1][1]] = '-';
        }
    }
    if(playerScore == 2700){
        puts("\nCongrats!\nTake your prize :");
        win("./flag.txt");
    }
    else if(playerScore > computerScore){
        puts("Better luck next time...");
        win("./not_flag.txt");
    }
    else
    {
        puts("\n:(");
    }
}

void how_to(){
    puts("https://en.wikipedia.org/wiki/Concentration_(card_game)");
}

void main_menu(){
    puts("\n--- MENU ---");
    puts("[1] Start");
    puts("[2] How to play");
    puts("[3] Exit");
    printf("> ");
}

int main(){
    int c;
    init();
    while(1)
    {
        main_menu();
        c = read_int();
        switch (c)
        {
        case 1:
            game_logic();
            exit(0);
            break;
        
        case 2:
            how_to();
            break;
        
        case 3:
            exit(0);
        
        default:
            puts("Invalid Choice");
        }
    }
    
}