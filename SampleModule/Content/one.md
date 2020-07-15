
# Noodle

Although Microsoft PowerPoint has quickly become the de-facto standard for pedagogic content creation, it provides very few options for creating content with anything but a handful of supported media types. <!-- .element: class="fragment" -->

Users are also locked into a proprietary system of content creation that makes sharing and collaborating dependent on all parties owning copies of the software.
<!-- .element: class="fragment" -->

---

Noodle attempts to provide a simple alternative to these proprietary systems, by pulling together a collection of open source tools, scripts, and custom code snippets for the generation of content for teaching and learning.

The framework is written with Moodle in mind, and all content can quickly be embedded into any Moodle homepage. 
<!-- .element: class="fragment" -->

---

### Overview

* Getting started <!-- .element: class="fragment" -->
* Content <!-- .element: class="fragment" -->
* Markdown <!-- .element: class="fragment" -->

---


## Getting started

This content creation framework requires the following packages:

---

## Visual Studio Code

<img src="imgs/vscode.png" style="width:60%" />

<blockquote style="color:#ff4">
Be sure to download an install Visual Studio Code, not Visual Studio!</blockquote>
<!-- .element: class="fragment" -->

---

## VS Code Live Server extension

<img src="imgs/liveserver.gif" style="width:50%" />

The Live Server extension will <font color="orange">*serve*</font> your content in a browser so you can see how it looks. 

---

## Python

<img src="imgs/python3.png" style="width:60%" />

The build scripts for this framework use Python 3. If you already have another version of Python installed, just edit the `.vscode/tasks.json` file.  

---

## Getting set up

Download or clone the Noodle source from https://github.com/rorywalsh/Noodle

<img src="imgs/noodlegithub.png" style="width:50%" />

The <font color="orange">*SampleModule*</font> folder can be use as a template for all modules. Simple copy, paste and rename. 

---

Open Visual Studio code, and then open the root Noodle folder, i.e., the one containing all the module folders. 

<p>
<img src="imgs/buildtask.gif" style="width:60%" />


To test that everything builds Ok, open the one.md file in the SampleModule folder and run the build task by pressing <font color="orange">Ctrl/Cmd + shift + b</font>. You can also browse for the build command by pressing <font color="cornflowerblue">Cmd/Ctrl + shift + p</font> and browsing for Tasks: Run Build Task. 
</p><!-- .element: class="fragment" -->

---

## Viewing your content

If the build was successful, you will have a new html file, called after the .md file. If your .md file is named lecture1, the corresponding html file, after you built it, will be called lecture1.html. 

<img src="imgs/liveserve.gif" style="width:50%" />

Launch your content in a web browser by serving it with the Live Server extension as shown above. 

<blockquote style="color:#ff4">
Live server uses the default web application. To change it, modify the Live Server extension settings in Visual Studio code. </blockquote><!-- .element: class="fragment" -->

---

<img src="imgs/content.jpg" style="width:70%" title="http://picpedia.org/handwriting/c/content.html"/>

Content is created using a mix of markdown and custom Visual Studio Code snippets. 

---

Markdown
<img src="imgs/acousticsChamber.JPG" style="width:80%" />

### Acoustics is the study of sound

Note:
* Acoustics is the science of sound. 
* Traditionally the term has meant the study of the physical nature of sound but today it is used in a more generic sense.
* Acoustics is one of the main divisions of classical physics, along with motion (mechanics), heat (thermo-dynamics), light (optics), electricity, and magnetism.

---

### Ultrasonics

<img src="imgs/machineParts.jpg" style="width:50%" />

vibrations too fast for the ear to detect, nevertheless useful for calling dogs, detecting burglars, and removing dirt from small machine parts!

---

### Infrasonics

<img src="imgs/aerial-view-atmosphere-clouds.jpg" style="width:50%" />

vibrations too slow for the ear to detect, used by atmospheric physicists to study blast waves or weather systems. Also known as Subsonic sound.

---

### Underwater sound
<img src="imgs/4k-wallpaper-hd-wallpaper-nature.jpg" style="width:50%" />

useful in detecting submerged objects, whether schools of fish or submarines, with sonar devices.

---

#### Structural vibration

<img src="imgs/palm-trees.jpg" style="width:50%" />

building motion caused by wind, earthquake, or trampling of feet.

--

#### Physiological acoustics

mechanisms of ear and nerve operation and their pathology.

---

####  Psychoacoustics

<img src="imgs/perception.jpg" style="width:50%" />

