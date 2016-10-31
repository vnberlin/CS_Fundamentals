import sys


def func():
    print "\nfunctional code here \n"


def main(args):

    print "Python Script Basic Shell"
    script_name = str(args[0]).split("/")

    print "Arguments Given = " + str(len(args))
    print "Script Path = " + str(args[0])
    print "Script Name = " + script_name[(len(script_name) - 1)]

    for i in range(len(args)):
        if i == 0:
            pass
        else:
            print "Arg [" + str(i) + "] = " + str(args[i])

    func()

if __name__ == '__main__':
    main(sys.argv)

