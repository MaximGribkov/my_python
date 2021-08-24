import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    #стиль точек
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    points_numvers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=points_numvers, cmap=plt.cm.Blues,
    edgecolors='none', s=1)

    #выделение первый и последней
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    #заупуск графика
    plt.show()

    #выход из программы
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
    if keep_running != 'y':
        print('Unidentified command ')
        keep_running = input('Re-enter ')
        if keep_running == 'n':
            break