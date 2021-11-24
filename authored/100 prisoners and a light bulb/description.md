### Story
There are 100 prisoners in solitary cells. There's a central living room with one light bulb; this bulb is initially off. No prisoner can see the light bulb from his or her own cell. Everyday, the warden picks a prisoner equally at random, and that prisoner visits the living room. While there, the prisoner can toggle the bulb if he or she wishes. Also, the prisoner has the option of asserting that all 100 prisoners have been to the living room by now. If this assertion is false, all 100 prisoners are shot. However, if it is indeed true, all prisoners are set free and inducted into MENSA, since the world could always use more smart people. Thus, the assertion should only be made if the prisoner is 100% certain of its validity. The prisoners are allowed to get together one night in the courtyard, to discuss a plan. What plan should they agree on, so that eventually, someone will make a correct assertion?

### Task
Change the initial code to allow the prisoners to win their freedom. You can assume that the prisoners can count how may days have elapsed (it increases by 1 every time) and that the initial state of the light bulb is off (False).
The code that you are given consists of:
* a class ```Prisoner``` with some methods. You can rewrite this class, but the the class cannot have static attributes and:
  * the constructor must take a string for the name (of length less than 1000) and an integer for the counter (of value less than 1000);
  * it has an ```enter_room``` method that takes in a boolean for the current state of the light bulb and an integer for the current day. It returns a tuple (an array in JavaScript) of two booleans, the first for the new state of the ligth bulb and the second one for the assertion;
* a function```gather_and_discuss``` that returns a tuple (an array in JavaScript) of 100 objects of type ```Prisoner```.

### Examples
In the example test the prisoners are taken in the room in order, from first to last, and then the cycle repeats:
* if an assertion is made before the 100th day, the prisoners are shot;
* if an assertion is made at or after the 100th day, the prisoners are set free;
* if no assertion is made after 80 years (29200), the prisoners are shot.

An assertion can be made anytime between the 100th and the 29200th day.

### Note
Review the following list when you get error messages from the anti-cheating tests:
* **DO** return a tuple (an array in JavaScript) of 100 objects of type ```Prisoner``` from the ```gather_and_discuss``` function;
* **DO** construct ```Prison``` objects just with a name of type ```str``` of length less than 1000, and a counter of type ```int``` of value less than 1000;
* **DO NOT** give static attributes to the ```Prisoner``` class;
* **DO NOT** create other variables in the global environment besides ```Prisoner``` or ```gather_and_discuss```;
* **DO NOT** use the ```global``` variables.
* **DO NOT** rename ```Prisoner``` or ```gather_and_discuss```;

In short, keep in mind that the prisoners cannot comunicate in any way other than through the light bulb after the first night.

### Constraints
* the prisoners are chosen at random;
* the prisoners have at least 29200 days to make an assertion.
