from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Step(ABC):
    @property
    def step_done(self) -> Step:
        return self._step_done

    @step_done.setter
    def step_done(self, step_done: Step):
        self._step_done = step_done

    def add(self, step: Step):
        pass

    def remove(self, step: Step):
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def realize(self):
        pass


class StepFetch(Step):
    def realize(self):
        return f"Step fetch - was done"

    def fetch(self):
        pass


class StepDecode(Step):
    def realize(self):
        return f"Step decode - was done"

    def decode(self):
        pass


class StepExecute(Step):
    def realize(self):
        return f"Step execute - was done"

    def execute(self):
        pass


class Pipeline(Step):
    def __init__(self):
        self._steps: List[Step] = []

    def add(self, step: Step):
        self._steps.append(step)
        step.step_done = self

    def remove(self, step: Step):
        self._steps.remove(step)
        step.step_done = None

    def is_composite(self) -> bool:
        return True

    def realize(self):
        results = []
        for step in self._steps:
            results.append(step.realize())
        return f"PipeLine({'+'.join(results)})"


class Software(ABC):

    @abstractmethod
    def create(self):
        pass


class MobileApp(Software):
    def create(self):
        return f'Mobile app was created'


class WebApp(Software):
    def create(self):
        return f'Web app was created'


class DataBaseAPI(Software):
    def create(self):
        return f'DataBase API was created'


class TechStack(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def programming(self):
        pass


class Swift(TechStack):
    def __init__(self, name):
        super().__init__(name)

    def programming(self):
        return f'Programming in Swift'


class Python(TechStack):
    def __init__(self):
        super().__init__(name)

    def programming(self):
        return f'Programming in Python'


class JavaScript(TechStack):
    def __init__(self):
        super().__init__(name)

    def programming(self):
        return f'Programming in JavaScript'


class Team(ABC):
    def __init__(self, name, quantity_of_members, type_of):
        self.name = name
        self.quantity_of_members = quantity_of_members
        self.type_of = type_of

    @abstractmethod
    def add_member(self, *args):
        pass


class Member:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary


class ScrumTeam(Team):
    def __init__(self, name, quantity_of_members, type_of):
        super().__init__(name, quantity_of_members, type_of)

    def add_member(self, *args):
        members = []
        for person in members:
            print(person.name, person.surname + " was added in team", sep=' ')


class KanbanTeam(Team):
    def __init__(self, name, quantity_of_members, type_of):
        super().__init__(name, quantity_of_members, type_of)

    def add_member(self, *args):
        members = []
        members.append(TeamLead(d.name, d.surname, d.salary, d.tech_stack, d.developer))
        for person in members:
            print(person.name, person.surname + f" was added in {k.name}", sep=' ')


class ScrumbanTeam(Team):
    def __init__(self, name, quantity_of_members, type_of, member: Member):
        super().__init__(name, quantity_of_members, type_of)

    def add_member(self, *args):
        members = []
        for person in members:
            print(person.name, person.surname + " was added in team", sep=' ')


class Developer(Member):
    def __init__(self, name, surname, salary, tech_stack, member):
        super().__init__(name, surname, salary)
        self._member = member
        self.tech_stack = tech_stack

    def do_work(self):
        self.tech_stack.programming()
        return print(f'{self.name} {self.surname} programming in {self.tech_stack.name}')


class BusinessAnalyst(Member):
    def __init__(self, name, surname, salary, member: Member):
        super().__init__(name, surname, salary)
        self._member = member

    def do_analysing(self):
        return print(f'{self.name} {self.surname} analysing')


class SoftwareArchitect(Developer):
    def __init__(self, name, surname, salary, tech_stack, developer: Developer):
        super().__init__(name, surname, salary, tech_stack, member5)
        self.developer = developer

    def create_template(self):
        return print(f'{self.name} {self.surname} created new template')

    def read_clean_architecture(self):
        return f"{self.name}'s skills was improved"

    def do_work(self, *args):
        self.developer.do_work()


class TeamLead(Developer):
    def __init__(self, name, surname, salary, tech_stack, developer: Developer):
        super().__init__(name, surname, salary, tech_stack, member1)
        self.developer = developer

    def divide_and_rule(self):
        return f'Ohh, i am working so hard...'

    def do_work(self, *args):
        self.developer.do_work()


class QA(Member):
    def __init__(self, name, surname, salary, member: Member):
        super().__init__(name, surname, salary)
        self._member = member

    def do_testing(self):
        return print(f'{self.name} {self.surname} testing unit')


def client_code(step: Step) -> None:
    print(f"RESULT: {step.realize()}", end="")


def client_code2(step1: Step, step2: Step) -> None:
    if step1.is_composite():
        step1.add(step2)
    print(f"RESULT: {step1.realize()}", end="")


if __name__ == "__main__":
    step_execute = StepExecute()
    print("First step was done:")
    client_code(step_execute)
    print("\n")
    pipe = Pipeline()
    step1 = Pipeline()
    step1.add(StepFetch())

    step2 = Pipeline()
    step2.add(StepExecute())
    pipe.add(step1)
    pipe.add(step2)

    print("SoftWare: I am almost ready for deployment: ")
    client_code(pipe)

    print("\n")

    print("Steps, which was realized: ")
    client_code2(pipe, step_execute)
    print("\n")
    member1 = Member('Andriy', 'Shevchenko', 3000000)
    member2 = Member('Taras', 'Iskovych', 20000)
    member3 = Member('Hryhoriy', 'Olenych', 15000)
    member4 = Member('Igor', 'Yarych', 20050)
    member5 = Member('Roman', 'Zabushko', 100000)
    tech_stack = Swift('Swift')
    developer1 = Developer(name=member1.name, surname=member1.surname,
                           salary=member1.salary, tech_stack=tech_stack, member=member1)

    developer2 = Developer(name=member5.name, surname=member5.surname,
                           salary=member5.salary, tech_stack=tech_stack, member=member5)

    d = TeamLead(name=member1.name, surname=member1.surname,
                 salary=member1.salary, tech_stack=tech_stack, developer=developer1)
    d2 = SoftwareArchitect(name=member5.name, surname=member5.surname,
                           salary=member5.salary, tech_stack=tech_stack, developer=developer1)
    k = KanbanTeam('Team', 6, 'Kanban')
    k.add_member()
    d2.create_template()
    d.do_work()
    d2.read_clean_architecture()
