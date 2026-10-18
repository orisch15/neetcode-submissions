class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []
    def push(self, val: int) -> None:

        self.st.append(val)
        #importent to put <= to handle duplicates of the minimum element
        if not self.minst or val <= self.minst[-1]:
            self.minst.append(val)
           
    def pop(self) -> None:
        x = self.st.pop()
        if x == self.minst[-1]:
            self.minst.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
        
