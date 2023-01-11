#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on December 30, 2022, at 09:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'Image_Psychopy'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\madih\\OneDrive\\Documents\\Image_Psychopy.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
textwelcome = visual.TextStim(win=win, name='textwelcome',
    text="Welcome to the image experiment !\n\nPress 'Space' to Begin",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Welcomekey = keyboard.Keyboard()

# --- Initialize components for Routine "Instructions" ---
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='C:/Users/madih/OneDrive/Desktop/Experiment/2022-12-06.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "trial1" ---
image2 = visual.ImageStim(
    win=win,
    name='image2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
skip = keyboard.Keyboard()

# --- Initialize components for Routine "Response1" ---
win.allowStencil = True
form = visual.Form(win=win, name='form',
    items='C:/Users/madih/Downloads/book1.xlsx',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 1),
    pos=(0, 0),
    itemPadding=0.05
)
sur_skip1 = keyboard.Keyboard()

# --- Initialize components for Routine "trial2" ---
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='C:/Users/madih/OneDrive/Desktop/Experiment/4.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
skip2 = keyboard.Keyboard()

# --- Initialize components for Routine "Response2" ---
win.allowStencil = True
form_2 = visual.Form(win=win, name='form_2',
    items='C:/Users/madih/Downloads/book1.xlsx',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 1),
    pos=(0, 0),
    itemPadding=0.05
)
Sur_skip2 = keyboard.Keyboard()

# --- Initialize components for Routine "trialv1" ---
geo = visual.MovieStim(
    win, name='geo',
    filename='C:/Users/madih/Downloads/mixkit-aerial-view-of-mountain-geography-a-town-and-a-lake-10090-medium.mp4', movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=(1,1), units=None,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)
skipv1 = keyboard.Keyboard()

# --- Initialize components for Routine "responsev1" ---
win.allowStencil = True
formv1 = visual.Form(win=win, name='formv1',
    items='C:/Users/madih/Downloads/book1.xlsx',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 1),
    pos=(0, 0),
    itemPadding=0.05
)
skip_v1 = keyboard.Keyboard()

# --- Initialize components for Routine "trial3" ---
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='C:/Users/madih/OneDrive/Desktop/Experiment/5.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
skip3 = keyboard.Keyboard()

# --- Initialize components for Routine "Response3" ---
win.allowStencil = True
form_3 = visual.Form(win=win, name='form_3',
    items='C:/Users/madih/Downloads/book1.xlsx',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 1),
    pos=(0, 0),
    itemPadding=0.05
)
sur_skip3 = keyboard.Keyboard()

# --- Initialize components for Routine "trialv2" ---
moviev2 = visual.MovieStim(
    win, name='moviev2',
    filename='C:/Users/madih/Downloads/mixkit-marine-life-in-a-fish-tank-18769-medium.mp4', movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=(1,1), units=None,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)
skipv3 = keyboard.Keyboard()

# --- Initialize components for Routine "Responsev2" ---
win.allowStencil = True
form_v2 = visual.Form(win=win, name='form_v2',
    items='C:/Users/madih/Downloads/book1.xlsx',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 1),
    pos=(0, 0),
    itemPadding=0.05
)
skipv4 = keyboard.Keyboard()

# --- Initialize components for Routine "trial4" ---
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='C:/Users/madih/OneDrive/Desktop/Experiment/8.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
skip4 = keyboard.Keyboard()

# --- Initialize components for Routine "Response4" ---
win.allowStencil = True
form_4 = visual.Form(win=win, name='form_4',
    items='C:/Users/madih/Downloads/book1.xlsx',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 1),
    pos=(0, 0),
    itemPadding=0.05
)
sur_skip4 = keyboard.Keyboard()

# --- Initialize components for Routine "trial5" ---
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='C:/Users/madih/OneDrive/Desktop/Experiment/11.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
skip5 = keyboard.Keyboard()

