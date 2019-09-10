#include "lists.h"

/**
 * check_cycle - checks if singly liked list has a cycle 
 * @list: linked list
 * Return: 0 if no cycle, 1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp, *second;

	tmp = list;
	second = list;
	while (tmp && second && second->next)
	{
		second = second->next->next;
		tmp = tmp->next;
		if (second == tmp)
			return (1);
	}
	return (0);
}
