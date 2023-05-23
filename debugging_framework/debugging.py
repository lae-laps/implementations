# debugging framework

class Debug:
    def __init__(self, procedure):
        self.hooks = []
        self.procedure = procedure()

    def hook(self, element):
        self.hooks.append(element)

    def run(self):


