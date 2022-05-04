#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Function that inserts a number into a sorted singly list.
 * @head: pointer to the list
 * @number: number to add
 *
 * Return: address of the added node else NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old, *new, *actual;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	old = NULL;
	actual = *head;

	for (; actual != NULL && actual->n < number;)
	{
		old = actual;
		actual = actual->next;
	}

	new->next = actual;

	if (old != NULL)
		old->next = new;
	else
		*head = new;

	return (new);
}
