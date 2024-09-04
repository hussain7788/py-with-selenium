# # components/translation_component.py

# from typing import Any, Text, Dict, List

# from rasa.nlu.components import Component
# from rasa.nlu.model import Metadata
# import requests

# class CustomTranslationComponent(Component):
#     name = "custom_translation_component"
#     provides = ["translated_text"]
#     requires = []
#     defaults = {}
#     language_list = ["hi"]

#     def __init__(self, component_config: Dict[Text, Any] = None) -> None:
#         super(CustomTranslationComponent, self).__init__(component_config)

#     def translate_text(self, text: Text) -> Text:
#         # Replace this with an actual translation service
#         translations = {
#             "नमस्ते": "hello",
#             "हैलो": "hello",
#             "कैसे हो?": "how are you?"
#         }
#         return translations.get(text, text)  # Default to returning the original text if no translation is found

#     def process(self, message, **kwargs) -> None:
#         translated_text = self.translate_text(message.text)
#         message.text = translated_text

#     def train(self, training_data, config, **kwargs) -> None:
#         pass

#     def load(self, model_dir, model_metadata: Metadata, cached_component, **kwargs) -> "CustomTranslationComponent":
#         return self

#     def persist(self, file_name: Text, model_dir: Text) -> None:
#         pass


# components/translation_component.py
# components/translation_component.py
# components/translation_component.py
# components/translation_component.py

# from typing import Any, Text, Dict, List
# from rasa.engine.graph import GraphComponent, ExecutionContext
# from rasa.engine.recipes.default_recipe import DefaultV1Recipe
# from rasa.shared.nlu.training_data.message import Message
# from rasa.shared.nlu.constants import TEXT
# from rasa.engine.storage.resource import Resource
# from rasa.engine.storage.storage import ModelStorage
# from rasa.shared.nlu.training_data.training_data import TrainingData
# from googletrans import Translator

# @DefaultV1Recipe.register([DefaultV1Recipe.ComponentType.MESSAGE_FEATURIZER], is_trainable=False)
# class CustomTranslationComponent(GraphComponent):
#     @classmethod
#     def create(
#         cls, config: Dict[Text, Any], model_storage: ModelStorage, resource: Resource, execution_context: ExecutionContext
#     ) -> GraphComponent:
#         return cls(config)

#     def __init__(self, config: Dict[Text, Any]) -> None:
#         self.config = config
#         self.translator = Translator()

#     def translate_text(self, text: Text) -> Text:
#         try:
#             translation = self.translator.translate(text, dest='en')
#             return translation.text
#         except Exception as e:
#             print(f"Error translating text: {e}")
#             return text

#     def process_training_data(self, training_data: TrainingData) -> TrainingData:
#         for example in training_data.training_examples:
#             translated_text = self.translate_text(example.get(TEXT))
#             example.set(TEXT, translated_text)
#         return training_data

#     def process(self, messages: List[Message]) -> List[Message]:
#         import pdb;pdb.set_trace()
#         for message in messages:
#             translated_text = self.translate_text(message.get(TEXT))
#             message.set(TEXT, translated_text)
#         import pdb;pdb.set_trace()
#         return messages


from typing import Any, Text, Dict, List
from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.constants import TEXT
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.training_data.training_data import TrainingData
from googletrans import Translator
import unicodedata
from langdetect import detect
import langid

@DefaultV1Recipe.register([DefaultV1Recipe.ComponentType.MESSAGE_FEATURIZER], is_trainable=False)
class CustomTranslationComponent(GraphComponent):
    @classmethod
    def create(
        cls, config: Dict[Text, Any], model_storage: ModelStorage, resource: Resource, execution_context: ExecutionContext
    ) -> GraphComponent:
        return cls(config)

    def __init__(self, config: Dict[Text, Any]) -> None:
        self.config = config
        self.translator = Translator()

    def normalize_text(self, text: Text) -> Text:
        try:
            normalized_text = unicodedata.normalize('NFC', text)
        except Exception as e:
            # print(f"Error normalizing text: {e}")
            return text
        return normalized_text

    def detect_language(self, text: Text) -> Text:
        try:
            lang, _ = langid.classify(text)
            return lang
        except Exception as e:
            print(f"Error detecting language: {e}")
            return 'unknown'

    def translate_text(self, text: Text) -> Text:
        normalized_text = self.normalize_text(text)
        print(f"Normalized text: {repr(normalized_text)}")
        try:
            language = self.detect_language(normalized_text)
            print(f"Detected language: {language}")
            if language != 'en':
                translation = self.translator.translate(normalized_text, dest='en')
                print(f"Translated text: {translation.text}")
                return translation.text
            return text
        except Exception as e:
            print(f"Error translating text: {e}")
            return text

    def process_training_data(self, training_data: TrainingData) -> TrainingData:
        for example in training_data.training_examples:
            translated_text = self.translate_text(example.get(TEXT))
            example.set(TEXT, translated_text)
        return training_data

    def process(self, messages: List[Message]) -> List[Message]:
        for message in messages:
            message_text = message.get(TEXT)
            print(f"Message text: {repr(message_text)}")
            translated_text = self.translate_text(message_text)
            message.set(TEXT, translated_text)
        return messages

