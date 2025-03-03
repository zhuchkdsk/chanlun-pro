import sys


class filter:
    def __init__(self, target):
        self.target = target

    def write(self, s):
        self.target.buffer.write(s.encode("utf-8"))

    def flush(self):
        self.target.flush()


sys.stdin = filter(sys.stdin)
sys.stdout = filter(sys.stdout)
sys.stderr = filter(sys.stderr)
