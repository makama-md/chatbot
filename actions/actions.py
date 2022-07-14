# This files contains your custom actions which can be used to run
# custom Python code.
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I am sorry, I don’t understand the question. You can reach our helpline on +2348178778501 or email: ncair@nitda.gov.ng for further clarification.")

        return []

