import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Accordion from "@/components/Accordion";
import CustomButton from "@/components/CustomButton";
import TextInput from "@/components/TextInput";
import * as Separator from "@radix-ui/react-separator";
import getCommunities from "@/api/services/communities/getCommunities";
import Loader from "@/components/Loader";
import createTeam from "@/api/services/teams/createTeam"; // Import createTeam function

interface AccordionData {
  title: string;
  description?: string;
  teams: Team[];
}

interface Team {
  name: string;
  id: number;
}

const CommunityPage: React.FC = () => {
  const [communityName, setCommunityName] = useState("");
  const [teamName, setTeamName] = useState("");
  const [teamId] = useState(0); // Assuming teamId is managed differently in actual implementation
  const [accordionData, setAccordionData] = useState<AccordionData[]>([]);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  // Function to fetch communities on page load
  useEffect(() => {
    const fetchCommunities = async () => {
      setLoading(true);
      try {
        const communities = await getCommunities();
        const accordionDataFromApi: AccordionData[] = communities.map((community) => ({
          title: community.name,
          teams: [],
        }));
        setAccordionData(accordionDataFromApi);
      } catch (error) {
        console.error("Failed to fetch communities:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchCommunities();
  }, []);

  const handleTeamNameChange = (value: string) => {
    setTeamName(value);
  };

  const handleTeamNameBlur = (value: string) => {
    setTeamName(value);
  };

  const handleCommunityNameChange = (value: string) => {
    setCommunityName(value);
  };

  const handleCommunityNameBlur = (value: string) => {
    setCommunityName(value);
  };

  const handleAddCommunity = () => {
    if (communityName.trim() !== "") {
      const newAccordionItem: AccordionData = {
        title: communityName,
        teams: [], // Initialize teams array for each community
      };
      setAccordionData([...accordionData, newAccordionItem]);
      setCommunityName(""); // Clear communityName input
    }
  };

  const handleAddTeam = async (index: number) => {
    try {
      const response = await createTeam({
        firstName: teamName, // Assuming firstName maps to team name in API call
        lastName: "", // Adjust as per API requirements if necessary
        age: 0, // Adjust as per API requirements if necessary
        dateOfBirth: "", // Adjust as per API requirements if necessary
        gender: "", // Adjust as per API requirements if necessary
        name: teamName, // Assuming name maps to team name in API call
        communityId: 0, // Adjust as per API requirements if necessary
      });

      // Assuming API returns team ID or relevant data for further handling
      const newTeamId = response.id; // Adjust as per API response structure

      const updatedAccordionData = [...accordionData];
      updatedAccordionData[index].teams.push({ name: teamName, id: newTeamId });
      setAccordionData(updatedAccordionData);
      setTeamName(""); // Clear teamName input
    } catch (error) {
      console.error("Error creating team:", error);
      // Handle error state or feedback to user as needed
    }
  };

  const handleEditTeam = (teamId: number) => {
    navigate(`/teams/${teamId}`);
  };

  return (
    <div className="p-8">
      {loading && <Loader loadingText={"Loading communities"} />}
      {!loading && (
        <>
          <TextInput
            className="mb-2"
            label="Community name"
            value={communityName}
            onChange={handleCommunityNameChange}
            onBlur={handleCommunityNameBlur}
          />
          <CustomButton
            label="Add Community"
            onClick={handleAddCommunity}
            variant={"primary"}
            className="hover:bg-card-dark hover:text-white"
          />
          {accordionData.map((item, index) => (
            <Accordion
              key={index}
              title={item.title}
              description={item.description}
              className="mt-2"
            >
              {item.teams.map((team, teamIndex) => (
                <div
                  key={teamIndex}
                  className="flex items-center justify-between mb-2"
                >
                  <p className="bg-text-light">{team.name}</p>
                  <CustomButton label="Edit" variant="secondary" onClick={() => handleEditTeam(team.id)} />
                </div>
              ))}
              {item.teams.length > 0 && <Separator.Root className="bg-primary data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:h-full data-[orientation=vertical]:w-px my-[15px]" />}
              <TextInput
                className="mb-2"
                value={teamName}
                onChange={handleTeamNameChange}
                onBlur={handleTeamNameBlur}
              />
              <CustomButton
                label="Add team"
                disabled={teamName === ''}
                onClick={() => handleAddTeam(index)}
                variant="secondary"
                className="hover:bg-card-secondary-dark hover:text-white"
              />
            </Accordion>
          ))}
        </>
      )}
    </div>
  );
};

export default CommunityPage;
