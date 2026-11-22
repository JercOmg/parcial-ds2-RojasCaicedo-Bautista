import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


class CampanaPruebas:

    def __init__(self, defectos):
        # defectos = lista con los defectos nuevos de cada semana [28, 23, 22, ...]
        self.defectos = defectos
        self.semanas = []
        self.acumulados = []
        # vamos sumando semana a semana
        total = 0
        semana = 1
        for d in defectos:
            total = total + d
            self.semanas.append(semana)
            self.acumulados.append(total)
            semana = semana + 1
        # a y b se llenan cuando se corre ajustar()
        self.a = 0
        self.b = 0

    def goel(self, t, a, b):
        # modelo de Goel-Okumoto: m(t) = a(1 - e^(-bt))
        # a = total de defectos que tiene el software
        # b = que tan rapido se van encontrando
        # m(t) = cuantos defectos se han encontrado hasta la semana t
        return a * (1 - np.exp(-b * t))

    def ajustar(self):
        # curve_fit busca los a y b que mejor se acomodan a los datos reales
        # p0 son los valores con los que empieza a buscar
        valores, covarianza = curve_fit(self.goel, self.semanas, self.acumulados, p0=[200, 0.1])
        self.a = valores[0]
        self.b = valores[1]
        return self.a, self.b

    def restantes(self):
        # defectos que faltan por encontrar = total - los que van hasta la ultima semana
        t = self.semanas[len(self.semanas) - 1]
        encontrados = self.goel(t, self.a, self.b)
        return self.a - encontrados

    def semana_95(self):
        # semana en la que se habra encontrado el 95% de los defectos
        # despejamos a(1 - e^(-bt)) = 0.95a  ->  t = ln(20) / b
        return np.log(20) / self.b

    def graficar(self):
        # la curva con puntoss entre la semana 0 y la 20
        t = np.linspace(0, 20, 100)
        curva = self.goel(t, self.a, self.b)
        plt.plot(self.semanas, self.acumulados, "o", label="Defectos acumulados reales")
        plt.plot(t, curva, label="Curva ajustada Goel-Okumoto")
        plt.axvline(self.semana_95(), linestyle="--", color="gray", label="95% de defectos")
        plt.title("Defectos acumulados de la version 11.0")
        plt.xlabel("Semana")
        plt.ylabel("Defectos acumulados")
        plt.legend()
        plt.savefig("graficas/resultado.png")
        plt.show()