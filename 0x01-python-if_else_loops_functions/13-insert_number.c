#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"
/**
 * insert_node - Inserts number into sorted singly linked list
 * @head: head of list
 * @number: number to insert
 * Return: address of new node; otherwise NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (*head == NULL)
	{
		*head = node;
		node->next = NULL;
		return (node);
	}

	tmp = *head;
	while (tmp->next != NULL)
	{
		if (number < tmp->n)
		{
			node->next = tmp;
			*head = node;
			return (node);
		}
		if (number <= tmp->next->n)
		{
			node->next = tmp->next;
			tmp->next = node;
			return (node);
		}
		tmp = tmp->next;
	}
	node->next = NULL;
	tmp->next = node;
	return (node);
}
