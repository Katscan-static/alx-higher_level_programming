#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util
    hd = "./hidden_4.pyc"
    spec = importlib.util.spec_from_file_location("hidden_4", hd)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    names = [name for name in dir(module) if not name.startswith("__")]
    for name in names:
        print(name)