human perception of sound; judgments, comparisons, and reactions to various sounds.

---

#### Architectural acoustics
designs and materials for improving homes, offices, and concert halls. Noise measurement and control: rapidly growing activity in response to concerns about environmental noise, including aircraft, highway traffic, industrial machinery, and rock concerts.

---

####  Musical acoustics
<img src="imgs/art-blur-bowed-instrument.jpg" style="width:50%" />

mechanisms of sound production by musical instruments; effects of reproduction processes or room design on musical sounds; human perception of sound as music.

---
<img src="imgs/ear-2973126_1920.png" style="width:70%" />

### What do we hear?

Note:
We hear anything that is ‘audible’. There are many contrasting types of audible sounds, the most relevant for us is music.

---
<img src="imgs/audience-band-concert.jpg" style="width:70%" />

### Music - what is it?

<section data-state="audioSlide" id="pianoMood.wav"></section>

Note:
* John Cage once described music as nothing more than a collection of organised sounds. 
* Music can be used to express emotions or certain ideas, but because of the subjective nature of listening these ideas are often lost on the audience. 
* Unlike other arts forms, music cannot be used to express a specific idea. This is what stands it apart from all other art forms.
---

<img src="imgs/mic-mic-stand-microphone.jpg" style="width:70%" />
<section data-state="audioSlide", id="DutchLadyTalking.ogg">

### Speech

Note:
* Speech has much in common with music but differs in that it can be used to communicate precise ideas without ambiguity. U
* Unlike music, speech does not have to be at a certain pitch or dynamic to be expressive; even the most monotonous of sentences can hold a profound meaning.

---

<img src="imgs/noise.jpg" style="width:70%" />

### Noise

---

<section style="left: -9999px;" data-state="editor">

instr NOISE
    aNoise randi .5, 15000       ;generate some white noise
    outs aNoise, aNoise          ;output noise
endin

<p>
schedule("NOISE", 0, 1)         ;play instrument NOISE for 1 second

</section>

---

### Music and Noise


<div style="width: 100%; overflow: hidden;">
<div style="width: 400px; float: left;">
Rite of Spring (Stravinsky, 1912)
</div>
<div style="margin-left: 420px;">
<audio controls>
<source src="media/RiteOfSpring.mp3" type="audio/mpeg" style="outline: none;">
</audio>
</div>
</div>
<br>
<br>
<br>
<div style="width: 100%; overflow: hidden;">
<div style="width: 400px; float: left;">
La fille aux cheveux de lin (Debussy, 1912)
</div>
<div style="margin-left: 420px;">
<audio controls>
<source src="media/Debussy.mp3" type="audio/mpeg" style="outline: none;">
</audio>
</div>
</div>

Note:
* The boundary between music and noise is not as distinct as we might imagine. 
* New generations seem to like music that its elders hear as an assault on their ears. 
* Many of the pieces which make up today's standard classical concert repertoire were once considered outrageous when first performed.

---

<div style="width: 100%; overflow: hidden;">
<div style="width: 400px; float: left;">
4' 33" (Cage, 1952)
</div>
<div style="margin-left: 420px;">
<audio style="outline:none;" controls>
<source src="media/Cage.ogg" type="audio/mpeg">
</audio>
</div>
</div>
<br>
<br>
<br>
<div style="width: 100%; overflow: hidden;">
<div style="width: 400px; float: left;">
Threnody for the victims of Hiroshima (Penderecki, 1960)
</div>
<div style="margin-left: 420px;">
<audio controls>
<source src="media/Penderecki.flac" type="audio/mpeg" style="outline: none;">
</audio>
</div>
</div>

Note:
* In 1952 John Cage wrote his most thought-provoking work, 4' 33” which calls for complete silence on the part of the performer. 
* Should this be considered as musical work or does it belong to a completely different art form?
* By 1960 the lines between music and ‘noise’ have become almost completely blurred. Krzysztof Penderecki’s ‘Threnody for the victims of Hiroshima’ is made up almost entirely of orchestral ‘noise’.

---

### Music and Noise

<img src="imgs/blurring-lines-and-light.jpg" style="width:50%" />

Note:
* We must be careful to keep an open mind and adopt a cautious attitude that almost any audible sound may reasonably appear in some composer's music.
* What might seem strange today will most likely become very acceptable as time passes by.
* As the producers of the future it’s imperative that you remain open to new ideas and approaches!

---

### Physics

force, pressure, mass, weight, work and energy
---

### Force

