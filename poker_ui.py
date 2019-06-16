import threading
from tkinter import *
from tkinter import messagebox

from PIL import Image as pImage
from PIL import ImageTk as pImageTk

import poker


def clear_label_poker():
    image1 = pImage.open(".\\poker_image\\empty.jpg")
    p1 = pImageTk.PhotoImage(image1)
    Other_Label1['image'] = p1
    Other_Label1.image = p1
    Other_Label1.place(x=150 + 0 * 150, y=300)
    Other_Label2['image'] = p1
    Other_Label2.image = p1
    Other_Label2.place(x=150 + 1 * 150, y=300)
    Other_Label3['image'] = p1
    Other_Label3.image = p1
    Other_Label3.place(x=150 + 2 * 150, y=300)
    Other_Label4['image'] = p1
    Other_Label4.image = p1
    Other_Label4.place(x=150 + 3 * 150, y=300)
    Other_Label5['image'] = p1
    Other_Label5.image = p1
    Other_Label5.place(x=150 + 4 * 150, y=300)
    Self_Label1['image'] = p1
    Self_Label1.image = p1
    Self_Label1.place(x=150 + 0 * 150, y=50)
    Self_Label2['image'] = p1
    Self_Label2.image = p1
    Self_Label2.place(x=150 + 1 * 150, y=50)
    Self_Label3['image'] = p1
    Self_Label3.image = p1
    Self_Label3.place(x=150 + 2 * 150, y=50)
    Self_Label4['image'] = p1
    Self_Label4.image = p1
    Self_Label4.place(x=150 + 3 * 150, y=50)
    Self_Label5['image'] = p1
    Self_Label5.image = p1
    Self_Label5.place(x=150 + 4 * 150, y=50)


def play_or_continue():
    '''
    开始/继续游戏按钮事件
    :return:
    '''
    if is_playing:
        play()
    else:
        go_on()


def finish():
    '''
    结束游戏按钮事件
    :return:
    '''
    global is_playing
    is_playing = True
    var_play_or_continue_btn.set('开始游戏')
    play_or_continue_btn.config(state=NORMAL)
    var_score.set('')
    var_compare_result.set('')
    var_point_player_mine.set('')
    var_point_player_other.set('')
    clear_label_poker()


def play():
    '''
    开始游戏逻辑
    :return:
    '''
    global is_playing
    is_playing = False
    var_play_or_continue_btn.set('继续游戏')
    var_score.set(SCORE)
    global score
    score = SCORE
    go_on()


def go_on():
    '''
    继续游戏逻辑
    :return:
    '''
    play_or_continue_btn.config(state=DISABLED)
    finish_btn.config(state=DISABLED)
    var_compare_result.set('')
    var_point_player_mine.set('')
    var_point_player_other.set('')
    clear_label_poker()

    poker.init_poker()
    global poker_mine
    global _poker_mine
    _poker_mine = poker.random_poker()
    poker_mine = poker.sum_value(_poker_mine)
    global poker_other
    global _poker_other
    _poker_other = poker.random_poker()
    poker_other = poker.sum_value(_poker_other)
    global i
    i = 1

    threading.Timer(delay, print_poker).start()


def poker_image_index(_poker):
    if _poker[-1] == '♥':
        index = 'h'
    elif _poker[-1] == '♦':
        index = 'd'
    elif _poker[-1] == '♠':
        index = 's'
    elif _poker[-1] == '♣':
        index = 'c'

    if _poker[:-1] == '10':
        index = index + '10'
    elif _poker[:-1] == 'J':
        index = index + '11'
    elif _poker[:-1] == 'Q':
        index = index + '12'
    elif _poker[:-1] == 'K':
        index = index + '13'
    elif _poker[:-1] == 'A':
        index = index + '1'
    else:
        index = index + _poker[0]

    print(index)

    return index


