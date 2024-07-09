import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Accordion from "@/components/Accordion";
import getTeams from "@/api/services/teams/getTeams";
import getTeamById from "@/api/services/teams/getTeamById";
import SelectInput from "@/components/SelectInput";
import CustomButton from "@/components/CustomButton";
import Modal from "@/components/Modal";
import TextInput from "@/components/TextInput";
import Loader from "@/components/Loader";

import { TeamWithChildren } from "@/types/teamWithChildren.interface";


interface Team {
  name: string,
  id: number
}

const TeamsPage: React.FC = () => {
  const { teamId } = useParams<{ teamId: string }>();
  const [teams, setTeams] = useState<Team[]>([]);
  const [selectedTeam, setSelectedTeam] = useState<TeamWithChildren | null>(null);
  const [modalVisible, setModalVisible] = useState(false);

  const [editChildId, setEditChildId] = useState<number | null>(null);
  const [editFirstName, setEditFirstName] = useState("");
  const [editLastName, setEditLastName] = useState("");
  const [editAge, setEditAge] = useState<number | null>(null); // Assuming age is a number
  const [editDateOfBirth, setEditDateOfBirth] = useState("");
  const [editGender, setEditGender] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [isLoadingTeam, setIsLoadingTeam] = useState(false)

  useEffect(() => {
    const fetchTeams = async () => {
      setIsLoading(true);
      try {
        const fetchedTeams = await getTeams();
        setTeams(fetchedTeams);
      } catch (error) {
        console.error("Failed to fetch teams:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchTeams();
  }, []);

  const handleTeamChange = async (value: string | number) => {
    const selectedId = typeof value === "string" ? parseInt(value, 10) : value;
    const selected = teams.find((team) => team.id === selectedId);

    if (selected) {
      setIsLoadingTeam(true)
      try {
        const teamDetails = await getTeamById(selected.id);
        setSelectedTeam(teamDetails);
      } catch (error) {
        console.error("Failed to fetch team details:", error);
      } finally {
        setIsLoadingTeam(false)
      }
    }
  };

  const handleAddChild = () => {
    setModalVisible(true);
  };

  const closeModal = () => {
    setModalVisible(false);
  };

  const handleFirstNameChange = (value: string) => {
    setEditFirstName(value);
  };

  const handleLastNameChange = (value: string) => {
    setEditLastName(value);
  };

  const handleAgeChange = (value: string) => {
    setEditAge(parseInt(value, 10));
  };

  const handleDateOfBirthChange = (value: string) => {
    setEditDateOfBirth(value);
  };

  const handleGenderChange = (value: string | number) => {
    setEditGender(value.toString()); // Ensure value is a string before setting state
  };

  const handleEditChild = (childId: number) => {
    const child = selectedTeam?.children.find((c) => c.id === childId);
    if (child) {
      setEditChildId(child.id);
      setEditFirstName(child.first_name);
      setEditLastName(child.last_name);
      setEditAge(child.age);
      setEditDateOfBirth(child.date_of_birth);
      setEditGender(child.gender);
      setModalVisible(true);
    }
  };

  return (
    <div className="p-8">
      {isLoading || isLoadingTeam && <Loader loadingText={"Loading teams"} />}
      {!isLoading && (
        <>
          <SelectInput
            className="mb-5"
            label={"Select team"}
            value={selectedTeam?.id}
            onChange={handleTeamChange}
          >
            <option value="">Select a team</option>
            {teams.map((team) => (
              <option key={team.id} value={team.id}>
                {team.name}
              </option>
            ))}
          </SelectInput>
          <CustomButton
            label="Add child"
            onClick={handleAddChild}
            variant={"primary"}
            className="hover:bg-card-dark hover:text-white"
          />

          {selectedTeam && (
            <>
              {selectedTeam.children.map((child, index) => (
                <Accordion
                  key={index}
                  title={`${child.first_name} ${child.last_name}`}
                  className="mt-2"
                >
                  <div>
                    <p>{`First Name: ${child.first_name}`}</p>
                    <p>{`Last Name: ${child.last_name}`}</p>
                    <div className="flex items-center justify-end border-t mt-4 border-gray-200 rounded-b dark:border-gray-600">
                      <CustomButton
                        className="mt-4"
                        label="Edit"
                        variant="secondary"
                        onClick={() => handleEditChild(child.id)}
                      />
                    </div>
                  </div>
                </Accordion>
              ))}
            </>
          )}

          {modalVisible && (
            <Modal onClose={closeModal} title="Add child">
              <TextInput
                className="mb-2"
                label="First Name"
                value={editFirstName}
                onChange={handleFirstNameChange}
              />
              <TextInput
                className="mb-2"
                label="Last Name"
                value={editLastName}
                onChange={handleLastNameChange}
              />
              <TextInput
                className="mb-2"
                label="Age"
                value={editAge?.toString() || ""}
                onChange={handleAgeChange}
              />
              <TextInput
                className="mb-2"
                label="Date of Birth"
                value={editDateOfBirth}
                onChange={handleDateOfBirthChange}
              />
              <SelectInput
                className="mb-2"
                label="Gender"
                value={editGender}
                onChange={handleGenderChange}
              >
                <option value="">Select gender</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
              </SelectInput>
            </Modal>
          )}
        </>
      )}
    </div>
  );
};

export default TeamsPage;
