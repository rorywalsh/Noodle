
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

Noodle uses the following open source frameworks:



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