# --- Initialize components for Routine "Response5" ---
win.allowStencil = True
form_5 = visual.Form(win=win, name='form_5',
    items='C:/Users/madih/Downloads/book1.xlsx',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 1),
    pos=(0, 0),
    itemPadding=0.05
)
sur_skip5 = keyboard.Keyboard()

# --- Initialize components for Routine "trialv3" ---
moviev3 = visual.MovieStim(
    win, name='moviev3',
    filename='C:/Users/madih/Downloads/mixkit-happy-little-girl-on-a-swing-in-a-park-8715-medium.mp4', movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=(1,1), units=None,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)
skip_v3 = keyboard.Keyboard()

# --- Initialize components for Routine "Responsev3" ---
win.allowStencil = True
form_v3 = visual.Form(win=win, name='form_v3',
    items='C:/Users/madih/Downloads/book1.xlsx',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 1),
    pos=(0, 0),
    itemPadding=0.05
)
skipv5 = keyboard.Keyboard()

# --- Initialize components for Routine "Goodbye" ---
Thankyou = visual.TextStim(win=win, name='Thankyou',
    text='Thank You !',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Welcomekey.keys = []
Welcomekey.rt = []
_Welcomekey_allKeys = []
# keep track of which components have finished
WelcomeComponents = [textwelcome, Welcomekey]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textwelcome* updates
    if textwelcome.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        textwelcome.frameNStart = frameN  # exact frame index
        textwelcome.tStart = t  # local t and not account for scr refresh
        textwelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textwelcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textwelcome.started')
        textwelcome.setAutoDraw(True)
    
    # *Welcomekey* updates
    waitOnFlip = False
    if Welcomekey.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Welcomekey.frameNStart = frameN  # exact frame index
        Welcomekey.tStart = t  # local t and not account for scr refresh
        Welcomekey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcomekey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Welcomekey.started')
        Welcomekey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Welcomekey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Welcomekey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Welcomekey.status == STARTED and not waitOnFlip:
        theseKeys = Welcomekey.getKeys(keyList=['space'], waitRelease=False)
        _Welcomekey_allKeys.extend(theseKeys)
        if len(_Welcomekey_allKeys):
            Welcomekey.keys = _Welcomekey_allKeys[-1].name  # just the last key pressed
            Welcomekey.rt = _Welcomekey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Welcomekey.keys in ['', [], None]:  # No response was made
    Welcomekey.keys = None
thisExp.addData('Welcomekey.keys',Welcomekey.keys)
if Welcomekey.keys != None:  # we had a response
    thisExp.addData('Welcomekey.rt', Welcomekey.rt)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [image_2, key_resp]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_2.started')
        image_2.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trial1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
image2.setImage('C:/Users/madih/OneDrive/Desktop/Experiment/2.jpg')
skip.keys = []
skip.rt = []
_skip_allKeys = []
# keep track of which components have finished
trial1Components = [image2, skip]
for thisComponent in trial1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image2* updates
    if image2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        image2.frameNStart = frameN  # exact frame index
        image2.tStart = t  # local t and not account for scr refresh
        image2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image2.started')
        image2.setAutoDraw(True)
    if image2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image2.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image2.tStop = t  # not accounting for scr refresh
            image2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image2.stopped')
            image2.setAutoDraw(False)
    
    # *skip* updates
    waitOnFlip = False
    if skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skip.frameNStart = frameN  # exact frame index
        skip.tStart = t  # local t and not account for scr refresh
        skip.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skip, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'skip.started')
        skip.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skip.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skip.status == STARTED and not waitOnFlip:
        theseKeys = skip.getKeys(keyList=['space'], waitRelease=False)
        _skip_allKeys.extend(theseKeys)
        if len(_skip_allKeys):
            skip.keys = _skip_allKeys[-1].name  # just the last key pressed
            skip.rt = _skip_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial1" ---
for thisComponent in trial1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if skip.keys in ['', [], None]:  # No response was made
    skip.keys = None
thisExp.addData('skip.keys',skip.keys)
if skip.keys != None:  # we had a response
    thisExp.addData('skip.rt', skip.rt)
