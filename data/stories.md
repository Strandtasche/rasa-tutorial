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

## dont roll anything
* choose{"dice_sides":"human"}
  - slot{"dice_sides":"human"}
  - utter_abort

## roll check happy
* greet
  - utter_greet
  - utter_question
* full_check
  - form{"name":"choose_check_form"}
  - form{"name":null}
  - utter_request_confirmation
* confirmation
  - action_roll_check
