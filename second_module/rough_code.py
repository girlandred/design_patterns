from abc import ABC, abstractmethod


class Software:
    pass


class MobileApp:
    pass


class WebApp:
    pass


class DataBaseAPI:
    pass


class AndroidApp:
    pass


class IOSApp:
    pass


class PythonWeb:
    pass


class JSBackEndWeb:
    pass


class JSFrontEndWeb:
    pass


class Pipeline:
    pass


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
    def __init__(self, name, quantity_of_members, type_of, member: Member):
        super().__init__(name, quantity_of_members, type_of)
        self.member = member

    # def add_member(self, *args):
    #     members = [member]
    #     for person in members:
    #         print(person.name, person.surname + " was added in team", sep=' ')


class KanbanTeam(Team):
    def __init__(self, name, quantity_of_members, type_of, member: Member):
        super().__init__(name, quantity_of_members, type_of)
        self.member = member

    def add_member(self, *args):
        members = []
        members.append(Developer(developer.name, developer.surname, developer.salary, developer.tech_stack))
        for person in members:
            print(person.name, person.surname + " was added in team", sep=' ')


class ScrumbanTeam(Team):
    def __init__(self, name, quantity_of_members, type_of, member: Member):
        super().__init__(name, quantity_of_members, type_of)
        self.member = member

    # def add_member(self, *args):
        # members = [member]
        # for person in members:
        #     print(person.name, person.surname + " was added in team", sep=' ')


class Developer(Member):
    def __init__(self, name, surname, salary, tech_stack):
        super().__init__(name, surname, salary)
        self._member = member
        self.tech_stack = tech_stack

    def do_work(self):
        self.tech_stack.programming()
        return print(f'{self.name} {self.surname} programming in {self.tech_stack.name}')


class BusinessAnalyst:
    pass


class SoftwareArchitect(Developer):
    def __init__(self, name, surname, salary, tech_stack, developer: Developer):
        super().__init__(name, surname, salary, tech_stack)
        self.developer = developer

    def create_template(self):
        return print(f'{self.name} {self.surname} created new template')

    def read_clean_architecture(self):
        return f"{self.name}'s skills was improved"

    def do_work(self, *args):
        self.developer.do_work()


class TeamLead(Developer):
    def __init__(self, name, surname, salary, tech_stack, developer: Developer):
        super().__init__(name, surname, salary, tech_stack)
        self.developer = developer

    def divide_and_rule(self):
        return f'Ohh, i am working so hard...'

    def do_work(self, *args):
        self.developer.do_work()


class QA:
    pass


member = Member('Andriy', 'Shevchenko', 3000000)
tech_stack = Swift('Swift')
developer = Developer(name=member.name, surname=member.surname,
                      salary=member.salary, tech_stack=tech_stack)
d = SoftwareArchitect(name=member.name, surname=member.surname,
                      salary=member.salary, tech_stack=tech_stack, developer=developer)
k = KanbanTeam('Team', 6, 'Kanban', member=member)
k.add_member()
d.create_template()
d.do_work()
d.read_clean_architecture()
