import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import CommunityPage from '@/pages/CommunityPage';
import TeamsPage from '@/pages/TeamsPage';
import TeamsDetailPage from '@/pages/TeamsDetailPage';
import AttendancePage from '@/pages/AttendancePage';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/communities" element={<CommunityPage />} />
        <Route path="/communities/:communityId/teams" element={<TeamsPage />} />
        <Route path="/teams" element={<TeamsDetailPage />} />
        <Route path="/communities/:communityId/teams/:teamId" element={<TeamsDetailPage />} />
        <Route path="/attendance" element={<AttendancePage />} />
        <Route path="*" element={<CommunityPage />} />
      </Routes>
    </Router>
  );
};

export default App;
