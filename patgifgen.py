import pygame,pyui,os,math
def getresourceexactpath(paff):
    return os.path.dirname(os.path.abspath(__file__))+paff
from PIL import Image
from tkinter import filedialog as tkFileDialog
global frameTime,t,running,surface,spriteposition,sprite,hideframe,size,giftimedelay,sqeeshiness,resolutionsize
resolutionsize = 100
size = 80
hideframe = False
buttons = []
textboxes = []
text = []
spriteposition = [30,30]
running = True
sqeeshiness = 0
giftimedelay = 0.06
pyui.uisize = 10
surface = pyui.makewindow((126,67),textboxes,buttons,text)
sprite = pygame.image.load(getresourceexactpath("\\py.png")).convert_alpha()
patframes = [
    pygame.image.load(getresourceexactpath("\\frame0.png")).convert_alpha(),
    pygame.image.load(getresourceexactpath("\\frame1.png")).convert_alpha(),
    pygame.image.load(getresourceexactpath("\\frame2.png")).convert_alpha(),
    pygame.image.load(getresourceexactpath("\\frame3.png")).convert_alpha(),
    pygame.image.load(getresourceexactpath("\\frame4.png")).convert_alpha()
    ]

def makegifframe(number):
    global surface,sprite,spriteposition,hideframe,size,sqeeshiness,resolutionsize
    gifframe = pygame.Surface((112 * (resolutionsize / 100),112 * (resolutionsize / 100)), pygame.SRCALPHA, 32)
    gifframe.convert_alpha()
    if sprite != None:
        sine = math.sin((number + 1) * 5) * (12 + sqeeshiness)
        s = size - sine
        if s < 0:
            s = 0
        s2 = size + sine
        if s2 < 0:
            s2 = 0
        rendersprite = pygame.transform.scale(sprite,(s2 * (resolutionsize / 100),s * (resolutionsize / 100)))
        y = (spriteposition[1] + ((size - rendersprite.get_height())))
        x = spriteposition[0] - (((rendersprite.get_width() * 1) - size) / 2)
        add = ((resolutionsize / 100))
        gifframe.blit(rendersprite,(x * add,y * add))
    if hideframe == False:
        gifframe.blit(pygame.transform.scale(patframes[number],(112 * (resolutionsize / 100),112 * (resolutionsize / 100))),(0,(math.sin((number + 1) * 5) * sqeeshiness) * (resolutionsize / 100)))
    return gifframe

def createrealgif():
    global giftimedelay
    images = []
    for v in range(2,6,1):
        pil_string_image = pygame.image.tobytes(makegifframe(v - 1), "RGBA",False)
        images.append(Image.frombytes("RGBA",(112,112),pil_string_image))
    pil_string_image = pygame.image.tobytes(makegifframe(0), "RGBA",False)
    frame_one = Image.frombytes("RGBA",(112,112),pil_string_image)
    frame_one.save(pyui.textboxes[6][3], format="GIF", append_images=images,save_all=True, duration=giftimedelay * 1000, loop=0, disposal=2)

def browseforspr():
    file = tkFileDialog.askopenfilename(filetypes=([('Images','*.png *.jpg *.jpeg *.tga *.bmp')]),title="Browse...")
    if file != "":
        pyui.textboxes[2][3] = file

def browseforsavegif():
    file = tkFileDialog.asksaveasfilename(filetypes=([('Images','*.gif')]),title="Browse...")
    if file != "":
        pyui.textboxes[6][3] = file


pyui.addbutton((2,67 - 7),(122,5),"Generate gif! :3",createrealgif)
pyui.addtextbox((2,2),(122,5),"frame delay   minimum: 0.02, default: 0.06",True,False)
pyui.addtextbox((2,7),(122,5),"squishiness   minimum: 0, default: 0",True,False)
pyui.addtextbox((2,12),(122 - 8,5),"sprite",False,True)
pyui.addtextbox((2,17),(122,5),"size          minimum: 0, default: 80",True,False)
pyui.addtextbox((2,22),(122,5),"x          default: 30",True,False)
pyui.addtextbox((2,27),(122,5),"y          default: 30",True,False)
pyui.addtextbox((2,32),(122 - 8,5),"save destination",False,True)
pyui.addbutton((122 - 5,12),(7,5),"Browse",browseforspr)
pyui.addbutton((122 - 5,32),(7,5),"Browse",browseforsavegif)
pyui.textboxes[0][3] = "0.06"
pyui.textboxes[1][3] = "0"
pyui.textboxes[2][3] = getresourceexactpath("\\py.png")
pyui.textboxes[3][3] = "80"
pyui.textboxes[4][3] = "30"
pyui.textboxes[5][3] = "30"
pyui.textboxes[6][3] = getresourceexactpath("\\generatedgif.gif")

clock = pygame.time.Clock()
giftime = 0
shiftheld = False
blitimg = None
gifframe = 0
oldtext = "a"
while running == True:
    running = pyui.render(surface)
    if pyui.gettextboxtext(0) != "":
        if float(pyui.gettextboxtext(0)) >= 0.02:
            giftimedelay = float(pyui.gettextboxtext(0))
        else:
            giftimedelay = 0.02
    else:
        giftimedelay = 0.02
    if pyui.gettextboxtext(1) != "" and pyui.gettextboxtext(1) != "-":
        sqeeshiness = float(pyui.gettextboxtext(1))
    else:
        sqeeshiness = 0
    if pyui.gettextboxtext(2) != oldtext:
        if os.path.exists(pyui.gettextboxtext(2)):
            if os.path.isdir(pyui.gettextboxtext(2)) == False:
                if pyui.gettextboxtext(2).lower().endswith(('.png', '.jpg', '.jpeg',".tga",".bmp")):
                    sprite = pygame.image.load(pyui.gettextboxtext(2)).convert_alpha()
    oldtext = pyui.gettextboxtext(2)
    ecks = 30
    if pyui.gettextboxtext(4) != "" and pyui.gettextboxtext(4) != "-":
        ecks = int(pyui.gettextboxtext(4))
    whuy = 30
    if pyui.gettextboxtext(5) != "" and pyui.gettextboxtext(5) != "-":
        whuy = int(pyui.gettextboxtext(5))
    spriteposition = [ecks,whuy]
    size = 80
    if pyui.gettextboxtext(3) != "":
        size = int(pyui.gettextboxtext(3))
    surface.blit(pygame.transform.scale(makegifframe(gifframe),(112 * 2,112 * 2)),(2 * pyui.uisize,(37.4) * pyui.uisize))
    
    giftime += pyui.getframetime() * 1
    if giftime > giftimedelay:
        while giftime > giftimedelay:
            giftime -= giftimedelay
            gifframe += 1
            if gifframe > 4:
                gifframe = 0
    pygame.display.update()