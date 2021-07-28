# Grid problem solver

### Background:
This is some POC code that I whipped up after watching a TED-ED riddle video ([Can you solve the virus riddle? - Lisa Winer](https://www.youtube.com/watch?v=ZKh6z0X6KRw)). The premise was that there was a scientist who had a virus broke containment. The facility had rooms in a 4x4 grid pattern and rooms that touch are connected (up, down, left, right and not diagonally). Each room was equipped with a lockout button which would shut all doors in that room sealing it off forever but leaving the scientist enough time to barrel roll under the closing doors. The scientist enters the top left room and is tasked with containing the virus in all rooms without the ability to double back. The catch is that there is only one escape door and it's at the bottom right. The video went on to prove that only rooms with an odd number of dimensions would be possible without using some dirty trick but at that point I was already coding.

**This software will try and brute force an escape route for the scientist. Spoiler alert, the conclusion in the video isn't wrong.**

## Screenshots
<img alt="First screenshot of 4x4 grid trying to be solved" src="/blob/screenshot_1.png?raw=true" width="250"><img alt="Second screenshot of 4x4 grid trying to be solved" src="/blob/screenshot_2.png?raw=true" width="250"><img alt="Third screenshot of 4x4 grid trying to be solved" src="/blob/screenshot_3.png?raw=true" width="250"><img alt="Fourth screenshot of 4x4 grid trying to be solved" src="/blob/screenshot_4.png?raw=true" width="250"><img alt="Screenshot of a solved 5x5 grid" src="/blob/screenshot_5.png?raw=true" width="250">

## Prerequisites
- Python 3
- Pygame

## Running the code

For production release:

```
python .\src\main.py
```

> Note: I put some constants in .\src\grid_solver\grid_solver_ui.py because I was in too much of a hurry to put in command line arguments. Feel free to tweak/play around with them.

## License
 
The MIT License (MIT)

Copyright (c) 2021 umbreon222

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
