interface Child {
  first_name: string;
  last_name: string;
  age: number;
  date_of_birth: string;
  gender: string;
}

export interface BodyInput {
  name: string;
  children: Child[];
  community_id: number;
}

const createTeam = async ({
  firstName,
  lastName,
  age,
  dateOfBirth,
  gender,
  name,
  communityId,
}: {
  firstName: string;
  lastName: string;
  age: number;
  dateOfBirth: string;
  gender: string;
  name: string;
  communityId: number;
}): Promise<void> => {
  try {
    const response = await fetch(
      "https://backend-production-7bbc.up.railway.app/api/v1/teams",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(
          createInput({
            firstName,
            lastName,
            age,
            dateOfBirth,
            gender,
            name,
            communityId,
          })
        ),
      }
    );

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

function createInput({
  firstName,
  lastName,
  age,
  dateOfBirth,
  gender,
  name,
  communityId,
}: {
  firstName: string;
  lastName: string;
  age: number;
  dateOfBirth: string;
  gender: string;
  name: string;
  communityId: number;
}): BodyInput {
  const child: Child = {
    first_name: firstName,
    last_name: lastName,
    age: age,
    date_of_birth: dateOfBirth,
    gender: gender,
  };

  return {
    name: name,
    children: [child],
    community_id: communityId,
  };
}

export default createTeam;
