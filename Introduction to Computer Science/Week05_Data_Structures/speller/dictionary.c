// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO

    int index = hash(word);
    node *cursor = table[index];
    for (node *temp = cursor; temp != NULL; temp = temp->next)
    {
      if (strcasecmp(temp->word,word) == 0)
        {
            return true;
        }
    }
    return false;
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hashvalue = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        hashvalue += tolower(word[i]);
        hashvalue = (hashvalue * tolower(word[i])) % N;
    }
    return hashvalue;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
     FILE *file = fopen(dictionary, "r");
      if (file == NULL)
    {
        fprintf(stderr, "Could not open dictionary file.\n");
        return false;
    }

    for(int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
     char word[LENGTH + 1];
    while (fscanf(file, "%s", word) != EOF)
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(file);
            fprintf(stderr, "Out of memory.\n");
            return false;
        }
        strcpy(new_node->word, word);
        int index = hash(word);
        new_node->next = table[index];
        table[index] = new_node;

    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO

    int count = 0;

    // Traverse each linked list in the hash table
    for (int i = 0; i < N; i++)
    {
        for (node *tmp = table[i]; tmp != NULL; tmp = tmp->next)
        {
            count++;
        }
    }

    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO

    // Traverse each linked list in the hash table
    for (int i = 0; i < N; i++)
    {
        // Free nodes in the linked list
        while (table[i] != NULL)
        {
            node *tmp = table[i]->next;
            free(table[i]);
            table[i] = tmp;
        }
    }

    return true;
}
