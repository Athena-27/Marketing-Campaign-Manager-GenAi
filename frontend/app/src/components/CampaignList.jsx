import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function CampaignList() {
  const [campaigns, setCampaigns] = useState([]);
  const [campaignName, setCampaignName] = useState("");
  const [campaignGoal, setCampaignGoal] = useState("");
  const [ageRange, setAgeRange] = useState("");
  const [targetAudience, setTargetAudience] = useState("");
  const [tone, setTone] = useState("");
  const [guidelines, setGuidelines] = useState("");

  useEffect(() => {
    fetchCampaigns();
  }, []);

  const fetchCampaigns = async () => {
    try {
      const response = await fetch("http://localhost:8000/campaigns/");
      if (!response.ok) {
        throw new Error(`Error fetching campaigns: ${response.statusText}`);
      }
      const data = await response.json();
      setCampaigns(data);
    } catch (err) {
      console.log(err);
    }
  };

  const addCampaign = async () => {
    const campaignData = {
      campaign_name: campaignName,
      campaign_goal: campaignGoal,
      age_range: ageRange,
      target_audience: targetAudience,
      tone: tone,
      guidelines: guidelines,
    };

    try {
      const response = await fetch("http://localhost:8000/campaign/generate/", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(campaignData),
      });
      if (!response.ok) {
        throw new Error(`Error creating campaign: ${response.statusText}`);
      }
      const data = await response.json();
      setCampaigns((prev) => [...prev, data]);
      setCampaignName("");
      setCampaignGoal("");
      setAgeRange("");
      setTargetAudience("");
      setTone("");
      setGuidelines("");
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="container">
      <h1>Create Instagram Campaign</h1>
      <form>
        <input
          type="text"
          placeholder="Campaign Name"
          value={campaignName}
          onChange={(e) => setCampaignName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Campaign Goal"
          value={campaignGoal}
          onChange={(e) => setCampaignGoal(e.target.value)}
        />
        <input
          type="text"
          placeholder="Age Range"
          value={ageRange}
          onChange={(e) => setAgeRange(e.target.value)}
        />
        <input
          type="text"
          placeholder="Target Audience"
          value={targetAudience}
          onChange={(e) => setTargetAudience(e.target.value)}
        />
        <input
          type="text"
          placeholder="Tone"
          value={tone}
          onChange={(e) => setTone(e.target.value)}
        />
        <textarea
          placeholder="Guidelines"
          value={guidelines}
          onChange={(e) => setGuidelines(e.target.value)}
        />
        <button type="button" onClick={addCampaign}>Create Campaign</button>
      </form>

      <h2>Campaign List</h2>
      {campaigns.length > 0 ? (
        <ul>
          {campaigns.map((campaign) => (
            <li key={campaign._id}>
              <Link to={`/campaign/${campaign._id}`}>{campaign.campaign_name}</Link>
            </li>
          ))}
        </ul>
      ) : (
        <p>No campaigns found</p>
      )}
    </div>
  );
}

export default CampaignList;
