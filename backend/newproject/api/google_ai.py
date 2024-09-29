from dotenv import dotenv_values
import google.generativeai as genai

# --- Configuration ---
config = dotenv_values('C:/Projects/Project2/.env')
GOOGLE_API_KEY = config.get('api_key')

# Ensure API key is available
if not GOOGLE_API_KEY:
    raise ValueError("Google API key not found in .env file")

# Configure Generative AI API
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_instagram_content(campaign_name, target_audience, brand_tone, goal, guidelines):
    """
    Generates Instagram post content based on user inputs.
    
    :param campaign_name: The name of the marketing campaign
    :param target_audience: A description of the target audience
    :param brand_tone: The desired tone for the brand (e.g., formal, casual)
    :param goal: The goal of the campaign (e.g., increase sales, brand awareness)
    :param guidelines: Additional brand guidelines to consider
    :return: A dictionary containing caption, hashtags, slogan, image description, and call to action
    """
    # Constructing the prompt dynamically using user input
    prompt = f"""
    You are tasked with generating Instagram marketing content for a campaign.
    
    Campaign Name: {campaign_name}
    Target Audience: {target_audience}
    Brand Tone: {brand_tone}
    Campaign Goal: {goal}
    Guidelines: {guidelines}
    

    Please create a compelling Instagram post with the following details:
    - A caption
    - Relevant hashtags
    - A short slogan
    - A description of the image to be used
    - A call to action (e.g., "Shop now", "Learn more")
    
    #I WANT THE ALL THESE WITH SUBHEADING AND DON'T ADD UNNECESSARY TEXT IN THE OUTPUT. ONLY THE REQUIRED INFORMATION SHOULD BE IN THE OUTPUT.
    #FOLLOW BELOW EXAMPLE:
    Caption: "Fall is coming, so shop now for the best clothing in style!"
    Hashtags: #FallWinter2022 #Clothing #ShopNow
    Slogan: "Fall is coming, so shop now!"
    Image Description: "Fall is coming, so shop now for the best clothing in style!"
    Call to Action: "Shop now"
    
    """
    
    try:
        # Generate content using Gemini AI
        response = model.generate_content(prompt)
        
        # Log the raw AI response to inspect its structure
        generated_text = response.text
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("Raw Response from AI:", generated_text)
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        
        # Example of a more structured parsing using keyword markers
        content_sections = {
            "caption": "",
            "hashtags": "",
            "slogan": "",
            "image_description": "",
            "call_to_action": ""
        }

        # Use keywords to extract specific sections (e.g., "Caption:", "Hashtags:", etc.)
        # This assumes that Gemini will format the output with labels or sections
        for line in generated_text.splitlines():
            line = line.strip().replace("**", "")  # Remove the '**' symbols
            if line.lower().startswith("caption:"):
                content_sections["caption"] = line[len("Caption:"):].strip()
            elif line.lower().startswith("hashtags:"):
                content_sections["hashtags"] = line[len("Hashtags:"):].strip()
            elif line.lower().startswith("slogan:"):
                content_sections["slogan"] = line[len("Slogan:"):].strip()
            elif line.lower().startswith("image description:"):
                content_sections["image_description"] = line[len("Image Description:"):].strip()
            elif line.lower().startswith("call to action:"):
                content_sections["call_to_action"] = line[len("Call to Action:"):].strip()


        # Return the parsed content
        return content_sections
    
    except Exception as e:
        raise Exception(f"Error generating content with Gemini: {e}")
