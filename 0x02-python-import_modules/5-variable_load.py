#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util as iu
    vr = "./variable_load_5.py"
    spec = iu.spec_from_file_location("variable_load_5", vr)
    module = iu.module_from_spec(spec)
    spec.loader.exec_module(module)
    a = module.a
    print(a)
