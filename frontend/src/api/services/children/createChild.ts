interface ApiResponse {
    team_id: number,
    age: number,
    dob: string,
    gender: string,
    first_name: string,
    last_name: string
}

const createChild = async (): Promise<ApiResponse[]> => {
try {
  const response = await fetch(`https://backend-production-7bbc.up.railway.app/api/v1/children`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  });
  console.log('Data:', response.json());
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

export default createChild;
