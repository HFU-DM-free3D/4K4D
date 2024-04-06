from easyvolcap.utils.import_utils import import_submodules
__all__ = import_submodules(__file__)

for module in __all__:
    try:
        # from . import *  # the actual imports
        exec(f'from . import {module}')
    except Exception as e:
        import os
        import sys
        from easyvolcap.utils.console_utils import *

        tb = sys.exc_info()[-1]
        tb = tb.tb_next
        filename = tb.tb_frame.f_code.co_filename
        line_number = tb.tb_lineno

        log(yellow(f'Failed to import {red(basename(filename))}:{red(line_number)}, {red(type(e).__name__)}: {e}'))
