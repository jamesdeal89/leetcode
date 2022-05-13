# take an integer and output as it's roman numeral representation
class intToRoman():
    def __init__(self):
        self.output = ''

    def solution(self, int):
        while True:
            if int >= 1000:
                int-=1000
                self.output = self.output + "M"
            elif int >= 500:
                int-=500
                self.output = self.output + 'D'
            elif int >= 100:
                int-=100
                self.output = self.output + 'C'
            elif int >= 50:
                int-=50
                self.output = self.output + 'L'
            elif int >= 10:
                int -= 10
                self.output = self.output + 'X'
            elif int >= 5:
                int -= 5
                self.output = self.output + 'V'
            elif int >= 1:
                int -= 1
                self.output = self.output + 'I'
            elif int <= 0:
                return self.output

int2Roman = intToRoman()
print(int2Roman.solution(121))

