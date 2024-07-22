interface ApiResponse {
    date: string;
    cancelled: false;
    cancellation_reason: string;
    id: number;
    team_id: number;
}

const getWorkShopById = async (workshopId: number): Promise<ApiResponse> => {
try {
  const response = await fetch(`https://backend-production-7bbc.up.railway.app/api/v1/workshops/${workshopId}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  });
  console.log('Data:', response.json());
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

export default getWorkShopById;
