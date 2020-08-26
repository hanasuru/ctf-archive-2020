

#include<stdio.h>
#include<stdlib.h>

int flag_index;
char *memo[3];

int read_int()	{
	char buf[5];
	fgets(buf, 5, stdin);
	return atoi(buf);
}

void print_menu()	{
	puts("1. New Memo");
	puts("2. Print Memo");
	puts("3. Delete Memo");
	puts("4. Get Flag Memo");
	printf("Choice: ");
}

void new_memo()	{
	printf("Index: ");
	int ind = read_int();
	if(ind < 0 || ind > 3)	{
		puts("Out of bounds!");
		return;
	}
	if(ind == flag_index)	{
		puts("Lol no");
		return;
	}
	memo[ind] = malloc(32);
	printf("Enter memo (max 32 characters, no overflow, we use fgets :D): ");
	fgets(memo[ind], 32, stdin);
	printf("The new memo is located at index %d\n", ind);
}

void print_memo()	{
	printf("Index: ");
	int ind = read_int();
	if(ind < 0 || ind > 3)	{
		puts("Out of bounds!");
		return;
	}
	if(ind == flag_index)	{
		puts("Lol no");
		return;
	}
	printf("Data: %s\n", memo[ind]);
}

void delete_memo()	{
	printf("Index: ");
	int ind = read_int();
	if(ind < 0 || ind > 3)	{
		puts("Out of bounds!");
		return;
	}
	if(ind == flag_index)	{
		puts("Lol no");
		return;
	}
	free(memo[ind]);
	printf("Memo at %d has been deleted\n", ind);
}

void get_flag_memo()	{
	if(flag_index != -1)	{
		puts("You cant get the flag twice!");
		return;
	}
	printf("Allocate to what index? ");
	int ind = read_int();
	if(ind < 0 || ind > 3)	{
		puts("Out of bounds!");
		return;
	}
	flag_index = ind;
	memo[flag_index] = malloc(32);
	FILE *fp = fopen("flag.txt", "r");
	fgets(memo[flag_index], 32, fp);
	printf("Ok flag is at index %d\n", flag_index);
}

int main(int argc, char const *argv[])
{
	setvbuf(stdout, NULL, _IONBF, 0);
	puts("Pada soal ini, akan diberi program untuk menyimpan sejumlah memo");
	puts("Ada opsi untuk medapatkan memo yang berisi flag, tapi gaboleh dibaca :)");
	puts("Gunakan Use-After-Free untuk mendapatkan flagnya");
	flag_index = -1;

	while(1)	{
		print_menu();
		int choice = read_int();
		switch(choice)	{
			case 1:
				new_memo();
				break;
			case 2:
				print_memo();
				break;
			case 3:
				delete_memo();
				break;
			case 4:
				get_flag_memo();
				break;
			default:
				puts("Invalid choice!");
		}
	}
	return 0;
}