### Story
There are 100 prisoners in solitary cells. There's a central living room with one light bulb; this bulb is initially off. No prisoner can see the light bulb from his or her own cell. Everyday, the warden picks a prisoner equally at random, and that prisoner visits the living room. While there, the prisoner can toggle the bulb if he or she wishes. Also, the prisoner has the option of asserting that all 100 prisoners have been to the living room by now. If this assertion is false, all 100 prisoners are shot. However, if it is indeed true, all prisoners are set free and inducted into MENSA, since the world could always use more smart people. Thus, the assertion should only be made if the prisoner is 100% certain of its validity. The prisoners are allowed to get together one night in the courtyard, to discuss a plan. What plan should they agree on, so that eventually, someone will make a correct assertion?

### Task
Change the initial code to allow the prisoners to win their freedom.
The ```living_room``` function returns the new state of the ligthbulb and the assertion.
The function will be called until the assertion is ```True```.
A test will fail if:
* the assertion in ```True``` when some of the prisoner numbers were never passed to the function
* the assertion is never ```True``` after 29200 times a test will fail

### Input
* an integer between 0 and 99 for the prisoner number
* a boolean for the current state of the light bulb
* an array of booleans that represents the states of the light bulb during the previous visits of the prisoner in the room (when they go in, before changing it)

### Output
* a boolean for the new state of the light bulb
* a boolean for the assertion

### Example
In the example test the prisoners are taken in the room in order, from first to last, and then the cycle repeats.

For example, prisoner #0 goes in on day 1, when the lightbulb off and they have no previous visits, and then again on day 101, finding the lightbulb in whatever state was left by prisoner #99, and with ```previous_visits == [False]```.

If an assertion is:
* made before the 100th day, the prisoners are shot;
* made at or after the 100th day, the prisoners are set free;
* not made after 80 years (29200 days), the prisoners are shot.

### Notes
* do not use other variables in the global scope
* do not rename ```living_room```

### Constraints
* the prisoners have 29200 days to make an assertion
* the initial state of the light bulb is off (False)
