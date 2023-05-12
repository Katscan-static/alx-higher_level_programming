#!/usr/bin/python3
import importlib.util
dr = "/root/alx-higher_level_programming/0x02-python-import_modules/"
spec = importlib.util.spec_from_file_location("hidden_4", dr + "hidden_4.pyc")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
names = [name for name in dir(module) if not name.startswith("__")]
for name in names:
    print(name)
