#!/usr/bin/python3
""" This is the base module """


import json
from pathlib import Path
import csv
import turtle


class Base:
    """ This is the base class
    It is the base of all the other classes : Rectangle and Square
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None and len(list_objs) != 0:
            file_name = list_objs[0].__class__.__name__ + ".json"
        else:
            file_name = "Base.json"
        l_dict = []
        with open(file_name, "w", encoding='utf-8') as f:
            for objs in list_objs:
                l_dict.append(vars(objs))
            f.write(cls.to_json_string(l_dict))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        rec = cls.__new__(cls)
        rec.update(**dictionary)
        return rec

    @classmethod
    def load_from_file(cls):
        l_instance = []
        filename = "./" + cls.__name__ + ".json"
        path = Path(filename)
        if not path.is_file():
            return l_instance
        else:
            with open(filename, "r", encoding='utf-8') as f:
                inst_list = cls.from_json_string(f.read())
                for inst in inst_list:
                    obj = cls.create(**inst)
                    l_instance.append(obj)
        return l_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is not None and len(list_objs) != 0:
            file_name = list_objs[0].__class__.__name__ + ".csv"
        else:
            file_name = "Base.csv"
        l_dict = []
        with open(file_name, "w", encoding='utf-8') as f:
            write = csv.writer(f)
            write.writerow(list(vars(list_objs[0]).keys()))
            for obj in list_objs:
                write.writerow(list(vars(obj).values()))

    @classmethod
    def load_from_file_csv(cls):
        l_instance = []
        filename = "./" + cls.__name__ + ".csv"
        path = Path(filename)
        if not path.is_file():
            return l_instance
        else:
            with open(filename, encoding='utf-8', newline='') as f:
                reader = csv.reader(f)
                header = next(reader)
                rows = []
                for row in reader:
                    rows.append(row)
                for row in rows:
                    dict_rep = {}
                    obj = None
                    for i in range(len(header)):
                        dict_rep[header[i]] = row[i]
                    obj = cls.create(**dict_rep)
                    l_instance.append(obj)
        return l_instance

    @staticmethod
    def draw(list_rectangles, list_squares):
        wnd = turtle.Screen()
        for rec in list_rectangles:
            abd = turtle.Turtle()
            turtle.setpos(rec.x, rec.y)
            for i in range(2):
                abd.forward(rec.width)
                abd.right(90)
                abd.forward(rec.height)
                abd.right(90)
        for squ in list_squares:
            abd = turtle.Turtle()
            turtle.setpos(squ.x, squ.y)
            for i in range(2):
                abd.forward(squ.width)
                abd.right(90)
                abd.forward(squ.height)
                abd.right(90)
