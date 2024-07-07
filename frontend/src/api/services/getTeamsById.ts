import axios from 'axios';

interface Child {
  first_name: string;
  last_name: string;
  id: number;
}

interface Community {
  name: string;
  id: number;
}

interface ApiResponse {
  is_active: boolean;
  name: string;
  id: number;
  children: Child[];
  community: Community;
}

const fetchData = async (teamsId: number): Promise<ApiResponse> => {
  try {
    const response: ApiResponse = {
      "is_active": true,
      "name": "Team Siyabonga",
      "id": 1,
      "children": [
        {
          "first_name": "Zibuyile",
          "last_name": "Bhensela",
          "id": 1
        }
      ],
      "community": {
        "name": "Nokulunga",
        "id": 3
      }
    };
    
    return response; // Wrap response in an array
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export default fetchData;
