# Brief overview
A discord bot which makes use of slash commands and Google's Gemini AI

# Details

<h3>
  main.py
</h3>

- I created my own instance of `discord.Bot`
- Set up a database pool within this instance
- Connected all the cogs within the cogs folder to this file
- Set up logging for the discord bot

<h3>
  Cogs
</h3>

- `help`: creates an instance of the discord default help command
- `on_message` is where I have implemented Google's Gemini AI
  - The bot AI generates responses to a user's input
- `on_ready` is invoked whenever the bot first starts
- `ping`: a slash command to test the latency of the discord bot

# Reflection
- Python is definitely my strongest programming language
- Unlike other programming languages, I have had several years of experience
- Making this discord bot has improved my knowledge of:
  - the discord library
  - use of APIs such as Google's Gemini AI
  - use of databases and SQL
