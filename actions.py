# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ds = tracker.get_slot("dice_sides")
        dispatcher.utter_message(text=f"Hello World! selected Dice size: {ds}")

        return []


class ActionRollDice(Action):

    def name(self) -> Text:
        return "action_roll_dice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        result = random.randint(1,20)
        dispatcher.utter_message(text=f"you rolled a {result}")

        return []



class ActionRollDiceSized(Action):

    def name(self) -> Text:
        return "action_roll_dice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ds = tracker.get_slot("dice_sides")
        if ds != "human":
            result = random.randint(1,int(ds))
            dispatcher.utter_message(text=f"you rolled a {result} out of {ds}")
        else:
            dispatcher.utter_message(text="no value set yet :(")

        return []