##go no go

#Hi, I’m trying to adapt a GO/NOGO protocol from Price et al., 2016. Food-specific response inhibition,
#dietary restraint and snack intake in lean and overweight/obese adults.
#The task consists in 50 trials (40 go and 10 no-go). During go trials the 
#subject should press a key as fast as possible. During no-go trials, no key should be pressed. 
#Each trial is composed by an image presented for 750ms and was separated by a blank screen for 500 ms 
#and preceded by a fixation cross for 500 ms. The sequence of go/nogo stimuli are predetermined. 
#Two set of images are used: 10 go images (each one is presented 4 times) and 10 no-go images 
#(each one is presented one time). Image order should be randomized across subjects.
# we are going to change for anorexia nervosa intervention

import pandas as pd
from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Circle, Rect, TextBox, DotStim
from psychopy.core import Clock, quit, wait
from psychopy.event import Mouse
from psychopy.hardware.keyboard import Keyboard
from psychopy import event, data
import random

exp_info = {'participant_nr': '', 'age': '21'}
dlg = DlgFromDict(exp_info)

p_name= exp_info['participant_nr']

# Initialize a fullscreen window with my monitor (HD format) size
# and my monitor specification called "samsung" from the monitor center
win = Window(size=(1200, 800), fullscr=False)

# Also initialize a mouse, although we're not going to use it
mouse = Mouse(visible=False)

# Initialize a (global) clock
clock = Clock() ##initialize clock
f_list = f"/Users/annieberkowitz/Desktop/Intro to Programming/HF_LF_60.csv" ## path location CVS into variable
foods = pd.read_csv(f_list) ## using pandas to put csv file into data frame called foods
hf = foods[foods['fat']==1] ## ask if foods in the column named food has fat 1 or 0 
lf = foods[foods['fat']==0] 
lf = lf.sample(frac=0.4) ## take 40% of the high fat food randomly  (sample which is from random package)
hf = hf.sample(frac=0.4) 
trial_foods=pd.concat([lf,lf,lf,lf,hf]) ## variable trial food - giving 10 lf 4 times + hf 1once
trial_foods = trial_foods.sample(frac=1) ## take 100% of trial foods and randomize list 
kb=Keyboard()

instruct_txt = """ 
In this experiment, a series of photos will appear with either a red or green circle

On every trial:
    press the space bar if the circle if green
    do not press the space bar if the circle is green
    
(Press ‘enter’ to start the experiment!)
 """
     
# Show instructions and wait until response (return)
instruct_txt_stim = TextStim(win, instruct_txt, alignText='left', height=0.085)
instruct_txt_stim.draw()
win.flip()

# Initialize keyboard and wait for response
kb = Keyboard()
while True:
    keys = kb.getKeys()
    if 'return' in keys:
        # The for loop was optional
        for key in keys:
            print(f"The {key.name} key was pressed within {key.rt:.3f} seconds for a total of {key.duration:.3f} seconds.")
        break  # break out of the loop!
        
        
for i in range(0,len(trial_foods)): ## whole dataframe / ## i start with 0 but goes through whole datafram
    trial=trial_foods.iloc[i] ## trail is going to be one i row ## iloc to find out where you are in a dataframe
    print(trial) 
    t=TextStim(win,"+") ## adding fixation
    t.draw()
    win.flip()
    wait(0.5) ## 500 ms
    path = "/Users/annieberkowitz/Desktop/Intro to Programming/stimuli/" + trial.food
    print(trial.fat)
    if trial.fat==1:
        correct = "nogo"
        circle = Circle(win,pos=(-0.62, 0), radius =.1, fillColor='red', units='height')
    else: 
        correct = "go"
        circle = Circle(win,pos=(-0.62, 0), radius =.1, fillColor='green', units='height')
    im=ImageStim(win, path)
    
    
    t_clock=Clock() ## setting clock per trial
    response = "nongo"
    rt="NA"
    while t_clock.getTime() < .75:
        im.draw()
        circle.draw()
        win.flip()
        keys = kb.getKeys(['space','escape'], waitRelease=False)
        if keys:
            resp = keys[0].name
            rt = keys[0].rt
            if resp == 'escape':
                win.close()
                quit()
            else:
                response = "go"

    win.flip()
    wait(.5)
    trial_foods['response']=response
    trial_foods['rt']= rt
    trial_foods['correct_response'] = correct
trials.save(f"{p_name}_gonogo.csv") ## save as participant name

## tasks
# 1. figure out what is happening in the task & add instructions
## they are showing healthy food for the go condition and for the no go coniditon they are showing fast food items = dont press anything
# 2. we need to add go-nogo! How would we do that?

    
## homework 
## (1) make github account
## (2) make a respitory __> call it GoNoGo --> MAKE IT PUBLIC
## (3) add all files today that we used to run the experiment 
##     uploading an existing file 
##     upload all files need to github
##     add instructions
##     add a readME --> explantion of what the file is for, what the repositry is going to do , explain what files you uploaded and how you would do to run the experiment ex) store files, hit play on psychopi
##     stimuli folder --> will be too big, can make it smaller
##     share link to github repositry as URL in canas
