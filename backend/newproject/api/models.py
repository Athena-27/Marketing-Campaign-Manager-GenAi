from django.db import models

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    goal = models.CharField(max_length=255)
    age_range = models.CharField(max_length=50)  # Store as a string like "18-35"
    target_audience = models.TextField()  # Describes the target audience
    tone = models.CharField(max_length=255)  # Describes the brand tone (e.g., casual, formal)
    guidelines = models.TextField()  # Any additional guidelines for the campaign

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class InstagramPost(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="instagram_posts")
    caption = models.TextField()
    hashtags = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255)
    image_description = models.TextField()
    call_to_action = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Instagram Post for {self.campaign.name}"
