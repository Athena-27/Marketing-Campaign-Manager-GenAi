
---

## Project Title: **Instagram Post Generator with Campaign Management**

### Description

This project is a full-stack web application that allows marketing teams to create and manage marketing campaigns and generate Instagram posts using an AI-powered content generator. The application features a simple and intuitive interface for campaign creation, listing, and post-generation based on user inputs such as campaign goals, target audience, and brand tone. The generated posts include captions, hashtags, slogans, image descriptions, and a call to action, making it easier for marketing teams to focus on campaign strategy.

### Features
- **Campaign Management**: Create, list, and view detailed marketing campaigns.
- **AI-Powered Instagram Post Generator**: Generate Instagram post content (caption, hashtags, image description, etc.) using an AI model.
- **Simple and Intuitive UI**: Built with React, users can easily interact with the app through forms and lists.
- **MongoDB for Data Storage**: All campaigns and Instagram posts are stored in MongoDB.

---

## Installation and Setup Instructions

### Prerequisites

- **Python** (3.8+)
- **Node.js** (14.x+)
- **MongoDB** (locally or on cloud, e.g., MongoDB Atlas)
- **NPM** or **Yarn**
- **Django** and **Django REST Framework**
  
Ensure you have the following installed on your system:
- Python 3.8+
- Node.js & npm
- MongoDB (or a cloud MongoDB service like Atlas)

### Backend Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/instagram-post-generator.git
   cd instagram-post-generator
   ```

2. **Create and activate a virtual environment**:

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install backend dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:

   Create a `.env` file in the root directory and add your environment variables:
   ```bash
   GOOGLE_API_KEY=<your-google-api-key>
   ```

5. **Set up MongoDB connection**:
   
   In the `.env` file, ensure you have the MongoDB connection URL:
   ```bash
   MONGO_URI=mongodb://localhost:27017/your_database_name
   ```

6. **Run the Django backend**:

   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. **Navigate to the `frontend` directory**:

   ```bash
   cd frontend
   ```

2. **Install frontend dependencies**:

   ```bash
   npm install
   ```

3. **Run the frontend**:

   ```bash
   npm yarn dev
   ```

---

## Usage

### Campaign Management

1. **Creating a New Campaign**: 
   - Go to the home page and fill out the campaign form with details like name, goal, age range, target audience, tone, and guidelines.
   - Click on "Create Campaign."

2. **Viewing Campaign Details**:
   - After creating a campaign, you can view it in the list on the homepage.
   - Click on a campaign to view detailed information.

3. **Generating Instagram Post**:
   - Once you have created a campaign, click on "View Generated Instagram Post" to generate content like captions, hashtags, slogans, image descriptions, and call-to-action based on the campaign's input.

---

## API Endpoints

### Campaign Endpoints

- **Create Campaign**: `POST /campaign/generate/`
  - Creates a new campaign and generates Instagram post content.

- **Get Campaign Details**: `GET /campaign/<campaign_id>/`
  - Fetches the details of a specific campaign by ID.

- **List Campaigns**: `GET /campaigns/`
  - Fetches a list of all campaigns.

- **Get Generated Post**: `GET /campaign/<campaign_id>/generated_post`
  - Fetches the generated Instagram post for a specific campaign.

---

## Future Implementations

As this project grows, there are several exciting features we plan to implement to expand the application's capabilities and offer more advanced content generation for marketing campaigns:

### 1. **Brand Differentiation**:
   - **Custom Brand Tone and Style**: Deeper integration of AI to learn and differentiate between multiple brands based on their tone, style, and guidelines, creating more tailored posts.
   - **Brand-Specific Templates**: Pre-built templates and tone-of-voice configurations for various industries (e.g., retail, automotive, fashion) to reflect their specific language and visual style.
   - **Dynamic Brand Color and Font Integration**: Use brand colors and fonts to dynamically generate image descriptions and even design ideas for visual content.

### 2. **Scripting for Social Media Videos**:
   - **Short Video Scripts**: Expanding the AI's capabilities to generate scripts for short-form social media videos (e.g., Instagram Reels, TikTok) based on the campaign's content and goals.
   - **Full-Length Advertisement Scripts**: Adding AI-generated full-length video advertisement scripts for YouTube, TV commercials, and product demos that reflect the campaign’s goals and branding.
   - **Voiceover and Scene Descriptions**: Generate scene-by-scene descriptions for advertisements, including voiceover scripts, actor actions, and visual transitions, making it easier for teams to create professional-quality content.

### 3. **Multi-Platform Content Generation**:
   - **Expand to Other Social Media Platforms**: Integration with other platforms like Twitter, Facebook, LinkedIn, and TikTok to generate platform-specific content.
   - **Post Scheduling and Management**: Allow marketing teams to schedule posts directly from the app using APIs for social media platforms like Instagram and Facebook.

---

## Folder Structure

```bash
├── backend/
│   ├── manage.py
│   ├── yourapp/
│   │   ├── views.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── google_ai.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── CampaignList.jsx
│   │   │   ├── CampaignDetails.jsx
│   │   │   └── GeneratedPostDetails.jsx
│   ├── App.jsx
│   ├── index.jsx
├── .env
├── requirements.txt
└── README.md
```

---
