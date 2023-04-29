#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
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
		}
		else
		{
			fprintf(stderr, "Fork failed\n");
			exit(1);
		}
	}

	while (1)
	{
		sleep(1);
	}
	return (0);
}
