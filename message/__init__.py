import sys


if sys.platform.startswith('win32'):
    from multiprocess import popen_spawn_win32

    # Fixes "No module named 'multiprocess'" error when calling functions with `wrapt_timeout_decorator.timeout`
    popen_spawn_win32.WINENV = False
