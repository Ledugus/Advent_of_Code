import numpy as np
from utils import *


def step_1(filename):

    f = open(filename)
    disk_map = f.readline().strip()
    f.close()
    disk_map = np.array([int(x) for x in disk_map])

    disk_block_index = 0
    checksum = 0
    file_from_end_index = len(disk_map) - 1
    remaining_end_file_block = disk_map[-1]
    disk_size = sum(disk_map)
    disk_empty_space = sum([disk_map[i] for i in range(1, len(disk_map), 2)])
    disk_use = disk_size - disk_empty_space

    end = False
    for file_from_begin_index, size in enumerate(disk_map):
        # pour chaque élément de la map
        # si c'est un nombre pair
        if file_from_begin_index % 2 == 0:
            # le long de la taille du bloc, update la checksum

            for _ in range(size):
                if disk_block_index == disk_use:
                    end = True
                    break
                checksum += file_from_begin_index // 2 * disk_block_index
                disk_block_index += 1

        else:

            # espace vide -> aller chercher le fichier du fond de la disk_map

            for _ in range(size):
                if disk_block_index == disk_use:
                    end = True
                    break
                if remaining_end_file_block == 0:
                    file_from_end_index -= 2
                    remaining_end_file_block = disk_map[file_from_end_index]
                checksum += file_from_end_index // 2 * disk_block_index
                disk_block_index += 1
                remaining_end_file_block -= 1
        if end:
            break

    return checksum


def step_2(filename):
    f = open(filename)
    disk_map = f.readline().strip()
    f.close()
    disk_map = [int(x) for x in disk_map]

    # get literal string of disk
    """
    disk = ""
    for i, size in enumerate(disk_map):
        if i % 2 == 0:

            for _ in range(size):
                disk += str(file_index)
            file_index += 1
        else:
            for _ in range(size):
                disk += "."
    print(disk)
    """
    # process disk

    current_block_index = 0
    checksum = 0
    checked_files_indexes = set()
    current_file_index = 0

    while current_file_index < len(disk_map):
        print()
        print("===== CURRENT DISK MAP POSITION =====", current_file_index)
        print(disk_map)
        # si c'est un fichier pas encore pris en compte
        if current_file_index % 2 == 0:
            print("COUTING REAL FILE", current_file_index)
            size = disk_map[current_file_index]
            read = current_file_index in checked_files_indexes
            for _ in range(size):
                if not read:
                    checksum += current_file_index // 2 * current_block_index
                current_block_index += 1
            checked_files_indexes.add(current_file_index)
            current_file_index += 1
        # c'est un espace disque libre
        # il faut chercher à le remplir
        else:
            size = disk_map[current_file_index]
            # si le trou est de taille nulle, passer au fichier suivant
            if size == 0:
                current_file_index += 1
                print("NULL SIZE HOLE")
                continue
            found = False
            for file_index in range(len(disk_map) - 1, current_file_index, -2):
                if file_index in checked_files_indexes:
                    continue
                found_file_size = disk_map[file_index]
                if found_file_size <= size:
                    # FICHIER OK -> COPIER ET AVANCER
                    print(found_file_size, "<=", size)
                    print(
                        "FILL HOLE",
                        current_file_index,
                        "OF SIZE",
                        size,
                        "WITH FILE",
                        file_index,
                        "OF SIZE",
                        found_file_size,
                    )
                    found = True
                    # remplir l'espace vide avec le fichier trouvé
                    # c'est à dire updater la checksum
                    for _ in range(found_file_size):
                        checksum += file_index * current_block_index
                        current_block_index += 1

                    checked_files_indexes.add(file_index)
                    # updater la taille du trou restant
                    disk_map[current_file_index] = (
                        disk_map[current_file_index] - found_file_size
                    )
                    break

            if not found:
                print("FOUND NO FILE TO FILL HOLE", current_file_index)
                current_file_index += 1
                current_block_index += size

    return checksum


# print(step_1("2024/09_test.txt"))

# print(step_1("2024/09_input.txt"))

print(step_2("2024/09_test.txt"))
# print(step_2("2024/09_input.txt"))
