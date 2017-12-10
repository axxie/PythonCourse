import sys


def main():
    try:
        source_lines = (line.rstrip() for line in sys.stdin)
        source = ''
        try:
            while True:
                source += next(source_lines) + "\n"
        except StopIteration:
            source = source[:-1]
            exec(source, {})
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
