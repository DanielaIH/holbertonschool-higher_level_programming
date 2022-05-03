#include "lists.h"

/**
 * check_cycle - check the code
 * @list: pointer to first element of linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *faster = list;

	while (current != NULL && faster != NULL && faster->next != NULL)
	{
		current = current->next;
		faster = faster->next->next;

		if (current == faster)
			return (1);
	}
	return (0);
}
