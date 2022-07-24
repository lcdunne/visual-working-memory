# # Visual Working Memory task

Total runtime: 11.2 mins

## Summary

- Subjects see an array of squares centred on an invisible circle with diameter 1/2 screen height, centred.
- Study period: Squares (number corresponding to load) filled with one of 7 colours for 200 ms.
- Retention period: Colour disappears for 1 second
- Test period: Same number of colours return. Either identical colours to study period (no change), or one of the squares changes to an unstudied colour (change).
- Subjects judge whether change or no change: 2.3 s judgement period.
- Trial duration is 3.5s.

## Methodology

### Conditions

4 (Load: 1, 2, 4, 6) x 2 (Change: change, no change). 

The file contains 6 trials for each of the 4x2 load conditions for a total of 48 trials. Set the `wm_runs` loop to repeat 4 times.

The aX columns in the file correspond to each of the square components ordered by position around the circle in a clockwise fashion, and determines whether they are activated or not. If it is off, then colour is set to screen background colour.

The (standardised) colours used are as follows:

- RED = [1.0, -0.7176470588235294, -0.7803921568627451]

- GREEN = [-1.0, 0.9450980392156862, -0.803921568627451]

- BLUE = [-1.0, 0.13725490196078427, 1.0]

- YELLOW = [1.0, 0.968627450980392, -0.7333333333333334]

- CYAN = [-1.0, 1.0, 1.0]

- PURPLE = [1.0, -0.5294117647058824, 1.0]

- WHITE = [0.9607843137254901, 0.9607843137254901, 0.9607843137254901]

- X = [-1,-1,-1]

These are mapped into the excel file. 