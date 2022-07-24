#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on July 24, 2022, at 11:25
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'VWM'  # from the Builder filename that created this script
expInfo = {'participant': '', 'version': '1', 'PROLIFIC_PID': ''}
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
    originPath='C:\\Users\\L\\Desktop\\vwm\\VWM_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "wm_intro"
wm_introClock = core.Clock()
# To select version run files
exp_version = str(expInfo['version'])

# AVOIDING NUMPY
bgcol = [-1,-1,-1]
basecol = [1,1,1]
distcol = basecol
salientcol = [1,1,1]

# Apparently I need to change code in order to update the experiment to store on/off times

distcol = basecol # default

good_feedback_col = '#a6d854'
slow_feedback_col = '#feb24c'

enc_rest_msg = "" # initialise to empty str
wm_rest_msg = ""
ret_rest_msg = ""


feedback_msg = ""
feedback_col = basecol
wm_intro_txt = visual.TextStim(win=win, name='wm_intro_txt',
    text='SECTION 2 of 3\n\nChange Detection\n\n\nPress [SPACE] for instructions',
    font='cambria',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
wm_intro_resp = keyboard.Keyboard()

# Initialize components for Routine "wm_instructions_1"
wm_instructions_1Clock = core.Clock()
rad = 0.25 # radius = a quarter of the screen
box_size = 0.1

study_frames = 0.2 * 60
retention_frames = 1 * 60
test_frames = 1.3 * 60
test_fix_frames = 2.3 * 60

## INITIAL COLOURS (DO NOT USE BECAUSE JS SUCKS!!!:
#clrs = {'RED':np.array([255,36,28]),
#       'GREEN':np.array([0, 248, 25]),
#       'BLUE':np.array([0, 145, 255]),
#       'YELLOW':np.array([255,251, 34]),
#       'CYAN':np.array([0, 255, 255]),
#       'PURPLE':np.array([255, 60, 255]),
#       'WHITE':np.array([250, 250, 250])}

## The _ is to differentiate these from builtin color vars.
#_RED = [1.0, -0.7176470588235294, -0.7803921568627451]
#_GREEN = [-1.0, 0.9450980392156862, -0.803921568627451]
#_BLUE = [-1.0, 0.13725490196078427, 1.0]
#_YELLOW = [1.0, 0.968627450980392, -0.7333333333333334]
#_CYAN = [-1.0, 1.0, 1.0]
#_PURPLE = [1.0, -0.5294117647058824, 1.0]
#_WHITE = [0.9607843137254901, 0.9607843137254901, 0.9607843137254901]
#_X = bgcol
#
#
#
## Seven colours plus a bacground blank colour (X). IF there's a change, the to-change slot's colour changes to the seventh.
#all_colours = {"RED":_RED, "GREEN":_GREEN, "BLUE":_BLUE, "YELLOW":_YELLOW, "CYAN":_CYAN, "PURPLE":_PURPLE, "WHITE":_WHITE, 'X':_X}

# Since these get set prior to reading in the file they need initializing
# ... they get updated on each trial so the X is just filler.

#study_clr1 = _X
#study_clr2 = _X
#study_clr3 = _X
#study_clr4 = _X
#study_clr5 = _X
#study_clr6 = _X
#
#test_clr1 = _X
#test_clr2 = _X
#test_clr3 = _X
#test_clr4 = _X
#test_clr5 = _X
#test_clr6 = _X
wm_instr_txt_1 = visual.TextStim(win=win, name='wm_instr_txt_1',
    text='You will see a circular array of coloured squares.\n\nThe colours will quickly disappear and then reappear after one second.\n\nWhen the colours reappear, they will either be identical or *one of the colours will have changed*.\n\nWhen they reappear, press [D] if there was a change, or press [J] if there was not a change.\n\nThis is fast, so respond as quickly and accurately as possible.\n\nPress [SPACE] to begin.',
    font='cambria',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
wm_start_resp_1 = keyboard.Keyboard()

# Initialize components for Routine "wm_instructions_2"
wm_instructions_2Clock = core.Clock()
rad = 0.25 # radius = a quarter of the screen
box_size = 0.1

study_frames = 0.2 * 60
retention_frames = 1 * 60
test_frames = 1.3 * 60
test_fix_frames = 2.3 * 60

## INITIAL COLOURS (DO NOT USE BECAUSE JS SUCKS!!!:
#clrs = {'RED':np.array([255,36,28]),
#       'GREEN':np.array([0, 248, 25]),
#       'BLUE':np.array([0, 145, 255]),
#       'YELLOW':np.array([255,251, 34]),
#       'CYAN':np.array([0, 255, 255]),
#       'PURPLE':np.array([255, 60, 255]),
#       'WHITE':np.array([250, 250, 250])}

## The _ is to differentiate these from builtin color vars.
#_RED = [1.0, -0.7176470588235294, -0.7803921568627451]
#_GREEN = [-1.0, 0.9450980392156862, -0.803921568627451]
#_BLUE = [-1.0, 0.13725490196078427, 1.0]
#_YELLOW = [1.0, 0.968627450980392, -0.7333333333333334]
#_CYAN = [-1.0, 1.0, 1.0]
#_PURPLE = [1.0, -0.5294117647058824, 1.0]
#_WHITE = [0.9607843137254901, 0.9607843137254901, 0.9607843137254901]
#_X = bgcol
#
#
#
## Seven colours plus a bacground blank colour (X). IF there's a change, the to-change slot's colour changes to the seventh.
#all_colours = {"RED":_RED, "GREEN":_GREEN, "BLUE":_BLUE, "YELLOW":_YELLOW, "CYAN":_CYAN, "PURPLE":_PURPLE, "WHITE":_WHITE, 'X':_X}

# Since these get set prior to reading in the file they need initializing
# ... they get updated on each trial so the X is just filler.

#study_clr1 = _X
#study_clr2 = _X
#study_clr3 = _X
#study_clr4 = _X
#study_clr5 = _X
#study_clr6 = _X
#
#test_clr1 = _X
#test_clr2 = _X
#test_clr3 = _X
#test_clr4 = _X
#test_clr5 = _X
#test_clr6 = _X
wm_instr_txt_2 = visual.TextStim(win=win, name='wm_instr_txt_2',
    text='You will see a circular array of coloured squares.\n\nThe colours will quickly disappear and then reappear after one second.\n\nWhen the colours reappear, they will either be identical or *one of the colours will have changed*.\n\nWhen they reappear, press [J] if there was a change, or press [D] if there was not a change.\n\nThis is fast, so respond as quickly and accurately as possible.\n\nPress [SPACE] to begin.',
    font='cambria',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
wm_start_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "wm_real_start"
wm_real_startClock = core.Clock()
wm_start_txt = visual.TextStim(win=win, name='wm_start_txt',
    text='You have finished the practice section. The next section is the same but your responses will be tracked.\n\nPress [SPACE] to begin the main section.',
    font='cambria',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color=basecol, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
buttons_reminder_wm = visual.TextStim(win=win, name='buttons_reminder_wm',
    text='',
    font='cambria',
    pos=(0, -0.2), height=0.035, wrapWidth=None, ori=0, 
    color=basecol, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
wm_start_resp_real = keyboard.Keyboard()

# Initialize components for Routine "wm_pre_fixation"
wm_pre_fixationClock = core.Clock()
wm_pre_fix = visual.TextStim(win=win, name='wm_pre_fix',
    text='+',
    font='cambria',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=basecol, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "wm_rest"
wm_restClock = core.Clock()
wm_rest_text = visual.TextStim(win=win, name='wm_rest_text',
    text='',
    font='cambria',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=basecol, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
wm_rest_resp = keyboard.Keyboard()

# Initialize components for Routine "wm_study"
wm_studyClock = core.Clock()
wm_study_fix = visual.TextStim(win=win, name='wm_study_fix',
    text='+',
    font='cambria',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
wm_loc1_study = visual.Rect(
    win=win, name='wm_loc1_study',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
wm_loc2_study = visual.Rect(
    win=win, name='wm_loc2_study',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-3.0, interpolate=True)
wm_loc3_study = visual.Rect(
    win=win, name='wm_loc3_study',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-4.0, interpolate=True)
wm_loc4_study = visual.Rect(
    win=win, name='wm_loc4_study',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-5.0, interpolate=True)
wm_loc5_study = visual.Rect(
    win=win, name='wm_loc5_study',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-6.0, interpolate=True)
wm_loc6_study = visual.Rect(
    win=win, name='wm_loc6_study',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "wm_retention"
wm_retentionClock = core.Clock()
wm_retention_fix = visual.TextStim(win=win, name='wm_retention_fix',
    text='+',
    font='cambria',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
wm_loc1_retention = visual.Rect(
    win=win, name='wm_loc1_retention',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-1.0, interpolate=True)
wm_loc2_retention = visual.Rect(
    win=win, name='wm_loc2_retention',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
wm_loc3_retention = visual.Rect(
    win=win, name='wm_loc3_retention',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-3.0, interpolate=True)
wm_loc4_retention = visual.Rect(
    win=win, name='wm_loc4_retention',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-4.0, interpolate=True)
wm_loc5_retention = visual.Rect(
    win=win, name='wm_loc5_retention',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-5.0, interpolate=True)
wm_loc6_retention = visual.Rect(
    win=win, name='wm_loc6_retention',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-6.0, interpolate=True)

# Initialize components for Routine "wm_test"
wm_testClock = core.Clock()
wm_test_fix = visual.TextStim(win=win, name='wm_test_fix',
    text='+',
    font='cambria',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
wm_loc1_test = visual.Rect(
    win=win, name='wm_loc1_test',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
wm_loc2_test = visual.Rect(
    win=win, name='wm_loc2_test',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-3.0, interpolate=True)
wm_loc3_test = visual.Rect(
    win=win, name='wm_loc3_test',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-4.0, interpolate=True)
wm_loc4_test = visual.Rect(
    win=win, name='wm_loc4_test',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-5.0, interpolate=True)
wm_loc5_test = visual.Rect(
    win=win, name='wm_loc5_test',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-6.0, interpolate=True)
wm_loc6_test = visual.Rect(
    win=win, name='wm_loc6_test',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-7.0, interpolate=True)
wm_resp = keyboard.Keyboard()
wm_test_fix_end = visual.TextStim(win=win, name='wm_test_fix_end',
    text='+',
    font='cambria',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "end_of_study"
end_of_studyClock = core.Clock()
end_study_text = visual.TextStim(win=win, name='end_study_text',
    text='END OF STUDY\n\nThank You!',
    font='cambria',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=basecol, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "wm_intro"-------
continueRoutine = True
# update component parameters for each repeat
wm_intro_txt.setColor(basecol, colorSpace='rgb')
wm_intro_resp.keys = []
wm_intro_resp.rt = []
_wm_intro_resp_allKeys = []
# keep track of which components have finished
wm_introComponents = [wm_intro_txt, wm_intro_resp]
for thisComponent in wm_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wm_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wm_intro"-------
while continueRoutine:
    # get current time
    t = wm_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wm_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wm_intro_txt* updates
    if wm_intro_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wm_intro_txt.frameNStart = frameN  # exact frame index
        wm_intro_txt.tStart = t  # local t and not account for scr refresh
        wm_intro_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wm_intro_txt, 'tStartRefresh')  # time at next scr refresh
        wm_intro_txt.setAutoDraw(True)
    
    # *wm_intro_resp* updates
    waitOnFlip = False
    if wm_intro_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wm_intro_resp.frameNStart = frameN  # exact frame index
        wm_intro_resp.tStart = t  # local t and not account for scr refresh
        wm_intro_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wm_intro_resp, 'tStartRefresh')  # time at next scr refresh
        wm_intro_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(wm_intro_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(wm_intro_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if wm_intro_resp.status == STARTED and not waitOnFlip:
        theseKeys = wm_intro_resp.getKeys(keyList=['space'], waitRelease=False)
        _wm_intro_resp_allKeys.extend(theseKeys)
        if len(_wm_intro_resp_allKeys):
            wm_intro_resp.keys = _wm_intro_resp_allKeys[-1].name  # just the last key pressed
            wm_intro_resp.rt = _wm_intro_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wm_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wm_intro"-------
for thisComponent in wm_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('wm_intro_txt.started', wm_intro_txt.tStartRefresh)
thisExp.addData('wm_intro_txt.stopped', wm_intro_txt.tStopRefresh)
# check responses
if wm_intro_resp.keys in ['', [], None]:  # No response was made
    wm_intro_resp.keys = None
thisExp.addData('wm_intro_resp.keys',wm_intro_resp.keys)
if wm_intro_resp.keys != None:  # we had a response
    thisExp.addData('wm_intro_resp.rt', wm_intro_resp.rt)
thisExp.addData('wm_intro_resp.started', wm_intro_resp.tStartRefresh)
thisExp.addData('wm_intro_resp.stopped', wm_intro_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "wm_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wm_instructions_1"-------
continueRoutine = True
# update component parameters for each repeat
wm_instr_txt_1.setColor(basecol, colorSpace='rgb')
wm_start_resp_1.keys = []
wm_start_resp_1.rt = []
_wm_start_resp_1_allKeys = []
# keep track of which components have finished
wm_instructions_1Components = [wm_instr_txt_1, wm_start_resp_1]
for thisComponent in wm_instructions_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wm_instructions_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wm_instructions_1"-------
while continueRoutine:
    # get current time
    t = wm_instructions_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wm_instructions_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if int(expInfo['version']) == 1:
        buttons_mapping = "D (change)\nJ (no change)"
        continueRoutine = True
        print("Version 1")
    else:
        buttons_mapping = "D (no change)\nJ (change)"
        continueRoutine = False
        print("Version 2")
    
    # *wm_instr_txt_1* updates
    if wm_instr_txt_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wm_instr_txt_1.frameNStart = frameN  # exact frame index
        wm_instr_txt_1.tStart = t  # local t and not account for scr refresh
        wm_instr_txt_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wm_instr_txt_1, 'tStartRefresh')  # time at next scr refresh
        wm_instr_txt_1.setAutoDraw(True)
    
    # *wm_start_resp_1* updates
    waitOnFlip = False
    if wm_start_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wm_start_resp_1.frameNStart = frameN  # exact frame index
        wm_start_resp_1.tStart = t  # local t and not account for scr refresh
        wm_start_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wm_start_resp_1, 'tStartRefresh')  # time at next scr refresh
        wm_start_resp_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(wm_start_resp_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(wm_start_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if wm_start_resp_1.status == STARTED and not waitOnFlip:
        theseKeys = wm_start_resp_1.getKeys(keyList=['space'], waitRelease=False)
        _wm_start_resp_1_allKeys.extend(theseKeys)
        if len(_wm_start_resp_1_allKeys):
            wm_start_resp_1.keys = _wm_start_resp_1_allKeys[-1].name  # just the last key pressed
            wm_start_resp_1.rt = _wm_start_resp_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wm_instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wm_instructions_1"-------
for thisComponent in wm_instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('wm_instr_txt_1.started', wm_instr_txt_1.tStartRefresh)
thisExp.addData('wm_instr_txt_1.stopped', wm_instr_txt_1.tStopRefresh)
# check responses
if wm_start_resp_1.keys in ['', [], None]:  # No response was made
    wm_start_resp_1.keys = None
thisExp.addData('wm_start_resp_1.keys',wm_start_resp_1.keys)
if wm_start_resp_1.keys != None:  # we had a response
    thisExp.addData('wm_start_resp_1.rt', wm_start_resp_1.rt)
thisExp.addData('wm_start_resp_1.started', wm_start_resp_1.tStartRefresh)
thisExp.addData('wm_start_resp_1.stopped', wm_start_resp_1.tStopRefresh)
thisExp.nextEntry()
# the Routine "wm_instructions_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wm_instructions_2"-------
continueRoutine = True
# update component parameters for each repeat
wm_instr_txt_2.setColor(basecol, colorSpace='rgb')
wm_start_resp_2.keys = []
wm_start_resp_2.rt = []
_wm_start_resp_2_allKeys = []
# keep track of which components have finished
wm_instructions_2Components = [wm_instr_txt_2, wm_start_resp_2]
for thisComponent in wm_instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wm_instructions_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wm_instructions_2"-------
while continueRoutine:
    # get current time
    t = wm_instructions_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wm_instructions_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if int(expInfo['version']) == 2:
        buttons_mapping = "D (no change)\nJ (change)"
        continueRoutine = True
        print("Version 2")
    else:
        buttons_mapping = "D (change)\nJ (no change)"
        continueRoutine = False
        print("Version 1")
        
    
    # *wm_instr_txt_2* updates
    if wm_instr_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wm_instr_txt_2.frameNStart = frameN  # exact frame index
        wm_instr_txt_2.tStart = t  # local t and not account for scr refresh
        wm_instr_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wm_instr_txt_2, 'tStartRefresh')  # time at next scr refresh
        wm_instr_txt_2.setAutoDraw(True)
    
    # *wm_start_resp_2* updates
    waitOnFlip = False
    if wm_start_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wm_start_resp_2.frameNStart = frameN  # exact frame index
        wm_start_resp_2.tStart = t  # local t and not account for scr refresh
        wm_start_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wm_start_resp_2, 'tStartRefresh')  # time at next scr refresh
        wm_start_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(wm_start_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(wm_start_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if wm_start_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = wm_start_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _wm_start_resp_2_allKeys.extend(theseKeys)
        if len(_wm_start_resp_2_allKeys):
            wm_start_resp_2.keys = _wm_start_resp_2_allKeys[-1].name  # just the last key pressed
            wm_start_resp_2.rt = _wm_start_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wm_instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wm_instructions_2"-------
for thisComponent in wm_instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('wm_instr_txt_2.started', wm_instr_txt_2.tStartRefresh)
thisExp.addData('wm_instr_txt_2.stopped', wm_instr_txt_2.tStopRefresh)
# check responses
if wm_start_resp_2.keys in ['', [], None]:  # No response was made
    wm_start_resp_2.keys = None
thisExp.addData('wm_start_resp_2.keys',wm_start_resp_2.keys)
if wm_start_resp_2.keys != None:  # we had a response
    thisExp.addData('wm_start_resp_2.rt', wm_start_resp_2.rt)
thisExp.addData('wm_start_resp_2.started', wm_start_resp_2.tStartRefresh)
thisExp.addData('wm_start_resp_2.stopped', wm_start_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "wm_instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
wm_runs = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("protocol/wm_main_" + exp_version + ".xlsx"),
    seed=None, name='wm_runs')
thisExp.addLoop(wm_runs)  # add the loop to the experiment
thisWm_run = wm_runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWm_run.rgb)
if thisWm_run != None:
    for paramName in thisWm_run:
        exec('{} = thisWm_run[paramName]'.format(paramName))

for thisWm_run in wm_runs:
    currentLoop = wm_runs
    # abbreviate parameter names if possible (e.g. rgb = thisWm_run.rgb)
    if thisWm_run != None:
        for paramName in thisWm_run:
            exec('{} = thisWm_run[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "wm_real_start"-------
    continueRoutine = True
    # update component parameters for each repeat
    # RESTART THE TRIAL COUNTER
    TRIAL_N = 0
    
    
    buttons_reminder_wm.setText(buttons_mapping)
    wm_start_resp_real.keys = []
    wm_start_resp_real.rt = []
    _wm_start_resp_real_allKeys = []
    # keep track of which components have finished
    wm_real_startComponents = [wm_start_txt, buttons_reminder_wm, wm_start_resp_real]
    for thisComponent in wm_real_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wm_real_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wm_real_start"-------
    while continueRoutine:
        # get current time
        t = wm_real_startClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wm_real_startClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if 'practice' in wm_file:
            continueRoutine = False
        else:
            continueRoutine = True
        
        
        # *wm_start_txt* updates
        if wm_start_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_start_txt.frameNStart = frameN  # exact frame index
            wm_start_txt.tStart = t  # local t and not account for scr refresh
            wm_start_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_start_txt, 'tStartRefresh')  # time at next scr refresh
            wm_start_txt.setAutoDraw(True)
        
        # *buttons_reminder_wm* updates
        if buttons_reminder_wm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttons_reminder_wm.frameNStart = frameN  # exact frame index
            buttons_reminder_wm.tStart = t  # local t and not account for scr refresh
            buttons_reminder_wm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttons_reminder_wm, 'tStartRefresh')  # time at next scr refresh
            buttons_reminder_wm.setAutoDraw(True)
        
        # *wm_start_resp_real* updates
        waitOnFlip = False
        if wm_start_resp_real.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_start_resp_real.frameNStart = frameN  # exact frame index
            wm_start_resp_real.tStart = t  # local t and not account for scr refresh
            wm_start_resp_real.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_start_resp_real, 'tStartRefresh')  # time at next scr refresh
            wm_start_resp_real.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(wm_start_resp_real.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(wm_start_resp_real.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if wm_start_resp_real.status == STARTED and not waitOnFlip:
            theseKeys = wm_start_resp_real.getKeys(keyList=['space'], waitRelease=False)
            _wm_start_resp_real_allKeys.extend(theseKeys)
            if len(_wm_start_resp_real_allKeys):
                wm_start_resp_real.keys = _wm_start_resp_real_allKeys[-1].name  # just the last key pressed
                wm_start_resp_real.rt = _wm_start_resp_real_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wm_real_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wm_real_start"-------
    for thisComponent in wm_real_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    wm_runs.addData('wm_start_txt.started', wm_start_txt.tStartRefresh)
    wm_runs.addData('wm_start_txt.stopped', wm_start_txt.tStopRefresh)
    wm_runs.addData('buttons_reminder_wm.started', buttons_reminder_wm.tStartRefresh)
    wm_runs.addData('buttons_reminder_wm.stopped', buttons_reminder_wm.tStopRefresh)
    # check responses
    if wm_start_resp_real.keys in ['', [], None]:  # No response was made
        wm_start_resp_real.keys = None
    wm_runs.addData('wm_start_resp_real.keys',wm_start_resp_real.keys)
    if wm_start_resp_real.keys != None:  # we had a response
        wm_runs.addData('wm_start_resp_real.rt', wm_start_resp_real.rt)
    wm_runs.addData('wm_start_resp_real.started', wm_start_resp_real.tStartRefresh)
    wm_runs.addData('wm_start_resp_real.stopped', wm_start_resp_real.tStopRefresh)
    # the Routine "wm_real_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "wm_pre_fixation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    wm_pre_fixationComponents = [wm_pre_fix]
    for thisComponent in wm_pre_fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wm_pre_fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wm_pre_fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = wm_pre_fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wm_pre_fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wm_pre_fix* updates
        if wm_pre_fix.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            wm_pre_fix.frameNStart = frameN  # exact frame index
            wm_pre_fix.tStart = t  # local t and not account for scr refresh
            wm_pre_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_pre_fix, 'tStartRefresh')  # time at next scr refresh
            wm_pre_fix.setAutoDraw(True)
        if wm_pre_fix.status == STARTED:
            if frameN >= (wm_pre_fix.frameNStart + 60):
                # keep track of stop time/frame for later
                wm_pre_fix.tStop = t  # not accounting for scr refresh
                wm_pre_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_pre_fix, 'tStopRefresh')  # time at next scr refresh
                wm_pre_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wm_pre_fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wm_pre_fixation"-------
    for thisComponent in wm_pre_fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    wm_runs.addData('wm_pre_fix.started', wm_pre_fix.tStartRefresh)
    wm_runs.addData('wm_pre_fix.stopped', wm_pre_fix.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    wm_trials = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("protocol/" + wm_file),
        seed=None, name='wm_trials')
    thisExp.addLoop(wm_trials)  # add the loop to the experiment
    thisWm_trial = wm_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWm_trial.rgb)
    if thisWm_trial != None:
        for paramName in thisWm_trial:
            exec('{} = thisWm_trial[paramName]'.format(paramName))
    
    for thisWm_trial in wm_trials:
        currentLoop = wm_trials
        # abbreviate parameter names if possible (e.g. rgb = thisWm_trial.rgb)
        if thisWm_trial != None:
            for paramName in thisWm_trial:
                exec('{} = thisWm_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "wm_rest"-------
        continueRoutine = True
        # update component parameters for each repeat
        n_wm_trials = len(wm_trials.trialList) * wm_trials.nReps
        
        print("N wm trials: ", n_wm_trials)
        
        print(wm_trials.thisTrialN)
        print("TRIAL_N = ", TRIAL_N)
        wm_rest_text.setText(wm_rest_msg)
        wm_rest_resp.keys = []
        wm_rest_resp.rt = []
        _wm_rest_resp_allKeys = []
        # keep track of which components have finished
        wm_restComponents = [wm_rest_text, wm_rest_resp]
        for thisComponent in wm_restComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        wm_restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "wm_rest"-------
        while continueRoutine:
            # get current time
            t = wm_restClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=wm_restClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            wm_rest_msg = "Completed " + str(TRIAL_N+1) + " of " + str(n_wm_trials) + " trials.\n\nPress [SPACE] to continue..."
            
            if (TRIAL_N > 0) and (TRIAL_N % (n_wm_trials / 3) == 0):
                print("Break time")
                print(wm_rest_msg)
                continueRoutine = True
            else:
                print("Not break time")
            
                continueRoutine = False
            
            
            # *wm_rest_text* updates
            if wm_rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_rest_text.frameNStart = frameN  # exact frame index
                wm_rest_text.tStart = t  # local t and not account for scr refresh
                wm_rest_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_rest_text, 'tStartRefresh')  # time at next scr refresh
                wm_rest_text.setAutoDraw(True)
            
            # *wm_rest_resp* updates
            waitOnFlip = False
            if wm_rest_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_rest_resp.frameNStart = frameN  # exact frame index
                wm_rest_resp.tStart = t  # local t and not account for scr refresh
                wm_rest_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_rest_resp, 'tStartRefresh')  # time at next scr refresh
                wm_rest_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(wm_rest_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(wm_rest_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if wm_rest_resp.status == STARTED and not waitOnFlip:
                theseKeys = wm_rest_resp.getKeys(keyList=['space'], waitRelease=False)
                _wm_rest_resp_allKeys.extend(theseKeys)
                if len(_wm_rest_resp_allKeys):
                    wm_rest_resp.keys = _wm_rest_resp_allKeys[-1].name  # just the last key pressed
                    wm_rest_resp.rt = _wm_rest_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wm_restComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "wm_rest"-------
        for thisComponent in wm_restComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if wm_rest_resp.keys in ['', [], None]:  # No response was made
            wm_rest_resp.keys = None
        wm_trials.addData('wm_rest_resp.keys',wm_rest_resp.keys)
        if wm_rest_resp.keys != None:  # we had a response
            wm_trials.addData('wm_rest_resp.rt', wm_rest_resp.rt)
        # the Routine "wm_rest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "wm_study"-------
        continueRoutine = True
        # update component parameters for each repeat
        wm_study_fix.setColor(basecol, colorSpace='rgb')
        wm_loc1_study.setFillColor(study_clr1)
        wm_loc1_study.setPos((rad*cos(0), rad*sin(0)))
        wm_loc1_study.setSize(box_size)
        wm_loc1_study.setLineColor(basecol)
        wm_loc2_study.setFillColor(study_clr2)
        wm_loc2_study.setPos((rad*cos(45), -rad*sin(45)))
        wm_loc2_study.setSize(box_size)
        wm_loc2_study.setLineColor(basecol)
        wm_loc3_study.setFillColor(study_clr3)
        wm_loc3_study.setPos((-rad*cos(45), -rad*sin(45)))
        wm_loc3_study.setSize(box_size)
        wm_loc3_study.setLineColor(basecol)
        wm_loc4_study.setFillColor(study_clr4)
        wm_loc4_study.setPos((-rad*cos(0), rad*sin(0)))
        wm_loc4_study.setSize(box_size)
        wm_loc4_study.setLineColor(basecol)
        wm_loc5_study.setFillColor(study_clr5)
        wm_loc5_study.setPos((-rad*cos(45), rad*sin(45)))
        wm_loc5_study.setSize(box_size)
        wm_loc5_study.setLineColor(basecol)
        wm_loc6_study.setFillColor(study_clr6)
        wm_loc6_study.setPos((rad*cos(45), rad*sin(45)))
        wm_loc6_study.setSize(box_size)
        wm_loc6_study.setLineColor(basecol)
        # keep track of which components have finished
        wm_studyComponents = [wm_study_fix, wm_loc1_study, wm_loc2_study, wm_loc3_study, wm_loc4_study, wm_loc5_study, wm_loc6_study]
        for thisComponent in wm_studyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        wm_studyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "wm_study"-------
        while continueRoutine:
            # get current time
            t = wm_studyClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=wm_studyClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wm_study_fix* updates
            if wm_study_fix.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_study_fix.frameNStart = frameN  # exact frame index
                wm_study_fix.tStart = t  # local t and not account for scr refresh
                wm_study_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_study_fix, 'tStartRefresh')  # time at next scr refresh
                wm_study_fix.setAutoDraw(True)
            if wm_study_fix.status == STARTED:
                if frameN >= (wm_study_fix.frameNStart + study_frames):
                    # keep track of stop time/frame for later
                    wm_study_fix.tStop = t  # not accounting for scr refresh
                    wm_study_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_study_fix, 'tStopRefresh')  # time at next scr refresh
                    wm_study_fix.setAutoDraw(False)
            
            # *wm_loc1_study* updates
            if wm_loc1_study.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc1_study.frameNStart = frameN  # exact frame index
                wm_loc1_study.tStart = t  # local t and not account for scr refresh
                wm_loc1_study.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc1_study, 'tStartRefresh')  # time at next scr refresh
                wm_loc1_study.setAutoDraw(True)
            if wm_loc1_study.status == STARTED:
                if frameN >= (wm_loc1_study.frameNStart + study_frames):
                    # keep track of stop time/frame for later
                    wm_loc1_study.tStop = t  # not accounting for scr refresh
                    wm_loc1_study.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc1_study, 'tStopRefresh')  # time at next scr refresh
                    wm_loc1_study.setAutoDraw(False)
            
            # *wm_loc2_study* updates
            if wm_loc2_study.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc2_study.frameNStart = frameN  # exact frame index
                wm_loc2_study.tStart = t  # local t and not account for scr refresh
                wm_loc2_study.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc2_study, 'tStartRefresh')  # time at next scr refresh
                wm_loc2_study.setAutoDraw(True)
            if wm_loc2_study.status == STARTED:
                if frameN >= (wm_loc2_study.frameNStart + study_frames):
                    # keep track of stop time/frame for later
                    wm_loc2_study.tStop = t  # not accounting for scr refresh
                    wm_loc2_study.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc2_study, 'tStopRefresh')  # time at next scr refresh
                    wm_loc2_study.setAutoDraw(False)
            
            # *wm_loc3_study* updates
            if wm_loc3_study.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc3_study.frameNStart = frameN  # exact frame index
                wm_loc3_study.tStart = t  # local t and not account for scr refresh
                wm_loc3_study.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc3_study, 'tStartRefresh')  # time at next scr refresh
                wm_loc3_study.setAutoDraw(True)
            if wm_loc3_study.status == STARTED:
                if frameN >= (wm_loc3_study.frameNStart + study_frames):
                    # keep track of stop time/frame for later
                    wm_loc3_study.tStop = t  # not accounting for scr refresh
                    wm_loc3_study.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc3_study, 'tStopRefresh')  # time at next scr refresh
                    wm_loc3_study.setAutoDraw(False)
            
            # *wm_loc4_study* updates
            if wm_loc4_study.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc4_study.frameNStart = frameN  # exact frame index
                wm_loc4_study.tStart = t  # local t and not account for scr refresh
                wm_loc4_study.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc4_study, 'tStartRefresh')  # time at next scr refresh
                wm_loc4_study.setAutoDraw(True)
            if wm_loc4_study.status == STARTED:
                if frameN >= (wm_loc4_study.frameNStart + study_frames):
                    # keep track of stop time/frame for later
                    wm_loc4_study.tStop = t  # not accounting for scr refresh
                    wm_loc4_study.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc4_study, 'tStopRefresh')  # time at next scr refresh
                    wm_loc4_study.setAutoDraw(False)
            
            # *wm_loc5_study* updates
            if wm_loc5_study.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc5_study.frameNStart = frameN  # exact frame index
                wm_loc5_study.tStart = t  # local t and not account for scr refresh
                wm_loc5_study.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc5_study, 'tStartRefresh')  # time at next scr refresh
                wm_loc5_study.setAutoDraw(True)
            if wm_loc5_study.status == STARTED:
                if frameN >= (wm_loc5_study.frameNStart + study_frames):
                    # keep track of stop time/frame for later
                    wm_loc5_study.tStop = t  # not accounting for scr refresh
                    wm_loc5_study.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc5_study, 'tStopRefresh')  # time at next scr refresh
                    wm_loc5_study.setAutoDraw(False)
            
            # *wm_loc6_study* updates
            if wm_loc6_study.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc6_study.frameNStart = frameN  # exact frame index
                wm_loc6_study.tStart = t  # local t and not account for scr refresh
                wm_loc6_study.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc6_study, 'tStartRefresh')  # time at next scr refresh
                wm_loc6_study.setAutoDraw(True)
            if wm_loc6_study.status == STARTED:
                if frameN >= (wm_loc6_study.frameNStart + study_frames):
                    # keep track of stop time/frame for later
                    wm_loc6_study.tStop = t  # not accounting for scr refresh
                    wm_loc6_study.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc6_study, 'tStopRefresh')  # time at next scr refresh
                    wm_loc6_study.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wm_studyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "wm_study"-------
        for thisComponent in wm_studyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        wm_trials.addData('wm_study_fix.started', wm_study_fix.tStartRefresh)
        wm_trials.addData('wm_study_fix.stopped', wm_study_fix.tStopRefresh)
        # the Routine "wm_study" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "wm_retention"-------
        continueRoutine = True
        # update component parameters for each repeat
        wm_retention_fix.setColor(basecol, colorSpace='rgb')
        wm_loc1_retention.setFillColor(bgcol)
        wm_loc1_retention.setPos((rad*cos(0), rad*sin(0)))
        wm_loc1_retention.setSize(box_size)
        wm_loc1_retention.setLineColor(basecol)
        wm_loc2_retention.setFillColor(bgcol)
        wm_loc2_retention.setPos((rad*cos(45), -rad*sin(45)))
        wm_loc2_retention.setSize(box_size)
        wm_loc2_retention.setLineColor(basecol)
        wm_loc3_retention.setFillColor(bgcol)
        wm_loc3_retention.setPos((-rad*cos(45), -rad*sin(45)))
        wm_loc3_retention.setSize(box_size)
        wm_loc3_retention.setLineColor(basecol)
        wm_loc4_retention.setFillColor(bgcol)
        wm_loc4_retention.setPos((-rad*cos(0), rad*sin(0)))
        wm_loc4_retention.setSize(box_size)
        wm_loc4_retention.setLineColor(basecol)
        wm_loc5_retention.setFillColor(bgcol)
        wm_loc5_retention.setPos((-rad*cos(45), rad*sin(45)))
        wm_loc5_retention.setSize(box_size)
        wm_loc5_retention.setLineColor(basecol)
        wm_loc6_retention.setFillColor(bgcol)
        wm_loc6_retention.setPos((rad*cos(45), rad*sin(45)))
        wm_loc6_retention.setSize(box_size)
        wm_loc6_retention.setLineColor(basecol)
        # keep track of which components have finished
        wm_retentionComponents = [wm_retention_fix, wm_loc1_retention, wm_loc2_retention, wm_loc3_retention, wm_loc4_retention, wm_loc5_retention, wm_loc6_retention]
        for thisComponent in wm_retentionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        wm_retentionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "wm_retention"-------
        while continueRoutine:
            # get current time
            t = wm_retentionClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=wm_retentionClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wm_retention_fix* updates
            if wm_retention_fix.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                wm_retention_fix.frameNStart = frameN  # exact frame index
                wm_retention_fix.tStart = t  # local t and not account for scr refresh
                wm_retention_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_retention_fix, 'tStartRefresh')  # time at next scr refresh
                wm_retention_fix.setAutoDraw(True)
            if wm_retention_fix.status == STARTED:
                if frameN >= (wm_retention_fix.frameNStart + retention_frames):
                    # keep track of stop time/frame for later
                    wm_retention_fix.tStop = t  # not accounting for scr refresh
                    wm_retention_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_retention_fix, 'tStopRefresh')  # time at next scr refresh
                    wm_retention_fix.setAutoDraw(False)
            
            # *wm_loc1_retention* updates
            if wm_loc1_retention.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc1_retention.frameNStart = frameN  # exact frame index
                wm_loc1_retention.tStart = t  # local t and not account for scr refresh
                wm_loc1_retention.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc1_retention, 'tStartRefresh')  # time at next scr refresh
                wm_loc1_retention.setAutoDraw(True)
            if wm_loc1_retention.status == STARTED:
                if frameN >= (wm_loc1_retention.frameNStart + retention_frames):
                    # keep track of stop time/frame for later
                    wm_loc1_retention.tStop = t  # not accounting for scr refresh
                    wm_loc1_retention.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc1_retention, 'tStopRefresh')  # time at next scr refresh
                    wm_loc1_retention.setAutoDraw(False)
            
            # *wm_loc2_retention* updates
            if wm_loc2_retention.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                wm_loc2_retention.frameNStart = frameN  # exact frame index
                wm_loc2_retention.tStart = t  # local t and not account for scr refresh
                wm_loc2_retention.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc2_retention, 'tStartRefresh')  # time at next scr refresh
                wm_loc2_retention.setAutoDraw(True)
            if wm_loc2_retention.status == STARTED:
                if frameN >= (wm_loc2_retention.frameNStart + retention_frames):
                    # keep track of stop time/frame for later
                    wm_loc2_retention.tStop = t  # not accounting for scr refresh
                    wm_loc2_retention.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc2_retention, 'tStopRefresh')  # time at next scr refresh
                    wm_loc2_retention.setAutoDraw(False)
            
            # *wm_loc3_retention* updates
            if wm_loc3_retention.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc3_retention.frameNStart = frameN  # exact frame index
                wm_loc3_retention.tStart = t  # local t and not account for scr refresh
                wm_loc3_retention.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc3_retention, 'tStartRefresh')  # time at next scr refresh
                wm_loc3_retention.setAutoDraw(True)
            if wm_loc3_retention.status == STARTED:
                if frameN >= (wm_loc3_retention.frameNStart + retention_frames):
                    # keep track of stop time/frame for later
                    wm_loc3_retention.tStop = t  # not accounting for scr refresh
                    wm_loc3_retention.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc3_retention, 'tStopRefresh')  # time at next scr refresh
                    wm_loc3_retention.setAutoDraw(False)
            
            # *wm_loc4_retention* updates
            if wm_loc4_retention.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc4_retention.frameNStart = frameN  # exact frame index
                wm_loc4_retention.tStart = t  # local t and not account for scr refresh
                wm_loc4_retention.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc4_retention, 'tStartRefresh')  # time at next scr refresh
                wm_loc4_retention.setAutoDraw(True)
            if wm_loc4_retention.status == STARTED:
                if frameN >= (wm_loc4_retention.frameNStart + retention_frames):
                    # keep track of stop time/frame for later
                    wm_loc4_retention.tStop = t  # not accounting for scr refresh
                    wm_loc4_retention.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc4_retention, 'tStopRefresh')  # time at next scr refresh
                    wm_loc4_retention.setAutoDraw(False)
            
            # *wm_loc5_retention* updates
            if wm_loc5_retention.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc5_retention.frameNStart = frameN  # exact frame index
                wm_loc5_retention.tStart = t  # local t and not account for scr refresh
                wm_loc5_retention.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc5_retention, 'tStartRefresh')  # time at next scr refresh
                wm_loc5_retention.setAutoDraw(True)
            if wm_loc5_retention.status == STARTED:
                if frameN >= (wm_loc5_retention.frameNStart + retention_frames):
                    # keep track of stop time/frame for later
                    wm_loc5_retention.tStop = t  # not accounting for scr refresh
                    wm_loc5_retention.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc5_retention, 'tStopRefresh')  # time at next scr refresh
                    wm_loc5_retention.setAutoDraw(False)
            
            # *wm_loc6_retention* updates
            if wm_loc6_retention.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc6_retention.frameNStart = frameN  # exact frame index
                wm_loc6_retention.tStart = t  # local t and not account for scr refresh
                wm_loc6_retention.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc6_retention, 'tStartRefresh')  # time at next scr refresh
                wm_loc6_retention.setAutoDraw(True)
            if wm_loc6_retention.status == STARTED:
                if frameN >= (wm_loc6_retention.frameNStart + retention_frames):
                    # keep track of stop time/frame for later
                    wm_loc6_retention.tStop = t  # not accounting for scr refresh
                    wm_loc6_retention.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc6_retention, 'tStopRefresh')  # time at next scr refresh
                    wm_loc6_retention.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wm_retentionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "wm_retention"-------
        for thisComponent in wm_retentionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        wm_trials.addData('wm_retention_fix.started', wm_retention_fix.tStartRefresh)
        wm_trials.addData('wm_retention_fix.stopped', wm_retention_fix.tStopRefresh)
        # the Routine "wm_retention" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "wm_test"-------
        continueRoutine = True
        # update component parameters for each repeat
        wm_test_fix.setColor(basecol, colorSpace='rgb')
        wm_loc1_test.setFillColor(test_clr1)
        wm_loc1_test.setPos((rad*cos(0), rad*sin(0)))
        wm_loc1_test.setSize(box_size)
        wm_loc1_test.setLineColor(basecol)
        wm_loc2_test.setFillColor(test_clr2)
        wm_loc2_test.setPos((rad*cos(45), -rad*sin(45)))
        wm_loc2_test.setSize(box_size)
        wm_loc2_test.setLineColor(basecol)
        wm_loc3_test.setFillColor(test_clr3)
        wm_loc3_test.setPos((-rad*cos(45), -rad*sin(45)))
        wm_loc3_test.setSize(box_size)
        wm_loc3_test.setLineColor(basecol)
        wm_loc4_test.setFillColor(test_clr4)
        wm_loc4_test.setPos((-rad*cos(0), rad*sin(0)))
        wm_loc4_test.setSize(box_size)
        wm_loc4_test.setLineColor(basecol)
        wm_loc5_test.setFillColor(test_clr5)
        wm_loc5_test.setPos((-rad*cos(45), rad*sin(45)))
        wm_loc5_test.setSize(box_size)
        wm_loc5_test.setLineColor(basecol)
        wm_loc6_test.setFillColor(test_clr6)
        wm_loc6_test.setPos((rad*cos(45), rad*sin(45)))
        wm_loc6_test.setSize(box_size)
        wm_loc6_test.setLineColor(basecol)
        wm_resp.keys = []
        wm_resp.rt = []
        _wm_resp_allKeys = []
        wm_test_fix_end.setColor(basecol, colorSpace='rgb')
        # keep track of which components have finished
        wm_testComponents = [wm_test_fix, wm_loc1_test, wm_loc2_test, wm_loc3_test, wm_loc4_test, wm_loc5_test, wm_loc6_test, wm_resp, wm_test_fix_end]
        for thisComponent in wm_testComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        wm_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "wm_test"-------
        while continueRoutine:
            # get current time
            t = wm_testClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=wm_testClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wm_test_fix* updates
            if wm_test_fix.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                wm_test_fix.frameNStart = frameN  # exact frame index
                wm_test_fix.tStart = t  # local t and not account for scr refresh
                wm_test_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_test_fix, 'tStartRefresh')  # time at next scr refresh
                wm_test_fix.setAutoDraw(True)
            if wm_test_fix.status == STARTED:
                if frameN >= (wm_test_fix.frameNStart + test_frames):
                    # keep track of stop time/frame for later
                    wm_test_fix.tStop = t  # not accounting for scr refresh
                    wm_test_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_test_fix, 'tStopRefresh')  # time at next scr refresh
                    wm_test_fix.setAutoDraw(False)
            
            # *wm_loc1_test* updates
            if wm_loc1_test.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc1_test.frameNStart = frameN  # exact frame index
                wm_loc1_test.tStart = t  # local t and not account for scr refresh
                wm_loc1_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc1_test, 'tStartRefresh')  # time at next scr refresh
                wm_loc1_test.setAutoDraw(True)
            if wm_loc1_test.status == STARTED:
                if frameN >= (wm_loc1_test.frameNStart + test_frames):
                    # keep track of stop time/frame for later
                    wm_loc1_test.tStop = t  # not accounting for scr refresh
                    wm_loc1_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc1_test, 'tStopRefresh')  # time at next scr refresh
                    wm_loc1_test.setAutoDraw(False)
            
            # *wm_loc2_test* updates
            if wm_loc2_test.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc2_test.frameNStart = frameN  # exact frame index
                wm_loc2_test.tStart = t  # local t and not account for scr refresh
                wm_loc2_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc2_test, 'tStartRefresh')  # time at next scr refresh
                wm_loc2_test.setAutoDraw(True)
            if wm_loc2_test.status == STARTED:
                if frameN >= (wm_loc2_test.frameNStart + test_frames):
                    # keep track of stop time/frame for later
                    wm_loc2_test.tStop = t  # not accounting for scr refresh
                    wm_loc2_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc2_test, 'tStopRefresh')  # time at next scr refresh
                    wm_loc2_test.setAutoDraw(False)
            
            # *wm_loc3_test* updates
            if wm_loc3_test.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc3_test.frameNStart = frameN  # exact frame index
                wm_loc3_test.tStart = t  # local t and not account for scr refresh
                wm_loc3_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc3_test, 'tStartRefresh')  # time at next scr refresh
                wm_loc3_test.setAutoDraw(True)
            if wm_loc3_test.status == STARTED:
                if frameN >= (wm_loc3_test.frameNStart + test_frames):
                    # keep track of stop time/frame for later
                    wm_loc3_test.tStop = t  # not accounting for scr refresh
                    wm_loc3_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc3_test, 'tStopRefresh')  # time at next scr refresh
                    wm_loc3_test.setAutoDraw(False)
            
            # *wm_loc4_test* updates
            if wm_loc4_test.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc4_test.frameNStart = frameN  # exact frame index
                wm_loc4_test.tStart = t  # local t and not account for scr refresh
                wm_loc4_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc4_test, 'tStartRefresh')  # time at next scr refresh
                wm_loc4_test.setAutoDraw(True)
            if wm_loc4_test.status == STARTED:
                if frameN >= (wm_loc4_test.frameNStart + test_frames):
                    # keep track of stop time/frame for later
                    wm_loc4_test.tStop = t  # not accounting for scr refresh
                    wm_loc4_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc4_test, 'tStopRefresh')  # time at next scr refresh
                    wm_loc4_test.setAutoDraw(False)
            
            # *wm_loc5_test* updates
            if wm_loc5_test.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc5_test.frameNStart = frameN  # exact frame index
                wm_loc5_test.tStart = t  # local t and not account for scr refresh
                wm_loc5_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc5_test, 'tStartRefresh')  # time at next scr refresh
                wm_loc5_test.setAutoDraw(True)
            if wm_loc5_test.status == STARTED:
                if frameN >= (wm_loc5_test.frameNStart + test_frames):
                    # keep track of stop time/frame for later
                    wm_loc5_test.tStop = t  # not accounting for scr refresh
                    wm_loc5_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc5_test, 'tStopRefresh')  # time at next scr refresh
                    wm_loc5_test.setAutoDraw(False)
            
            # *wm_loc6_test* updates
            if wm_loc6_test.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                wm_loc6_test.frameNStart = frameN  # exact frame index
                wm_loc6_test.tStart = t  # local t and not account for scr refresh
                wm_loc6_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_loc6_test, 'tStartRefresh')  # time at next scr refresh
                wm_loc6_test.setAutoDraw(True)
            if wm_loc6_test.status == STARTED:
                if frameN >= (wm_loc6_test.frameNStart + test_frames):
                    # keep track of stop time/frame for later
                    wm_loc6_test.tStop = t  # not accounting for scr refresh
                    wm_loc6_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_loc6_test, 'tStopRefresh')  # time at next scr refresh
                    wm_loc6_test.setAutoDraw(False)
            
            # *wm_resp* updates
            waitOnFlip = False
            if wm_resp.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                wm_resp.frameNStart = frameN  # exact frame index
                wm_resp.tStart = t  # local t and not account for scr refresh
                wm_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_resp, 'tStartRefresh')  # time at next scr refresh
                wm_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(wm_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(wm_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if wm_resp.status == STARTED:
                if frameN >= (wm_resp.frameNStart + test_frames*2):
                    # keep track of stop time/frame for later
                    wm_resp.tStop = t  # not accounting for scr refresh
                    wm_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_resp, 'tStopRefresh')  # time at next scr refresh
                    wm_resp.status = FINISHED
            if wm_resp.status == STARTED and not waitOnFlip:
                theseKeys = wm_resp.getKeys(keyList=['d', 'j'], waitRelease=False)
                _wm_resp_allKeys.extend(theseKeys)
                if len(_wm_resp_allKeys):
                    wm_resp.keys = _wm_resp_allKeys[-1].name  # just the last key pressed
                    wm_resp.rt = _wm_resp_allKeys[-1].rt
            
            # *wm_test_fix_end* updates
            if wm_test_fix_end.status == NOT_STARTED and frameN >= test_frames:
                # keep track of start time/frame for later
                wm_test_fix_end.frameNStart = frameN  # exact frame index
                wm_test_fix_end.tStart = t  # local t and not account for scr refresh
                wm_test_fix_end.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_test_fix_end, 'tStartRefresh')  # time at next scr refresh
                wm_test_fix_end.setAutoDraw(True)
            if wm_test_fix_end.status == STARTED:
                if frameN >= (wm_test_fix_end.frameNStart + test_frames):
                    # keep track of stop time/frame for later
                    wm_test_fix_end.tStop = t  # not accounting for scr refresh
                    wm_test_fix_end.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_test_fix_end, 'tStopRefresh')  # time at next scr refresh
                    wm_test_fix_end.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wm_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "wm_test"-------
        for thisComponent in wm_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TRIAL_N = TRIAL_N + 1
        wm_trials.addData('wm_test_fix.started', wm_test_fix.tStartRefresh)
        wm_trials.addData('wm_test_fix.stopped', wm_test_fix.tStopRefresh)
        # check responses
        if wm_resp.keys in ['', [], None]:  # No response was made
            wm_resp.keys = None
        wm_trials.addData('wm_resp.keys',wm_resp.keys)
        if wm_resp.keys != None:  # we had a response
            wm_trials.addData('wm_resp.rt', wm_resp.rt)
        wm_trials.addData('wm_resp.started', wm_resp.tStartRefresh)
        wm_trials.addData('wm_resp.stopped', wm_resp.tStopRefresh)
        wm_trials.addData('wm_test_fix_end.started', wm_test_fix_end.tStartRefresh)
        wm_trials.addData('wm_test_fix_end.stopped', wm_test_fix_end.tStopRefresh)
        # the Routine "wm_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2 repeats of 'wm_trials'
    
# completed 1 repeats of 'wm_runs'


# ------Prepare to start Routine "end_of_study"-------
continueRoutine = True
routineTimer.add(2.500000)
# update component parameters for each repeat
# keep track of which components have finished
end_of_studyComponents = [end_study_text]
for thisComponent in end_of_studyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_of_studyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_of_study"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_of_studyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_of_studyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_study_text* updates
    if end_study_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_study_text.frameNStart = frameN  # exact frame index
        end_study_text.tStart = t  # local t and not account for scr refresh
        end_study_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_study_text, 'tStartRefresh')  # time at next scr refresh
        end_study_text.setAutoDraw(True)
    if end_study_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_study_text.tStartRefresh + 2.5-frameTolerance:
            # keep track of stop time/frame for later
            end_study_text.tStop = t  # not accounting for scr refresh
            end_study_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_study_text, 'tStopRefresh')  # time at next scr refresh
            end_study_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_of_studyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_of_study"-------
for thisComponent in end_of_studyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_study_text.started', end_study_text.tStartRefresh)
thisExp.addData('end_study_text.stopped', end_study_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
