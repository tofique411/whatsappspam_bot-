import asyncio
from playwright.async_api import async_playwright
import random

async def send_unofficial_msg():
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            user_data_dir="./whatsapp_session",
            headless=False
        )
        page = await browser.new_page()
        await page.goto("https://web.whatsapp.com")
        
        print("WhatsApp loading... Please wait.")
        
        # WhatsApp ko sahi se screen load karne ke liye 20 seconds ka time dein
        await asyncio.sleep(5)
        
        print("Searching for contact...")
        # WhatsApp Web ka universal shortcut jo search bar par focus karta hai
        await page.keyboard.press("Control+Alt+/")
        await asyncio.sleep(0.1)
        
        # Contact name type karein
        contact_name = "hello"
        await page.keyboard.type(contact_name)
        await asyncio.sleep(0.1)
        await page.keyboard.press("Enter")
        
        print("Chat khulne ka wait kar rahe hain...")
        await asyncio.sleep(1)
        
        # Direct keyboard se message type karna aur send karna (No complex selectors!)
        print("Messages sending...")
        for i in range(1000):
            await page.keyboard.type(f"dogesh bhai on top")
            await asyncio.sleep(0.1)
            await page.keyboard.press("Enter")
            # Safe interval takay ban na ho
          
            
        print("Kaam poora ho gaya! Browser close ho raha hai.")
        await asyncio.sleep(5)
        await browser.close()

asyncio.run(send_unofficial_msg())