#custom print function to print variavle names
import inspect

def v_print(*args):
    frame = inspect.currentframe().f_back
    names = frame.f_code.co_names
    values = [frame.f_locals[name] for name in names if name in frame.f_locals and name in args]
    
    for name, value in zip(names, values):
        print(f"{name}: {value}")
'''
import inspect

def v_print(*args):
    frame = inspect.currentframe().f_back
    names = frame.f_code.co_names
    values = [frame.f_locals[name] for name in names if name in frame.f_locals]
    
    for name, value in zip(names, values):
        print(f"{name}: {value}")
        
'''
# Testing Zone
#my_name = "Tech_101"
#my_org = "LearnTech"
v_print("my_name", "my_org")
