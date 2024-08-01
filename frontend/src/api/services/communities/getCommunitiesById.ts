interface ApiResponse {
  name: string;
  id: number;
}

const getCommunities = async (communityId: string): Promise<ApiResponse[]> => {
  try {
    const response = await fetch(`https://backend-staging-ffae.up.railway.app/api/v1/communities/${communityId}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
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

export default getCommunities;
