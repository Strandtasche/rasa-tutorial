## happy path
* greet
  - action_hello_world

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## action: hello world
* radiant
  - utter_ask_color

## roll a d20
* trigger_dice_roll
  - action_roll_dice

## roll a d4
* choose{"dice_sides":"d4"}
  - slot{"dice_sides":"d4"}
  - action_roll_dice_sized