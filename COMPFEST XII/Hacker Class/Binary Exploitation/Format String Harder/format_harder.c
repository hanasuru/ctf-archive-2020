

#include<stdio.h>
#include<stdlib.h>

int main(int argc, char const *argv[])
{
	setvbuf(stdout, NULL, _IONBF, 0);

	char buf[20];
	int* hack_me = malloc(10);
	*hack_me = 5;

	printf("This is the location of the hack_me varible: %lp\n", hack_me);

	puts("Ok now change its value to 420");

	fgets(buf, 20, stdin);
	printf(buf);

	if(*hack_me == 420)
		system("cat flag.txt");
	else
		puts("Sorry you failed");

	return 0;
}