<img src="imgs/adult-athlete-black-and-white-163403.jpg" style="width:70%" />

The metric unit of force is a newton (N). <!-- .element: class="fragment" -->


> 9.8N equals roughly 1 kg of force, which correlates roughly to how much force we must exert in order to pick up a textbook. <!-- .element: class="fragment" -->
<!-- .element: class="fragment" -->

Note:
* Force is something which causes an object to accelerate and can be exerted in many different ways, by ropes, sticks, fingers, wind, magnets, and so on.
---

<img src="imgs/force_large.png" title="NASA-Edu" style="width:40%" />

When calculating force one must always take into account the direction with which the force is being exerted. For example if two people push a big green thing in the same direction at 300N the combined force of the car will be 600N, if however they push from opposite directions the force of the car will be 0. 

---

### Pressure

<img src="imgs/pressure8.gif" title="NASA-Edu" style="width:80%" />


$$ P_{(Pressure)} = {{F_{(Force)}} \over {A_{(Area)}}} $$

Note:
* Pressure is the measure of how much force is exerted on each part of a surface. The precise definition is:

---

Appropriate units of pressure are *N* per square meter, n/m2

<img src="imgs/pressure.jpg" style="width:40%" />

Under normal conditions, air pressure is approximately $$10^5 N/m2$$

Note:
* If a shop window with an area of 10m2 is subjected to nearly 106 N of force from the air outside that makes contact with it, why does it not break?

---

### Mass

<img src="imgs/father-ted-mass.jpg" style="width:50%" />

Mass tells how much matter an object is made of and is measured in kilograms; it is an intrinsic property of the object.

---

### Mass

<img src="imgs/mass.png" style="width:50%;background-color:#fff" />

Mass tells how much matter an object is made of and is measured in kilograms; it is an intrinsic property of the object.

>“Every object in a state of uniform motion tends to remain in that state of motion unless an external force is applied to it.” (Newton’s first law of motion, ‘Law of inertia’) 
<!-- .element: class="fragment" -->
---

### Interia 

Mass is responsible for the property of ***inertia***. It is a measure of a body's resistance to acceleration. More mass equals more interia. 

>“Acceleration = Force/Mass" (Isaac Newton's second law of motion)
<!-- .element: class="fragment" -->

Note:
* It’s clear to see from this equation that two objects with different mass will move at different speeds.
---

### Weight


>Weight is a vector whose magnitude (a scalar quantity), often denoted by an italic letter W, is the product of the mass m of the object and the magnitude of the local gravitational acceleration g;

In other words ***Weight(w) = Mass( m ) x Gravity ( g )***
<!-- .element: class="fragment" -->

<blockquote style="color:#ff4">
Weight is actually a force, measured in Netwons. The 'weight' we attribute to quantities is actually a measure of the amount of mass.
</blockquote>
<!-- .element:  class="fragment" -->
---

The value of g on the Earth's surface is approximately$9.8 m/s^2$ (read as metres per second squared). 

<img src="imgs/freefall.jpg" style="width:40%" />

Therefore, every second an object remains in free fall (***neglecting air resistance***), it will increase its downward speed another $9.8 m/s^2$ over what it was before. Weight is as an extrinsic property.

>While one’s mass will always be the same one’s weight will fluctuate depending on gravity.
<!-- .element: class="fragment" -->
---

### Work 

Work is the amount of energy transferred by a force.

<img src="imgs/work.jpg" style="width:40%" />

>Work (w) = Force (f) x Distance(d)
<!-- .element: class="fragment" -->

Note:
* If there is no motion, there is no work, however great the force may be.
---

### Energy

Energy is an intangible property gained by anything upon which we do work.

<img src="imgs/energy.jpg" style="width:40%" />

It is a quantity that is transferred from one body to another by the process of doing work. It may also be stored, like money in the bank, and withdrawn later.
<!-- .element: class="fragment" -->

---

<img src="imgs/kineticPotential.jpg" style="width:70%" />

---

### Summary

* Force is something which causes an object to accelerate
<!-- .element: class="fragment" -->
* Pressure is the measure of how much force is exerted on each part of a surface
<!-- .element: class="fragment" -->
* Mass tells us how much matter an object is made of and is measured in kilograms
<!-- .element: class="fragment" -->
* Weight is the force with which a mass is attracted to the Earth
<!-- .element: class="fragment" -->
* Work is defined as the transfer of energy
<!-- .element: class="fragment" -->
* Energy is defined as the ability to do work
<!-- .element: class="fragment" -->

---
