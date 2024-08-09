interface ApiBody {
  is_active: boolean;
  age: number | null;
  dob: string | null;
  gender: string | null;
  first_name: string;
  last_name: string;
}

const updateChildById = async ({
  childId,
  isActive,
  age,
  dateOfBirth,
  gender,
  firstName,
  lastName,
}: {
  childId: number;
  isActive: boolean;
  age: number  | null;
  dateOfBirth: string | null;
  gender: string | null;
  firstName: string;
  lastName: string;
}): Promise<void> => {
  try {
    const body: ApiBody = {
      is_active: isActive,
      age: age,
      dob: dateOfBirth,
      gender: gender,
      first_name: firstName,
      last_name: lastName,
    };

    const response = await fetch(
      `https://backend-staging-ffae.up.railway.app/api/v1/children/${childId}`,
      {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      }
    );
    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }
  } catch (error) {
    console.error("Error updating child data:", error);
    throw error;
  }
};

export default updateChildById;
