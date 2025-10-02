import logging
from livekit.agents import function_tool,RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun
import os
import smtplib
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
from typing import Optional

@function_tool()
async def get_weather(
        context: RunContext,
        city: str) -> str:
    """Get the current weather for a given city"""
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            logging.info(f"Weather for {city}: {response.text.strip()}")
            return response.text.strip()   
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"Could not retrieve weather for {city}."
    except Exception as e:
        logging.error(f"Error retrieving weather for {city}: {e}")
        return f"An error occurred while retrieving weather for {city}." 

@function_tool()
async def search_web(
    context: RunContext,  # type: ignore
    query: str) -> str:
    """
    Search the web using DuckDuckGo.
    """
    try:
        results = DuckDuckGoSearchRun().run(tool_input=query)
        logging.info(f"Search results for '{query}': {results}")
        return results
    except Exception as e:
        logging.error(f"Error searching the web for '{query}': {e}")
        return f"An error occurred while searching the web for '{query}'." 
    

# Undecorated core function – works standalone
async def send_email_core(
    to_email: str,
    subject: str,
    message: str,
    cc_email: Optional[str] = None
) -> str:
    """
    Core email sending function using Gmail SMTP.
    Can be called directly for standalone testing.
    """
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_APP_PASSWORD")

    if not gmail_user or not gmail_password:
        return "❌ Gmail credentials not found in environment variables."

    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = gmail_user
        msg["To"] = to_email

        recipients = [to_email]
        if cc_email:
            msg["Cc"] = cc_email
            recipients.append(cc_email)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, recipients, msg.as_string())
        server.quit()

        logging.info(f"Email sent successfully to {', '.join(recipients)}")
        return f"✅ Email sent successfully to {', '.join(recipients)}"

    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        return f"❌ Failed to send email: {str(e)}"


# Decorated function for LiveKit agent usage
@function_tool()
async def send_email(context: RunContext, to_email: str, subject: str, message: str, cc_email: Optional[str] = None) -> str:
    print("DEBUG send_email called!")
    print("to_email:", to_email)
    print("subject:", subject)
    print("message:", message)
    print("cc_email:", cc_email)
    
    from tools import send_email_core
    return await send_email_core(to_email, subject, message, cc_email)
