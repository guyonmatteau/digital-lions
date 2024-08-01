interface ApiResponse {
  name: string;
  id: number;
}

const getCommunities = async (communityName: string): Promise<ApiResponse> => {
  try {
    const response = await fetch('https://backend-staging-ffae.up.railway.app/api/v1/communities', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ "name": communityName })
    });

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    const data: ApiResponse = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export default getCommunities;
