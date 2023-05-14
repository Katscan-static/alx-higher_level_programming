#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util
    hd = "./hidden_4.pyc"
    module = importlib.import_module("hidden_4", hd)
    names = [name for name in dir(module) if not name.startswith("__")]
    for name in names:
        print(name)
