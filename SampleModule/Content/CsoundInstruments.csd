<CsoundSynthesizer>
<CsOptions>
-n -d 
</CsOptions>
<CsInstruments>
sr = 44100
ksmps = 64
nchnls = 2
0dbfs = 1

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

</CsInstruments>
<CsScore>
;causes Csound to run for about 7000 years...
f0 z
</CsScore>
</CsoundSynthesizer>
