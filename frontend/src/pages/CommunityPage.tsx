import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Accordion from "@/components/Accordion";
import CustomButton from "@/components/CustomButton";
import TextInput from "@/components/TextInput";
import * as Separator from "@radix-ui/react-separator";
import getCommunities from "@/api/services/getCommunities";

interface AccordionData {
  title: string;
  description?: string;
  teams: Team[];
}

interface Team {
  name: string;
  // Add more fields as needed
}

const CommunityPage: React.FC = () => {
  const [communityName, setCommunityName] = useState("");
  const [teamName, setTeamName] = useState("");
  const [accordionData, setAccordionData] = useState<AccordionData[]>([]);
  const navigate = useNavigate();

  // Function to fetch communities on page load
  useEffect(() => {
    const fetchCommunities = async () => {
      try {
        const communities = await getCommunities();
        const accordionDataFromApi: AccordionData[] = communities.map((community) => ({
          title: community.name,
          teams: [],
        }));
        setAccordionData(accordionDataFromApi);
      } catch (error) {
        console.error("Failed to fetch communities:", error);
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

  const handleAddTeam = (index: number) => {
    const updatedAccordionData = [...accordionData];
    updatedAccordionData[index].teams.push({ name: teamName });
    setAccordionData(updatedAccordionData);
    setTeamName(""); // Clear teamName input
  };


  const handleEditTeam = (teamId: number) => {
    navigate(`/teams/${teamId}`);
  };

  return (
    <div className="p-8">
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
      />
      {accordionData.map((item, index) => (
        <Accordion
          key={index}
          title={item.title}
          description={item.description}
          className="mt-4"
        >
          {item.teams.map((team, teamIndex) => (
            <div
              key={teamIndex}
              className="flex items-center justify-between mb-2"
            >
              <p className="bg-text-light">{team.name}</p>
              <CustomButton label="Edit" variant="secondary"   onClick={() => handleEditTeam(team.id)} />
            </div>
          ))}
          {item.teams.length > 0 && <Separator.Root  className="bg-primary data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:h-full data-[orientation=vertical]:w-px my-[15px]" />}
            <TextInput
              className="mb-2"
              value={teamName}
              onChange={handleTeamNameChange}
              onBlur={handleTeamNameBlur}
            />
            <CustomButton
              label="Add team"
              onClick={() => handleAddTeam(index)}
              variant="secondary"
            />
        </Accordion>
      ))}
    </div>
  );
};

export default CommunityPage;
