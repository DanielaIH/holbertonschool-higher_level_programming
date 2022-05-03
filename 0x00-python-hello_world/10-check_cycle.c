#include "lists.h"

/**
 * check_cycle - check the code
 * @list: pointer to first element of linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *temp;
	int i = 0;

	current = list;

	while (current != NULL)
	{
		temp = list;
		i = 0;
		while (temp != NULL)
		{
			if (current == temp)
				i++;
			if (i > 1)
				return (1);
			temp = temp->next;
		}
		current = current->next;
	}
	return (0);
}
