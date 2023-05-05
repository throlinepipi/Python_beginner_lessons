def func1():
    print("func1() function started")
    def func2():
        print("func2() function execution")
    print("func1() function calling func2() function")
    func2()

func1()
func2()