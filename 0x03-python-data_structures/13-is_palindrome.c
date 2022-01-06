#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * is_palindrome - Check if linked list is palindrome
 *
 * @head: linked list
 *
 * Return: 1 or 0.
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int new_array[4096];
	int size_list = 0, mitad = 0, i = 0;

	if (!head)
	{
		return (1);
	}
	current = *head;

	while (current)
	{
		new_array[size_list] = current->n;
		size_list++;
		current = current->next;
	}
	size_list--; 
	mitad = size_list / 2;

	for (i = 0; i <= mitad; i++, size_list--)
	{
		if (new_array[i] != new_array[size_list])
			return (0);
	}
	return (1);
}
