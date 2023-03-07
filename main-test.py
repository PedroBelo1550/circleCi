# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(5,5) == 10 g i t add .
g i t commit −m ‘ ‘ Adds t e s t t o make s u r e 5 + 5 i s e q u al t o 10”
3 g i t push −−s e t−upstream o r i g i n add−t e s t
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()