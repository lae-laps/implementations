# debugging framework

import inspect

class Debug:
    def __init__(self, function, hooks):

        self.space = 10
        self.keyword = "debug"
        self.hooks = hooks
        self.debug_statement = self.construct_debug_statement()
        self.function = function
        self.source = self.get_source()

    def get_source(self):
        lines = inspect.getsourcelines(self.function)[0][1:]
        common_indentation = min(len(line) - len(line.lstrip()) for line in lines)
        unindented_lines = [line[common_indentation:] for line in lines]
        src = ''.join(unindented_lines)
        return src.replace(self.keyword, self.debug_statement)

    def construct_debug_statement(self):
        statement = "print(f\" |"
        for i in self.hooks:
            statement += "{(" + str(self.space) + " // 2 - (len(str(" + i + ")) // 2)) * ' '} {" + i + "} {((" + str(self.space) + " // 2 - (len(str(" + i + "))) // 2 ) + 1 * (len(str(" + i + ")) % 2 == 0 )) * ' '}|"
        statement += "\")"

        return statement

    def run(self):
        g = ' -' + ((self.space + 4) * len(self.hooks)) * '-'
        f = " |"
        for i in self.hooks:
            f += f" {(self.space // 2 - len(i) // 2) * ' ' }{i}{((self.space // 2 - len(i) // 2) + (1 * (len(i) % 2 == 0))) * ' '} |"

        print(g)
        print(f)
        print(g)

        exec(self.source)

        print(g)