thisExp.nextEntry()
# the Routine "trial1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Response1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
form.setContrast(1.0)
sur_skip1.keys = []
sur_skip1.rt = []
_sur_skip1_allKeys = []
# keep track of which components have finished
Response1Components = [form, sur_skip1]
for thisComponent in Response1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Response1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *form* updates
    if form.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        form.frameNStart = frameN  # exact frame index
        form.tStart = t  # local t and not account for scr refresh
        form.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form, 'tStartRefresh')  # time at next scr refresh
        form.setAutoDraw(True)
    
    # *sur_skip1* updates
    waitOnFlip = False
    if sur_skip1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sur_skip1.frameNStart = frameN  # exact frame index
        sur_skip1.tStart = t  # local t and not account for scr refresh
        sur_skip1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sur_skip1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sur_skip1.started')
        sur_skip1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(sur_skip1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(sur_skip1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if sur_skip1.status == STARTED and not waitOnFlip:
        theseKeys = sur_skip1.getKeys(keyList=['space'], waitRelease=False)
        _sur_skip1_allKeys.extend(theseKeys)
        if len(_sur_skip1_allKeys):
            sur_skip1.keys = _sur_skip1_allKeys[-1].name  # just the last key pressed
            sur_skip1.rt = _sur_skip1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Response1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Response1" ---
for thisComponent in Response1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
form.addDataToExp(thisExp, 'rows')
form.autodraw = False
# check responses
if sur_skip1.keys in ['', [], None]:  # No response was made
    sur_skip1.keys = None
thisExp.addData('sur_skip1.keys',sur_skip1.keys)
if sur_skip1.keys != None:  # we had a response
    thisExp.addData('sur_skip1.rt', sur_skip1.rt)
thisExp.nextEntry()
# the Routine "Response1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trial2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skip2.keys = []
skip2.rt = []
_skip2_allKeys = []
# keep track of which components have finished
trial2Components = [image_3, skip2]
for thisComponent in trial2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3.started')
        image_3.setAutoDraw(True)
    if image_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_3.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_3.tStop = t  # not accounting for scr refresh
            image_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3.stopped')
            image_3.setAutoDraw(False)
    
    # *skip2* updates
    waitOnFlip = False
    if skip2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skip2.frameNStart = frameN  # exact frame index
        skip2.tStart = t  # local t and not account for scr refresh
        skip2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skip2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'skip2.started')
        skip2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skip2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skip2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skip2.status == STARTED and not waitOnFlip:
        theseKeys = skip2.getKeys(keyList=['space'], waitRelease=False)
        _skip2_allKeys.extend(theseKeys)
        if len(_skip2_allKeys):
            skip2.keys = _skip2_allKeys[-1].name  # just the last key pressed
            skip2.rt = _skip2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial2" ---
for thisComponent in trial2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if skip2.keys in ['', [], None]:  # No response was made
    skip2.keys = None
thisExp.addData('skip2.keys',skip2.keys)
if skip2.keys != None:  # we had a response
    thisExp.addData('skip2.rt', skip2.rt)
thisExp.nextEntry()
# the Routine "trial2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Response2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Sur_skip2.keys = []
Sur_skip2.rt = []
_Sur_skip2_allKeys = []
# keep track of which components have finished
Response2Components = [form_2, Sur_skip2]
for thisComponent in Response2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Response2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *form_2* updates
    if form_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form_2.frameNStart = frameN  # exact frame index
        form_2.tStart = t  # local t and not account for scr refresh
        form_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'form_2.started')
        form_2.setAutoDraw(True)
    
    # *Sur_skip2* updates
    waitOnFlip = False
    if Sur_skip2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Sur_skip2.frameNStart = frameN  # exact frame index
        Sur_skip2.tStart = t  # local t and not account for scr refresh
        Sur_skip2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Sur_skip2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Sur_skip2.started')
        Sur_skip2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Sur_skip2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Sur_skip2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Sur_skip2.status == STARTED and not waitOnFlip:
        theseKeys = Sur_skip2.getKeys(keyList=['space'], waitRelease=False)
        _Sur_skip2_allKeys.extend(theseKeys)
        if len(_Sur_skip2_allKeys):
            Sur_skip2.keys = _Sur_skip2_allKeys[-1].name  # just the last key pressed
            Sur_skip2.rt = _Sur_skip2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Response2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Response2" ---
