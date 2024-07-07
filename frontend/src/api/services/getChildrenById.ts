interface ApiResponse {
  is_active: boolean;
  age: number;
  dob: string | null;
  gender: string | null;
  first_name: string;
  last_name: string;
  id: number;
}

const fetchData = async (childId: number): Promise<ApiResponse> => {
try {
  // const response = await fetch('https://backend-production-7bbc.up.railway.app/api/v1/communities', {
  //   method: 'GET',
  //   headers: {
  //     'Content-Type': 'application/json'
  //   }
  // });
  // console.log('Data:', response.json());
  // if (!response.ok) {
  //   throw new Error(`Error: ${response.statusText}`);
  // }
  // const data: ApiResponse[] = await response.json();
  // return data;
  const   response = {
    "is_active": true,
    "last_updated_at": "2024-07-07T06:19:15.634336",
    "created_at": "2024-07-07T06:19:15.634341",
    "age": 15,
    "dob": null,
    "gender": null,
    "first_name": "Zibuyile",
    "last_name": "Bhensela",
    "id": 1
  }
  return response
} catch (error) {
  console.error('Error fetching data:', error);
  throw error;
}
};

export default fetchData;
