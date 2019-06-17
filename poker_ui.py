import threading
from tkinter import *
from tkinter import messagebox

import pygame
from PIL import Image as pImage
from PIL import ImageTk as pImageTk

import poker


def clear_label_poker():
    Self_Label1.place_forget()
    Self_Label2.place_forget()
    Self_Label3.place_forget()
    Self_Label4.place_forget()
    Self_Label5.place_forget()

    Other_Label1.place_forget()
    Other_Label2.place_forget()
    Other_Label3.place_forget()
    Other_Label4.place_forget()
    Other_Label5.place_forget()


def clear_label():
    var_bet_input.set('')
    var_compare_result.set('')

    point_player_mine.place_forget()
    point_player_other_label.place_forget()
    compare_result_label.place_forget()
    pass


def show():
    '''
    开牌按钮事件
    :return:
    '''
    bet = bet_input_entry.get()
    if not bet.isdigit() or int(bet) < 1 or int(bet) > 10:
        messagebox.showerror(title='错误', message='请输入1-10的数字！')
        return
    bet_input_entry.config(state=DISABLED)
    show_btn.config(state=DISABLED)

    threading.Timer(delay, print_my_point).start()


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
    score_label.place_forget()

    clear_label_poker()
    clear_label()


def play():
    '''
    开始游戏逻辑
    :return:
    '''
    global is_playing
    is_playing = False
    var_play_or_continue_btn.set('继续游戏')
    score_label.place(x=180, y=520)
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

    clear_label_poker()
    clear_label()

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
            if i == 2:
                Other_Label1['image'] = poker_back
                Other_Label1.image = poker_back
                Other_Label1.place(x=180 + (int(i / 2) - 1) * 150, y=230)
            elif i == 4:
                Other_Label2['image'] = poker_back
                Other_Label2.image = poker_back
                Other_Label2.place(x=180 + (int(i / 2) - 1) * 150, y=230)
            elif i == 6:
                Other_Label3['image'] = poker_back
                Other_Label3.image = poker_back
                Other_Label3.place(x=180 + (int(i / 2) - 1) * 150, y=230)
            elif i == 8:
                Other_Label4['image'] = poker_back
                Other_Label4.image = poker_back
                Other_Label4.place(x=180 + (int(i / 2) - 1) * 150, y=230)
            elif i == 10:
                Other_Label5['image'] = poker_back
                Other_Label5.image = poker_back
                Other_Label5.place(x=180 + (int(i / 2) - 1) * 150, y=230)
        else:
            image_index = poker_image_index(_poker_mine[int(i / 2)])
            image1 = pImage.open(".\\poker_image\\" + image_index + ".jpg")
            p1 = pImageTk.PhotoImage(image1)
            if i == 1:
                Self_Label1['image'] = p1
                Self_Label1.image = p1
                Self_Label1.place(x=180 + int(i / 2) * 150, y=30)
            elif i == 3:
                Self_Label2['image'] = p1
                Self_Label2.image = p1
                Self_Label2.place(x=180 + int(i / 2) * 150, y=30)
            elif i == 5:
                Self_Label3['image'] = p1
                Self_Label3.image = p1
                Self_Label3.place(x=180 + int(i / 2) * 150, y=30)
            elif i == 7:
                Self_Label4['image'] = poker_back
                Self_Label4.image = poker_back
                Self_Label4.place(x=180 + int(i / 2) * 150, y=30)
            elif i == 9:
                Self_Label5['image'] = poker_back
                Self_Label5.image = poker_back
                Self_Label5.place(x=180 + int(i / 2) * 150, y=30)
        i = i + 1

        threading.Timer(delay, print_poker).start()
    else:
        bet_input_entry.config(state=NORMAL)
        show_btn.config(state=NORMAL)


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
    point_player_mine.place(x=920, y=100)
    print_my_rest_poker()
    global point_mine
    point_mine = poker.poker_point(poker_mine)
    if point_mine is None:
        var_point_player_mine.set('没牛，最大：' + transform(max(real_compare_max(_poker_mine))))
    else:
        var_point_player_mine.set('牛数：%d' % point_mine)

    threading.Timer(delay, print_other_point).start()


def print_my_rest_poker():
    '''
    展示我剩余的牌
    :return:
    '''
    for i in range(3, 5):
        image_index = poker_image_index(_poker_mine[i])
        image1 = pImage.open(".\\poker_image\\" + image_index + ".jpg")
        p1 = pImageTk.PhotoImage(image1)
        if i == 3:
            Self_Label4['image'] = p1
            Self_Label4.image = p1
        elif i == 4:
            Self_Label5['image'] = p1
            Self_Label5.image = p1


