#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * len_list - Return the length of a singly linked list.
 * @head : Pointer to pointer to head of singly linked list.
 * Return: Len of list.
 */
int len_list(listint_t *head)
{
	int len = 0;
	listint_t *current = head;

	while (current != NULL)
	{
		len++;
		current = current->next;
	}
	return (len);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head : Pointer to pointer to head of singly linked list.
 * Return: 1 if palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int len = len_list(*head);
	int numbers[len], i = 0, result = 1;

	if (*head == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		numbers[i] = (*current).n;
		current = (*current).next;
		i++;
	}
	i = 0;
	while (i < len / 2)
	{
		if (numbers[i] != numbers[len - 1 - i])
		{
			result = 0;
			break;
		}
		i++;
	}
	return (result);
}
