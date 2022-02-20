# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Payment (зарплата). В классе должны быть представлены поля: фамилия-имя-отчество, оклад,
год поступления на работу, процент надбавки, подоходный налог, количество отработанных дней в месяце, количество
рабочих дней в месяце, начисленная и удержанная суммы. Реализовать методы: вычисления начисленной суммы, вычисления
удержанной суммы, вычисления суммы, выдаваемой на руки, вычисления стажа. Стаж вычисляется как полное количество
лет, прошедших от года поступления на работу, до текущего года. Начисления представляют собой сумму, начисленную за
отработанные дни, и надбавки, то есть доли от первой суммы. Удержания представляют собой отчисления в пенсионный
фонд (1% от начисленной суммы) и подоходный налог. Подоходный налог составляет 13% от начисленной суммы без
отчислений в пенсионный фонд.
"""


class Payment:

    def __init__(self, name='', salary=0, year=0, percent=0, worked_days=0, working_day=1):
        self.name = str(name)
        self.salary = int(salary)
        self.year = int(year)
        self.percent = float(percent)
        self.worked_days = int(worked_days)
        self.working_day = int(working_day)
        self.amount = 0
        self.held_amount = 0
        self.hand_amount = 0
        self.exp = 0

        self.accrued_amount()
        self.withheld_amount()
        self.handed_amount()
        self.experience()

    def read(self):
        name = input('Введите ФИО: ')
        salary = input('Введите оклад: ')
        year = input('Введите год вашего поступления на работу: ')
        percent = input('Введите процент надбавки: ')
        worked_days = input('Введите количество отработанных дней в месяце: ')
        working_day = input('Введите количество рабочих дней в месяце: ')

        self.name = str(name)
        self.salary = int(salary)
        self.year = int(year)
        self.percent = float(percent)
        self.worked_days = int(worked_days)
        self.working_day = int(working_day)

        self.accrued_amount()
        self.withheld_amount()
        self.handed_amount()
        self.experience()

    def display(self):
        print(f"Начисленная сумма: {round(self.amount)} руб.")
        print(f"Удержанная сумма: {round(self.held_amount)} руб.")
        print(f"Сумма выданная на руки: {round(self.hand_amount)} руб.")
        print(f"Трудовой стаж: {self.exp} лет")

    def accrued_amount(self):
        a = self.salary / self.working_day
        b = a * self.worked_days
        percent = self.percent / 100 + 1
        self.amount = b * percent

    def withheld_amount(self):
        plata = (self.salary / self.working_day) * self.worked_days
        self.held_amount = (plata * 0.13) + (plata * 0.01)

    def handed_amount(self):
        self.hand_amount = self.amount - self.held_amount

    def experience(self):
        self.exp = 2022 - self.year


if __name__ == '__main__':
    r1 = Payment("Иванов Иван Иванович", 30000, 2010, 15, 25, 30)
    r1.display()

    r2 = Payment()
    r2.read()
    r2.display()
