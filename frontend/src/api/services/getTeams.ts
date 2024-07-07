import axios from 'axios';

interface ApiResponse {
    name: string
    id: number
}

const fetchData = async (): Promise<ApiResponse[]> => {
  try {
    // const response = await axios.get('/communities');
    // console.log('Data:', response.data);
    // return response.data;
    const response = [
        {
          "name": "Team Siyabonga",
          "id": 1
        },
        {
          "name": "Team Ndumiso",
          "id": 2
        },
        {
          "name": "Team SimphiweyiNkosi",
          "id": 3
        },
        {
          "name": "Team Thandeka",
          "id": 4
        },
        {
          "name": "Team Bhekokwakhe",
          "id": 5
        },
        {
          "name": "Team Dumisani",
          "id": 6
        },
        {
          "name": "Team Sihawukele",
          "id": 7
        },
        {
          "name": "Team Zibuyile",
          "id": 8
        },
        {
          "name": "Team Mthokozisi",
          "id": 9
        },
        {
          "name": "Team Dumisani",
          "id": 10
        },
        {
          "name": "Team Nothando",
          "id": 11
        },
        {
          "name": "Team Nomcebo",
          "id": 12
        },
        {
          "name": "Team Sphiwe",
          "id": 13
        },
        {
          "name": "Team Thalente",
          "id": 14
        },
        {
          "name": "Team Nokulunga",
          "id": 15
        },
        {
          "name": "Team Siphesihle",
          "id": 16
        },
        {
          "name": "Team Nomusa",
          "id": 17
        },
        {
          "name": "Team Thandazile",
          "id": 18
        },
        {
          "name": "Team Nonhlanhla",
          "id": 19
        },
        {
          "name": "Team Vusumuzi",
          "id": 20
        }
      ]
    return response
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export default fetchData;
