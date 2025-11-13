# ca_checkin.py
# Tests for the Employee class org chart

from lab9 import Employee

def build_org():
    alex = Employee("Alex LaGrassa", 1)
    sydney = Employee("Sydney Faranetra", 2_000_000)
    cecilia = Employee("Cecilia Esteban", 365)
    josh = Employee("Josh", 99)
    jamil = Employee("Jamil", 80)

    # org chart
    alex.assign(sydney)
    alex.assign(cecilia)
    sydney.assign(josh)
    cecilia.assign(jamil)

    return alex, sydney, cecilia, josh, jamil


def main():
    alex, sydney, cecilia, josh, jamil = build_org()

    print("Org chart employees:")
    for e in [alex, sydney, cecilia, josh, jamil]:
        print(e, "| depth:", e.org_depth())

    # quick relationship checks
    print()
    print("Manager checks:")
    print("Sydney manager:", sydney.manager)
    print("Cecilia manager:", cecilia.manager)
    print("Josh manager:", josh.manager)
    print("Jamil manager:", jamil.manager)


if __name__ == "__main__":
    main()
