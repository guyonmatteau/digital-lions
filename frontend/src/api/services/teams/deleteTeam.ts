import { TeamWithChildren } from "@/types/teamWithChildren.interface";

interface ApiInput {
  teamId: number;
  cascade: boolean;
}

const deleteTeam = async ({
  teamId,
  cascade,
}: ApiInput): Promise<TeamWithChildren> => {
  try {
    const response = await fetch(
      `https://backend-production-7bbc.up.railway.app/api/v1/teams/${teamId}?cascade=${cascade}
`,
      {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    const data: TeamWithChildren = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

export default deleteTeam;
