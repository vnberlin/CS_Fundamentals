import sys
import two_stack_queue as que


def main(args):

    print "\nPython Script : Queue Data Structure"
    script_name = str(args[0]).split("/")

    print "Arguments Given = " + str(len(args))
    print "Script Path = " + str(args[0])
    print "Script Name = " + script_name[(len(script_name) - 1)]

    for i in range(len(args)):
        if i == 0:
            pass
        else:
            print "Arg [" + str(i) + "] = " + str(args[i])

    print "\n*******************************************************************************"
    print "running script >>>\n"



    q = que.Queue(5)
    test1 = q.dequeue()
    print "test1 = ", test1
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)

    test2 = q.dequeue()
    t21 = q.dequeue()
    t22 = q.dequeue()
    t23 = q.dequeue()
    t24 = q.dequeue()
    print "dequeued : "
    print test2, t21, t22, t23, t24
    test3 = q.dequeue()

if __name__ == '__main__':
    main(sys.argv)
