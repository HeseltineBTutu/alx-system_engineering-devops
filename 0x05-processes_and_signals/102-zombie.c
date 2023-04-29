#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - Run an infinite while loop.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
}

/**
 * main- a C program that creates 5 zombie processes.
 *
 * Return: Always 0 (Success)
 *
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i <= 5; i++)
	{
		pid = fork();

		if (pid == 0)
		{
			exit(0);
		}
		else if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
		else
		{
			exit(0);
		}
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
