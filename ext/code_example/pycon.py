import sys
from code import InteractiveInterpreter
from subprocess import Popen, DEVNULL
import os.path
import os
import tempfile

def main():
    try:
        source_lines = (line.rstrip() for line in sys.stdin)
        source = ''
        try:
            while True:
                source += next(source_lines) + "\n"
        except StopIteration:
            source = source[:-1]
            new_file, filename = tempfile.mkstemp(suffix=".py")
            os.write(new_file, source.encode("utf-8"))
            os.close(new_file)

            proc = Popen(["cmd.exe", "/c", os.path.join(os.path.dirname(__file__), "convert.cmd"), filename, sys.argv[1]], stdout=DEVNULL, stderr=DEVNULL)
            proc.wait()
            os.remove(filename)

            exec(source, {})
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
