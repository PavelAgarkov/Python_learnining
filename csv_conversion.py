from datetime import datetime
import pprint


def csv_dict_conversion(csv_file: str) -> None:
    def convert2ampm(time24: str) -> str:
        return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

    with open(csv_file) as data:
        data.readline()
        flights = {}
        for line in data:
            k, v = line.strip().split(',')
            flights[k] = v

    pprint.pprint(flights)
    print()

    # flights2 = {}
    # for k, v in flights.items():
    #     flights2[convert2ampm(k)] = v.title()

    # pprint.pprint(flights2)

    # генератор списка
    # destinations = []
    # for dest in flights.values():
    #     destinations.append(dest.title())
    #
    # more_dests = [dest.title() for dest in flights.values()]

    # генератор словаря
    # flights2 = {}
    # for k, v in flights.items():
    #     flights2[convert2ampm(k)] = v.title()
    #
    # more_flights = {convert2ampm(k): v.title()
    #                 for k, v in flights.items()}

    # pprint.pprint(more_flights)

    # генератор с фильтром
    # just_freeport2 = {convert2ampm(k): v.title()
    #                   for k, v in flights.items()
    #                   if v == 'FREEPORT'}

    # def events1():
    #     data1 = [1, 2, 3, 4, 5, 6, 7, 8]
    #     first_generator = [num for num in data1 if not num % 2]
    #     return first_generator
    #
    #
    # def events2():
    #     data2 = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
    #     second_generator = [num for num in data2 if isinstance(num, str)]
    #     return second_generator
    #
    #
    # def events3():
    #     data3 = list('So long and thanks for all the fish'.split())
    #     third_generator = [word.title() for word in data3]
    #     return third_generator
    #
    #
    # print(events1())
    # print(events2())
    # print(events3())

    fts = {convert2ampm(k): v.title() for k, v in flights.items()}

    pprint.pprint(fts)
    print()

    # внешний генератор словарей содержит внутренний генератор списков
    # when = {}
    # for dest in set(fts.values()):
    #     when[dest] = [k for k, v in fts.items() if v == dest]

    when = {dest: [k for k, v in fts.items() if v == dest]
            for dest in set(fts.values())}

    pprint.pprint(when)
    print()
