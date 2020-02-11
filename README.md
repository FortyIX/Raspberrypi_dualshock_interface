# Raspberrypi dualshock interface
Allows you to control your raspberry pi and indeed any linux and mac (maybe windows?) with PS4 contoller dualshock(indeed any controller) base on pygame and pynput) 

## Dependencies 
You will need [pygame](https://www.pygame.org/) and [pynput](https://pypi.org/project/pynput/) in order to run this program properly </br>
```sudo pip install pygame pynput```

It is recommonded to run it within a independent environment, [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) can be used to do so </br>

``` conda create --name game_env python=3.x ```

and install dependencies into your environment 

## Documentation 
- Receivin joystick input ==> [this link](https://www.pygame.org/docs/ref/joystick.html?highlight=joystick)
- Simulate keyboard input ==> [this link](https://pypi.org/project/pynput/)

## Usage 
```python  raspberry_gamepad_interface.py  ```

## Futher Modification
It is possible that you modify the behaviour of each joystick input by modifing the event handlder in the code 
```python 


def AxisEventHandler(self, axis, degree)
    #define your action 
    
def ArrowButtonEventHandler(self,button)
    #define your action 


```
