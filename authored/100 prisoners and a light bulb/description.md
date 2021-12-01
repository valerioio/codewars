### Story
There are 100 prisoners in solitary cells. There's a central living room with one light bulb; this bulb is initially off. No prisoner can see the light bulb from his or her own cell. Everyday, the warden picks a prisoner at random, and that prisoner visits the living room. While there, the prisoner can toggle the bulb if he or she wishes. Also, the prisoner has the option of asserting that all 100 prisoners have been to the living room by now. If this assertion is false, all 100 prisoners are shot. However, if it is indeed true, all prisoners are set free and inducted into MENSA, since the world could always use more smart people. Thus, the assertion should only be made if the prisoner is 100% certain of its validity. The prisoners are allowed to get together one night in the courtyard, to discuss a plan. What plan should they agree on, so that eventually, someone will make a correct assertion?

### Task
Change the ```living_room``` function in the initial code to allow the prisoners to win their freedom in every game.

The function ```living_room``` takes in three argument, the first of which is an integer that identifies a prisoner. To call ```living_room``` with ```i``` as first argument means to call the prisoner ```#i``` into the living room.

The function returns a tuple (array in JavaScript) of two booleans, the latter of which represents the assertion. If the second value of the tuple returned is ```True``` an assertion is made by the prisoner in the living room.

A game is a sequence of calls of the function ```living_room``` that ends when an assertion is made (or after 29200 times if no assertion is made). The prisoners win the game and are set free if an assertion is made after all the prisoners were called into the living room at least once during the game.

### Input
* an integer between 0 and 99 for the prisoner number
* a boolean for the current state of the light bulb
* an array of booleans that represents the states of the light bulb during the previous visits of the prisoner in the room (when they go in, before changing it)

### Output
A tuple (array in JavaScript) with:
* a boolean for the new state of the light bulb
* a boolean for the assertion

### Example
In the example test the prisoners are taken in the room in order, from first to last, then the cycle repeats.

For example, prisoner #0 goes in on day 1, when the lightbulb is off and they have no previous visits, and then again on day 101, finding the lightbulb in whatever state was left by prisoner #99, and with ```previous_visits == [False]```.

If an assertion is:
* made before the 100th day, the prisoners are shot;
* made at or after the 100th day, the prisoners are set free;
* not made after 80 years (29200 days), the prisoners are shot.

### Notes
To make sure that none of the prisoners is communicating, your solution should not rely on any kind of state.
The arguments to the function are designed to make keeping state unnecessary.
The only information needed by the prisoners a prisoner will have at any time is:
* the predecided plan (i.e. the ```living_room``` function)
* who they themselves are and what role they play in the plan (```prisoner_number```)
* the current state of the lightbulb (```lightbulb```), and all the previous times which they had seen the lightbulb since the game started (```previousVisits```)

The prisoners may also wish to remember conclusions they had arrived at previously, however since they have all the same information they did when they reached that conclusion, they can merely do it again.

The tests are designed to fail solutions that use a state. Please do not:
* use closures
* add attributes to the function
* add other arguments to the function
* use other variables in the global scope
* rename ```living_room```

### Constraints
* the prisoners have 80 years (29200 days) to make an assertion
* the initial state of the light bulb is off (False)

### Bonus points
Solve the task without the assumption that the light bulb is initially off for a bonus point.
The initial state of the light bulb can be on or off, the prisoners know that is chosen at random but they don't know what is the initial state. They also don't know when the game starts.
