from pyrogram import Client
import asyncio

async def generate_session():
    print("Telegram String Session Generator\n")
    
    # Get user input
    api_id = input("Enter your API ID: ")
    api_hash = input("Enter your API Hash: ")
    
    # Create a client
    async with Client(
        name="my_account",
        api_id=api_id,
        api_hash=api_hash,
        in_memory=True
    ) as app:
        # Get the string session
        string_session = await app.export_session_string()
        
        # Save to Saved Messages
        await app.send_message("me", 
            f"**Your String Session**\n\n"
            f"`{string_session}`\n\n"
            "Keep this string safe! Never share it with anyone!"
        )
        
        print("\nSuccess! Your string session has been:")
        print("1. Generated successfully")
        print("2. Saved to your Telegram Saved Messages")
        print("\nPlease check your Saved Messages in Telegram.")

if __name__ == "__main__":
    try:
        # Run the async function
        asyncio.run(generate_session())
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("\nPlease make sure:")
        print("1. Your API ID and Hash are correct")
        print("2. You have a stable internet connection")
        print("3. You can receive Telegram messages/codes")