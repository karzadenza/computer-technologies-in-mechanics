"""
Модуль реализации расчета кривой оттока VLP
"""

import numpy as np

class Well:
    """
    Класс расчета кривой притока, описывает пласт.
    """
    def __init__(self, 
                 P_wh: float, 
                 h: float, 
                 rho_f: float, 
                 k: float) -> None:
        """
        Метод инициализации 

        Parameters
        ---
        :param: self
        :param P_wh: Давление на забое, [атм.].
        :param h: Мощность пласта [м].
        :param rho_f: Плотность флюида, [кг/м3].
        :param k: Производительность скважины, [безразм.].

        Returns
        ---
        :return: None
        """
        self.P_wh = P_wh
        self.h = h
        self.rho_f = rho_f
        self.k = k

    def calc_P_wf(self, q):
        """
        Метод расчета забойного давления 

        Parameters
        ---
        :param: self
        :param q: Дебит, [м3/сут].

        Returns
        ---
        :return: значение забойного давления [атм.]
        """
        return self.k * q + (self.rho_f * 9.81 * self.h) / 101325 + self.P_wh

    def calc_vlp(self, 
                 P_e: float) -> tuple[list]:
        """
        Метод расчета кривой оттока 

        Parameters
        ---
        :param: self
        :param P_e: Давление в пласте, [атм.]

        Returns
        ---
        :return: кортеж из списков значений дебита и забойного давления (Q, Pwf)
        """
        q_max = (P_e - (self.rho_f * 9.81 * self.h) / 101325) / self.k
        q_list = np.linspace(0, q_max, 10)
        P_wf_list = self.calc_P_wf(q_list)
        return (q_list, P_wf_list)
