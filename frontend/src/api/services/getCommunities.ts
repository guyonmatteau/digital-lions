  interface ApiResponse {
    name: string;
    id: number;
  }

  const fetchData = async (): Promise<ApiResponse[]> => {
  try {
    const response = await fetch('http://backend-production-7bbc.up.railway.app/api/v1/communities', {
      method: 'GET',
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
    // const   response = [{"name":"Nothando","id":1},{"name":"Thandiwe","id":2},{"name":"Nokulunga","id":3},{"name":"Busisiwe","id":4},{"name":"Njabulo","id":5}]
    // return response
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
  };

  export default fetchData;