for thisComponent in Response2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
form_2.addDataToExp(thisExp, 'rows')
form_2.autodraw = False
# check responses
if Sur_skip2.keys in ['', [], None]:  # No response was made
    Sur_skip2.keys = None
thisExp.addData('Sur_skip2.keys',Sur_skip2.keys)
if Sur_skip2.keys != None:  # we had a response
    thisExp.addData('Sur_skip2.rt', Sur_skip2.rt)
thisExp.nextEntry()
# the Routine "Response2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trialv1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skipv1.keys = []
skipv1.rt = []
_skipv1_allKeys = []
# keep track of which components have finished
trialv1Components = [geo, skipv1]
for thisComponent in trialv1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trialv1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *geo* updates
    if geo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        geo.frameNStart = frameN  # exact frame index
        geo.tStart = t  # local t and not account for scr refresh
        geo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(geo, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'geo.started')
        geo.setAutoDraw(True)
        geo.play()
    
    # *skipv1* updates
    waitOnFlip = False
    if skipv1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skipv1.frameNStart = frameN  # exact frame index
        skipv1.tStart = t  # local t and not account for scr refresh
        skipv1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skipv1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'skipv1.started')
        skipv1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skipv1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skipv1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skipv1.status == STARTED and not waitOnFlip:
        theseKeys = skipv1.getKeys(keyList=['space'], waitRelease=False)
        _skipv1_allKeys.extend(theseKeys)
        if len(_skipv1_allKeys):
            skipv1.keys = _skipv1_allKeys[-1].name  # just the last key pressed
            skipv1.rt = _skipv1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialv1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trialv1" ---
for thisComponent in trialv1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
geo.stop()
# check responses
if skipv1.keys in ['', [], None]:  # No response was made
    skipv1.keys = None
thisExp.addData('skipv1.keys',skipv1.keys)
if skipv1.keys != None:  # we had a response
    thisExp.addData('skipv1.rt', skipv1.rt)
thisExp.nextEntry()
# the Routine "trialv1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "responsev1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skip_v1.keys = []
skip_v1.rt = []
_skip_v1_allKeys = []
# keep track of which components have finished
responsev1Components = [formv1, skip_v1]
for thisComponent in responsev1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "responsev1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *formv1* updates
    if formv1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        formv1.frameNStart = frameN  # exact frame index
        formv1.tStart = t  # local t and not account for scr refresh
        formv1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(formv1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'formv1.started')
        formv1.setAutoDraw(True)
    
    # *skip_v1* updates
    waitOnFlip = False
    if skip_v1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skip_v1.frameNStart = frameN  # exact frame index
        skip_v1.tStart = t  # local t and not account for scr refresh
        skip_v1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skip_v1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'skip_v1.started')
        skip_v1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skip_v1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skip_v1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skip_v1.status == STARTED and not waitOnFlip:
        theseKeys = skip_v1.getKeys(keyList=['space'], waitRelease=False)
        _skip_v1_allKeys.extend(theseKeys)
        if len(_skip_v1_allKeys):
            skip_v1.keys = _skip_v1_allKeys[-1].name  # just the last key pressed
            skip_v1.rt = _skip_v1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in responsev1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "responsev1" ---
for thisComponent in responsev1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
formv1.addDataToExp(thisExp, 'rows')
formv1.autodraw = False
# check responses
if skip_v1.keys in ['', [], None]:  # No response was made
    skip_v1.keys = None
thisExp.addData('skip_v1.keys',skip_v1.keys)
if skip_v1.keys != None:  # we had a response
    thisExp.addData('skip_v1.rt', skip_v1.rt)
