"""
Модуль визуализации основных расчетов узлового анализа
"""
import matplotlib.pyplot as plt

def nodal_plot(
        ipr: tuple[list[float],list[float]], 
        vlp: tuple[list[float],list[float]], 
        root: tuple[float, float]
    ) -> None:
    """
    Функция для визуализации кривых притока и оттока, а также решения задачи узлового анализа.

    Parameters
    ---
    :param ipr: Данные кривой притока: кортеж из массивов Qipr [м3/сут], Pwf [атм]
    :param vlp: Данные кривой оттока: кортеж из массивов Qvlp [м3/сут], Pwf [атм]
    :param root: Рабочая точка - решение задачи узлового анализа: кортеж (Q, Pwf)

    Returns
    ---
    :return: None
    """
    plt.plot(ipr[0], ipr[1], label='IPR')
    plt.plot(vlp[0], vlp[1], label='VLP')

    if type(root) == tuple:
        plt.scatter(root[0], root[1], c='g', label='Working point')
        print(f'Рабочая точка равна: {root}')
    else:
        print(root)
    
    plt.xlabel('Q, м^3/сут')
    plt.ylabel('Pwf, атм.')
    plt.title('Узловой анализ')
    plt.legend()
    plt.grid()
    plt.show()
