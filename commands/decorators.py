from functools import wraps


def game_required(func):
    @wraps(func)
    def wrapper(self, game):
        if not game:
            return

        return func(self, game)

    return wrapper
