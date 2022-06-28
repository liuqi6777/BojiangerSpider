import json
import keyword
import os

from collections import abc
from typing import Mapping, Dict


data_dir = 'data'


class JsonLoader:
    """
    To deal with json data.
    Read Only.
    """
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping: Mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        elif item in self.__data:
            return JsonLoader(self.__data[item])
        else:
            raise AttributeError


class JsonWriter:
    def __init__(self, file_path):
        self.file_path = os.path.join(data_dir, file_path) + '.jsonl'

    def __enter__(self):
        self.file = open(self.file_path, 'a', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def write(self, json_dict: Dict):
        self.file.write(json.dumps(json_dict, ensure_ascii=False))
        self.file.write('\n')


def jsonl_to_csv(json_file: str, csv_file: str, headers: list = None):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = f.readlines()
    if headers is not None:
        headers = ','.join(headers)
    else:
        headers = ','.join(list(json.loads(data[0]).keys()))
    with open(csv_file, 'w', encoding='utf-8') as f:
        f.write(headers + '\n')
        for line in data:
            f.write(','.join([str(i) for i in list(json.loads(line).values())]) + '\n')


class Pipeline:
    """
    Data pipeline.
    """
