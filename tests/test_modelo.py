import sys
sys.path.append("src")

from modelo import CampanaPruebas


def test_goel_en_cero():
    # prueba del enunciado: en la semana 0 no se ha encontrado ningun defecto
    campana = CampanaPruebas([28, 23])
    assert campana.goel(0, 150, 0.2) == 0


def test_acumulados():
    # 28, luego 28+23 = 51, luego 51+22 = 73
    campana = CampanaPruebas([28, 23, 22])
    assert campana.acumulados == [28, 51, 73]
