# ch 6.6.2 ctrl.py
class Control:
    
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self): # calculate 메서드 추가, 내용은 추후에 작성
        num1 = float(self.view.le1.text()) # 첫 번째 라인 에디트에 입력된 숫자를 읽어옴
        num2 = float(self.view.le2.text()) # 두 번째 라인 에디트에 입력된 숫자를 읽어옴
        operator = self.view.cb.currentText() # 콤보 박스에 선택된 연산자 확인

        if operator == '+': # 연산자가 '+'이면 덧셈 결과를 문자열로 리턴
            return f'{num1} + {num2} = {self.sum(num1, num2)}'
        else:
            return "Calculation Error"

    def connectSignals(self): # btn1을 클릭하면 calculate 결과가 화면에 표시되도록 수정
        self.view.btn1.clicked.connect(lambda:\
                                        self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b): # 예외 처리 제거 : 향후 calculate 함수에서 처리하도록 구현 예정
            return a+b