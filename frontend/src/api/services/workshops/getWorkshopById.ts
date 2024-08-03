import { WorkshopAttendance } from "@/types/workshopAttendance.interface";

const getWorkshopById = async (workshopId: number): Promise<WorkshopAttendance> => {
  try {
    // Updated mock response to include the missing `number` property
    const response: WorkshopAttendance = {
      workshop: {
        name: "Workshop 1",
        id: 1000,
        number: 1,
        date: "2021-01-01",
      },
      attendance: [
        {
          attendance: "present",
          child_id: 1,
          first_name: "Nelson",
          last_name: "Mandela",
        },
        {
          attendance: "present",
          child_id: 2,
          first_name: "Kasper",
          last_name: "Vin",
        },
      ],
    };

    return response;

    // Uncomment and use the following code to fetch real data
    // const response = await fetch(`https://backend-staging-ffae.up.railway.app/api/v1/workshops/${workshopId}`, {
    //   method: 'GET',
    //   headers: {
    //     'Content-Type': 'application/json'
    //   }
    // });
    // if (!response.ok) {
    //   throw new Error(`Error: ${response.statusText}`);
    // }
    // const data: ApiResponse = await response.json();
    // return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

export default getWorkshopById;
