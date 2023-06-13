import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    Scrape information from LinkedIn profiles.

    Args:
        linkedin_profile_url (str): The URL of the LinkedIn profile to scrape.

    Returns:
        dict: A dictionary containing scraped information from the LinkedIn profile.
    """
    # API endpoint for LinkedIn profile scraping
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"

    # Authorization header with API key
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    # Send GET request to the API endpoint with the profile URL and headers
    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    # Parse the response as JSON
    data = response.json()

    # Filter out empty or None values and unwanted keys from the data dictionary
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    # Remove the "profile_pic_url" key from each group dictionary, if present
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    # Return the scraped data dictionary
    return data