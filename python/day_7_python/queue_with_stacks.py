class queue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def stack_input(self,x):
        self.stack_in.append(x)
        
    def stack_input_print(self):
        print(self.stack_in)    

    def stack_out_print(self):
        print(self.stack_out)

    def stack_pop(self):
        self.stack_out.append(self.stack_in.pop())

q1 = queue()
q1.stack_input(1)
q1.stack_input(2)
q1.stack_input(3)
q1.stack_input(4)
q1.stack_input_print()
q1.stack_pop()
q1.stack_pop()
q1.stack_pop()
q1.stack_pop()
q1.stack_out_print()
