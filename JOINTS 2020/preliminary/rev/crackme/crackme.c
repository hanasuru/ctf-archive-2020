#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
}

int checker(char s[25]){
	if(s[20] - s[0] != 24) return 0;
	if(s[8] + s[5] != 126) return 0;
	if(s[14] * s[5] != 3696) return 0;
	if(s[21] - s[1] != 33) return 0;
	if(s[10] - s[0] != 2) return 0;
	if(s[17] - s[0] != 19) return 0;
	if(s[17] * s[1] != 3848) return 0;
	if(s[4] + s[6] != 123) return 0;
	if(s[13] * s[16] != 4488) return 0;
	if(s[1] * s[6] != 2600) return 0;
	if(s[13] * s[23] != 3536) return 0;
	if(s[8] - s[5] != 14) return 0;
	if(s[15] + s[5] != 123) return 0;
	if(s[20] - s[17] != 5) return 0;
	if(s[17] + s[16] != 140) return 0;
	if(s[16] + s[14] != 132) return 0;
	if(s[3] * s[6] != 4250) return 0;
	if(s[18] + s[14] != 145) return 0;
	if(s[13] + s[13] != 136) return 0;
	if(s[17] - s[10] != 17) return 0;
	if(s[11] + s[8] != 145) return 0;
	if(s[9] + s[1] != 135) return 0;
	if(s[11] + s[24] != 146) return 0;
	if(s[3] - s[7] != 11) return 0;
	if(s[0] - s[2] != 2) return 0;
	if(s[11] - s[13] != 7) return 0;
	if(s[3] + s[4] != 158) return 0;
	if(s[3] - s[16] != 19) return 0;
	if(s[4] - s[14] != 7) return 0;
	if(s[12] * s[1] != 4056) return 0;
	if(s[20] + s[8] != 149) return 0;
	if(s[9] - s[4] != 10) return 0;
	if(s[9] - s[6] != 33) return 0;
	if(s[9] * s[13] != 5644) return 0;
	if(s[16] + s[5] != 122) return 0;
	if(s[16] - s[10] != 9) return 0;
	if(s[17] + s[24] != 145) return 0;
	if(s[20] - s[13] != 11) return 0;
	if(s[18] * s[11] != 5925) return 0;
	if(s[21] * s[23] != 4420) return 0;
	if(s[22] * s[7] != 5698) return 0;
	if(s[15] - s[19] != 12) return 0;
	if(s[16] - s[1] != 14) return 0;
	if(s[3] - s[13] != 17) return 0;
	if(s[12] * s[8] != 5460) return 0;
	if(s[21] * s[13] != 5780) return 0;
	if(s[7] * s[1] != 3848) return 0;
	if(s[22] + s[6] != 127) return 0;
	if(s[13] + s[5] != 124) return 0;
	if(s[24] + s[1] != 123) return 0;
	
	return 1;
}

void unlock(){
	FILE *fp;
	char ch;
	fp = fopen("flag.txt","r");
	while((ch = fgetc(fp)) !=EOF)
		printf("%c", ch);
	fclose(fp);
}

int main(){
	char s[25];
	scanf("%5c-%5c-%5c-%5c-%5c",&s[0],&s[5],&s[10],&s[15],&s[20]);
	s[25]=0;
	if(checker(s)) unlock();
	else printf("Invalid serial key");
}
