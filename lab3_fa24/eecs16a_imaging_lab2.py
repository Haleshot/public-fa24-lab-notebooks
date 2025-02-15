# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "matplotlib==3.10.0",
#     "numpy==2.2.3",
#     "pyserial==3.5",
# ]
# ///

import marimo

__generated_with = "0.11.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Imaging Lab 2: Single Pixel Scanning

        ### EECS 16A: Designing Information Devices and Systems I, Fall 2024
        <!--- Lily Bhattacharjee (lbhattacharjee@berkeley.edu)
              Wahid Rahman (wahid.rahman@berkeley.edu)
              Leyla Kabuli (lakabuli@berkeley.edu)
              Raghav Gupta (raghav.tech13@berkeley.edu)
              Nikhil Ograin (ncograin@berkeley.edu)
        ---->
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Table of Contents

        * [Instructions](#instructions)
        * [Lab Policies](#policies)
        * [Overview](#overview)
        * [Task 1: Images, Vectors, and Matrices](#images)
            * [Task 1a: Working with Images](#task2a)
            * [Task 1b: Scanning Mask Matrix](#task2b)
        * [Task 2: Imaging Real Pictures](#task3)
        * [Feedback](#feedback)
        * [Checkoff](#checkoff)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        <a id='instructions'></a>
        ## Instructions

        * Complete this lab by filling in all of the required sections, marked with `"YOUR CODE HERE"` or `"YOUR COMMENTS HERE"`.
        * When you finish, submit a checkoff request to get checked off (i.e. earn credit) for this lab. Be ready to answer a few questions to show your understanding of **each section**.
        * Labs will be graded based on completion for **teams of 2 students**.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        <a id='policies'></a>
        ## Lab Policies
        * **YOU MUST ATTEND THE LAB SECTION YOU ARE ENROLLED IN. If you anticipate missing a section, please notify your GSI in advance.**
        * **You are required to return all parts checked out at the beginning of the lab section unless told otherwise.**
        * **You are free to stay for the full allotted time and hack around with the lab equipment, but please reserve the GSI's time for lab-related questions.**
        * **Food and drinks are not allowed in the lab.** 
        * **Clean up, turn off all equipment, and log off of computers before leaving.**
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # <a id='overview'><span style='color:blue'>Overview</span></a>
        <center>
        <img src="images/systemdiagram.png" style="height:256px" />
        </center>

        This week, you will photograph a real-life object pixel-by-pixel using a projector and light sensor circuit (a.k.a. <b>single pixel camera</b>) and write code in your Jupyter notebook to display the captured image. 

        You will begin by checking that the imaging circuit (pre-built for you) works and that the projector is properly connected to the computer.

        Next, you will write code to generate the "mask" patterns that the projector uses to scan the object. 

        Then, you will use your generated mask matrix to photograph an object with the projector and imaging circuit setup (seen below). Finally, you will write code to recreate the image from light sensor readings that are sent to your computer via the Arduino.

        To prevent room lighting from affecting these measurements, the projector setup is usually placed in a closed cardboard box. 

        **You will not have to worry about building or understanding any circuits**, as they have already been made and debugged for you. If you are interested in learning more about circuits, please ask any lab staff member and/or take EECS 16B.

        <br><br>
        <center>
            <b>Setup</b>
        <img src="images/projector_setup.jpg" style="height:350px" />
        </center>
        <br>


        The single pixel imaging process (including some circuit detail, which again you do not need to know) would involve the following steps:
        - The projector illuminates the object with a mask.
        - The ambient light sensor detects the total amount of light reflected off the object. More light leads to more current through the sensor.
        - The analog circuit converts the sensor's current into an output voltage. More light $\rightarrow$ higher sensor current $\rightarrow$ higher output voltage.
        - This analog voltage is converted into a digital brightness value.   

        <b>Note:</b> In the real world, we come across random irregular fluctuations while taking measurements. This is called noise. It is important to consider noise while designing any system, and this lab is no different. You will learn more about noisy imaging in the Imaging 3 lab.
        </font>
        """
    )
    return


@app.cell
def _():
    # Import necessary libraries
    import numpy as np
    import matplotlib.pyplot as plt

    # '%matplotlib inline' command supported automatically in marimo
    # magic command not supported in marimo; please file an issue to add support
    # %run scripts/test.py
    return np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        <a id='images'></a>
        # <span style='color:blue'>Task 1: Images, Vectors, and Matrices </span>
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        <a id='task2a'></a>
        ## <span style="color:blue">Task 1a: Working with Images</span>

        <br>

        How can we represent an image? Consider a 5x5 grayscale image, where each of the 25 pixel intensities vary in shades of gray. One way to represent this is with a 2D matrix (2D NumPy array). The values stored in this array, varying from 0 to 1, correspond to different shades of gray: the lower the pixel value, the darker the pixel, with 0 being completely black and 1 being completely white. 

        For example, take the 5x5 **`gradient_image`** shown below. Starting from the top-left pixel (pixel[0,0]), each pixel becomes progressively brighter as you traverse the image row-by-row. 

        Note: We will be using 0 indexing in lab as most programming languages (including Python) index in lists starting from 0.

        <center>
        <img src="images/gradient.JPG" align="center" style="height:200px" />
        <figcaption>Gradient image example</figcaption>
        </center>

        We can create this in Python using a $5 \times 5$ NumPy 2D array called **`gradient_image`** with *linearly-spaced* floating point values from 0 to 1. The Python code to generate this is provided for you below. Take a look at the numerical 2D array and the corresponding image that is displayed by using the `imshow` function.
        </font>
        """
    )
    return


@app.cell
def _(np, plt):
    # A 5x5 gradient image with values from 0 to 1.
    gradient_image = np.linspace(0, 1, 25).reshape([5, 5])

    print(gradient_image)
    plt.imshow(gradient_image, cmap = "gray", interpolation = "nearest")
    return (gradient_image,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**<span style="color:red">What color does 1.0 correspond to? What about 0?</span>**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Instead of treating our images as 2D matrices, we can "reshape" or "flatten" our images into 1-D vectors. That is, instead of having a $5 \times 5$ matrix for our image, we can represent it using a $25 \times 1$ vector. This makes it simpler for us to use the linear algebra techniques learned in class for image processing. 

        Let's look at the 3x3 example image below (colored for illustrative purposes). How can we transform this 2D vector matrix into a 1-D column vector?   

        Essentially, the $0$th row is transposed (or flipped on its side by rotating 90 degress clockwise), such that its left-most element is on top and its right-most element is on the bottom. The $1$st row is also transposed on its side in the same way and appended below. These steps are repeated for each subsequent row of the original 2D image until you build a $9 \times 1$ **column vector**.    

        <center>
        <img src="images/matrix_to_col_new.png" style="width:500px"/>
        </center>

        Mathematically, each pixel value in the $3 \times 3$ image is represented as a variable $p_{ij}$, where $i$ is the row and $j$ is the column associated with the pixel location. This same image represented as a 1-D column vector (called $\vec{i}$) is:

        $$\vec{i} = \begin{bmatrix} p_{00} \\ p_{01} \\ p_{02} \\ p_{10} \\ p_{11} \\ p_{12} \\ p_{20} \\ p_{21} \\ p_{22} \end{bmatrix}$$    

        The procedure described above can be used to convert any $N \times M$ 2D image into a `num_pixels` $\times 1$ **column vector**, where `num_pixels` $= N \times M$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**<span style="color:red">Convert the 5x5 `gradient_image` that you created above into a 25x1 column vector `gradient_image_vector` and display it. You will find the command `np.reshape` helpful. What pattern do you notice? Think about why you see this pattern.</span>**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        <a id='task2b'></a>
        ## <span style="color:blue">Task 1b: Scanning Mask Matrix</span>

        Next, we will create a "mask" matrix (array) to enable our projector to illuminate and scan individual pixels, one at a time. This is the magic behind our single pixel camera. 

        If **`gradient_image_vector`** is represented by the column vector variable $\vec{i}$, the act of transforming $\vec{i}$ by a matrix $H$ into another 1D column vector $\vec{s}$ is represented mathematically as:

        $$\vec{s} = H \vec{i}$$

        This matrix-vector multiplication represents what happens when we scan an image with our single pixel camera! In the context of a real-world imaging system, $H$ represents the scanning "mask matrix," whose rows are projected one-by-one onto the image we want to scan. $\vec{s}$ represents digitized readings from the analog circuit's light sensor. 

        Each element $s_k$ of $\vec{s}$ corresponds to one scan (using one row $k$ of $H$, that we refer to as $H_k$). Each 1D **row of $H$** represents a **mask**. But what is a mask? Here, a mask is a way to highlight certain locations in the image while hiding others during scanning. For a 3x4 image (where 3 = height, 4 = width), a mask taken from **row 0 of $H$** is represented as the $1 \times 12$ row vector below: 

        $$
        H_0 
        = \begin{bmatrix} 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\end{bmatrix}
        $$

        However, the mask must first be converted into its 2D form, as shown below, before it's projected over the 2D image. The mask exposes only the top-left pixel of the 2D image and hides all other pixels. Note that you can convert a 2D mask into a 1D row of $H$ by appending each of the 2D mask's rows to the right of the previous row.
        <br><br>
        <center>
        <img src="images/black_hite.png" style="width:400px"/>
        </center>

        To expose each pixel of the 3x4 image $\vec{i}$ individually, we would need a 12x12 $H$ that has 12 masks (rows), each with a single white "exposed" pixel in a unique location. This means that **row 1 of $H$** (exposing $iv_{01}$) would look like:

        $$
        H_1 
        = \begin{bmatrix} 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\end{bmatrix}
        $$

        <br><br>
        <center>
        <img src="images/black_white_shifted.jpg" style="width:400px"/>
        </center>
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The process of masking an image, then uncovering one pixel at a time, and sensing the resultant ambient light performs the matrix multiplication $\vec{s} = H \vec{i}$ in real life. This equation implies that each element of the sensor output vector $\vec{s}$ can be determined as:

        $$s_k = H_k \vec{i}$$

        Where the $k$th sensor reading is determined by the mask given by $k$th row of $H$, $H_k$. Thus, projecting the 2D representation of $H_0$ shown above onto a 3x4 image represented by the column vector $\vec{i}$ to obtain the sensor reading $s_0$ would be mathematically equivalent to:

        $$
        s_0 = \begin{bmatrix} 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\end{bmatrix} \vec{i}
        $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**<span style="color:red">What dimensions does the mask matrix $H$ have for a 5x5 image? Why? </span>**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        **<span style="color:red">
        Create the mask matrix $H$ for a 5x5 image.</span>**

        *Hint: Google the function `np.eye`.*
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        **<span style="color:red">
        Multiply the $H$ matrix with `gradient_image_vector`. Remember to use `np.dot` to do matrix multiplication and pay attention to the order of multiplcation!</span>**
        """
    )
    return


app._unparsable_cell(
    r"""
    # TODO: Multiply `H` and `gradient_image_vector`
    s = # YOUR CODE HERE

    # Display the result and compare it to `gradient_image_vector`
    plt.imshow(s, cmap = \"gray\", interpolation = \"nearest\")
    plt.xticks([])
    plt.yticks(np.arange(0, 30, 5))
    plt.show()
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**<span style="color:red">Is the resultant `s` equal to `gradient_image_vector`? Why?</span>**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        What happens when this matrix multiplication is performed? To reiterate, each row of $H$ is responsible for "illuminating," or selecting, a single pixel in the gradient image. `gradient_image_vector` was created by converting the 5x5 `gradient_image` into a 1D *column vector*. Similarly, *every row* in $H$ can be represented as a 5x5 image that, in real imaging, would be projected over `gradient_image`. 

        **<span style="color:red">
        Iterate through each row of the matrix $H$. *Reshape* each row into a 5x5 image, and check that each row illuminates a unique pixel of the original 5x5 image! Based on $\vec{s} = H \vec{i}$, why are the rows of $H$ used for masking when $\vec{i}$ is a column vector?</span>**
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Each of the images above are masks. During a single scan, we project one of these masks over our object. The white pixel illuminates a particular location on the object that we want to capture, and the black pixels obscure the other parts of the object. Thus, using the rows of $H$, we gather information one pixel at a time.

        Let's try to make another mask matrix, $H_{alt}$, that's a little more complicated. We want $\vec{s}$ to contain information on each pixel of the image, but in a random order. Sensing pixels in a random order and being able to reconstruct the right image is a good way to test the correctness of our imaging model. 

        **<span style="color:red">
        Generate $H_{alt}$ for a 5x5 image that illuminates each pixel of the image one at a time, but in a random order. Multiply $H_{alt}$ by `gradient_image_vector` to produce the new output vector $\vec{s}_{alt}$.
        </span>**

        <b>Hint</b>: We can use rows from the existing $H$ matrix and then shuffle their order randomly. Consider using [np.random.permutation()](https://numpy.org/doc/stable/reference/random/generated/numpy.random.permutation.html) for this.  The code to correctly generate `H_alt` should only require you to type 1 short line.

        <b>Hint 2</b>: Here's one of many variations of $H_{alt}$ for an image of size 4x4.
        <br><br>
        <center>
        <img src="images/H_alt_new_4x4.png" style="width:300px"/>
            <figcaption>A variation of $H_{alt}$ for a 4x4 image. </figcaption>
        </center>
        """
    )
    return


app._unparsable_cell(
    r"""
    # TODO: Create the new mask matrix `H_alt` for a 5x5 image
    H_alt = # YOUR CODE HERE

    # Test H_alt for correctness
    test1b_H_alt(H_alt)

    # Display `H_alt`
    plt.figure()
    plt.imshow(H_alt, cmap = \"gray\", interpolation = \"nearest\")

    # TODO: Multiply `H_alt` and `gradient_image_vector`
    s_alt = # YOUR CODE HERE

    # Display the result `s` and compare to `gradient_image_vector`
    plt.figure()
    plt.imshow(s_alt, cmap = \"gray\", interpolation = \"nearest\")
    plt.xticks([])
    plt.yticks(np.arange(0, 30, 5))
    plt.show()
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Because of how we designed `H_alt`, `s_alt` is clearly different from `gradient_image_vector`. Each pixel of `gradient_image_vector` is still illuminated only once by `H_alt`, but the order in which the pixels are illuminated has changed. Therefore, we say that `s_alt` is a "scrambled" version of `gradient_image_vector`. How could we "reconstruct" $\vec{s}_{alt}$ back into the original `gradient_image_vector`? 

        Recall that our original matrix $H$ was actually the **identity matrix** $I_n$. In other words, the original $\vec{s}$ was computed as:

        $$ \vec{s} = H \vec{i} = I_n \vec{i}$$

        <br />    
        Using the alternate mask, $H_{alt}$, we compute the alternate output $\vec{s}_{alt}$ as:

        $$ \vec{s}_{alt} = H_{alt} \vec{i} $$

        To "reconstruct" $\vec{s}_{alt}$ back into the original `gradient_image_vector` (i.e. $\vec{i}$), we must find a matrix $M$ that multiplies $\vec{s}_{alt}$ to make the following true:

        $$ M \vec{s}_{alt} = \vec{i} $$

        i.e.

        $$ M H_{alt} \vec{i} = \vec{i} $$

        **<span style="color:red">What should M be to recover $\vec{i}$?</span>**
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""`YOUR COMMENTS HERE`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**<span style="color:red">Write code to reconstruct `gradient_image_vector` from `s_alt`.</span>**""")
    return


app._unparsable_cell(
    r"""
    # TODO: Reconstruct `gradient_image_vector`
    M = # YOUR CODE HERE
    gradient_image_vector_reconstruct = # YOUR CODE HERE

    # Display M
    plt.figure()
    plt.imshow(M, cmap = \"gray\", interpolation = \"nearest\")
    plt.title(\"M\")
    plt.show()

    # Display M*H_alt
    plt.figure()
    plt.imshow(np.dot(M,H_alt), cmap = \"gray\", interpolation = \"nearest\")
    plt.title(\"M*H_alt\")
    plt.show()

    # Display the result
    plt.imshow(gradient_image_vector_reconstruct, cmap = \"gray\", interpolation = \"nearest\")
    plt.xticks([])
    plt.yticks(np.arange(0, 30, 5))
    plt.show()
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        <a id='task3'></a>
        ## <span style="color:blue">Task 2: Imaging Real Pictures</span>

        Finally, we will use our two matrices to image a real object; any drawing of your choice!

        There are index cards and markers at the GSI desk; **<span style="color:red">take an index card and draw something on its blank (no lines) side.** Feel free to be creative and draw something cool! The course staff always loves to see cool drawings! Keep in mind though that this is not the most sophisticated imaging setup ever. Keep details to a minimum and use large features where possible to ensure a good quality image.

        Because our object is fairly large, we want each individual mask to have dimensions 30x40 (i.e. height = 30, width = 40) to match the 4:3 (W:H) aspect ratio of the index card. Think about how big the mask matrix was for the 5x5 example. How big must it be for a 30x40 picture?

        **<span style="color:red">
        Recreate both the $H$ and $H_{alt}$ masks to match these new dimensions. </span>**
        """
    )
    return


@app.cell
def _():
    # magic command not supported in marimo; please file an issue to add support
        # %run scripts/test.py
    return


app._unparsable_cell(
    r"""
    # TODO: Recreate `H`
    H = # YOUR CODE HERE

    plt.figure(figsize = (10, 10))
    plt.imshow(H, cmap = 'gray', interpolation=\"nearest\")
    """,
    name="_"
)


app._unparsable_cell(
    r"""
    # TODO: Recreate `H_alt`      
    H_alt = # YOUR CODE HERE

    plt.figure(figsize = (10, 10))
    plt.imshow(H_alt, cmap = 'gray', interpolation=\"nearest\")
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Let's make sure that the two matrices we made are invertible and the correct size. Run the code block below to invert the matrices and test dimensions - if any of the lines fail, it means the code used to generate either matrix resulted in a incorrect size or non-invertible, linearly dependent matrix, which is incorrect.""")
    return


@app.cell
def _(H, H_alt, test_masks_img2):
    test_masks_img2(H, H_alt)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Our mask matrices must be saved as files before they can be used to perform real imaging. The files are read by our imaging script, as seen below.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**<span style="color:red">Run the cell below to save `H` and `H_alt`!</span>**""")
    return


@app.cell
def _(H, H_alt, np):
    np.save('H.npy', H)
    np.save('H_alt.npy', H_alt)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## <a id ='setup'></a><span style = "color: blue">Hardware Setup</span>""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In order to transfer this theoretical masking procedure to a real-life imaging setup, you will build some hardware. Summarized briefly, the hardware performs the following functions:
        1. Project a mask matrix for a given pixel onto an index card
        2. Read the amount of light reflected off the card using an ambient light sensor. We will refer to this as the "imaging circuit" though you may see older references use this terminology.
        3. Store this reading in a result matrix
        4. Repeat steps 1-3 until the entire image is stored in the result matrix

        Most of the circuits which do the heavy lifting have already been built for you, so you will only have to set up the following pieces:
        1. Box: This holds the entire setup together and is where you will connect most of the hardware pieces together.
        2. Projector: The projector displays the mask matrix onto the index card, so it must be setup correctly to do this.
        3. Arduino Leonardo: An Arduino is a microcontroller (think of a small computer) that reads the light reflected off the card and sends it back to your computer for further processing.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### <a id ='setup'></a><span style = "color: blue">Box Setup</span>
        <img src="images/projector_setup.jpg" style="width:400px"/>
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        1. Take the cardboard box at your station down from the top left next to some of the lab equipment, and open the top. **Only remove cables and loose items as needed**. The projector setup shown above should be **left inside the box**.
        2. Tape the index card you drew on inside the box so that the projector can project onto it (see image).
        3. Place the breadboard such that the side with the holes on it is facing the index card. The Arduino should then rest on the bottom of the box behind the imaging circuit and underneath the projector. Make sure the light sensor is centered at the top, as in the picture above. Try your best to ensure that the wires do not obstruct the projection from the projector onto the index card.
        4. Orient the projector so the lens is facing towards the object being imaged, and the ports are facing the opposite direction (see image).
        5. **Pay close attention to where the holes are in the box, picture on next page**. The holes are cut out to make connecting the mini-HDMI and power cables easier. Align the holes to both the circular power connector and the mini-HDMI port on the back of the projector to the short, back side of the box that has a hole in it.
        6. Route the power cable through the back to the DC connector and the mini-HDMI cable (at your lab station behind the keyboard under the monitor stand, **one end already connected to your lab computer**) through the back and connect them both to the projector **very gently**. Please ensure you’re using the right projector ports.
            <img src="images/projector_overview_ports.png" style="width:400px"/>
        7. Take the long USB cable and route it through the side hole (or back) and connect it to the Arduino.
        8. The power cable must be plugged into an outlet - there are outlets at each station (see picture). Make sure the barrel connector is fully plugged into your projector - if the connection is loose during the scan you may have issues. A red light should show on the back of the projector to indicate that it is charging. Turn on the projector by pressing and holding the power button on the back.
        9. Plug the USB 2.0 end of the USB cable into the lab computer.
        10. Confirm your setup with the full setup below
        <img src="images/box_setup.jpg" style="width:400px"/>
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### <a id ='setup'></a><span style = "color: blue">Projector Setup</span>""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""<img src="images/projector_overview.png" style="width:500px"/>""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        **Setup the projector with the following steps:**
        1. Turn on the projector by holding down the Power button (see the previous figure). You should see a green light turn on when it powers on.
        2. Find the Focus Adjustment wheel on the side of the projector to adjust the focus of the projection onto the box. Focus it as close as possible.
        <img src="images/projector_home.jpg" style="width:400px"/>
        3. Using the left/right arrows on the Directional Pads, select **INPUTS** on the projector's main menu, then **DIGITAL**. After a few seconds, you should see the Windows 10 desktop.
        <img src="images/projector_inputs.jpg" style="width:400px"/>
        4. If you see the Windows 10 taskbar at the bottom of the projected screen, take the following precautions:
            - Hit the Windows key and type Settings.
            - Click on the Personalization icon.
            - Click on Taskbar on the left side.
            - Under the Multiple Displays section, turn Show taskbar on all displays off.
        5. If your monitor turns off, hit Windows key and P at the same time. Then select “Extend”
        6. Use the **Back button** on the projector to return to displaying the **main menu**.
        7. Use the left/right arrows to select the **Settings** option (gears icon, see picture on previous page).
        <img src="images/projector_settings.jpg" style="width:400px"/>
        8. Select **Picture Mode** and change the **Picture Mode** from Standard to **User**.
        9. **IMPORTANT**: Use the down arrow to move the cursor down to Contrast. Then use the right arrow to adjust the contrast to **100**.
        10. **IMPORTANT**: Move the cursor down to Brightness and use the left arrow to adjust the brightness to **0**.
        11. To **Confirm the selection**, hit **OK** and exit the menu with the **Back button**.
        12. Go back to **Settings** and select **ECO** for **brightness**
        13. Hit the button **SOURCE** and then **DIGITAL** and make sure that you see the Windows 10 desktop on your projector.
        14. Place the properly set up projector inside the box, as shown in the image above.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### <a id ='setup'></a><span style = "color: blue">Arduino Leonardo Setup</span>""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        1. Launch **Arduino IDE** (from Desktop)
        2. Open the **AnalogReadSerial.ino** file in Arduino IDE (*File > Open*). This will be located in the lab files you downloaded.
        3. Select *Tools > Board > Arduino Leonardo*.
        4. Verify the correct Serial Port is selected in the Ardunio IDE by going to *Tools > Port*. If the selected value already displays the board name after the COM port (i.e. "COM5 (Arduino Leonardo)"), proceed to the next step. If not, open the Windows "Device Manager" and look for the Arduino Leonardo's COM Port under "COM Ports", then select this port in the Arduino IDE.
        5. Upload the code by clicking on the Upload button (white circle with a right-pointing arrow, as shown below):
        <img src="images/arduino_menu.png" style="width:200px"/>
        6. Hit the **RESET** button on your Arduino (labeled reset or RST).
        7. To verify that the program is working, **type a 6 into the serial monitor** (*Tools > Serial Monitor*). **You will need to set the Baud Rate to 115200**. You should see a reading from the ambient light sensor appear. If the numbers increase with light and decrease with less light your setup is good. You must close this window before continuing.
        <img src="images/arduino_serial_monitor.png" style="width:400px"/>
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        **<span style="color:red">Double check that you've done the following before proceeding:</span>**

        * Upload `AnalogReadSerial` to the Arduino. Press the reset button on the Arduino to make sure the script is running.

        * **Close out of the Arduino IDE Serial Monitor.** Not doing so will result in your COM port being unavailable.

        * Make sure the projector is connected and projecting the correct image. It should show a smaller version of your desktop (windows logo by default).

        * Seal the imaging system inside the box to keep ambient light out during scanning. If the holes for cables are too big, try to have them face a solid, unmoving object that can block out light. Alternatively, cover the entire the box with clothing.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        **<span style="color:red">You will then run the `capture_image.scan(...)` function (through the cell below) that projects mask patterns onto your image based on the $H$ matrix that you designate. This function controls the scanning process.</span>** 

        When running **`capture_image.scan(...)`**, a new icon shaped like a white web will appear in the taskbar. The window depicting our masks will appear on the projector's screen. *You can confirm this by looking into the box. (Don't forget to close the box when you're done checking!)*

        `capture_image.scan(...)` iterates over the rows of the $H$ matrix you made. These rows are translated, one-by-one, into real masks projected onto the screen. If you take a peek inside your scanning system while the scan is completing (*Only from the side wire ports! Never open the top while scanning!*), you will see white rectangles where your mask has value `1` and black rectangles where your mask has value `0`.

        The whole scanning process should take roughly **4 minutes**. 

        Running the code block below will start your scan.
        """
    )
    return


@app.cell
def _(np):
    # Import necessary libraries (so you don't have to start from the top)
    # magic command not supported in marimo; please file an issue to add support
    # %run scripts/helpers.py
    # '%matplotlib inline' command supported automatically in marimo
    import capture_image

    H = np.load("H.npy")
    sr = capture_image.scan(H, multi_pixel=False, width=40, height=30)
    return H, capture_image, sr


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        **Not getting a good image?**

        Make sure you have the following:
        1. The projector turned on and oriented in the correct direction
        2. The projector input set to "Digital"
        3. Verified the mask is displaying from the projector
            - You should see white squares scrolling across the projected screen
        4. Code successfully uploaded to the Arduino
            - The Arduino IDE will notify you if the upload fails
        5. Nothing obstructing the ambient light sensor's view of the projected screen
        6. The taskbar disabled
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        After the sensor readings have been captured, load the sensor reading vector into the cell below. Once again, here is the equation relating $H$, the sensor reading column vector $\vec{s}$, and the image column vector $\vec{i}$:

        $$\vec{s} = H \vec{i}$$

        **<span style="color:red">Recreate the image from the sensor readings obtained with `H`.</span>**
        """
    )
    return


app._unparsable_cell(
    r"""
    # TODO: Create the image vector from `H` and `sr`
    # Hint: `H` is a special matrix. What is so special about this matrix?
    iv = # YOUR CODE HERE

    img = np.reshape(iv, (30, 40))
    plt.figure(figsize = (8, 8))
    plt.imshow(img, cmap = 'gray', interpolation=\"nearest\")
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Congratulations! You have imaged your first image using your single pixel camera! 

        **<span style="color:red">
        Does your recreated image match the real image? What are some problems you notice? 
        </span>**

        Here is an example of a picture we took using this setup:

        <center>
        <img src="images/ee16a_picture.png"/>
        </center>
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**<span style="color:red">Next, use the second mask `H_alt` for imaging. Can you repeat the same reconstruction procedure just by replacing $H$ with $H_{alt}$? Why or why not?</span>**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Run `capture_image.scan(...)` again (taking the same precautions as above) to collect sensor readings. Make sure to run it from the code block below to point the script to `H_alt`. Then reconstruct the image.""")
    return


@app.cell
def _(capture_image, np):
    H_alt = np.load('H_alt.npy')
    sr_1 = capture_image.scan(H_alt, multi_pixel=False, width=40, height=30)
    return H_alt, sr_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Observe your sensor reading. Since we're scanning pixels of the image in a random order, it should be a scrambled version of the image.""")
    return


app._unparsable_cell(
    r"""
    # TODO: Create the image vector from `H_alt` and `sr`
    # Hint: You need to perform a matrix operation before multiplying
    iv = # YOUR CODE HERE 

    img = np.reshape(iv, (30, 40))
    plt.figure(figsize = (8, 8))
    plt.imshow(img, cmap = 'gray', interpolation=\"nearest\")
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        **<span style="color:red">The sensor reading is a scrambled version of the image. Were you able to reconstruct the image correctly? How did it get "unscrambled"?  </span>**

        `YOUR ANSWER HERE`
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""You are done for the week! Save your code and setup for next lab, where you will illuminate multiple pixels per mask!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        <a id='task4'></a>
        # <span style="color:blue">(OPTIONAL) Task 3: Color Imaging</span>
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We've seen how we can perform reconstruction of our hand-drawn picture using the model $\vec{s} = H \vec{i}$. But what if we wanted to image in color instead of just in grayscale?

        Recall that our system works by projecting masks onto our image and measuring the reflected light. In Task 2, the masks we used were black and white. If we shine white light on any color, we'll get some amount of reflected light back, which makes our system work regardless of what color we use to draw our image. The downside is we can't differentiate between colors.

        One way to "select" colors is by changing the color of the masks we project. If we shine red light at a particular pixel on the index card, we expect to only get reflected light when the color of that pixel is red (or close to it). This idea prompts us to consider channel-wise reconstruction. That is, instead of

        $$\vec{s_{gray}} = H_{gray} \vec{i_{gray}}$$

        we now have

        $$\vec{s_{red}} = H_{red} \vec{i_{red}}$$
        $$\vec{s_{green}} = H_{green} \vec{i_{green}}$$
        $$\vec{s_{blue}} = H_{blue} \vec{i_{blue}}$$

        which we can then solve to find $i_{red}$, $i_{green}$, and $i_{blue}$. By appropriately combining these channels, we can produce a color image!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Below, we implement this process. Note that for each pixel, we sequentially measure its red, green, and blue channels rather than measuring the red channel of the entire image, followed by the green and blue channels. If we used the latter process, a small disturbance in the position of the projector would result in misaligned red, green, and blue channels. This would cause the entire image to be inaccurate. By using the former process, we are significantly reducing this risk, since a temporary disturbance in the position would only cause few pixels to be inaccurate.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Use colored markers to make a new index card! Then, following the same procedure as in Task 2, run the following cell block. Note that this will take 3 times as long as before (probably around 10 minutes) because we have to take thrice the measurements.""")
    return


@app.cell
def _(np, plt):
    H_1 = np.eye(1024)
    np.save('H.npy', H_1)
    sr_blue = np.load('sensor_readingsH_100_0_blue.npy')[:1024]
    sr_green = np.load('sensor_readingsH_100_0_green.npy')[:1024]
    sr_red = np.load('sensor_readingsH_100_0_red.npy')[:1024]
    sr_2 = np.zeros((32, 32, 3))
    sr_2[:, :, 0] = np.reshape(sr_red, (32, 32))
    sr_2[:, :, 1] = np.reshape(sr_green, (32, 32))
    sr_2[:, :, 2] = np.reshape(sr_blue, (32, 32))
    mx = np.amax(sr_2)
    sr_2 = sr_2 * (255 / mx)
    sr_2 = np.require(sr_2, np.uint8, 'C')
    plt.imshow(sr_2, interpolation='nearest')
    return H_1, mx, sr_2, sr_blue, sr_green, sr_red


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Did the scan work? Don't worry if it doesn't look that great; we have provided some post-processing to adjust your measurements. You do not need to know how post-processing works in this lab.""")
    return


@app.cell
def _(np, plt, post_process, sr_blue, sr_green, sr_red):
    sr_3 = post_process(sr_blue, sr_green, sr_red)
    sr_3 = np.require(sr_3, np.uint8, 'C')
    plt.imshow(sr_3, interpolation='nearest')
    return (sr_3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## **<span style="color:red"> Do not take apart your setup. Do not take any of it with you! </span>**

        **Please ensure you've placed the entire imaging setup box with the following items back on the station shelf:**

        1. Pico Projector
        2. Power Adapter
        3. Long micro USB cable
        4. Wooden Stand
        5. Arduino Leonardo
        6. Imaging circuit on breadboard
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        <a id='feedback'></a>
        ## Feedback
        If you have any feedback to give the teaching staff about the course (lab content, staff, etc), you can submit it through this Google form. Responses are **fully anonymous** and responses are actively monitored to improve the labs and course. Completing this form is **not required**.

        [Anyonymous feedback Google form](https://docs.google.com/forms/d/e/1FAIpQLSdSbJHYZpZqcIKYTw8CfpfrX6OYaGzqlgBtKfsNKEOs4BzZJg/viewform?usp=sf_link)

        *If you have a personal matter to discuss or need a response to your feedback, please contact <a href="mailto:eecs16a.lab@berkeley.edu">eecs16a.lab@berkeley.edu</a> and/or <a href="mailto:eecs16a@berkeley.edu">eecs16a@berkeley.edu</a>*.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        <a id='checkoff'></a>
        ## Checkoff
        When you are ready to get checked off, fill out the checkoff google form. **[Checkoff Form](https://docs.google.com/forms/d/e/1FAIpQLSfIOjvEJXew-M0-h9uJ3C25UOdmmABFK0GGNl3o9p7po7Cc0A/viewform?usp=sf_link)**

        Your GSI or a Lab Assistant will join you when they are available and go through some checkoff questions with your group. They will go through the checkoff list in order. Please be patient!

        #### Post-checkoff Clean Up: (this applies to each week's lab)
        2. Throw away any trash at your station
        4. SIGN OUT of the computers - DO NOT SHUT DOWN
        5. Check that the projector is powered off and disconnected
        """
    )
    return


if __name__ == "__main__":
    app.run()
