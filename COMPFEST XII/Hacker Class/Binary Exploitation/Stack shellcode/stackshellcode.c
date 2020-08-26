

#include <stdio.h>

int main(int argc, char const *argv[])
{
	setvbuf(stdout, NULL, _IONBF, 0);

	char buf[400];
	printf("Here is the address of buf: %lp\n", &buf);
	printf("Now input the shellcode and run it: ");

	gets(buf);
	return 0;
}