def print_other_point():
    '''
    输出对方的牛数或最大数
    :return:
    '''
    point_player_other_label.place(x=920, y=290)
    for i in range(5):
        image_index = poker_image_index(_poker_other[i])
        image1 = pImage.open(".\\poker_image\\" + image_index + ".jpg")
        p1 = pImageTk.PhotoImage(image1)
        if i == 0:
            Other_Label1['image'] = p1
            Other_Label1.image = p1
        elif i == 1:
            Other_Label2['image'] = p1
            Other_Label2.image = p1
        elif i == 2:
            Other_Label3['image'] = p1
            Other_Label3.image = p1
        elif i == 3:
            Other_Label4['image'] = p1
            Other_Label4.image = p1
        elif i == 4:
            Other_Label5['image'] = p1
            Other_Label5.image = p1

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
    compare_result_label.place(x=win_width / 2 - 100, y=550)
    bet = int(bet_input_entry.get())
    if point_mine is None:
        if point_other is None:
            compare_score = poker.compare(max(real_compare_max(_poker_mine)),
                                          max(real_compare_max(_poker_other)), bet)
        else:
            compare_score = poker.compare(0, point_other, bet)
    else:
        if point_other is None:
            compare_score = poker.compare(point_mine, 0, bet)
        else:
            compare_score = poker.compare(point_mine, point_other, bet)

    if compare_score > 0:
        var_compare_result.set('恭喜你！你赢了，加%d分！' % compare_score)
    elif compare_score < 0:
        var_compare_result.set('很遗憾，你输了，扣%d分.' % abs(compare_score))
    else:
        if point_mine is not None:
            compare_score = poker.compare(max(real_compare_max(_poker_mine)),
                                          max(real_compare_max(_poker_other)), bet)
            var_point_player_other.set(
                '牛数：' + repr(point_other) + '，最大：' + transform(max(real_compare_max(_poker_other))))
            var_point_player_mine.set(
                '牛数：' + repr(point_mine) + '，最大：' + transform(max(real_compare_max(_poker_mine))))
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


def play_music():
    '''
     播放背景音乐
     :return:
     '''
    file = r'.\\resource\\background.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)

    pygame.mixer.music.play(-1)


if __name__ == '__main__':
    play_music()

    SCORE = 80

    # 是否开始游戏
    is_playing = True
    delay = 0.3

    window = Tk()
    # 牌的背面
    poker_back = pImageTk.PhotoImage(pImage.open(".\\poker_image\\back.jpg"))

    # 窗口标题
    window.title('斗牛——很好玩的一款小游戏')

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    win_width = 1080
    win_height = 750

    x = (screen_width - win_width) / 2
    y = (screen_height - win_height) / 2

    # 窗口居中显示到屏幕
    window.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y))

    # 禁止调整窗口大小
    window.resizable(width=False, height=False)

    # 背景图片
    image = pImage.open(".\\resource\\background.jpg")
    photo = pImageTk.PhotoImage(image.resize((win_width, win_height), pImage.ANTIALIAS))
    background = Label(window, image=photo)
    background.pack()

    # 你的牌界面
    Label(window, text='你的牌：', font=(14)).place(x=30, y=100)
    Self_Label1 = Label(window)
    Self_Label2 = Label(window)
    Self_Label3 = Label(window)
    Self_Label4 = Label(window)
    Self_Label5 = Label(window)
    # 你的牛数界面
    var_point_player_mine = StringVar()
    point_player_mine = Label(window, textvariable=var_point_player_mine, fg='blue', font=(16))

    # 对方的牌界面
    Label(window, text='对方的牌：', font=(14)).place(x=30, y=290)
    Other_Label1 = Label(window)
    Other_Label2 = Label(window)
    Other_Label3 = Label(window)
    Other_Label4 = Label(window)
    Other_Label5 = Label(window)
    # 对方的牛数界面
    var_point_player_other = StringVar()
    point_player_other_label = Label(window, textvariable=var_point_player_other, fg='blue',
                                     font=(16))

    # 赌注界面
    Label(window, text='输入赌注：', font=(14)).place(x=30, y=430)
    # 赌注输入
    var_bet_input = StringVar()
    bet_input_entry = Entry(window, textvariable=var_bet_input, width=10)
    bet_input_entry.place(x=180, y=430)
    bet_input_entry.config(state=DISABLED)

    # 开牌按钮
    show_btn = Button(window, text='开牌', command=show, width=15, height=2)
    show_btn.place(x=win_width / 2 + 50, y=430)
    show_btn.config(state=DISABLED)

    # 比较结果界面
    var_compare_result = StringVar()
    compare_result_label = Label(window, textvariable=var_compare_result, fg='red',
                                 font=('Times New Roman', 14))

    # 得分界面
    Label(window, text='得分：', font=(14)).place(x=30, y=530)
    var_score = StringVar()
    # 得分
    score_label = Label(window, textvariable=var_score, fg='green', font=('Times New Roman', 28))

    # 开始/继续游戏按钮
    var_play_or_continue_btn = StringVar()
    var_play_or_continue_btn.set('开始游戏')
    play_or_continue_btn = Button(window, textvariable=var_play_or_continue_btn,
                                  command=play_or_continue, width=15,
                                  height=2)
    play_or_continue_btn.place(x=win_width / 2 - 150, y=660)

    # 结束游戏按钮
    finish_btn = Button(window, text='结束游戏', command=finish, width=15, height=2)
    finish_btn.place(x=win_width / 2 + 50, y=660)
    finish_btn.config(state=DISABLED)

    window.mainloop()
