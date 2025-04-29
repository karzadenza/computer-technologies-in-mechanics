"""
Модуль реализует решение задачи узлового анализа
"""

from scipy.interpolate import interp1d
from scipy.optimize import brentq

class Nodal_ANALysis:
    """
    Класс решения задачи узлового анализа
    """
    def __init__(self,
                ipr: tuple,
                vlp: tuple) -> tuple:
        """
        Метод инициализации 

        Parameters
        ---
        :param ipr: кривая притока
        :param vlp: кривая оттока

        Returns
        ---
        :return: None
        """
        self.ipr = interp1d(ipr[0], ipr[1])
        self.vlp = interp1d(vlp[0], vlp[1])
        q_max = min(ipr[0][-1], vlp[0][-1])
        self.q_range = (0, q_max)

    def calc_NA(self) -> tuple:
        """
        Метод расчета узлового анализа

        Parameters
        ---
        :param: self 

        Returns
        ---
        :return: кортеж с координатой точки пересечения 
        графиков IPR и VLP (Q, Pwf).
        """
        def difference(q):
            "разность между кривой притока и кривой оттока при данном дебите"
            return self.ipr(q) - self.vlp(q)
        
        try:
            # Ищем дебит межу q_range0 qrange1 при котором differece станет равен нулю - кривая притока будет равна кривой оттока
            root = brentq(
                difference,
                self.q_range[0],
                self.q_range[1]
            )
        except:
            return 'Решения узлового анализа нет'

        
        P_wf = self.ipr(root)
        
        return (root, P_wf)
    