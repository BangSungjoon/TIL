# 클래스 정의
class Counter:
    # 인스턴스 변수 count를 0으로 초기화하는 메소드
    def set_count(self): # 메소드의 첫 번째 매개변수는 반드시 self로 지정
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
    
# 객체(인스턴스) 생성
c1 = Counter()
c2 = Counter()

# 각 객체마다 자신의 인스턴스 변수와 메소드를 갖음
c1.set_count()
c2.set_count()