def phq_question():
    print("")

print("สวัสดี คุณชื่ออะไรหรอ ?")
firstname = input("ชื่อ :")
lastname = input("นาสกุล :")
nickname  = input("ชื่อเล่น : ")

fullname = firstname +" "+lastname
print ("ยินดีที่ได้รู้จักคุณ :", fullname)
print ("ฉันชื่อ KAPX :3 ขอเรียกคุณว่า คุณ", nickname)
pass

print("ก่อนอื่นฉันอยากให้คุณทำคำถามประเมินสุขภาพจิต phq-9 ซึ่งมีทั้งหมด 9 ข้อ โดยคำถามแต่ละข้อจะมีระดับการให้คะแนนดังนี้")
print("0 = ไม่เลย")
print("1 = เป็นบางวัน")
print("2 = เป็นบ่อย ")
print("3 = เป็นประจำ")
print("เมื่อคุณทำแบบประเมินเสร็จ ฉันจะแจ้งการประเมินให้คุณทราบ")
pass

def phq(answer):
    answer = input("เริ่มกันเลยไหม? (y/n): ")
    if answer == "y":
        print("โอเค เริ่มกันเลย")
        pass
        
    elif answer == "n":
        print("น่าเสียดายจังเลย ไม่โอกาสหน้ามาใหม่นะ")
    else:
        print("น่าเสียดายจังเลย ไม่โอกาสหน้ามาใหม่นะ")
        '/'
        #break
