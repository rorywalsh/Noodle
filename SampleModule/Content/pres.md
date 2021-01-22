

---

#### <font color="cornflowerblue">Taking the 'con' out of content</font>

<img src="imgs/hereitcomes.gif" style="width:50%" />
<!-- .element: class="fragment" -->
<br>
Rory Walsh

---

#### <font color="cornflowerblue">So what's the problem?</font>

Notes:
* Proprietary software is a con!
* Like most proprietary systems, it tends to lead you toward their way of doing things
* Things get extremely frustrating when you want to do something different. 
* Then there are the limited list of supported formats for a range of multi-media  

---

#### <font color="cornflowerblue">Ok, and what's the solution?</font>

Notes:
* The solution is to use free and open source framework
* Frameworks that compliment the open source content management system used in the school
* Frameworks that can open up new levels of interactivity in presentations

---

#### <font color="cornflowerblue">Frameworks such as?</font>

<font color="orange">**RevealJS**</font> A HTML-based presentation framework 
<!-- .element: class="fragment" -->

<font color="lime">**Katex**</font> Math typesetting similar to Latex, but built specifically for the web. 
<!-- .element: class="fragment" -->

<font color="hotpink">**p5js**</font> A graphics library that provides easy to the HTML5 canvas
<!-- .element: class="fragment" -->

<font color="red">**Plotly**</font> A JS based version of the well known Python library for interactive graphing  
<!-- .element: class="fragment" -->

<font color="yellow">**Csound**</font> A web-based version of the popular audio programming language - for when WebAudio based libraries isn't up to the task...
<!-- .element: class="fragment" -->

---

#### <font color="cornflowerblue">Can we see some example?</font>

Certainly. 

Notes:
* The following are a selection of the slides from various modules I've thought in the past year or two. 
* All content is hosting as a website directly within the student's Moodle homepage where the students can interact directly with the content 


---

The following is from <font color="orange">Sound Design</font>, a module on the <font color="cornflowerblue">Certificate in Sound Design for Interactive Applications</font>.   

---

#### <font color="#9c2131">Loudness perception</font>

<img src="imgs/vu.gif" style="background:#fff;width:60%" />

The seminal work on loudness perception was done by <font color="orange">Fletcher</font> and <font color="orange">Munson</font> at Bell Laboratories, and reported in 1933. Since that time, many refinements have been made. 

The result of all of this was the development of so-called equal loudness contours.
<!-- .element: class="fragment" -->

---

In their experiments they ask a number of people to match a signal ascending upwards in frequency, with that of a steady tone at 1Kz, at a fixed amplitude. 

The results are shown in the following graph.

<img src="imgs/FletcherMunson.png" style="background:#fff;width:60%" />

---

<div class = "stretch">
     <iframe width="100%" height="100%" scrolling="no" frameBorder="0" data-src="https://editor.p5js.org/rorywalsh/embed/h3IAAxmbSZ"></iframe>
</div>

---

The following is from <font color="orange">Properties of Sound</font>, a first year module on <font color="cornflowerblue">B.A. in Audio and Music Production</font>.   

---

#### <font color="#9c2131">Tell us more, this is really interesting...</font>

Feast your eyes upon the Discrete Fourier Transform!! 

