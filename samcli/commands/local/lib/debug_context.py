"""
Information and debug options for a specific runtime.
"""


class DebugContext(object):

    def __init__(self,
                 debug_port=None,
                 debugger_path=None,
                 debug_args=None):

        self.debug_port = debug_port
        self.debugger_path = debugger_path
        self.debug_args = debug_args
