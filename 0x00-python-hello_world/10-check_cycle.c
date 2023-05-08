#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - checks if linked list has cycle
 * @head: head of list to be checked
 *
 * Return: 0 if no cycle and 1 if cycle
 */
int check_cycle(listint_t *head)
{
	listint_t *tort = NULL;
	listint_t *hare = NULL;

	if (!head || !(head->next))
		return (0);

	tort = head;
	hare = head;

	do {
		tort = tort->next;
		hare = hare->next->next;
		if (tort == hare)
			return (1);
		if (!hare)
			return (0);
	} while (tort != hare);

	return (0);
}