def print_poker():
    '''
    输出牌数
    :return:
    '''
    global i
    if i <= 2 * len(poker_mine):
        if i % 2 == 0:
            image1 = pImage.open(".\\poker_image\\0.jpg")
            p1 = pImageTk.PhotoImage(image1)
            if i == 2:
                Other_Label1['image'] = p1
                Other_Label1.image = p1
                Other_Label1.place(x=150 + (int(i / 2) - 1) * 150, y=300)
            elif i == 4:
                Other_Label2['image'] = p1
                Other_Label2.image = p1
                Other_Label2.place(x=150 + (int(i / 2) - 1) * 150, y=300)
            elif i == 6:
                Other_Label3['image'] = p1
                Other_Label3.image = p1
                Other_Label3.place(x=150 + (int(i / 2) - 1) * 150, y=300)
            elif i == 8:
                Other_Label4['image'] = p1
                Other_Label4.image = p1
                Other_Label4.place(x=150 + (int(i / 2) - 1) * 150, y=300)
            elif i == 10:
                Other_Label5['image'] = p1
                Other_Label5.image = p1
                Other_Label5.place(x=150 + (int(i / 2) - 1) * 150, y=300)
        else:
            image_index = poker_image_index(_poker_mine[int(i / 2)])
            image1 = pImage.open(".\\poker_image\\" + image_index + ".jpg")
            p1 = pImageTk.PhotoImage(image1)
            if i == 1:
                Self_Label1['image'] = p1
                Self_Label1.image = p1
                Self_Label1.place(x=150 + int(i / 2) * 150, y=50)
            elif i == 3:
                Self_Label2['image'] = p1
                Self_Label2.image = p1
                Self_Label2.place(x=150 + int(i / 2) * 150, y=50)
            elif i == 5:
                Self_Label3['image'] = p1
                Self_Label3.image = p1
                Self_Label3.place(x=150 + int(i / 2) * 150, y=50)
            elif i == 7:
                Self_Label4['image'] = p1
                Self_Label4.image = p1
                Self_Label4.place(x=150 + int(i / 2) * 150, y=50)
            elif i == 9:
                Self_Label5['image'] = p1
                Self_Label5.image = p1
                Self_Label5.place(x=150 + int(i / 2) * 150, y=50)
        i = i + 1

        threading.Timer(delay, print_poker).start()
    else:
        threading.Timer(delay, print_my_point).start()


def real_compare_max(_poker):
    L = []
    for i in _poker:
        if i[:-1] == '10':
            num = 10
        elif i[:-1] == 'J':
            num = 11
        elif i[:-1] == 'Q':
            num = 12
        elif i[:-1] == 'K':
            num = 13
        elif i[0] == 'A':
            num = 1
        else:
            num = int(i[0])
        L.append(num)

    return L


def transform(max_num):
    if max_num == 11:
        _str = 'J'
    elif max_num == 12:
        _str = 'Q'
    elif max_num == 13:
        _str = 'K'
    elif max_num == 1:
        _str = 'A'
    else:
        _str = str(max_num)
    print(_str)
    return _str


def print_my_point():
    '''
    输出我的牛数或最大数
    :return:
    '''
    global point_mine
    point_mine = poker.poker_point(poker_mine)
    if point_mine is None:
        var_point_player_mine.set('没牛，最大：' + transform(max(real_compare_max(_poker_mine))))
    else:
        var_point_player_mine.set('牛数：%d' % point_mine)

    threading.Timer(delay, print_other_point).start()


def print_other_point():
    '''
    输出对方的牛数或最大数
    :return:
    '''
    for i in range(5):
        image_index = poker_image_index(_poker_other[i])
        image1 = pImage.open(".\\poker_image\\" + image_index + ".jpg")
        p1 = pImageTk.PhotoImage(image1)
        if i == 0:
            Other_Label1['image'] = p1
            Other_Label1.image = p1
            Other_Label1.place(x=150, y=300)
        elif i == 1:
            Other_Label2['image'] = p1
            Other_Label2.image = p1
            Other_Label2.place(x=150 + i * 150, y=300)
        elif i == 2:
            Other_Label3['image'] = p1
            Other_Label3.image = p1
            Other_Label3.place(x=150 + i * 150, y=300)
        elif i == 3:
            Other_Label4['image'] = p1
            Other_Label4.image = p1
            Other_Label4.place(x=150 + i * 150, y=300)
        elif i == 4:
            Other_Label5['image'] = p1
            Other_Label5.image = p1
            Other_Label5.place(x=150 + i * 150, y=300)

    global point_other
    point_other = poker.poker_point(poker_other)
    if point_other is None:
        var_point_player_other.set('没牛，最大：' + transform(max(real_compare_max(_poker_other))))
    else:
        var_point_player_other.set('牛数：%d' % point_other)

    threading.Timer(delay, compare).start()


