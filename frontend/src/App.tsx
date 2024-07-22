import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from '@/components/Layout'; 
import CommunityPage from '@/pages/CommunityPage';
import TeamsPage from '@/pages/TeamsPage';
import WorkshopPage from '@/pages/WorkshopPage';
import LoginPage from '@/pages/LoginPage';

const App: React.FC = () => {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/login" element={<LoginPage/>} />
          <Route path="/community" element={<CommunityPage/>} />
          <Route path="/teams" element={<TeamsPage />} />
          <Route path="/teams/:teamId" element={<TeamsPage />} />
          <Route path="/workshop" element={<WorkshopPage/>} />
          <Route path="*" element={<LoginPage/>} />
        </Routes>
      </Layout>
    </Router>
  );
};

export default App;
