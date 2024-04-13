from datetime import datetime
import os
import requests
import telepot
from dotenv import load_dotenv
from telepot.loop import MessageLoop

from profile import extract_codechef_data, extract_leetcode_data

# Get the day name
day_name = datetime.today().strftime('%A').lower()


load_dotenv()

# Importing API and Tokens from dotenv file.
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TARGET_CHAT_ID = os.getenv('TARGET_CHAT_ID')

def create_engaging_message_codechef(username, global_rank, country_rank, division, solved_count, current_rating, contest_participated):
    """Creates an engaging message with emojis for CodeChef stats."""
    # Get today's weekday and format contest time
    today = datetime.today().strftime("%A")
    contest_time = "8:00 PM"  # Assuming the contest is at 8 PM

    message = f"""
    🏆 <b>CodeChef Stats for {username}!</b> 🏆

    <b>Global Rank:</b> {global_rank} 🌎
    <b>Country Rank:</b> {country_rank} 🇮🇳  
    <b>Division:</b> {division} 
    <b>Problems Solved:</b> {solved_count} 💪
    <b>Current Rating:</b> {current_rating} ⭐
    <b>Contests Participated:</b> {contest_participated} 🏅

    <b>Exciting News!</b> 🎉
    Today is {today} and there's a Starters contest scheduled for {contest_time}. Get ready to code your way to the top! 🚀

    Good luck and happy coding! 🎉🎉🎉

    👉 <a href="https://www.github.com/notsointresting">Developer: Notsointresting</a> 👈
    """
    return message

def send_profile_details(profile_url, chat_id):
    user_data = extract_codechef_data(profile_url)

    if user_data:
        username = user_data['username']
        global_rank = user_data['global_rank']
        country_rank = user_data['country_rank']
        division = user_data['division']
        solved_count = user_data['solved_count']
        current_rating = user_data['current_rating']
        contest_participated = user_data['contest_participated']

        message = create_engaging_message_codechef(username, global_rank, country_rank, division, solved_count, current_rating, contest_participated)

        bot.sendMessage(chat_id=chat_id, text=message, parse_mode='HTML')
    else:
        bot.sendMessage(chat_id, "Failed to extract CodeChef user data.")

def create_engaging_message_leetcode(username, ranking, streak):
    """Creates an engaging message with emojis for LeetCode stats."""
    today = datetime.today().strftime("%A").lower()

    if today == 'saturday':
        contest_name = 'Biweekly Contest'
        contest_time = "8:00 PM"
    elif today == 'sunday':
        contest_name = 'Weekly Contest'
        contest_time = "8:00 AM"

    ranking = format(ranking, ",")
    message = f"""
    🏆 <b>LeetCode Stats for {username}!</b> 🏆

    <b>Rank:</b> {ranking} 🌎
    <b>Streak:</b> {streak} 💪
    <b>Badges:</b> <a href="https://leetcode-badge-showcase.vercel.app/api?username=notsointresting&theme=github-dark">LeetCode Badges</a> 🏅

    <b>Exciting News!</b> 🎉
    Today is {today} and there's a {contest_name} scheduled for {contest_time}. Get ready to code your way to the top! 🚀

    Good luck and happy coding! 🎉🎉🎉

    👉 <a href="https://www.github.com/notsointresting">Developer: Notsointresting</a> 👈
    """
    return message

def send_profile_details_leetcode(profile_url, chat_id):
    user_data = extract_leetcode_data(profile_url)

    if user_data:
        username = 'notsointresting'
        ranking = user_data['ranking']
        streak = user_data['streak']

        message = create_engaging_message_leetcode(username, ranking, streak)
        bot.sendMessage(chat_id=chat_id, text=message, parse_mode='HTML')
    else:
        bot.sendMessage(chat_id, "Failed to extract Leetcode user data.")

bot = telepot.Bot(TOKEN)

if day_name == 'wednesday':
    send_profile_details('https://www.codechef.com/users/sahiil_20', TARGET_CHAT_ID)
elif day_name == 'saturday' or day_name == 'sunday':
    send_profile_details_leetcode('https://leetcode-stats-api.herokuapp.com/notsointresting', TARGET_CHAT_ID)
