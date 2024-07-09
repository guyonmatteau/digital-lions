interface ApiResponse {
    name: string;
    id: number;
  }
  
  interface Attendance {
    attendance: string;
    child_id: number;
    workshop_id: number;
  }
  
  interface ApiBody {
    date: string;
    cancelled: boolean;
    cancellation_reason: string;
    team_id: number;
    attendance: Attendance[];
  }
  
  const createWorkshopToTeam = async (teamId: number, input: ApiBody): Promise<ApiResponse[]> => {
    try {
      const response = await fetch(`https://backend-production-7bbc.up.railway.app/api/v1/teams/${teamId}/workshops`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(input)
      });
  
      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }
  
      const data: ApiResponse[] = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error;
    }
  };
  
  export default createWorkshopToTeam;
  