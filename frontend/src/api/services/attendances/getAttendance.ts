interface Child {
  is_active: boolean;
  age: number;
  dob: string;
  gender: string;
  first_name: string;
  last_name: string;
  id: number;
}

interface Workshop {
  date: string;
  cancelled: boolean;
  cancellation_reason: string;
  id: number;
  team_id: number;
}

interface ApiResponse {
  attendance: string;
  child: Child;
  workshop: Workshop;
}

const getAttendance = async (childId: number, communityId: number): Promise<ApiResponse[]> => {
  try {
    const response = await fetch(
      `https://backend-production-7bbc.up.railway.app/api/v1/attendance?child_id=${childId}&community_id=${communityId}`,
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

    const data: ApiResponse[] = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

export default getAttendance;
