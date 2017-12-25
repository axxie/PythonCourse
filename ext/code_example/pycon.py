import sys
import os


def main():
    try:
        source_lines = sys.stdin.readlines()
        source = ''
        source += "\n".join(source_lines)
        exec(source, {})
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
