

import { Team } from "@/types/team.interface";

const getTeams = async (): Promise<Team[]> => {
try {
  const response = await fetch('https://backend-staging-ffae.up.railway.app/api/v1/teams', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  })

  if (!response.ok) {
    throw new Error(`Error: ${response.statusText}`);
  }

  const data: Team[] = await response.json();
  return data;
} catch (error) {
  console.error('Error fetching data:', error);
  throw error;
}
};

export default getTeams;
