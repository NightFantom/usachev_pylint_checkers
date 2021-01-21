import pylint.testutils
import astroid

from usachev.checkers.print_checker import PrintChecker


class TestPrintChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = PrintChecker

    def test_finds_print(self):
        print_node, class_method_call_node = astroid.extract_node("""
            class PrintExample:
            
                def do_smth(self):
                    a = 1
                    b = 2
                    c = a + b
                    print(c) #@
                    self.do_nothing("a") #@
                    return c
            
                def do_nothing(self, name:str):
                    pass
        """)

        message = pylint.testutils.Message(msg_id=PrintChecker.CODE, node=print_node)
        with self.assertAddsMessages(message):
            self.checker.visit_call(print_node)

        with self.assertNoMessages():
            self.checker.visit_call(class_method_call_node)
