import { TeamWithChildren} from '@/types/teamWithChildren.interface'

const getTeamById = async (teamsId: number): Promise<TeamWithChildren> => {
  try {
    // const response = await fetch(`https://backend-staging-ffae.up.railway.app/api/v1/teams/${teamsId}`, {
    //   method: 'GET',
    //   headers: {
    //     'Content-Type': 'application/json'
    //   }
    // });

    const response = {
      is_active: true,
      last_updated_at: "2024-08-02T08:31:04.816Z",
      created_at: "2024-08-02T08:31:04.816Z",
      id: 1,
      name: "The A-Team",
      community: {
        id: 1,
        name: "Khayelitsha",
      },
      children: [
        {
          id: 1,
          first_name: "Nelson",
          last_name: "Mandela",
        },
      ],
      program: {
        id: 1,
        name: "Program 1",
        progress: {
          current: 1,
          total: 12,
        },
      },
    };
    return response;
    // if (!response.ok) {
    //   throw new Error(`Error: ${response.statusText}`);
    // }

    // const data: TeamWithChildren = await response.json();
    // return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

export default getTeamById;
