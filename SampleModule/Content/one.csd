<CsoundSynthesizer>
<CsOptions>
-n -d 
</CsOptions>
<CsInstruments>
sr = 44100
ksmps = 64
nchnls = 2
0dbfs = 1

;sound "pianoMood.wav"
;sound "DutchLadyTalking.ogg"
;instr "NOISE"

instr PLAY_FILE
    SFilename strcpy p4
    iLength = filelen(SFilename)
    iChannels = filenchnls(SFilename)
    p3 = iLength
    if active("PLAY_FILE") == 1 then
        prints "Still active instance performing..."
        if iChannels == 2 then
            a1, a2 diskin2 SFilename, 1, 0, 0
            outs a1, a2
        else
            a1 diskin2 SFilename, 1, 0, 0
            outs a1, a1
        endif
    endif
endin


instr NOISE
    a1 linen .5, 1, p3, 1   ;generate slope to control amplitude
    a2 randi a1, 5000       ;generte some white noise, and shape with envelop
    outs a2, a2             ;output noise
endin
 

</CsInstruments>
<CsScore>
;causes Csound to run for about 7000 years...
f0 z
</CsScore>
</CsoundSynthesizer>
