#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — дробное положительное число, оклад; поле second — целое число,
количество отработанных дней в месяце. Реализовать метод summa () — вычисление начисленной
суммы за данное количество дней для заданного месяца: оклад/дни месяца * отработанные дни.
"""


class Payment:

    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def read(self):
        self.first = float(input("Введите дробное число, оклад: "))
        self.second = int(input("Введите целое число, число отработанных дней в месяце: "))
        self.third = int(input("Введите целое число, количество дней в месяце: "))

    def display(self):
        print(f"Начисленное сумма за данное количество дней: {self.first / self.third * self.second}")

    def summa(self):
        return self.first / self.third * self.second


if __name__ == "__main__":
    amount = Payment(28500.5, 25, 30)
    amount.display()
    amount.read()
    amount.summa()
    amount.display()
