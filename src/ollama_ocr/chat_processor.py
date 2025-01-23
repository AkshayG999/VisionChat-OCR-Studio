import base64
import requests
import json
from typing import Dict, Any, List

class ChatProcessor:
    def __init__(self, model_name: str = "llama3.2-vision:11b",
                 base_url: str = "http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url
        self.chat_endpoint = f"{base_url}/api/chat"

    def _encode_image(self, image_path: str) -> str:
        """Convert image to base64 string"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def chat_with_image(self, image_path: str, prompt: str) -> str:
        """
        Process a chat interaction with an image
        
        Args:
            image_path: Path to the image file
            prompt: User's question or prompt about the image
            
        Returns:
            Model's response as a string
        """
        try:
            image_base64 = self._encode_image(image_path)
            
            # Prepare the request payload
            payload = {
                "model": self.model_name,
                "prompt": f"Please look at this image and answer the following question: {prompt}",
                "stream": False,
                "images": [image_base64]
            }

            # Make the API call to Ollama
            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()
            
            return response.json().get("response", "I couldn't process your request.")
            
        except Exception as e:
            return f"Error processing chat: {str(e)}"

    def chat(self, prompt: str) -> str:
        """
        Process a normal chat interaction
        
        Args:
            prompt: User's question or prompt
            
        Returns:
            Model's response as a string
        """
        try:
            # Prepare the request payload
            payload = {
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            }

            # Make the API call to Ollama
            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()
            
            return response.json().get("response", "I couldn't process your request.")
            
        except Exception as e:
            return f"Error processing chat: {str(e)}"

    def chat_stream(self, prompt: str, messages: List[Dict[str, str]] = None):
        """
        Process a chat interaction with streaming response and context
        
        Args:
            prompt: User's question or prompt
            messages: List of previous messages in the format [{"role": "...", "content": "..."}]
            
        Yields:
            Chunks of the model's response as they arrive
        """
        try:
            # Prepare chat messages
            formatted_messages = []
            if messages:
                for msg in messages:
                    formatted_messages.append({
                        "role": msg["role"],
                        "content": msg["content"]
                    })
            
            # Add current message
            formatted_messages.append({
                "role": "user",
                "content": prompt
            })

            # Prepare the request payload
            payload = {
                "model": self.model_name,
                "messages": formatted_messages,
                "stream": True
            }

            # Make the streaming API call to Ollama
            with requests.post(self.chat_endpoint, json=payload, stream=True) as response:
                response.raise_for_status()
                for line in response.iter_lines():
                    if line:
                        json_response = json.loads(line)
                        if 'message' in json_response:
                            yield json_response['message'].get('content', '')
                        
        except Exception as e:
            yield f"Error processing chat: {str(e)}"