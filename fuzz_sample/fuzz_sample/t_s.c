#include <stdio.h>
#include <string.h>
#include <io.h>
#define _CRT_SECURE_NO_WARNINGS

void main(int argc, char* argv[])
{
	char buffer[256];
	puts("Write your buf!!!!!!!!");
	_read(0, buffer, 0x200);
	_write(1, buffer, 0x100);

}