"""
Модуль расчета кривой притока IPR
"""

import numpy as np

class Layer:
    """
    Класс расчета кривой притока, описывает пласт.
    """
    def __init__(
            self, 
            P_e, 
            product_coef
        ):
        """
        Метод инициализации 

        Parameters
        ---
        :param: self
        :param P_e: Давление в пласте, [атм.].
        :param product_coef: коэффициент продуктивности, [безразм.].

        Returns
        ---
        :return: None
        """
        self.P_e = P_e
        self.product_coef = product_coef

    def calc_P_wf(self,
                  q: float) -> float:
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
        return - self.product_coef * q + self.P_e
    

    def calc_ipr(self) -> tuple[list]:
        """
        Метод расчета кривой притока 

        Parameters
        ---
        :param: self

        Returns
        ---
        :return: кортеж из списков значений дебита и забойного давления (Q, Pwf)
        """
        q_max = (self.P_e - 1) / self.product_coef
        q_list = np.linspace(0, q_max, 10)
        P_wf_list = self.calc_P_wf(q_list)

        return (q_list, P_wf_list)
