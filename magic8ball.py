import time
import random

responses = ['It is certain',
             'It is decidedly so',
             'Without a doubt',
             'Yes definitely',
             'You may rely on it',
             'As I see it, yes',
             'You may rely on it',
             'Most likely',
             'Outlook good',
             'Yes',
             'Reply hazy try again',
             'Ask again later',
             'Better not tell you now',
             'Cannot predict now',
             'Concentrate and ask again',
             'Dont count on it',
             'My reply is no',
             ' My sources say no',
             'Outlook not so good',
             'Very doubtful'
             ]


def magic8ball():
    resp_len = len(responses)
    input("Ask me a question!!\n")
    print("Ok. Let me think ....")
    time.sleep(1)
    rand_index = random.randint(0,resp_len-1)
    print (responses[rand_index])


def main():
    magic8ball()


if __name__ == '__main__':
    while True:
        main()
        if (input('Enter Q to quit or any key to continue\n').lower())=='q':
            break



