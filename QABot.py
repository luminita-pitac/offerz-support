# --- Abstract Base Class ---
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam
import streamlit as st
import time
from openai import OpenAI
from abc import ABC, abstractmethod
class AbstractQABot(ABC):
    def __init__(self, faq_source: str):
        self.faq_source = faq_source
        self.load_faq()

    @abstractmethod
    def load_faq(self):
        pass

    @abstractmethod
    def answer_question(self, question: str) -> str:
        pass

# --- Concrete OpenRouter Bot ---
class OpenRouterQABot(AbstractQABot):
    def __init__(self, faq_source: str, api_key: str, site_url: str, site_name: str):
        super().__init__(faq_source)
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )
        self.site_url = site_url
        self.site_name = site_name

    def load_faq(self):
        with open(self.faq_source, "r") as f:
            self.faq = f.read()

    def answer_question(self, messages: list, retries: int = 5, delay: int = 5) -> str:
        # Start with a system instruction
        system_message = ChatCompletionSystemMessageParam(
            role="system",
            content="You are a helpful assistant that answers questions strictly based on the FAQ. "
                    "Always give clear, concise answers that are easy to understand and not too long. "
                    "If the FAQ doesn’t contain the answer, say 'I couldn’t find that in the FAQ, an Admin will contact you shortly.'"
        )

        # Always prepend the FAQ context at the beginning of the conversation
        faq_context = ChatCompletionUserMessageParam(
            role="user",
            content=f"FAQ: {self.faq}"
        )

        # Build the full message list = system + faq + conversation history
        all_messages = [system_message, faq_context] + messages

        for attempt in range(retries):
            try:
                completion = self.client.chat.completions.create(
                    extra_headers={
                        "HTTP-Referer": self.site_url,
                        "X-Title": self.site_name,
                    },
                    model="deepseek/deepseek-chat-v3-0324:free",
                    messages=all_messages
                )
                return completion.choices[0].message.content
            except Exception as e:
                error_msg = f"[Attempt {attempt + 1}/{retries}] Error: {e}"
                print(error_msg)
                st.session_state.setdefault("logs", []).append(error_msg)

                if attempt < retries - 1:
                    time.sleep(delay)
                else:
                    return "Sorry, the service is temporarily unavailable. Please try again later."
        return None
