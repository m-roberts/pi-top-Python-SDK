from ptbuttons import PTUpButton, PTDownButton, PTSelectButton, PTCancelButton

up_button = PTUpButton()
down_button = PTDownButton()
select_button = PTSelectButton()
cancel_button = PTCancelButton()


def do_up_thing():
    print("Up button was pressed")


def do_down_thing():
    print("Down button was pressed")


def do_another_thing():
    print("do_another_thing invoked")


def select_something():
    print("select_something called")


# To invoke a function when the button is pressed/released, you can assign the function the when_pressed or when_released data member of a button
up_button.when_pressed = do_up_thing
down_button.when_pressed = do_down_thing
down_button.when_released = do_another_thing


# Another way to react to button events is to poll the is_pressed data member
while True:
    if select_button.is_pressed:
        select_something()