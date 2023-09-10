#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head : Pointer to pointer to head of singly linked list.
 * Return: 1 if palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int len = 0, i = 0, result = 1, *array;

	if (*head == NULL)
		return (1);
	current = *head;
        while (current != NULL)
	{
		len++;
		current = current->next;
	}
	array = malloc(len * sizeof(int));
	if (array == NULL)
		return (0);
	current = *head;
	while (current != NULL)
	{
		array[i] = (*current).n;
		current = (*current).next;
		i++;
	}
	i = 0;
	while (i < len / 2)
	{
		if (array[i] != array[len - 1 - i])
		{
			result = 0;
			break;
		}
		i++;
	}
	free(array);
	return (result);
}