thisExp.nextEntry()
# the Routine "responsev1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trial3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skip3.keys = []
skip3.rt = []
_skip3_allKeys = []
# keep track of which components have finished
trial3Components = [image_4, skip3]
for thisComponent in trial3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_4.started')
        image_4.setAutoDraw(True)
    if image_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_4.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_4.tStop = t  # not accounting for scr refresh
            image_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_4.stopped')
            image_4.setAutoDraw(False)
    
    # *skip3* updates
    waitOnFlip = False
    if skip3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skip3.frameNStart = frameN  # exact frame index
        skip3.tStart = t  # local t and not account for scr refresh
        skip3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skip3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'skip3.started')
        skip3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skip3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skip3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skip3.status == STARTED and not waitOnFlip:
        theseKeys = skip3.getKeys(keyList=['space'], waitRelease=False)
        _skip3_allKeys.extend(theseKeys)
        if len(_skip3_allKeys):
            skip3.keys = _skip3_allKeys[-1].name  # just the last key pressed
            skip3.rt = _skip3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial3" ---
for thisComponent in trial3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if skip3.keys in ['', [], None]:  # No response was made
    skip3.keys = None
thisExp.addData('skip3.keys',skip3.keys)
if skip3.keys != None:  # we had a response
    thisExp.addData('skip3.rt', skip3.rt)
thisExp.nextEntry()
# the Routine "trial3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Response3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
sur_skip3.keys = []
sur_skip3.rt = []
_sur_skip3_allKeys = []
# keep track of which components have finished
Response3Components = [form_3, sur_skip3]
for thisComponent in Response3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Response3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *form_3* updates
    if form_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form_3.frameNStart = frameN  # exact frame index
        form_3.tStart = t  # local t and not account for scr refresh
        form_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'form_3.started')
        form_3.setAutoDraw(True)
    
    # *sur_skip3* updates
    waitOnFlip = False
    if sur_skip3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sur_skip3.frameNStart = frameN  # exact frame index
        sur_skip3.tStart = t  # local t and not account for scr refresh
        sur_skip3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sur_skip3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sur_skip3.started')
        sur_skip3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(sur_skip3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(sur_skip3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if sur_skip3.status == STARTED and not waitOnFlip:
        theseKeys = sur_skip3.getKeys(keyList=['space'], waitRelease=False)
        _sur_skip3_allKeys.extend(theseKeys)
        if len(_sur_skip3_allKeys):
            sur_skip3.keys = _sur_skip3_allKeys[-1].name  # just the last key pressed
            sur_skip3.rt = _sur_skip3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Response3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Response3" ---
for thisComponent in Response3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
form_3.addDataToExp(thisExp, 'rows')
form_3.autodraw = False
# check responses
if sur_skip3.keys in ['', [], None]:  # No response was made
    sur_skip3.keys = None
thisExp.addData('sur_skip3.keys',sur_skip3.keys)
if sur_skip3.keys != None:  # we had a response
    thisExp.addData('sur_skip3.rt', sur_skip3.rt)
thisExp.nextEntry()
# the Routine "Response3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trialv2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skipv3.keys = []
skipv3.rt = []
_skipv3_allKeys = []
# keep track of which components have finished
trialv2Components = [moviev2, skipv3]
for thisComponent in trialv2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trialv2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *moviev2* updates
    if moviev2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        moviev2.frameNStart = frameN  # exact frame index
        moviev2.tStart = t  # local t and not account for scr refresh
        moviev2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(moviev2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'moviev2.started')
        moviev2.setAutoDraw(True)
        moviev2.play()
    
    # *skipv3* updates
    waitOnFlip = False
    if skipv3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skipv3.frameNStart = frameN  # exact frame index
        skipv3.tStart = t  # local t and not account for scr refresh
        skipv3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skipv3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'skipv3.started')
        skipv3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skipv3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skipv3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skipv3.status == STARTED and not waitOnFlip:
        theseKeys = skipv3.getKeys(keyList=['space'], waitRelease=False)
        _skipv3_allKeys.extend(theseKeys)
        if len(_skipv3_allKeys):
            skipv3.keys = _skipv3_allKeys[-1].name  # just the last key pressed
            skipv3.rt = _skipv3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialv2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trialv2" ---
for thisComponent in trialv2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
moviev2.stop()
# check responses
if skipv3.keys in ['', [], None]:  # No response was made
    skipv3.keys = None
thisExp.addData('skipv3.keys',skipv3.keys)
if skipv3.keys != None:  # we had a response
    thisExp.addData('skipv3.rt', skipv3.rt)
thisExp.nextEntry()
# the Routine "trialv2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Responsev2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skipv4.keys = []
skipv4.rt = []
_skipv4_allKeys = []
# keep track of which components have finished
Responsev2Components = [form_v2, skipv4]
for thisComponent in Responsev2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Responsev2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *form_v2* updates
    if form_v2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form_v2.frameNStart = frameN  # exact frame index
        form_v2.tStart = t  # local t and not account for scr refresh
        form_v2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form_v2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'form_v2.started')
        form_v2.setAutoDraw(True)
    
    # *skipv4* updates
    waitOnFlip = False
    if skipv4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skipv4.frameNStart = frameN  # exact frame index
        skipv4.tStart = t  # local t and not account for scr refresh
        skipv4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skipv4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'skipv4.started')
        skipv4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skipv4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skipv4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skipv4.status == STARTED and not waitOnFlip:
        theseKeys = skipv4.getKeys(keyList=['space'], waitRelease=False)
        _skipv4_allKeys.extend(theseKeys)
        if len(_skipv4_allKeys):
            skipv4.keys = _skipv4_allKeys[-1].name  # just the last key pressed
            skipv4.rt = _skipv4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Responsev2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Responsev2" ---
