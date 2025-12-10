# Nombre màxim d'asteris
max_files = 3

# Primera part: de 1 fins a max_files
for i in range(1, max_files + 1):
    print('*' * i)

# Segona part: de max_files-1 fins a 1
for i in range(max_files - 1, 0, -1):
    print('*' * i)
