"""
Проект для решения задач узлового анализа
"""

# from nodal_analysis.inflow_perfomance.ipr_model import Layer
# from nodal_analysis.outflow_perfomance.vlp_model import Well
# from nodal_analysis.nodal_analysis import Nodal_ANALysis
# from nodal_analysis.plotting import nodal_plot


from nodal_analysis.inflow_perfomance import Layer
from nodal_analysis.outflow_perfomance import Well
from nodal_analysis import Nodal_ANALysis
from nodal_analysis import nodal_plot


def input_data() -> list[float]:

    """
    Функция для инициализации входных данных.

    Parameters
    ---
    :param: None

    Returns
    ---
    :return: список введенных параметров
    """

    # P_e = input("Давление пластовое [атм.]: ")
    # P_wh = input("Давление буферное [атм.]: ")
    # product_coef = input("Коэффициент продуктивности пласта [безразм.]: ")
    # k = input("Производительность скважины [безразм.]: ")
    # h = input("Глубина скважины [м]: ")
    # rho_f = input("Плотность флюида [кг/м3]: ")

    P_e = 250
    product_coef = 1
    P_wh = 1
    h = 1500
    rho_f = 900
    k = 1

    try:
        P_e, product_coef, P_wh, h, rho_f, k = float(P_e), float(product_coef), float(P_wh), float(h), float(rho_f), float(k)
    except ValueError:
        return None
    
    return [P_e, product_coef, P_wh, h, rho_f, k]
    

def solve(P_e: float,
        product_coef: float,
        P_wh: float,
        h: float,
        rho_f: float,
        k: float) -> None:
    """
    Функция для запуска расчетов кривых притока, а узлового анализа.

    Parameters
    ---
    :param P_e: Давление пластовое [атм.]: "
    :param P_wh: Давление буферное [атм.]: "
    :param product_coef: Коэффициент продуктивности пласта [безразм.]: "
    :param k: Производительность скважины [безразм.]: "
    :param h: Глубина скважины [м]: "
    :param rho_f: Плотность флюида [кг/м3]: "

    Returns
    ---
    :return: None
    """
    layer = Layer(
        P_e=P_e,
        product_coef=product_coef
    )
    ipr = layer.calc_ipr()

    well = Well(
        P_wh=P_wh,
        h=h, 
        rho_f=rho_f,
        k=k
    )
    vlp = well.calc_vlp(P_e=P_e)

    nodal = Nodal_ANALysis(
        ipr=ipr,
        vlp=vlp
    )
    point = nodal.calc_NA()

    nodal_plot(
        ipr=ipr,
        vlp=vlp,
        root=point
    )

def main():
    """
    Функция для инициализации данных и запуска расчетов.

    Parameters
    ---
    :param: None

    Returns
    ---
    :return: None
    """
    data = input_data()
    solve(*data)


if __name__ == '__main__':
    main()
