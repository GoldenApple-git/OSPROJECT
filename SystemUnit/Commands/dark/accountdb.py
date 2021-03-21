class DataManager:
    def __init__(self):
        try:
            self.get = open("./datasrand.db", "r", newline="").read().split("$")
        except:
            self.get = open("./Commands/dark/datasrand.db", "r", newline="").read().split("$")

    def adddata(self,one,two=None,possibleadd=None):
        if possibleadd is not None:
            try:
                open("./Commands/dark/datasrand.db", "a", newline="").write(f"$\n{one},{two},{possibleadd}")
                return "sucess"
            except:
                try:
                    open("./datasrand.db", "a", newline="").write(f"$\n{one},{two},{possibleadd}")
                    return "sucess"
                except Exception as error:
                    return error
        elif possibleadd is None and two is not None:
            try:
                open("./Commands/dark/datasrand.db", "a", newline="").write(f"$\n{one},{two}")
                return "sucess"
            except:
                try:
                    open("./datasrand.db", "a", newline="").write(f"$\n{one},{two}")
                    return "sucess"
                except Exception as error:
                    return error
        else:
            try:
                open("./Commands/dark/datasrand.db", "a", newline="").write(f"$\n{one}")
                return "sucess"
            except:
                try:
                    open("./datasrand.db", "a", newline="").write(f"$\n{one}")
                    return "sucess"
                except Exception as error:
                    return error
    def readdata(self):
        return ''.join([i for i in self.get])