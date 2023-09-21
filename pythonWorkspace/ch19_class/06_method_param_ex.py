class Television:
    def __init__(self, channel, volume, on): # 생성자
        self.channel = channel
        self.volume = volume
        self.on = on

    def set_channel(self, channel):
        self.channel = channel

    def set_volume(self, volume):
        self.volume = volume

    
    def show_tv_info(self):
        print(f'채널 : {self.channel}')
        print(f'볼륨 : {self.volume}')
        print(f'전원 ON : {self.on}')
    
# 인스턴스 생성
p1 = Television(9, 10, True)
p1.show_tv_info()

print()

p1.set_channel(11)
p1.set_volume(15)
p1.show_tv_info()