$$X(k) = {{1}\over{N}} \sum_{t=1}^\{n-1} \cdot x(t) \cdot [ cos(2  \pi  k  ({{t}\over{SR}}) - j sin(2  \pi  k  ({{t}\over{SR}})]$$
<!-- .element: class="fragment" -->

<blockquote style="font-size:18px;color:#ddd;background-color:#111">
where $x(t)$ is the time domain signal, $N$ is its size in samples, $x(k)$ is the output spectra, $t$ is the time index and k is the frequency sample index. $N$ in this case is referred to as the transform size. </blockquote>
<!-- .element: class="fragment" -->

---

#### <font color="#9c2131">What the text books fail to mention...</font>

...is that the average of the product of two sine waves will be 0 if they don't have the same frequency.  
<!-- .element: class="fragment" -->

---

#### <font color="#9c2131">Check it!</font>

Each time a mouse click is detected, this sketch will generate two random waveforms with frequencies between 1 and 5. The waveform on the right is the product(multiplication) of the these two waveforms

<div class = "stretch">
     <iframe width="100%" height="100%" frameBorder="0" data-src="https://editor.p5js.org/rorywalsh/embed/qifpJ74dS"></iframe>
</div>

Do you notice anything about the resulting waveforms when the two waves on the left have the same frequency?

---

#### <font color="#9c2131">And what about complex waveforms?</font>

<div class = "stretch">
     <iframe width="100%" height="100%" frameBorder="0" data-src="https://editor.p5js.org/rorywalsh/embed/gM9KiQrlr"></iframe>
</div>

This sketch shows a complex waveform with 10 harmonics. A slider can be used to change the frequency of the probe wave. 

---

The following is taken from a lecture in <font color="orange">Creative Coding for interactive applications</font> in the <font color="cornflowerblue">B.A. in Creative Media</font> module.

---

#### <font color="#9c2131">Step Sequencer</font>

<iframe height="400px" width="100%" src="https://editor.p5js.org/rorywalsh/sketches/9hSoVOQ8s"></iframe>

---

#### <font color="#9c2131">Oh shoot</font>

What's a <font color="orange">*shoot'em'up*</font> without some shooting?!

<div class = "stretch">
     <iframe width="100%" height="100%" frameBorder="0" data-src="https://editor.p5js.org/rorywalsh/sketches/i-j3u4Gpr"></iframe>
</div>

---

The following is from a <font color="orange">Sound Synthesis</font> module in the old <font color="cornflowerblue">B.A in Music and Audio Production</font>

---

#### <font color="#9c2131">Manipulating the audio stream</font> 

Audio streams can be manipulated in two unique ways. The first and most common approach is the modify the sample data directly.  

<div class = "stretch">
   <iframe width="100%" height="100%" scrolling="no" frameBorder="0" data-src="https://editor.p5js.org/rorywalsh/embed/YP7THMBly"></iframe>
</div>

When audio is processed in this way, an algorithm is applied to a number of samples. This type of processing is known as time-domain processing.

---

#### <font color="#9c2131">Classic time domain processing</font>

Almost all time-domain processes are based on the idea of mixing a delayed signal with its not delayed self. So let's start there, with the delay line. 

<div class = "stretch">
   <iframe width="100%" height="100%" scrolling="no" frameBorder="0" data-src="https://editor.p5js.org/rorywalsh/embed/H03cR32U5"></iframe>
</div>

---

A wet mix gain is typically applied to the delayed output to control how much of the delayed signal is heard.

<div class = "stretch">
   <iframe width="100%" height="100%" scrolling="no" frameBorder="0" data-src="https://editor.p5js.org/rorywalsh/embed/Qsk4ejnHr"></iframe>
</div>

---

#### <font color="#9c2131">Comb filters</font>

A comb filter is a delay line with a <font color="orange">feedback loop</font>. 

<div class = "stretch">
   <iframe width="100%" height="100%" scrolling="no" frameBorder="0" data-src="https://editor.p5js.org/rorywalsh/embed/lYiwVBXTm"></iframe>
</div>

One must be careful with the gain of a comb filter as anything greater than 1 will cause the signal to get louder and louder on each iteration.
<!-- .element: class="fragment" -->

---

<section style="left: -9999px;" data-state="editor">

instr COMB_FILTER
    a1, a2 diskin2 "DutchLadyTalking.ogg", 1, 0, 1       ;load sound file
    aComb comb (a1+a2)/2, 5, .01                         ;add comb filter
    outs aComb, aComb                                    ;output
endin

<p>
schedule("COMB_FILTER", 0, 10)                           ;trigger instrument

</section>

---

#### <font color="cornflowerblue"> Where to start?</font>

Starting visiting the [https://github.com/rorywalsh/Noodle](https://github.com/rorywalsh/Noodle) repository where you will find a quick overview of how to get set up.   

<div class = "stretch">
     <iframe width="100%" height="100%" scrolling="no" frameBorder="0" data-src="https://rorywalsh.github.io/Noodle/SampleModule/Content/one.html#/
"></iframe>
</div>

---

<div class = "stretch">
     <iframe width="100%" height="100%" scrolling="no" frameBorder="0" data-src="https://editor.p5js.org/rorywalsh/embed/8L_sXLDBU"></iframe>
</div>