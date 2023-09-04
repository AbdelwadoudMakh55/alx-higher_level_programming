#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Check if a linked list has a cycle.
 * @list : Pointer to head of linked list.
 * Return: 1 if there is a cycle, 0 if not.
 */
int check_cycle(listint_t *list)
{
	int values[100], i = 0, j;

	while (list != NULL)
	{
		values[i] = (*list).n;
		for (j = 0; j < i; j++)
			if (values[j] == values[i])
				return (1);
		i++;
		list = (*list).next;
	}
	return (0);
}
