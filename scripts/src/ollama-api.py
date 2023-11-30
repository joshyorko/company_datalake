import json
import asyncio
import aiohttp

class OllamaAPI:
    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.headers = {"Content-Type": "application/json"}
        self.generated_names = []  # List to store generated names

    async def generate_completion(self, model, prompt, existing_names):
        # Include the existing names in the prompt
        modified_prompt = prompt + "\nExisting Names: " + json.dumps(existing_names)
        payload = {"model": model, "prompt": modified_prompt}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=payload, headers=self.headers) as response:
                response_parts = []
                async for line in response.content:
                    if line:
                        decoded_line = line.decode("utf-8")
                        response_json = json.loads(decoded_line)
                        if "response" in response_json:
                            response_parts.append(response_json["response"])
        return "".join(response_parts)

    async def process_prompt(self, user_model_key, user_prompt):
        completion = await self.generate_completion(user_model_key, user_prompt, self.generated_names)
        self.generated_names.append(completion)  # Add the new name to the list
        print(completion)

async def main():
    ollama_api = OllamaAPI()
    USER_PROMPT = "Provide a Unique Software Company Name in json format {\"name\": \"<company_name>\"}}, return only json and nothing else"
    ITEMS_TO_RETURN = int(input("Enter number of items to return: "))
    for _ in range(ITEMS_TO_RETURN):
        await ollama_api.process_prompt("mistral", USER_PROMPT)

    # Write generated names to a JSON file
    with open("generated_names.json", "w", encoding="utf-8") as json_file:
        json.dump(ollama_api.generated_names, json_file, indent=4)

if __name__ == "__main__":
    asyncio.run(main())
