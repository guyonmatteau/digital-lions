import { TeamWithChildren } from "@/types/teamWithChildren.interface";

const getTeamById = async (teamsId: number): Promise<TeamWithChildren> => {
  try {
    const response = await fetch(`https://backend-staging-ffae.up.railway.app/api/v1/teams/${teamsId}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    });

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    const data: TeamWithChildren = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export default getTeamById;