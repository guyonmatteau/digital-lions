import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Accordion from "@/components/Accordion";
import CustomButton from "@/components/CustomButton";
import TextInput from "@/components/TextInput";
import * as Separator from "@radix-ui/react-separator";
import getCommunities from "@/api/services/communities/getCommunities";
import Loader from "@/components/Loader";
import createTeam from "@/api/services/teams/createTeam"; 
import createCommunity from "@/api/services/communities/createCommunity";

interface AccordionData {
  title: string;
  description?: string;
  teams: Team[];
  id: number; // Added id to store the community ID
}

interface Team {
  name: string;
  id: number;
}

const CommunityPage: React.FC = () => {
  const [communityName, setCommunityName] = useState("");
  const [teamName, setTeamName] = useState("");
  const [accordionData, setAccordionData] = useState<AccordionData[]>([]);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const fetchCommunities = async () => {
    setLoading(true);
    try {
      const communities = await getCommunities();
      const accordionDataFromApi: AccordionData[] = communities.map((community) => ({
        title: community.name,
        teams: [],
        id: community.id,
      }));
      setAccordionData(accordionDataFromApi);
    } catch (error) {
      console.error("Failed to fetch communities:", error);
    } finally {
      setLoading(false);
    }
  };
  

  useEffect(() => {
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

  const handleAddCommunity = async () => {
    if (communityName.trim() !== "") {
      setLoading(true);
      try {
        const newCommunity = await createCommunity(communityName);
        setAccordionData([...accordionData, { title: newCommunity.name, teams: [], id: newCommunity.id }]);
        setCommunityName(""); // Clear communityName input
      } catch (error) {
        console.error("Error adding community:", error);
      } finally {
        setLoading(false); 
      }
    }
  };

  const handleAddTeam = async (index: number) => {
    if (teamName.trim() !== "") {
      setLoading(true);
      try {
        const communityId = accordionData[index].id; 
        const response = await createTeam({
          name: teamName,
          communityId: communityId,
        });
  
        const newTeamId = response.id;
  
        const updatedAccordionData = [...accordionData];
        updatedAccordionData[index].teams.push({ name: teamName, id: newTeamId });
        setAccordionData(updatedAccordionData);
        setTeamName("");
      } catch (error: any) {
        console.error("Error creating team:", error);
        alert(error.message);
      } finally {
        setLoading(false);
      }
    }
  };

  const handleEditTeam = (teamId: number) => {
    navigate(`/teams/${teamId}`);
  };

  return (
    <div className="p-8">
      {loading && <Loader loadingText={"Loading communities"} />}
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
    </div>
  );
};

export default CommunityPage;
