import random





# 列表生成式，牌大小
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# 牌花色
suits = ['♥', '♦', '♠', '♣']


def init_poker():
    global sum_poker
    sum_poker = [i+j for i in ranks for j in suits]


# 自定义一个函数
# 一到十四十张牌
# 随机发五张
def random_poker():
    poker = []
    for i in range(5):
        choice = (random.choice(sum_poker))
        poker.append(choice)
        sum_poker.remove(choice)

    print(poker)
    return poker


# 自定义一个函数
# 凑出三张和为十的倍数
# 剩下两张相加
# 若大于十则减十，否则直接得出牛数
# 凑不出三张为十的倍数
# 为没牛
def poker_point(poker):
    length = len(poker)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                _sum = poker[i] + poker[j] + poker[k]
                if _sum % 10 == 0:
                    if sum(poker) - _sum > 10:
                        if (sum(poker) - _sum) % 10 == 0:
                            return 10
                        else :
                            return sum(poker) % 10
                    else:
                        return sum(poker) - _sum


# 返回真实值
def sum_value(poker):
    L = []
    for i in poker:
        if i[:-1] in ['10','J','Q','K']:
            num = 10
        elif i[0] == 'A':
            num = 1
        else:
            num = int(i[0])
        L.append(num)
    return L


# 没牛比大小
# 选出五张中最大的比大小
def compare(self, computer):
    if self > computer:
        print('电脑小，分数加三')
        return 3
    elif self < computer:
        print('电脑大，分数减三')
        return -3
    else:
        print('一样大，分数不变')
        return 0


# 输入开始游戏，您当前分数为80
# 开始发牌
# 比较大小
# 如果电脑大，则分数减三
# 如果电脑小，则分数加三
# 一样大，则分数不变

# 分数小于零，游戏结束
if __name__ == '__main__':
    score = 80
    while True:
        str = input('输入开始游戏，您当前分数为%d' % score)
        if str == '开始游戏':
            print('开始发牌')

            _poker_self = random_poker()
            poker_self = sum_value(_poker_self)
            print('你的牌：%s' % poker_self)

            _poker_computer = random_poker()
            poker_computer = sum_value(_poker_computer)
            print('电脑的牌：%s' % poker_computer)

            print('比较大小')
            point_self = poker_point(poker_self)
            point_computer = poker_point(poker_computer)
            if point_self is None:
                print('你的牌没牛，最大：%d' % max(poker_self))
            else:
                print('你的牌牛数：%d' % point_self)

            if point_computer is None:
                print('电脑的牌没牛，最大：%d' % max(poker_computer))
            else:
                print('电脑的牌牛数：%d' % point_computer)

            if point_self is None:
                if point_computer is None:
                    score += compare(max(poker_self), max(poker_computer))
                else:
                    score += compare(0, point_computer)
            else:
                if point_computer is None:
                    score += compare(point_self, 0)
                else:
                    score += compare(point_self, point_computer)

            if score < 0:
                print('分数小于零，游戏结束')
                break
