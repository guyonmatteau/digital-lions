const getChildrenById = async (childId: number, cascade: boolean): Promise<void> => {
try {
  const response = await fetch(`https://backend-production-7bbc.up.railway.app/api/v1/children/${childId}?cascade=${cascade}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    },
  });

} catch (error) {
  console.error('Error fetching data:', error);
  throw error;
}
};

export default getChildrenById;