for thisComponent in Responsev2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
form_v2.addDataToExp(thisExp, 'rows')
form_v2.autodraw = False
# check responses
if skipv4.keys in ['', [], None]:  # No response was made
    skipv4.keys = None
thisExp.addData('skipv4.keys',skipv4.keys)
if skipv4.keys != None:  # we had a response
    thisExp.addData('skipv4.rt', skipv4.rt)
thisExp.nextEntry()
# the Routine "Responsev2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trial4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skip4.keys = []
skip4.rt = []
_skip4_allKeys = []
# keep track of which components have finished
trial4Components = [image_6, skip4]
for thisComponent in trial4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_6.started')
        image_6.setAutoDraw(True)
    if image_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_6.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_6.tStop = t  # not accounting for scr refresh
            image_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_6.stopped')
            image_6.setAutoDraw(False)
    
    # *skip4* updates
    waitOnFlip = False
    if skip4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skip4.frameNStart = frameN  # exact frame index
        skip4.tStart = t  # local t and not account for scr refresh
        skip4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skip4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'skip4.started')
        skip4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skip4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skip4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skip4.status == STARTED and not waitOnFlip:
        theseKeys = skip4.getKeys(keyList=['space'], waitRelease=False)
        _skip4_allKeys.extend(theseKeys)
        if len(_skip4_allKeys):
            skip4.keys = _skip4_allKeys[-1].name  # just the last key pressed
            skip4.rt = _skip4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial4" ---
for thisComponent in trial4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if skip4.keys in ['', [], None]:  # No response was made
    skip4.keys = None
thisExp.addData('skip4.keys',skip4.keys)
if skip4.keys != None:  # we had a response
    thisExp.addData('skip4.rt', skip4.rt)
