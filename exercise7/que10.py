class invalidnumerror ('exception'):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return repr(self.value)
try:
    num = int(input("enter number of results :"))
    for itr in range(num):
        result = int(input("enter marks{}".format(itr+1)))
        if result <0 or result >100:
            raise(invalidnumerror("invalid input error"))
        else:
            print("results processing.")
except invalidnumerror as error:
    print("exception:",error.value)