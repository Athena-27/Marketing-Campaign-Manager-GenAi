from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bson.objectid import ObjectId
from pymongo import MongoClient
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os

from .google_ai import generate_instagram_content

# Load environment variables for MongoDB connection
load_dotenv()
client = MongoClient("mongodb://localhost:27017/")
db = client["Instagram"]
campaigns_collection = db["campaigns"]
posts_collection = db["instagram_posts"]

@csrf_exempt
@api_view(['POST'])
def generate_instagram_post_view(request):
    """
    Generate Instagram post content for a campaign (POST request)
    """
    try:
        data = request.data

        # Log the incoming data to ensure it's received correctly
        campaign_name = data.get('campaign_name')
        campaign_goal = data.get('campaign_goal')
        age_range = data.get('age_range')
        target_audience = data.get('target_audience')
        tone = data.get('tone')
        guidelines = data.get('guidelines')

        # Validate required fields
        if not all([campaign_name, campaign_goal, age_range, target_audience, tone, guidelines]):
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Insert campaign data into MongoDB
        campaign_data = {
            "campaign_name": campaign_name,
            "campaign_goal": campaign_goal,
            "age_range": age_range,
            "target_audience": target_audience,
            "tone": tone,
            "guidelines": guidelines
        }
        result = campaigns_collection.insert_one(campaign_data)
        campaign_id = str(result.inserted_id)

        # Generate Instagram content using AI
        content = generate_instagram_content(campaign_name, target_audience, tone, campaign_goal, guidelines)

        # Ensure content is generated correctly
        if not content:
            return Response({"error": "Failed to generate Instagram content"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Save generated Instagram post to the database
        post_data = {
            "campaign_id": ObjectId(campaign_id),
            "caption": content.get('caption', ''),
            "hashtags": content.get('hashtags', ''),
            "slogan": content.get('slogan', ''),
            "image_description": content.get('image_description', ''),
            "call_to_action": content.get('call_to_action', ''),
        }
        posts_collection.insert_one(post_data)

        # Return the campaign ID in response
        return Response({"campaign_id": campaign_id}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_instagram_post_view(request, campaign_id):
    """
    Get the generated Instagram post content by campaign ID (GET request)
    """
    try:
        # Convert the campaign_id to ObjectId, check if it's valid
        try:
            campaign_id_obj = ObjectId(campaign_id)
        except Exception as e:
            return Response({"error": "Invalid campaign ID"}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch Instagram post by campaign ID from MongoDB
        post = posts_collection.find_one({"campaign_id": campaign_id_obj})

        if not post:
            return Response({"error": "Instagram post not found"}, status=status.HTTP_404_NOT_FOUND)

        # Prepare the content to be returned
        content = {
            "caption": post.get("caption", ""),
            "hashtags": post.get("hashtags", ""),
            "slogan": post.get("slogan", ""),
            "image_description": post.get("image_description", ""),
            "call_to_action": post.get("call_to_action", "")
        }
        return Response(content, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_campaigns_view(request):
    """
    List all the campaigns (GET request)
    """
    try:
        # Fetch all campaigns from MongoDB
        campaigns = campaigns_collection.find()
        campaigns_list = []

        for campaign in campaigns:
            campaigns_list.append({
                '_id': str(campaign['_id']),  # Convert ObjectId to string
                'campaign_name': campaign.get('campaign_name', ''),
                'campaign_goal': campaign.get('campaign_goal', ''),
                'age_range': campaign.get('age_range', ''),
                'target_audience': campaign.get('target_audience', ''),
                'tone': campaign.get('tone', ''),
                'guidelines': campaign.get('guidelines', ''),
            })

        if not campaigns_list:
            return Response({"error": "No campaigns found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(campaigns_list, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_campaign_details_view(request, campaign_id):
    """
    Get the campaign details by campaign ID (GET request)
    """
    try:
        # Convert the campaign_id to ObjectId
        try:
            campaign_id_obj = ObjectId(campaign_id)
        except Exception as e:
            return Response({"error": "Invalid campaign ID"}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch campaign by campaign ID from MongoDB
        campaign = campaigns_collection.find_one({"_id": campaign_id_obj})

        if not campaign:
            return Response({"error": "Campaign not found"}, status=status.HTTP_404_NOT_FOUND)

        # Prepare the content to be returned
        campaign_details = {
            "_id": str(campaign["_id"]),
            "campaign_name": campaign.get("campaign_name", ""),
            "campaign_goal": campaign.get("campaign_goal", ""),
            "age_range": campaign.get("age_range", ""),
            "target_audience": campaign.get("target_audience", ""),
            "tone": campaign.get("tone", ""),
            "guidelines": campaign.get("guidelines", ""),
        }
        return Response(campaign_details, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
