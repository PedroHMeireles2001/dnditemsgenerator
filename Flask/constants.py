import os
import dotenv

dotenv.load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

PROMPT_SHEET="Create a data sheet for a magic item in Dungeons & Dragons 5th Edition. Include details such as name, rarity, damage, gp value, item type, usage requirements, magical properties, and any additional information necessary to integrate the item into the game system in a balanced way.\nOnly respond if you receive an item, otherwise ignore."
PROMPT_VISUAL="You are an RPG master.\nYou will receive a general concept of an item and visually describe its appearance.\nOnly respond if it's an item, otherwise ignore.\nOnly include the visual description of the item in your output."