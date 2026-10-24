from __future__ import annotations

from abc import ABC, abstractmethod


class AIProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class GoogleGeminiProvider(AIProvider):
    def __init__(self, api_key: str, model_name: str):
        import google.generativeai as genai

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name=model_name)

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text


def get_provider(provider_name: str, api_key: str, model_name: str) -> AIProvider:
    provider_name = (provider_name or "google").lower()

    if provider_name == "google":
        return GoogleGeminiProvider(api_key=api_key, model_name=model_name)

    raise ValueError(f"Unsupported AI provider: {provider_name}. Available provider: google")
