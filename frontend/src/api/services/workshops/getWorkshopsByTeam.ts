import { WorkshopInfo } from "@/types/workshopInfo.interface";


const getWorkshopsByTeam = async (teamId: number): Promise<WorkshopInfo[]> => {
  try {
    const response = await fetch(
      `https://backend-staging-ffae.up.railway.app/api/v1/teams/${teamId}/workshops`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    // const response = [
    //   {
    //     "workshop": {
    //       "name": "Workshop 1",
    //       "id": 1000,    
    //       "number": 1,     
    //       "date": "2021-01-01",
    //     },
    //     "attendance": {
    //       "present": 6,
    //       "cancelled": 1,
    //       "absent": 3,
    //       "total": 10
    //     }
    //   }
    // ]
    // return response

    const data: WorkshopInfo[] = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

export default getWorkshopsByTeam;
