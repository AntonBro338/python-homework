def do_twice (function):
    function ()
    function ()
def print_spam ():
    print ("спам")
do_twice (print_spam)
def do_twice(function, argument):
    a1 = function(argument)
    a2 = function(argument)
    return a1, a2
def print_twice (text):
    print (text)
    print (text)
a = do_twice(print_twice, "спам")
print_twice ("спам")
def do_four (function, argument):
    a1 = function(argument)
    a2 = function(argument)
    a1 = function(argument)
    a1 = function(argument)
a = do_four(print_twice, "спамм")
def do_four_short (function, argument):
    a1 = do_twice (print_spam)
    a2 = do_twice (print_spam)
    return a1, a2
a = do_twice(print_twice, "спаммм")
print_twice ("спаммм")

    

