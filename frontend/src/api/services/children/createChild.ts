interface ApiResponse {
  team_id: number;
  age: number;
  dob: string;
  gender: string;
  first_name: string;
  last_name: string;
}

const createChild = async ({
  teamId,
  age,
  dateOfBirth,
  gender,
  firstName,
  lastName,
}: {
  teamId: number;
  age: number;
  dateOfBirth: string;
  gender: string;
  firstName: string;
  lastName: string;
}): Promise<ApiResponse> => {
  try {
    const response = await fetch(
      `https://backend-staging-ffae.up.railway.app/api/v1/children`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          team_id: teamId,
          age: age,
          dob: dateOfBirth,
          gender: gender,
          first_name: firstName,
          last_name: lastName,
        }),
      }
    );

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    const data: ApiResponse = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

export default createChild;
