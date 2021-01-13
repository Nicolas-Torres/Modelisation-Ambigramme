#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <semaphore.h>

// Limite de l'incrément
//#define TAILLE 5

int ordre = 0;
typedef struct thread_data
{
    int thread_id;
    int valIndTab1;
    int valIndTab2;
    int taille;
} Data;
sem_t *sem;

void *add2(void *arg)
{
    pthread_t tid = pthread_self();
    Data *data = (Data *)arg;
    //section critique
    sem_wait(&sem[data->thread_id]);
    printf("Le thread [%ld], la somme des deux valeurs à l'indice [%d] = %d \n", tid, data->thread_id, (data->valIndTab1 + data->valIndTab2));
    //fin de la section critique
    if (data->thread_id != data->taille - 1)
    {
        int indiceSuivant = data->thread_id + 1;
        sem_post(&sem[indiceSuivant]);
    }
    free(data);
    pthread_exit(NULL);
}

//processus principal
void add2tabs(int *tab1, int *tab2, int taille)
{
    pthread_t threadsId[taille];
    //allocation de mémoire du tableau des sémaphores
    sem = (sem_t *)malloc(sizeof(sem_t) * taille);
    // initialiser tous les sémaphores à O ccupé (valeur à 0) sauf le premier à 1
    for (int count = 1; count < taille; count++)
    {
        // vérifier les paramètres d'initialisation : pshared =0 si le sem est partagé par tous les threads
        // value =0 alors le semaphore est occupé et 1 pour libre!
        sem_init(sem + count, 0, 0);
    }
    //le premier sem est libre
    sem_init(sem, 0, 1);

    for (int count = 0; count < taille; count++)
    {
        Data *data = (Data *)malloc(sizeof(Data));
        data->thread_id = count;
        data->valIndTab1 = tab1[count];
        data->valIndTab2 = tab2[count];
        data->taille = taille;
        pthread_create(&threadsId[count], NULL, add2, data);
    }

    for (int count = 0; count < taille; count++)
    {
        pthread_join(threadsId[count], NULL);
    }
    for (int i = 0; i < taille; i++)
        sem_destroy(sem + i);
}

void main()
{

    int tab1[5] = {1, 2, 3, 10, -1};

    int tab2[5] = {1, 1, 2, 1, 11};
    add2tabs(tab1, tab2, 5);
}