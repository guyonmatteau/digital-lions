interface ApiResponse {
  name: string
  id: number
}

const getTeams = async (): Promise<ApiResponse[]> => {
try {
  const response = await fetch('https://backend-production-7bbc.up.railway.app/api/v1/teams', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  })

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

export default getTeams;
