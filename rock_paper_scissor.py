from tkinter import *  # * means import every method
from PIL import Image, ImageTk  # for images
from random import randint

# main window
app = Tk()  # because we are using tkinter
app.title("Rochambeau")  # title of my game app
app.configure(background='#473e78')  # bg color of app. we can give the name or hec code.

# images... open images one by one that we are going to use in our app
rock_img = ImageTk.PhotoImage(Image.open('rock-user.png'))
paper_img = ImageTk.PhotoImage(Image.open('paper-user.png'))
scissor_img = ImageTk.PhotoImage(Image.open('scissors-user.png'))
rock_img_pc = ImageTk.PhotoImage(Image.open('rock.png'))
paper_img_pc = ImageTk.PhotoImage(Image.open('paper.png'))
scissor_img_pc = ImageTk.PhotoImage(Image.open('scissors.png'))

# insert picture
user_label = Label(app, image=scissor_img, bg='#473e78')  # inserting pics for each label
pc_label = Label(app, image=scissor_img_pc, bg='#473e78')
pc_label.grid(row=1, column=0)  # positioning the labels
user_label.grid(row=1, column=4)

# points
playerPoint = Label(app, text=0, font=100, bg='#473e78', fg='white')
pcPoint = Label(app, text=0, font=100, bg='#473e78', fg='white')
pcPoint.grid(row=1, column=1)
playerPoint.grid(row=1, column=3)

# Indicator
user_indicator = Label(app, font=50, text='USER', bg='#473e78', fg='white')
pc_indicator = Label(app, font=50, text='PC', bg='#473e78', fg='white')
user_indicator.grid(row=0, column=3)
pc_indicator.grid(row=0, column=1)

# score message
msg = Label(app, font=50, bg='#473e78', fg='white')
msg.grid(row=3, column=2)


# update message
def updateMessage(x):
    msg['text'] = x


# update user sscore
def updateUserScore():
    score = int(playerPoint['text'])
    score += 1
    playerPoint['text'] = str(score)


# update pc score
def updatePcScore():
    score = int(pcPoint['text'])
    score += 1
    pcPoint['text'] = str(score)


# check winner
def checkWin(player, pc):
    if player == pc:
        updateMessage('It\'s a tie')
    elif player == 'rock':
        if pc == 'paper':
            updateMessage('You loose')
            updatePcScore()
        else:
            updateMessage('You win')
            updateUserScore()
    elif player == 'paper':
        if pc == 'scissor':
            updateMessage('You loose')
            updatePcScore()
        else:
            updateMessage('You win')
            updateUserScore()
    elif player == 'scissor':
        if pc == 'rock':
            updateMessage('You loose')
            updatePcScore()
        else:
            updateMessage('You win')
            updateUserScore()
    else:
        pass


# update the choice of button

choices = ['rock', 'paper', 'scissor']


def updateChoice(x):
    # for pc
    pcChoices = choices[randint(0, 2)]
    if pcChoices == 'rock':
        pc_label.configure(image=rock_img_pc)
    elif pcChoices == 'paper':
        pc_label.configure(image=paper_img_pc)
    else:
        pc_label.configure(image=scissor_img_pc)

    # for user
    if x == 'rock':
        user_label.configure(image=rock_img)
    elif x == 'paper':
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, pcChoices)


# buttons
rock = Button(app, width=20, height=2, text='ROCK', bg='#FF3E4D', fg='white',
              command=lambda: updateChoice('rock')).grid(row=2, column=1)
paper = Button(app, width=20, height=2, text='PAPER', bg='#FAD02E', fg='white',
               command=lambda: updateChoice('paper')).grid(row=2, column=2)
scissor = Button(app, width=20, height=2, text='SCISSOR', bg='#0ABDE3', fg='white',
                 command=lambda: updateChoice('scissor')).grid(row=2, column=3)

app.mainloop()  # it will run in loop when our project becomes ready
