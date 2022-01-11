#include "lists.h"

/**
 * insert_node - .
 *
 * @head: head.
 * @number: number.
 *
 * Return: The address of the new node, or NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list, *new, *prev;

	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	list = *head;
	prev = NULL;
	new->n = number;

	while (list && list->n < number)
	{
		prev = list;
		list = list->next;
	}

	new->next = list;

	if (prev)
		prev->next = new;

	else
		*head = new;

	return (list);
}