thisExp.nextEntry()
# the Routine "trial4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Response4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
sur_skip4.keys = []
sur_skip4.rt = []
_sur_skip4_allKeys = []
# keep track of which components have finished
Response4Components = [form_4, sur_skip4]
for thisComponent in Response4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Response4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *form_4* updates
    if form_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form_4.frameNStart = frameN  # exact frame index
        form_4.tStart = t  # local t and not account for scr refresh
        form_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'form_4.started')
        form_4.setAutoDraw(True)
    
    # *sur_skip4* updates
    waitOnFlip = False
    if sur_skip4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sur_skip4.frameNStart = frameN  # exact frame index
        sur_skip4.tStart = t  # local t and not account for scr refresh
        sur_skip4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sur_skip4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sur_skip4.started')
        sur_skip4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(sur_skip4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(sur_skip4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if sur_skip4.status == STARTED and not waitOnFlip:
        theseKeys = sur_skip4.getKeys(keyList=['space'], waitRelease=False)
        _sur_skip4_allKeys.extend(theseKeys)
        if len(_sur_skip4_allKeys):
            sur_skip4.keys = _sur_skip4_allKeys[-1].name  # just the last key pressed
            sur_skip4.rt = _sur_skip4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Response4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Response4" ---
for thisComponent in Response4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
form_4.addDataToExp(thisExp, 'rows')
form_4.autodraw = False
# check responses
if sur_skip4.keys in ['', [], None]:  # No response was made
    sur_skip4.keys = None
thisExp.addData('sur_skip4.keys',sur_skip4.keys)
if sur_skip4.keys != None:  # we had a response
    thisExp.addData('sur_skip4.rt', sur_skip4.rt)
thisExp.nextEntry()
# the Routine "Response4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trial5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skip5.keys = []
skip5.rt = []
_skip5_allKeys = []
# keep track of which components have finished
trial5Components = [image_7, skip5]
for thisComponent in trial5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_7.started')
        image_7.setAutoDraw(True)
    if image_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_7.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_7.tStop = t  # not accounting for scr refresh
            image_7.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_7.stopped')
            image_7.setAutoDraw(False)
    
    # *skip5* updates
    waitOnFlip = False
    if skip5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skip5.frameNStart = frameN  # exact frame index
        skip5.tStart = t  # local t and not account for scr refresh
        skip5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skip5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'skip5.started')
        skip5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skip5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skip5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skip5.status == STARTED and not waitOnFlip:
        theseKeys = skip5.getKeys(keyList=['space'], waitRelease=False)
        _skip5_allKeys.extend(theseKeys)
        if len(_skip5_allKeys):
            skip5.keys = _skip5_allKeys[-1].name  # just the last key pressed
            skip5.rt = _skip5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial5" ---
for thisComponent in trial5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if skip5.keys in ['', [], None]:  # No response was made
    skip5.keys = None
thisExp.addData('skip5.keys',skip5.keys)
if skip5.keys != None:  # we had a response
    thisExp.addData('skip5.rt', skip5.rt)
thisExp.nextEntry()
# the Routine "trial5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Response5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
sur_skip5.keys = []
sur_skip5.rt = []
_sur_skip5_allKeys = []
# keep track of which components have finished
Response5Components = [form_5, sur_skip5]
for thisComponent in Response5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Response5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *form_5* updates
    if form_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form_5.frameNStart = frameN  # exact frame index
        form_5.tStart = t  # local t and not account for scr refresh
        form_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'form_5.started')
        form_5.setAutoDraw(True)
    
    # *sur_skip5* updates
    waitOnFlip = False
    if sur_skip5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sur_skip5.frameNStart = frameN  # exact frame index
        sur_skip5.tStart = t  # local t and not account for scr refresh
        sur_skip5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sur_skip5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sur_skip5.started')
        sur_skip5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(sur_skip5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(sur_skip5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if sur_skip5.status == STARTED and not waitOnFlip:
        theseKeys = sur_skip5.getKeys(keyList=['space'], waitRelease=False)
        _sur_skip5_allKeys.extend(theseKeys)
        if len(_sur_skip5_allKeys):
            sur_skip5.keys = _sur_skip5_allKeys[-1].name  # just the last key pressed
            sur_skip5.rt = _sur_skip5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Response5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Response5" ---
for thisComponent in Response5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
form_5.addDataToExp(thisExp, 'rows')
form_5.autodraw = False
# check responses
if sur_skip5.keys in ['', [], None]:  # No response was made
    sur_skip5.keys = None
thisExp.addData('sur_skip5.keys',sur_skip5.keys)
if sur_skip5.keys != None:  # we had a response
    thisExp.addData('sur_skip5.rt', sur_skip5.rt)
thisExp.nextEntry()
# the Routine "Response5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trialv3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skip_v3.keys = []
skip_v3.rt = []
_skip_v3_allKeys = []
# keep track of which components have finished
trialv3Components = [moviev3, skip_v3]
for thisComponent in trialv3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trialv3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *moviev3* updates
    if moviev3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        moviev3.frameNStart = frameN  # exact frame index
        moviev3.tStart = t  # local t and not account for scr refresh
        moviev3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(moviev3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'moviev3.started')
        moviev3.setAutoDraw(True)
        moviev3.play()
    
    # *skip_v3* updates
    waitOnFlip = False
    if skip_v3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skip_v3.frameNStart = frameN  # exact frame index
        skip_v3.tStart = t  # local t and not account for scr refresh
        skip_v3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skip_v3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'skip_v3.started')
        skip_v3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skip_v3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skip_v3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skip_v3.status == STARTED and not waitOnFlip:
        theseKeys = skip_v3.getKeys(keyList=['space'], waitRelease=False)
        _skip_v3_allKeys.extend(theseKeys)
        if len(_skip_v3_allKeys):
            skip_v3.keys = _skip_v3_allKeys[-1].name  # just the last key pressed
            skip_v3.rt = _skip_v3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialv3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trialv3" ---
for thisComponent in trialv3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
moviev3.stop()
# check responses
if skip_v3.keys in ['', [], None]:  # No response was made
    skip_v3.keys = None
thisExp.addData('skip_v3.keys',skip_v3.keys)
if skip_v3.keys != None:  # we had a response
    thisExp.addData('skip_v3.rt', skip_v3.rt)
thisExp.nextEntry()
# the Routine "trialv3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Responsev3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skipv5.keys = []
skipv5.rt = []
_skipv5_allKeys = []
# keep track of which components have finished
Responsev3Components = [form_v3, skipv5]
for thisComponent in Responsev3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Responsev3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *form_v3* updates
    if form_v3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form_v3.frameNStart = frameN  # exact frame index
        form_v3.tStart = t  # local t and not account for scr refresh
        form_v3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form_v3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'form_v3.started')
        form_v3.setAutoDraw(True)
    
    # *skipv5* updates
    waitOnFlip = False
    if skipv5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skipv5.frameNStart = frameN  # exact frame index
        skipv5.tStart = t  # local t and not account for scr refresh
        skipv5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skipv5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'skipv5.started')
        skipv5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skipv5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skipv5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skipv5.status == STARTED and not waitOnFlip:
        theseKeys = skipv5.getKeys(keyList=['space'], waitRelease=False)
        _skipv5_allKeys.extend(theseKeys)
        if len(_skipv5_allKeys):
            skipv5.keys = _skipv5_allKeys[-1].name  # just the last key pressed
            skipv5.rt = _skipv5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Responsev3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Responsev3" ---
for thisComponent in Responsev3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
form_v3.addDataToExp(thisExp, 'rows')
form_v3.autodraw = False
# check responses
if skipv5.keys in ['', [], None]:  # No response was made
    skipv5.keys = None
thisExp.addData('skipv5.keys',skipv5.keys)
if skipv5.keys != None:  # we had a response
    thisExp.addData('skipv5.rt', skipv5.rt)
thisExp.nextEntry()
# the Routine "Responsev3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Goodbye" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
GoodbyeComponents = [Thankyou]
for thisComponent in GoodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Goodbye" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Thankyou* updates
    if Thankyou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Thankyou.frameNStart = frameN  # exact frame index
        Thankyou.tStart = t  # local t and not account for scr refresh
        Thankyou.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Thankyou, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Thankyou.started')
        Thankyou.setAutoDraw(True)
    if Thankyou.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Thankyou.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            Thankyou.tStop = t  # not accounting for scr refresh
            Thankyou.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Thankyou.stopped')
            Thankyou.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Goodbye" ---
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
