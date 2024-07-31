import { Workshop } from "@/types/workshop.interface";

const getWorkShopsByTeam = async (teamId: number): Promise<Workshop[]> => {
  try {
    const response = await fetch(
      `https://backend-production-7bbc.up.railway.app/api/v1/teams/${teamId}/workshops`,
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

    const data: Workshop[] = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

export default getWorkShopsByTeam;
