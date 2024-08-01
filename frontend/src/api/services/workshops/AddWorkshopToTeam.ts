import { Workshop } from "@/types/workshop.interface";

interface AttendanceRecord {
    attendance: string;
    child_id: number;
  }
  
  export interface ApiBody {
    date: string;
    workshop_number: number;
    attendance: AttendanceRecord[];
  }

  const AddWorkshopToTeam = async (teamId: number, data: ApiBody): Promise<Workshop[]> => {
    try {
      const response = await fetch(
        `https://backend-staging-ffae.up.railway.app/api/v1/teams/${teamId}/workshops`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        }
      );
  
      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }
  
      const responseData: Workshop[] = await response.json();
      console.log("Data:", responseData);
      return responseData;
    } catch (error) {
      console.error("Error fetching data:", error);
      throw error;
    }
  };

export default AddWorkshopToTeam;
