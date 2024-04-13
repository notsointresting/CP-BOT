## CPCopilot Bot: Fetching and Sending Programming Platform Updates

### Introduction
CPCopilot Bot is a Python script designed to fetch and send statistics and updates from two popular programming platforms, CodeChef and LeetCode, to a specified Telegram chat. The script runs daily and retrieves user data from the platforms' APIs. It then generates engaging messages containing the fetched statistics and sends them to the specified Telegram chat.

### Key Concepts
- **Telegram Bot**: A Telegram bot is an automated program that interacts with users through the Telegram messaging app. It can receive and send messages, handle commands, and perform various tasks.
- **CodeChef**: CodeChef is a competitive programming platform that hosts coding contests and provides a platform for programmers to practice and improve their skills. It offers a wide range of programming challenges and tracks users' performance through rankings and ratings.
- **LeetCode**: LeetCode is another popular platform for practicing coding skills and preparing for technical interviews. It offers a vast collection of coding problems and tracks users' progress through rankings and streaks.
- **API**: An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other. In this case, the script interacts with the CodeChef and LeetCode APIs to fetch user data.
- **Telegram Chat**: A Telegram chat refers to a conversation or group chat within the Telegram messaging app. The script sends the fetched statistics and updates to a specified Telegram chat.

### Code Structure
The Python script is structured as follows:

1. **Importing necessary libraries and modules**: 
    - `datetime`: Used to get the current day of the week.
    - `os`: Used to access environment variables.
    - `requests`: Used to make HTTP requests to the APIs.
    - `telepot`: A Python wrapper for the Telegram Bot API.
    - `dotenv`: Used to load environment variables from a .env file.
    - `telepot.loop.MessageLoop`: Used to handle incoming messages in the Telegram chat.
   
2. **Loading environment variables**: The script loads environment variables from a .env file, which contains the Telegram bot token and the target chat ID.

3. **Defining helper functions**: 
    - `create_engaging_message_codechef()`: Generates an engaging message with emojis containing CodeChef user data.
    - `send_profile_details()`: Sends the generated message to the specified Telegram chat after extracting user data from CodeChef.
    - Helper functions for LeetCode follow a similar pattern.

4. **Initializing the Telegram bot**: The script initializes the Telegram bot using the provided bot token.

5. **Fetching and sending updates**: 
    - The script checks the current day of the week.
    - If it is Wednesday, it fetches CodeChef updates and sends them to the target chat.
    - If it is Saturday or Sunday, it fetches LeetCode updates and sends them to the target chat.

### Instructions for User Configuration
To customize the CPCopilot Bot for your use, follow these steps:

1. **LeetCode Username**: Replace `'notsointresting'` with your LeetCode username in the `send_profile_details_leetcode()` function.
   
    Example:
    ```python
    send_profile_details_leetcode('https://leetcode-stats-api.herokuapp.com/your_username', TARGET_CHAT_ID)
    ```

2. **CodeChef Profile Link**: Replace `'https://www.codechef.com/users/sahiil_20'` with your CodeChef profile link in the `send_profile_details()` function.
   
    Example:
    ```python
    send_profile_details('https://www.codechef.com/users/your_username', TARGET_CHAT_ID)
    ```
### Conclusion
CPCopilot Bot simplifies the process of staying updated on programming platform statistics and contest schedules. By leveraging the Telegram messaging app, users can receive personalized updates and reminders to enhance their competitive programming journey.