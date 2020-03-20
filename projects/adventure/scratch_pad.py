import random
dirs = ['n', 's', 'e', 'w']





for i in range(0, 1000):
    rand_num = random.randrange(0, len(dirs))
    print(dirs[rand_num])