#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - sleeps indefinitly
 * Return: returns 0 on success
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - the main function
 * Return: returns 0 on success
*/
int main(void)
{
	int i = 0;

	for (; i < 5; i++)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
