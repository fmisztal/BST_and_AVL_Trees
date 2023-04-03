import random
import time
import gc
import AVL
import BST
import matplotlib.pyplot as plt


if __name__ == '__main__':

    random.seed(45)

    testing_list = [random.randint(1, 30000) for _ in range(10000)]
    first_n_numbers = [i for i in range(1000, 10001, 1000)]
    times_bst_insert = [] # tablica z czasami bst insert
    times_bst_search = []
    times_avl_insert = []
    times_avl_search = []
    times_bst_delete = []

    # --------------------------------------------------------------------------------------------------------------
    # BST insert

    for n in first_n_numbers:

        gc_old = gc.isenabled()
        gc.disable()

        bst_insert_start = time.process_time()

        bst = BST.BST()
        for i in range(n):
            bst.insert(testing_list[i])

        bst_insert_stop = time.process_time()

        if gc_old:
            gc.enable()

        times_bst_insert.append(bst_insert_stop - bst_insert_start)

    # --------------------------------------------------------------------------------------------------------------
    # AVL insert
    for n in first_n_numbers:
        gc_old = gc.isenabled()
        gc.disable()

        avl_insert_start = time.process_time()

        avl = AVL.BST_AVL()
        for i in range(n):
            avl.insert(testing_list[i])

        avl_insert_stop = time.process_time()

        if gc_old:
            gc.enable()

        times_avl_insert.append(avl_insert_stop - avl_insert_start)

    # --------------------------------------------------------------------------------------------------------------
    # BST search

    for n in first_n_numbers:

        gc_old = gc.isenabled()
        gc.disable()

        bst_search_start = time.process_time()

        for i in range(n):
            bst.search(testing_list[i])

        bst_search_stop = time.process_time()

        if gc_old:
            gc.enable()

        times_bst_search.append(bst_search_stop - bst_search_start)

    # --------------------------------------------------------------------------------------------------------------
    # AVL search

    for n in first_n_numbers:

        gc_old = gc.isenabled()
        gc.disable()

        avl_search_start = time.process_time()

        for i in range(n):
            avl.search(testing_list[i])

        avl_search_stop = time.process_time()

        if gc_old:
            gc.enable()

        times_avl_search.append(avl_search_stop - avl_search_start)

    # --------------------------------------------------------------------------------------------------------------
    # BST delete

    for n in first_n_numbers:
        bst = BST.BST()
        for i in range(10000):
            bst.insert(testing_list[i])

        gc_old = gc.isenabled()
        gc.disable()

        bst_delete_start = time.process_time()

        for i in range(n):
            bst.delete(testing_list[i])

        bst_delete_stop = time.process_time()

        if gc_old:
            gc.enable()

        times_bst_delete.append(bst_delete_stop - bst_delete_start)

    plt.plot(times_bst_insert, label="BST")
    plt.plot(times_avl_insert, label="AVL")
    plt.title('Czas wstawiania węzłów')
    plt.xlabel('Liczba elementów')
    plt.ylabel('Czas')
    plt.legend()
    plt.xticks(range(len(first_n_numbers)), first_n_numbers)
    plt.savefig('Czas_wstawiania_węzlów.jpg', dpi=100)
    plt.show()

    plt.plot(times_bst_search, label="BST")
    plt.plot(times_avl_search, label="AVL")
    plt.title('Czas wyszukiwania węzlow')
    plt.xlabel('Liczba elementów')
    plt.ylabel('Czas')
    plt.legend()
    plt.xticks(range(len(first_n_numbers)), first_n_numbers)
    plt.savefig('Czas_wyszukiwania_węzlow.jpg', dpi=100)
    plt.show()

    plt.plot(times_bst_delete, label="BST")
    plt.title('Czas usuwania węzłów')
    plt.xlabel('Liczba elementów')
    plt.ylabel('Czas')
    plt.legend()
    plt.xticks(range(len(first_n_numbers)), first_n_numbers)
    plt.savefig('Czas_usuwania_węzlow.jpg', dpi=100)
    plt.show()




