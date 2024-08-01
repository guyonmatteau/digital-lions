  interface Attendance {
    attendance: string;
    child_id: number;
  }
  
  interface ApiBody {
    date: string;
    workshop_number: number;
    attendance: Attendance[];
  }
  
  const createWorkshopToTeam = async (teamId: number, input: ApiBody): Promise<void> => {
    try {
      const response = await fetch(`https://backend-staging-ffae.up.railway.app/api/v1/teams/${teamId}/workshops`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(input)
      });
  
      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }
  
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error;
    }
  };
  
  export default createWorkshopToTeam;
  