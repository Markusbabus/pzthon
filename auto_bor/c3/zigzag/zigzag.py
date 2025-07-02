import time, sys
indent = 0
indent_inc = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if indent_inc:
            indent = indent + 1

            if indent == 20:
                indent_inc = False

        else:
            indent = indent - 1
            if indent == 0:
                indent_inc = True

except KeyboardInterrupt:
    sys.exit()