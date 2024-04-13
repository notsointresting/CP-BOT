import re
import requests
from bs4 import BeautifulSoup

def extract_codechef_data(profile_url):
    """Extracts CodeChef user data from a profile URL."""

    # Fetch the HTML content
    response = requests.get(profile_url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    

    # Extract username
    username_tag = soup.find('span', class_='m-username--link')
    username = username_tag.text.strip() if username_tag else None

    # Extract global rank and division
    global_rank_tag = soup.find('a', href='/ratings/all')
    if global_rank_tag:
        global_rank_text = global_rank_tag.text.strip()
        match = re.search(r'(\d+)\s*\(Div\s*(\d+)\)', global_rank_text)
        if match:
            global_rank, division = match.groups()
        else:
            global_rank, division = global_rank_text, None
    else:
        global_rank, division = None, None

    # Extract country rank (if available)
    country_rank_tag = soup.find('a', href=re.compile(r'/ratings/all\?filterBy=Country%3D\w+'))
    country_rank = country_rank_tag.text.strip() if country_rank_tag else None

    # Extract number of problems solved (corrected)
    solved_count_tag = soup.find('h3', string=re.compile(r'Practice Problems \(\d+\):'))
    if solved_count_tag:
        match = re.search(r'\((\d+)\)', solved_count_tag.string.strip()) 
        solved_count = int(match.group(1)) if match else None
    else:
        solved_count = None

    # Extract current rating
    rating_tag = soup.find('div', class_='rating-number')
    current_rating = int(rating_tag.text.strip()) if rating_tag else None

    # Get Division
    if current_rating in range(0,1400):
        division = '4'
    elif current_rating in range(1400,1600):
        division = '3'
    elif current_rating in range(1600,1800):
        division = '2'
    else:
        division = '1'

    # Contest participated
    contest_count_element = soup.find('div', class_='contest-participated-count')

    # Extract the count (assuming the format "No. of Contests Participated: **XX**")
    if contest_count_element:
        contest_count = int(contest_count_element.find('b').text)
        contest_participated = contest_count
    else:
        contest_participated = None

    


    return {
        'username': username,
        'global_rank': global_rank,
        'country_rank': country_rank,
        'division': division, 
        'solved_count': solved_count,
        'current_rating': current_rating,
        'contest_participated': contest_participated
        

    }

def extract_leetcode_data(profile_url):
    # Make the request
    response = requests.get(profile_url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        
        # Extract ranking
        ranking = data.get('ranking')

        # Extract length of submissionCalendar (Streak)
        submission_calendar_length = len(data.get('submissionCalendar', {}))-24
    
    return {
        'ranking': ranking,
        'streak': submission_calendar_length
    }
