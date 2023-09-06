#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * listint_t : inserts a number into a sorted singly linked list.
 * @head : Pointer to pointer to head of function.
 * @number : Number to be added.
 * Return: Adress of new node or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *tmp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	(*new).n = number;
	current = *head;
	if (current == NULL)
	{
		*head = new;
		(*new).next = NULL;
		return (new);
	}
	if (number < (*current).n)
	{
		(*new).next = current;
		return (new);
	}
	while (current != NULL)
	{
		if ((*current).n < number)
		{
			tmp = current;
			current = (*current).next;
		}
		else
		{
			(*tmp).next = new;
			(*new).next = current;
			break;
		}
	}
	return (new);
}
