import pygame
import sys
from src import jokerequest
from src import speech
from gtts import gTTS
import random
import math


class Controller():

    def __init__(self, width = 1280, height = 720):
        pygame.init()
        pygame.mixer.pre_init()
        pygame.mixer.init()
        pygame.mixer.get_init()
        self.screen = pygame.display.set_mode((width,height))
        pygame.font.init()
        self.background = pygame.Surface(self.screen.get_size())
        self.height = height
        self.width = width
        self.state = "EDDIE"
        self.joke = jokerequest.JokesAPI()
        self.speech = speech.TtsAPI()
        self.tries = 3
        self.num_correct = 0
        self.flag = True
        self.currentjoke = ""
        self.currentround = 0


    def mainloop(self, state1):
        self.state = state1
        while True:
            if(self.state == "EDDIE"):
                self.eddieloop()
            elif(self.state == "MATH"):
                self.mathloop()
            elif(self.state == "MUSIC"):
                self.musicloop()
            elif(self.state == "JOKE"):
                self.jokeloop()
            elif(self.state == "TEST"):
                self.testloop()
            elif(self.state == "EXIT"):
                #self.endloop()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
    def eddieloop(self):
        #self.playvoice(self.speech.gentts("Hello and welcome to eddie, please read the instructions before beginning","sample"))
        self.background_image = pygame.image.load("assets/images/background2.png").convert()
        self.screen.blit(self.background_image, (0, 0))
        self.hal_eye_image = pygame.image.load("assets/images/hal_eye.png").convert()
        self.screen.blit(self.hal_eye_image, (650, 120))
        pygame.display.flip()
        #pygame.time.wait(6000)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.mainloop("JOKE")
                    elif event.key == pygame.K_2:
                        self.playvoice(self.speech.gentts("Choose a band and listen to a random song", "sample"))
                        self.mainloop("MUSIC")
                    elif event.key == pygame.K_3:
                        self.state = "MATH"
                        self.mainloop("MATH")

    def jokeloop(self):
        self.background_image = pygame.image.load("assets/images/joke_background.png").convert()
        self.screen.blit(self.background_image, (0, 0))
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and not event.key == pygame.K_q:
                self.currentjoke = self.joke.tellajoke()
                font = pygame.font.SysFont("arial", 15, True)
                joke_label = font.render(str(self.currentjoke), False, (0,0,0))
                self.screen.blit(joke_label, (360,650))
                self.playvoice(self.speech.gentts(self.currentjoke,"joke"))
                pygame.display.flip()
                pygame.time.wait(7000)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.mainloop("EDDIE")


    def mathloop(self):
        self.round1()
        self.round2()

    def round1(self):
        #Round 1, angle conversions
        self.currentround = 1
        self.background_image = pygame.image.load("assets/images/mathslide_angle_conversions.png").convert()
        self.screen.blit(self.background_image, (0, 0))
        self.helpful_image = pygame.image.load("assets/images/helpful_image_round1.png").convert()
        self.screen.blit(self.helpful_image, (650, 200))
        pygame.display.flip()

        questionbank = [[180, math.radians(180)], [60, math.radians(60)], [math.radians(270), 270], [math.radians(360), 360]]
        question = questionbank[random.randint(1,len(questionbank))-1]
        print(str(question))
        c1 = float("{0:.2f}".format(random.randint(1,1000)))
        c2 = float("{0:.2f}".format(random.randint(1,1000)*math.pi))
        c3 = float("{0:.2f}".format(random.randint(1,1000)/math.pi))
        c4 = float("{0:.2f}".format(random.randint(1,1000)-math.pi))
        choices = [c1,c2,c3,c4]
        replaced_index = random.randint(0,3)
        choices[replaced_index] = float("{0:.2f}".format(question[1]))
        print(str(choices))
        self.flag = True

        font = pygame.font.SysFont("arial", 70, True)

        choice1 = font.render("1: "+str(choices[0]), False, (0,0,0))
        self.screen.blit(choice1, (10,100))

        choice2 = font.render("2: "+str(choices[1]), False, (0,0,0))
        self.screen.blit(choice2, (10,200))

        choice3 = font.render("3: "+str(choices[2]), False, (0,0,0))
        self.screen.blit(choice3, (10,300))

        choice4 = font.render("4: "+str(choices[3]), False, (0,0,0))
        self.screen.blit(choice4, (10,400))

        font = pygame.font.SysFont("arial", 40, True)

        question_label = font.render("what is "+str(float("{0:.2f}".format(question[0])))+" converted into its opposite form?", False, (0,0,0))
        self.screen.blit(question_label, (360,650))

        pygame.display.flip()

        while(self.flag):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        if replaced_index == 0:
                            self.correct()
                        else:
                            self.incorrect()
                    elif event.key == pygame.K_2:
                        if replaced_index == 1:
                            self.correct()
                        else:
                            self.incorrect()
                    elif event.key == pygame.K_3:
                        if replaced_index == 2:
                            self.correct()
                        else:
                            self.incorrect()
                    elif event.key == pygame.K_4:
                        if replaced_index == 3:
                            self.correct()
                        else:
                            self.incorrect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.round2()

    def round2(self):
        print("\n=======================\n")
        print("   moving onto round 2     ")
        print("\n=======================\n")
        #Round 2, trig
        self.currentround = 2
        self.background_image = pygame.image.load("assets/images/mathslide_trig.png").convert()
        self.screen.blit(self.background_image, (0, 0))
        self.helpful_image2 = pygame.image.load("assets/images/arccos.png").convert()
        self.screen.blit(self.helpful_image2, (650, 200))
        pygame.display.flip()

        #What is the acos of [-1, 0, 1, 0]
        questionbank = [-1, 0, 1]
        chosen_question = questionbank[random.randint(0,2)]
        font = pygame.font.SysFont("arial", 70, True)
        question_label = font.render("what is the arccos of "+str(chosen_question), False, (0,0,0))
        self.screen.blit(question_label, (360,650))
        self.flag = True

        font = pygame.font.SysFont("arial", 70, True)

        choice1 = font.render("1: 0", False, (0,0,0))
        self.screen.blit(choice1, (10,100))

        choice2 = font.render("2: pi/2", False, (0,0,0))
        self.screen.blit(choice2, (10,200))

        choice3 = font.render("3: pi", False, (0,0,0))
        self.screen.blit(choice3, (10,300))

        choice4 = font.render("4: -pi/2", False, (0,0,0))
        self.screen.blit(choice4, (10,400))

        font = pygame.font.SysFont("arial", 40, True)


        pygame.display.flip()

        while(self.flag):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        if math.acos(chosen_question) == 0:
                            self.correct()
                        else:
                            self.incorrect()
                    elif event.key == pygame.K_2:
                        if math.acos(chosen_question) == math.pi/2:
                            self.correct()
                        else:
                            self.incorrect()
                    elif event.key == pygame.K_3:
                        if math.acos(chosen_question) == math.pi:
                            self.correct()
                        else:
                            self.incorrect()
                    elif event.key == pygame.K_4:
                        if math.acos(chosen_question) == -1*(math.pi/2):
                            self.correct()
                        else:
                            self.incorrect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.round2()


    def musicloop(self):

        self.background_image = pygame.image.load("assets/images/music_background.png").convert()
        self.screen.blit(self.background_image, (0, 0))
        pygame.display.flip()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    song = str(random.randint(1,3))
                    self.playmusic(song)
                elif event.key == pygame.K_2:
                    song = str(random.randint(4,6))
                    self.playmusic(song)
                elif event.key == pygame.K_3:
                    song = str(random.randint(7,9))
                    self.playmusic(song)
                elif event.key == pygame.K_q:
                    pygame.mixer.music.stop()
                    self.mainloop("EDDIE")



    def correct(self):
        self.num_correct+= 1
        self.playvoice(self.speech.gentts("you got "+str(self.num_correct)+" correct","sample"))
        print("you got "+str(self.num_correct)+" correct")
        if self.num_correct >= 3 and self.currentround == 1:
            pygame.time.wait(3000)
            self.playvoice(self.speech.gentts("Moving onto round two","sample"))
            pygame.time.wait(3000)
            self.tries = 3
            self.num_correct = 0
            self.round2()
        elif self.num_correct >= 3 and self.currentround == 2:
            pygame.time.wait(3000)
            self.playvoice(self.speech.gentts("Congratz, you completed the trig practice","sample"))
            pygame.time.wait(3000)
            self.tries = 3
            self.num_correct = 0
            self.mainloop("EDDIE")
        elif self.currentround == 1:
            self.round1()
        elif self.currentround == 2:
            self.round2()
        else:
            pass

    def incorrect(self):
        pygame.mixer.music.load("assets/music/sound_effects/wrong_answ.mp3")
        pygame.mixer.music.play()
        self.tries+= -1
        print("you have "+str(self.tries)+" tries left")
        if self.tries <= 0:
            pygame.mixer.music.load("assets/music/sound_effects/lost_round.mp3")
            pygame.mixer.music.play()
            self.tries = 3
            pygame.time.wait(6000)
            self.mainloop("EDDIE")


    def testloop(self):
        self.background_image = pygame.image.load("assets/images/test_background.png").convert()
        self.screen.blit(self.background_image, (0, 0))
        self.testing_sign = pygame.image.load("assets/images/testing_sign.png").convert()
        self.screen.blit(self.testing_sign, (600, 350))
        #self.all_sprites.draw(self.screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.playmusic("the_trooper.mp3")
                elif event.key == pygame.K_s:
                    self.playmusic("run_to_the_hills.mp3")
                elif event.key == pygame.K_d:
                    self.quitmusic()
                elif event.key == pygame.K_f:
                    self.getjoke()
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_r:
                    self.playvoice(self.speech.gentts("helloworld","sample"))
                elif event.key == pygame.K_j:
                    self.playvoice(self.speech.gentts(self.getjoke(),"joke"))


    def playmusic(self,file_name):
        pygame.mixer.music.load("assets/music/"+str(file_name)+".mp3")
        pygame.mixer.music.play()

    def playvoice(self, file_name):
        pygame.mixer.music.load("assets/voice/"+str(file_name))
        pygame.mixer.music.play()

    def quitmusic(self):
        pygame.mixer.music.stop()

    def getjoke(self):
        joke = str(self.joke.tellajoke())
        if "insufficient voltage" in joke or "feto" in joke:
            self.getjoke()
        print(joke)
        return joke






    #Electronic Digital Dedicated Interfacing Employee
