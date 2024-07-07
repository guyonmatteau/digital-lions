import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Accordion from '@/components/Accordion';
import getChildren from '@/api/services/getChildren';
import getTeams from '@/api/services/getTeams';
import getTeamsById from '@/api/services/getTeamsById';

interface Team {
  id: number;
  name: string;
}

interface Child {
  id: number;
  first_name: string;
  last_name: string;
}

interface ApiResponse {
  is_active: boolean;
  name: string;
  id: number;
  children: Child[];
  community: {
    name: string;
    id: number;
  };
}

const TeamsPage: React.FC = () => {
  const { teamId } = useParams<{ teamId: string }>();
  const [teams, setTeams] = useState<Team[]>([]);
  const [selectedTeam, setSelectedTeam] = useState<ApiResponse | null>(null); // Use ApiResponse type for selectedTeam
  const [children, setChildren] = useState<Child[]>([]);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const fetchedTeams = await getTeams();
        setTeams(fetchedTeams);
      } catch (error) {
        console.error('Failed to fetch teams:', error);
      }
    };

    fetchTeams();
  }, []);

  const fetchChildren = async (teamId: number) => {
    try {
      const fetchedChildren = await getChildren();
      setChildren(fetchedChildren);
    } catch (error) {
      console.error('Failed to fetch children:', error);
    }
  };

  const handleTeamChange = async (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedId = parseInt(event.target.value, 10);
    const selected = teams.find((team) => team.id === selectedId);
    setSelectedTeam(null); // Reset selectedTeam to null
    setChildren([]); // Clear children
    if (selected) {
      try {
        const teamDetails = await getTeamsById(selected.id);
        console.log('teamDetails', teamDetails)
        setSelectedTeam(teamDetails); // Set selectedTeam with the fetched details
        fetchChildren(selected.id); // Fetch children for the selected team
      } catch (error) {
        console.error('Failed to fetch team details:', error);
      }
    }
  };

  return (
    <div className="p-8">
      <h1>Teams Page</h1>
      <select value={selectedTeam?.id} onChange={handleTeamChange}>
        <option value="">Select a team</option>
        {teams.map((team) => (
          <option key={team.id} value={team.id}>
            {team.name}
          </option>
        ))}
      </select>
      {selectedTeam && (
        <>
          <h2>{selectedTeam.name}</h2>
          <Accordion title="Children">
            {selectedTeam.children.map((child) => (
              <div key={child.id} className="mb-2">
                <p>{`${child.first_name} ${child.last_name}`}</p>
              </div>
            ))}
          </Accordion>
        </>
      )}
    </div>
  );
};

export default TeamsPage;
