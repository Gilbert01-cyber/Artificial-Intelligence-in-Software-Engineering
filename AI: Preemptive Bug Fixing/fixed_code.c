#include <stdlib.h>

struct list_s {
    int n;
    struct list_s *next;
};
typedef struct list_s list_t;

list_t *add_node_end(list_t **head, const int n) {
    list_t *new_node;
    list_t *current;

    if (!head)
        return (NULL);

    new_node = malloc(sizeof(list_t));
    if (!new_node)
        return (NULL);

    new_node->n = n;
    new_node->next = NULL;

    if (*head == NULL) {
        *head = new_node;
        return (new_node);
    }

    current = *head;
    while (current->next != NULL) {
        current = current->next;
    }

    current->next = new_node;
    return (new_node);
}
