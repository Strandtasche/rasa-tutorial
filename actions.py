# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
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


class ActionRollCheck(Action):

    def name(self) -> Text:
        return "action_roll_check"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        roller = "you" if ("character_name" not in tracker.slots.keys()) else tracker.get_slot("character_name")
        result = random.randint(1,20)
        dispatcher.utter_message(text=f"{roller} rolled a {result}")

        return []

class ChooseCheckForm(FormAction):
    """choose check form..."""
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "choose_check_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        """
        A list of required slots that the form has to fill
        """

        if tracker.get_slot("attribute") == "strength":
            return ["attribute", "character_name"]
        else:
            return ["attribute"]