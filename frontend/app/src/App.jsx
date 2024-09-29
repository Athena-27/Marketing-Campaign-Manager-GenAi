import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import CampaignList from './components/CampaignList';
import CampaignDetails from './components/CampaignDetails';
import GeneratedPostDetails from './components/GeneratedPostDetails';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<CampaignList />} />
          <Route path="/campaign/:id" element={<CampaignDetails />} />
          <Route path="/campaign/:id/generated_post" element={<GeneratedPostDetails />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
