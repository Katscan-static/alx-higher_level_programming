#!/usr/bin/python3
if __name__ == "__main__":
    import importlib
    vr = "./variable_load_5.py"
    module = importlib.import_module("variable_load_5", vr)
    a = module.a
    print(a)
