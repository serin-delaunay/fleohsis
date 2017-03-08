
# coding: utf-8
from functools import wraps

def hook_priority(priority):
    def hook_priority_aux(hook):
        @wraps(hook)
        def f(*args, **kwargs):
            return hook(*args, **kwargs)
        f.priority = priority
        return f
    return hook_priority_aux
