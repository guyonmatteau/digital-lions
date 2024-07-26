import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import LinkCard from "@/components/LinkCard";
import Loader from "@/components/Loader";
import getTeamsOfCommunity from "@/api/services/teams/getTeamsOfCommunity"; 
import Layout from "@/components/Layout";
import TextInput from "@/components/TextInput";
import CustomButton from "@/components/CustomButton";
import createTeam from "@/api/services/teams/createTeam"; 

const TeamsPage: React.FC = () => {
  const { communityId } = useParams<{ communityId: string }>();

  const [teams, setTeams] = useState<{ name: string; id: number }[]>([]);
  const [loading, setLoading] = useState(false);
  const [teamName, setTeamName] = useState(""); 
  const [communityName, setCommunityName] = useState<string | null>(null);

  
  useEffect(() => {
    const storedState = localStorage.getItem('linkCardState');
    if (storedState) {
      const { communityName } = JSON.parse(storedState);
      setCommunityName(communityName);
    }
  }, []);

  const breadcrumbs = [
    { label: "Communities", path: "/communities" },
    { label: `${communityName}`, path: `/communities/${communityId}/teams` },
  ];

  // Fetch teams when the component mounts or when communityId changes
  useEffect(() => {
    const fetchTeams = async () => {
      setLoading(true);
      try {
        const teamsData = await getTeamsOfCommunity(Number(communityId)); 
        setTeams(teamsData);
      } catch (error) {
        console.error("Failed to fetch teams:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchTeams();
  }, [communityId]);

  const handleTeamNameChange = (value: string) => {
    setTeamName(value);
  };

  const handleTeamNameBlur = (value: string) => {
    setTeamName(value);
  };

  const handleAddTeam = async () => {
    if (teamName.trim() !== "") {
      setLoading(true);
      try {
        const newTeam = await createTeam({
          name: teamName,
          communityId: Number(communityId),
        });
        setTeams((prevTeams) => [
          ...prevTeams,
          { name: teamName, id: newTeam.id },
        ]);
        setTeamName(""); // Clear the input field
      } catch (error) {
        console.error("Error adding team:", error);
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <Layout breadcrumbs={breadcrumbs}>
      {loading && <Loader loadingText={"Loading teams"} />}
      <h1 className="text-2xl font-bold mb-4">Teams in {communityName}</h1>
      <TextInput
        className="mb-2"
        value={teamName}
        onChange={handleTeamNameChange}
        onBlur={handleTeamNameBlur}
        placeholder="Add a new team"
      />
      <CustomButton
        label="Add team"
        onClick={handleAddTeam}
        variant={"primary"}
        className="hover:bg-card-dark hover:text-white mb-4"
      />
      {teams.map((team) => (
        <LinkCard
          key={team.id}
          title={team.name}
          to={`/communities/${encodeURIComponent(String(communityId))}/teams/${encodeURIComponent(team.id)}`}
          state={{ communityName: communityName, teamName: team.name }}
          className="mb-2"
        />
      ))}
    </Layout>
  );
};

export default TeamsPage;
