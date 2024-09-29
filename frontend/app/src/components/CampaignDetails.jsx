import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';

function CampaignDetails() {
  const { id } = useParams();
  const [campaign, setCampaign] = useState(null);

  useEffect(() => {
    fetchCampaignDetails();
  }, []);

  const fetchCampaignDetails = async () => {
    try {
      const response = await fetch(`http://localhost:8000/campaign/${id}/`);
      if (!response.ok) {
        throw new Error(`Error fetching campaign: ${response.statusText}`);
      }
      const data = await response.json();
      setCampaign(data);
    } catch (err) {
      console.log(err);
    }
  };

  if (!campaign) return <p>Loading...</p>;

  return (
    <div className="campaign-details">
      <h1>{campaign.campaign_name}</h1>
      <p><strong>Goal:</strong> {campaign.campaign_goal}</p>
      <p><strong>Age Range:</strong> {campaign.age_range}</p>
      <p><strong>Target Audience:</strong> {campaign.target_audience}</p>
      <p><strong>Tone:</strong> {campaign.tone}</p>
      <p><strong>Guidelines:</strong> {campaign.guidelines}</p>
      <Link to={`/campaign/${id}/generated_post`}>View Generated Instagram Post</Link>
    </div>
  );
}

export default CampaignDetails;
