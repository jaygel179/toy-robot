from functools import wraps


def robot_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if hasattr(self, "_robot") and self._robot is None:
            return

        return func(self, *args, **kwargs)

    return wrapper
