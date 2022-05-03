#include "lists.h"

/**
 * check_cycle - check the code
 * @list: pointer to first element of linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;
	if (list != NULL)
		current = current->next;
	while (current != NULL)
	{
		if (current == list)
			return (1);
		current = current->next;
	}
	return (0);
}
