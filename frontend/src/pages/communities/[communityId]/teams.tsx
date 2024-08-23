import React, { useState, useEffect, useCallback } from "react";

import Loader from "@/components/Loader";
import Layout from "@/components/Layout";

import LinkCard from "@/components/LinkCard";
import TextInput from "@/components/TextInput";
import CustomButton from "@/components/CustomButton";
import Modal from "@/components/Modal";
import SkeletonLoader from "@/components/SkeletonLoader";

import createTeam from "@/api/services/teams/createTeam";
import getTeamsOfCommunity from "@/api/services/teams/getTeamsOfCommunity";

import { useRouter } from "next/router";

const TeamsPage: React.FC = () => {
  const router = useRouter();
  const { communityId } = router.query;
  // const { communityId } = useParams<{ communityId: string }>();
  const [teams, setTeams] = useState<{ name: string; id: number }[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [teamName, setTeamName] = useState("");
  const [communityName, setCommunityName] = useState<string | null>(null);
  const [isAddingTeam, setIsAddingTeam] = useState(false);
  const [openAddTeamModal, setOpenAddTeamModal] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string>("");

  useEffect(() => {
    const storedState = localStorage.getItem("linkCardState");
    if (storedState) {
      const { communityName } = JSON.parse(storedState);
      setCommunityName(communityName);
    }
  }, []);

  const breadcrumbs = [
    { label: "Communities", path: "/communities" },
    { label: `${communityName}`, path: `/communities/${communityId}/teams` },
  ];

  const fetchTeams = useCallback(async () => {
    setIsLoading(true);
    try {
      // Simulate a delay in fetching data
      await new Promise((resolve) => setTimeout(resolve, 300));

      const teamsData = await getTeamsOfCommunity(Number(communityId));
      setTeams(teamsData);
    } catch (error) {
      console.error("Failed to fetch teams:", error);
    } finally {
      setIsLoading(false);
    }
  }, [communityId]);

  useEffect(() => {
    fetchTeams();
  }, [fetchTeams]);

  const handleOpenTeamModal = () => {
    setOpenAddTeamModal(true);
  };

  const handleCloseTeamModal = () => {
    setOpenAddTeamModal(false);
  };

  const handleTeamNameChange = (value: string) => {
    setTeamName(value);
  };

  const handleTeamNameBlur = (value: string) => {
    setTeamName(value);
  };

  const handleAddTeam = async () => {
    if (teamName.trim() !== "") {
      setIsAddingTeam(true);
      try {
        const newTeam = await createTeam({
          name: teamName,
          communityId: Number(communityId),
        });
        setTeams((prevTeams) => [
          ...prevTeams,
          { name: teamName, id: newTeam.id },
        ]);
        setTeamName("");
        fetchTeams();
      } catch (error) {
        setErrorMessage(String(error));
        console.error("Error adding team:", error);
      } finally {
        setIsAddingTeam(false);
        setOpenAddTeamModal(false);
      }
    }
  };

  return (
    <Layout breadcrumbs={breadcrumbs}>
      {isLoading ? (
        <>
          <SkeletonLoader width="142px" type="button" />
          <div className="flex justify-between">
            <SkeletonLoader width="227px" height="40px" type="text" />
            <SkeletonLoader width="142px" type="button" />
          </div>
          {Array.from({ length: 5 }, (_, i) => (
            <SkeletonLoader key={i} type="card" />
          ))}
        </>
      ) : (
        <>
          {isAddingTeam && <Loader loadingText={"Adding new team"} />}
          <CustomButton
            label="Add team"
            onClick={handleOpenTeamModal}
            variant={"primary"}
            className="hover:bg-card-dark hover:text-white mb-4"
          />
          <div className="flex justify-between">
            <h1 className="text-2xl font-bold mb-4">
              Teams in {communityName}
            </h1>
            <CustomButton
              label="Show all"
              onClick={handleOpenTeamModal}
              variant={"secondary"}
              className="hover:bg-card-dark hover:text-white mb-4"
            />
          </div>
          {teams.map((team) => (
            <LinkCard
              key={team.id}
              title={team.name}
              href={`/communities/${communityId}/teams/${team.id}`}
              state={{ communityName: communityName, teamName: team.name }}
              className="mb-2"
            />
          ))}

          {openAddTeamModal && (
            <Modal
              onClose={handleCloseTeamModal}
              title="Add Team"
              acceptText="Add"
              onAccept={handleAddTeam}
              isBusy={isAddingTeam}
              isDisabledButton={!teamName}
            >
              <form
                onSubmit={(e) => {
                  e.preventDefault();
                  handleAddTeam();
                }}
              >
                <TextInput
                  className="mb-2"
                  label="Team name"
                  value={teamName}
                  onChange={handleTeamNameChange}
                  onBlur={handleTeamNameBlur}
                  autoFocus
                />
                {errorMessage && <p className="text-error">{errorMessage}</p>}
              </form>
            </Modal>
          )}
        </>
      )}
    </Layout>
  );
};

export default TeamsPage;