phq("answer")

    
def phq_9():
    num1=  int(input("คุณมีอาการเบื่อ ทำอะไร ๆ ก็ไม่เพลิดเพลิน:"))  
    if num1 == 0:
             newthing1 = 0
             motivate1 = 0
             cheering1  = 0
             food1 = 0
             social1 = 0
             resting1 = 0
             meditation1 = 0
             suicide1 = 0 
             exercise1 = 0
    elif num1 == 1:
             newthing1 = 0.33
             motivate1 = 0.33
             cheering1  = 0.33
             food1 = 0.17
             social1 = 0.17
             resting1 = 0
             meditation1 = 0
             suicide1 = 0
             exercise1 = 0
    elif num1 == 2:
             newthing1 = 0.66
             motivate1 = 0.66
             cheering1  = 0.66
             food1 = 0.34
             social1 = 0.34
             resting1 = 0
             meditation1 = 0
             suicide1 = 0
             exercise1 = 0
    elif num1 == 3:
             newthing1 = 0.99
             motivate1 = 0.99
             cheering1  = 0.99
             food1 = 0.49
             social1 = 0
             resting1 = 0
             meditation1 = 0
             suicide1 = 0
             exercise1 = 0 
            
    num2=  int(input("คุณไม่สบายใจ ซึมเศร้า หรือท้อแท้:"))
    if num2 == 0:
             newthing2 = 0
             motivate2 = 0
             cheering2  = 0
             food2 = 0
             social2 = 0
             resting2 = 0
             meditation2 = 0
             suicide2 = 0 
             exercise2 = 0
    elif num2 == 1:
             newthing2 = 0
             motivate2 = 0.33
             cheering2  = 0.33
             food2 = 0
             social2 = 0.33
             resting2 = 0
             meditation2 = 0
             suicide2 = 0
             exercise2 = 0
    elif num2 == 2:
             newthing2 = 0
             motivate2 = 0.66
             cheering2  = 0.66
             food2 = 0
             social2 = 0.66
             resting2 = 0
             meditation2 = 0
             suicide2 = 0
             exercise2 = 0
    elif num2 == 3:
             newthing2 = 0
             motivate2 = 0.99
             cheering2  = 0.99
             food2 = 0
             social2 = 0.99
             resting2 = 0
             meditation2 = 0
             suicide2 = 0
             exercise2 = 0 
    num3 = int(input("คุณมีอาการหลับยาก หรือหลับ ๆ ตื่น ๆ หรือหลับมากไป:"))
    if num3 == 0:
             newthing3 = 0
             motivate3 = 0
             cheering3  = 0
             food3 = 0
             social3 = 0
             resting3 = 0
             meditation3 = 0
             suicide3 = 0
             exercise3 = 0 
    elif num3 == 1:
             newthing3 = 0
             motivate3 = 0
             cheering3  = 0.17
             food3 = 0.17
             social3 = 0
             resting3 = 0.33
             meditation3 = 0.17
             suicide3 = 0
             exercise3 = 0.17 
    elif num3 == 2:
             newthing3 = 0
             motivate3 = 0
             cheering3  = 0.34
             food3 = 0.34
             social3 = 0
             resting3 = 0.66
             meditation3 = 0.34
             suicide3 = 0
             exercise3 = 0.34
    elif num3 == 3:
             newthing3 = 0
             motivate3 = 0
             cheering3  = 0.49
             food3 = 0.49
             social3 = 0
             resting3 = 0.99
             meditation3 = 0.49
             suicide3 = 0
             exercise3 = 0.54
    num4 = int(input("คุณเหนื่อยง่าย หรือไม่ค่อยมีแรง:"))
    if num4 == 0:
             newthing4 = 0
             motivate4 = 0
             cheering4  = 0
             food4 = 0
             social4 = 0
             resting4 = 0
             meditation4 = 0
             suicide4 = 0
             exercise4 = 0  
    elif num4 == 1:
             newthing4 = 0
             motivate4 = 0
             cheering4  = 0
             food4 = 0.17
             social4 = 0
             resting4 = 0.33
             meditation4 = 0
             suicide4 = 0
             exercise4 = 0.33
    elif num4 == 2:
             newthing4 = 0
             motivate4 = 0
             cheering4  = 0
             food4 = 0.34
             social4 = 0
             resting4 = 0.66
             meditation4 = 0
             suicide4 = 0
             exercise4 = 0.66
    elif num4 == 3:
             newthing4 = 0
             motivate4 = 0
             cheering4  = 0
             food4 = 0.49
             social4 = 0
             resting4 = 0.99
             meditation4 = 0
             suicide4 = 0
             exercise4 = 0.99 
    num5 = int(input("คุณเบื่ออาหาร หรือกินมากเกินไป:"))
    if num5 == 0:
             newthing5 = 0
             motivate5 = 0
             cheering5  = 0
             food5 = 0
             social5 = 0
             resting5 = 0
             meditation5 = 0
             suicide5 = 0
             exercise5 = 0 
    elif num5 == 1:
             newthing5 = 0.33
             motivate5 = 0
             cheering5  = 0.17
             food5 = 0.33
             social5 = 0
             resting5 = 0
             meditation5 = 0
             suicide5 = 0
             exercise5 = 0.17
    elif num5 == 2:
             newthing5 = 0.66
             motivate5 = 0
             cheering5  = 0.34
             food5 = 0.66
             social5 = 0
             resting5 = 0
             meditation5 = 0
             suicide5 = 0
             exercise5 = 0.34
    elif num5 == 3:
             newthing5 = 0.99
             motivate5 = 0
             cheering5  = 0.
             food5 = 0.99
             social5 = 0
             resting5 = 0
             meditation5 = 0
             suicide5 = 0
             exercise5 = 0.49
    num6 = int(input("คุณรู้สึกไม่ดีกับตัวเอง คิดว่าตัวเองล้มเหลว หรือเป็นคนทำให้ตัวเอง หรือครอบครัวผิดหวัง:"))
    if num6 == 0:
             newthing6 = 0
             motivate6 = 0
             cheering6  = 0
             food6 = 0
             social6 = 0
             resting6 = 0
             meditation6 = 0
             suicide6 = 0
             exercise6 = 0
    elif num6 == 1:
             newthing6 = 0.33
             motivate6 = 0.33
             cheering6  = 0.33
             food6 = 0
             social6 = 0
             resting6 = 0
             meditation6 = 0
             suicide6 = 0
             exercise6 = 0 
    elif num6 == 2:
             newthing6 = 0.6
             motivate6 = 0.66
             cheering6  = 0.66
             food6 = 0.66
             social6 = 0
             resting6 = 0
             meditation6 = 0
             suicide6 = 0
             exercise6 = 0 
    elif num6 == 3:
             newthing6 = 0.99
             motivate6 = 0.99
             cheering6  = 0.99
             food6 = 0
             social6 = 0
             resting6 = 0
             meditation6 = 0
             suicide6 = 0 
             exercise6 = 0 
    num7 = int(input("คุณสมาธิไม่ดีเวลาทำอะไร เช่น ดูโทรทัศน์ ฟังวิทยุ หรือทำงานท่ีต้องใช้ความตั้งใจ:"))
    if num7 == 0:
             newthing7 = 0
             motivate7 = 0
             cheering7  = 0
             food7 = 0
             social7 = 0
             resting7 = 0
             meditation7 = 0
             suicide7 = 0 
             exercise7 = 0 
    elif num7 == 1:
             newthing7 = 0
             motivate7 = 0
             cheering7  = 0
             food7 = 0.17
             social7 = 0
             resting7 = 0.33
             meditation7 = 0.33
             suicide7 = 0
             exercise7 = 0
    elif num7 == 2:
             newthing7 = 0
             motivate7 = 0
             cheering7  = 0
             food7 = 0.34
             social7 = 0
             resting7 = 0.66
             meditation7 = 0.66
             suicide7 = 0
             exercise7 = 0
    elif num7 == 3:
             newthing7 = 0
             motivate7 = 0
             cheering7  = 0
             food7 = 0.49
             social7 = 0
             resting7 = 0.99
             meditation7 = 0.99
             suicide7 = 0 
             exercise7 = 0
    num8 = int(input("คุณพูดหรือทำอะไรช้าจนคนอื่นมองเห็น หรือกระสับกระส่ายจนท่านอยู่ไม่นิ่งเหมือนเคย:"))
    if num8 == 0 :
             newthing8 = 0
             motivate8 = 0
             cheering8  = 0
             food8 = 0
             social8 = 0
             resting8 = 0
             meditation8 = 0
             suicide8 = 0 
             exercise8 = 0
    elif num8 == 1:
             newthing8 = 0
             motivate8 = 0
             cheering8  = 0
             food8 = 0
             social8 = 0.17
             resting8 = 0.33
             meditation8 = 0.33
             suicide8 = 0
             exercise8 = 0.17
    elif num8 == 2:
             newthing8 = 0
             motivate8 = 0
             cheering8  = 0
             food8 = 0
             social8 = 0.34
             resting8 = 0.66
             meditation8 = 0.66
             suicide8 = 0
             exercise8 = 0.34
    elif num8 == 3:
             newthing8 = 0
             motivate8 = 0
             cheering8  = 0
             food8 = 0
             social8 = 0.49
             resting8 = 0.99
             meditation8 = 0.99
             suicide8 = 0
             exercise8 = 0.49 
    num9 = int(input("คุณ คิดทำร้ายตนเอง หรือคิดว่าถ้าตาย ๆ ไปเสียคงจะดี:"))
    if num9 == 0:
             newthing9 = 0
             motivate9 = 0
             cheering9 = 0
             food9 = 0
             social9 = 0
             resting9 = 0
             meditation9 = 0
             suicide9 = 0 
             exercise9 = 0
    elif num9 == 1:
             newthing9 = 0
             motivate9 = 0
             cheering9  = 0.99
             food9 = 0
             social9 = 0.49
             resting9 = 0
             meditation9 = 0
             suicide9 = 0.99
             exercise9 = 0
    elif num9 == 2:
             newthing9 = 0
             motivate9 = 0
             cheering9  = 0.99
             food9 = 0
             social9 = 0.49
             resting9 = 0
             meditation9 = 0
             suicide9 = 0.99
             exercise9 = 0
    elif num9 == 3:
             newthing9 = 0
             motivate9 = 0
             cheering9  = 0.99
             food9 = 0
             social9 = 0.49
             resting9 = 0
             meditation9 = 0
             suicide9 = 0.99
             exercise9 = 0


    phqscore = num1+num2+num3+num4+num5+num6+num7+num8+num9
    newthing = (newthing1+newthing2+newthing3+newthing4+newthing5+newthing6+newthing7+newthing8+newthing9)/3
    motivate = (motivate1+motivate2+motivate3+motivate4+motivate5+motivate6+motivate7+motivate8+motivate9)/3
    cheering = (cheering1+cheering2+cheering3+cheering4+cheering5+cheering6+cheering7+cheering8+cheering9)/6
    food = (food1+food2+food3+food4+food5+food6+food7+food8+food9)/4
    social = (social1+social2+social3+social4+social5+social6+social7+social8+social9)/3
    resting = (resting1+resting2+resting3+resting4+resting5+resting6+resting7+resting8+resting9)/4
    meditation = (meditation1+meditation2+meditation3+meditation4+meditation5+meditation6+meditation7+meditation8+meditation9)/3
    suicide = (suicide1+suicide2+suicide3+suicide4+suicide5+suicide6+suicide7+suicide8+suicide9)/1
    exercise = (exercise1+exercise2+exercise3+exercise4+exercise5+exercise6+exercise7+exercise8+exercise9)/4


    # print("Content matching score : ",newthing,motivate,cheering,food,social,resting,meditation,exercise,suicide)
    print("relevant score :1 1 1 0 2 3 1 0 1 ")
    print("คะแนนจากการประเมินสุขภาพจิตรของคุณคือ :",phqscore)
    if phqscore < 7:
        print("คุณไม่มีอาการซึมเศร้า ช่างสดใสจริงๆ!!")
    elif phqscore >7 & phqscore <=12:
        print("คุณมีอาการซึมเศร้าเล็กน้อย โชคดีนะจ๊ะ")
    elif phqscore ==13 & phqscore <=18:
        print("คุณมีอาการซึมเศร้าปานกลาง ควรไปพบแพทย์เพื่อขอคำปรึกษา")
    else:
        print("คุณมีอาการซึมเศร้าระดับรุนแรง ควรไปพบแพทย์เพื่อขอคำปรึกษาและทำการรักษา")
        return phqscore , newthing , motivate , cheering , food , social , resting , meditation , suicide, exercise
phq_9()

class Content:
    def __init__(self, cname, ccontent, cnewthing, cmotivate, ccheering, cfood, csocial, cresting, csuicide , cexercise):
        self.cname = cname
        self.ccontent = ccontent
        self.cnewthing = cnewthing
        self.cmotivate = cmotivate
        self.ccheering = ccheering
        self.cfood = cfood
        self.csocial = csocial
        self.cresting = cresting
        self.csuicide = csuicide
        self.cexercise = cexercise
        
first_content = Content('พักผ่อนนอนหลับ','อิอิ:3',0,0,0,0,0,0.33,0,0) 
second_content = Content('ออกกำลังกายทำให้นอนหลับ','อิอิ:3',0,0.33,0,0,0,0.33,0,0.33)
third_content = Content('ออกกำลังกายแบบใหม่','อิอิ:3',0.33,0.0,0,0,0,0.33,0,0.33) 