def compare():
    '''
    比较大小
    :return:
    '''
    if point_mine is None:
        if point_other is None:
            compare_score = poker.compare(max(real_compare_max(_poker_mine)), max(real_compare_max(_poker_other)))
        else:
            compare_score = poker.compare(0, point_other)
    else:
        if point_other is None:
            compare_score = poker.compare(point_mine, 0)
        else:
            compare_score = poker.compare(point_mine, point_other)

    if compare_score > 0:
        var_compare_result.set('恭喜你！你赢了，加%d分！' % compare_score)
    elif compare_score < 0:
        var_compare_result.set('很遗憾，你输了，扣%d分.' % abs(compare_score))
    else:
        if point_mine is not None:
            compare_score = poker.compare(max(real_compare_max(_poker_mine)), max(real_compare_max(_poker_other)))
            var_point_player_other.set(
                '牛数：' + repr(point_other) + '，最大：' + transform(max(real_compare_max(_poker_other))))
            var_point_player_mine.set('牛数：' + repr(point_mine) + '，最大：' + transform(max(real_compare_max(_poker_mine))))
            if compare_score > 0:
                var_compare_result.set('恭喜你！你赢了，加%d分！' % compare_score)
            elif compare_score < 0:
                var_compare_result.set('很遗憾，你输了，扣%d分.' % abs(compare_score))
            else:
                var_compare_result.set('平局，分数不变')
        else:
            var_compare_result.set('平局，分数不变')
    global score
    score += compare_score
    var_score.set(score)
    if score < 0:
        messagebox.showerror(title='错误', message='分数小于零，游戏结束！')
        finish()
    else:
        play_or_continue_btn.config(state=NORMAL)
        finish_btn.config(state=NORMAL)


if __name__ == '__main__':
    SCORE = 80

    # 是否开始游戏
    is_playing = True
    delay = 0.3

    window = Tk()
    # 窗口标题
    window.title('斗牛——很好玩的一款小游戏')

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    win_width = 1050
    win_height = 750

    x = (screen_width - win_width) / 2
    y = (screen_height - win_height) / 2

    # 窗口居中显示到屏幕
    window.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y))

    Label(window, text='你的牌：', font=(14)).place(x=50, y=100)
    Self_Label1 = Label(window)
    Self_Label2 = Label(window)
    Self_Label3 = Label(window)
    Self_Label4 = Label(window)
    Self_Label5 = Label(window)
    var_point_player_mine = StringVar()
    Label(window, textvariable=var_point_player_mine, fg='blue', font=(14)).place(x=860, y=100)

    Label(window, text='对方的牌：', font=(14)).place(x=50, y=350)
    Other_Label1 = Label(window)
    Other_Label2 = Label(window)
    Other_Label3 = Label(window)
    Other_Label4 = Label(window)
    Other_Label5 = Label(window)
    var_point_player_other = StringVar()
    Label(window, textvariable=var_point_player_other, fg='blue', font=(14)).place(x=860, y=350)

    Label(window, text='得分：', font=('宋体', 24)).place(x=450, y=600)
    var_score = StringVar()
    Label(window, textvariable=var_score, fg='green', font=('Times New Roman', 24)).place(x=530, y=600)

    var_compare_result = StringVar()
    Label(window, textvariable=var_compare_result, fg='red', font=('Times New Roman', 14)).place(x=win_width / 2 - 100,
                                                                                                 y=520)

    # 开始/继续游戏按钮
    var_play_or_continue_btn = StringVar()
    var_play_or_continue_btn.set('开始游戏')
    play_or_continue_btn = Button(window, textvariable=var_play_or_continue_btn, command=play_or_continue, width=15,
                                  height=2)
    play_or_continue_btn.place(x=win_width / 2 - 150, y=680)

    # 结束游戏按钮
    finish_btn = Button(window, text='结束游戏', command=finish, width=15, height=2)
    finish_btn.place(x=win_width / 2 + 50, y=680)
    finish_btn.config(state=DISABLED)

    window.mainloop()
