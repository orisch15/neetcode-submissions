class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []
        self.mini = 0
        
        
    def push(self, val: int) -> None:
        if len(self.st) == 0:
            self.mini = val
            self.minst.append(val)

        self.st.append(val)
        if val <= self.mini:
            self.mini = val
            self.minst.append(self.mini)
        
        
    def pop(self) -> None:
        x = self.st.pop()
        if x == self.mini:
            self.minst.pop()
            if len(self.minst) == 0:
                self.mini = 0 
            else:
                self.mini = self.minst[-1]


    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mini
        
