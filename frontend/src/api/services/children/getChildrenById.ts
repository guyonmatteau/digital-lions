interface ApiResponse {
  is_active: boolean;
  age: number;
  dob: string | null;
  gender: string | null;
  first_name: string;
  last_name: string;
  id: number;
}

const getChildrenById = async (childId: number): Promise<ApiResponse> => {
try {
  const response = await fetch(`https://backend-production-7bbc.up.railway.app/api/v1/children/${childId}`, {
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

export default getChildrenById;
