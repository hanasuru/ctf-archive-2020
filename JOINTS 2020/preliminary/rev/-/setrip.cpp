#include<iostream>
#include<string.h>
using namespace std;

int check(string text){
	string flag_enc="/{}-:'\x0f\r}-:'3{A'+\x10-+3-:";
	string enc;
	for(int i=0;i<text.length();i++){
            enc += char(int(text[i]+200)%128);
	}
	return enc == flag_enc;
}


int main(){
	string pass;
	cout <<"password: ";
	fflush(stdout);
	cin >> pass ;
	if(check(pass))
		printf("PogChamp\n");
	else
		printf("PepeHands\n");
}
