interface ApiBody {
  is_active: boolean;
  age: number;
  dob: string | null;
  gender: string | null;
  first_name: string;
  last_name: string;
}

const getChildrenById = async (
  childId: number,
  input: ApiBody
): Promise<void> => {
  try {
    const response = await fetch(
      `https://backend-production-7bbc.up.railway.app/api/v1/children/${childId}`,
      {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(input),
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

export default getChildrenById;
