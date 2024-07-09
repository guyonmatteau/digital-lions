interface ApiInput {
  is_active: boolean;
  name: string;
}

const getCommunities = async (
  communityId: string,
  input: ApiInput
): Promise<void> => {
  try {
    const response = await fetch(
      `https://backend-production-7bbc.up.railway.app/api/v1/communities/${communityId}`,
      {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(input),
      }
    );

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

export default getCommunities;
