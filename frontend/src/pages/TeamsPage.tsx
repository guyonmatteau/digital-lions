import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import Accordion from "@/components/Accordion";
import getTeams from "@/api/services/teams/getTeams";
import getTeamById from "@/api/services/teams/getTeamById";
import createChild from "@/api/services/children/createChild";
import updateChild from "@/api/services/children/updateChild";
import SelectInput from "@/components/SelectInput";
import CustomButton from "@/components/CustomButton";
import Modal from "@/components/Modal";
import TextInput from "@/components/TextInput";
import Loader from "@/components/Loader";
import { TeamWithChildren } from "@/types/teamWithChildren.interface";

interface Team {
  name: string;
  id: number;
}

const TeamsPage: React.FC = () => {
  const { teamId } = useParams<{ teamId: string }>();
  const [teams, setTeams] = useState<Team[]>([]);
  const [selectedTeam, setSelectedTeam] = useState<TeamWithChildren | null>(null);
  const [modalVisible, setModalVisible] = useState(false);

  const [editChildId, setEditChildId] = useState<number | null>(null);
  const [editFirstName, setEditFirstName] = useState("");
  const [editLastName, setEditLastName] = useState("");
  const [editAge, setEditAge] = useState<number | null>(null);
  const [editDateOfBirth, setEditDateOfBirth] = useState("");
  const [editGender, setEditGender] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [isLoadingTeam, setIsLoadingTeam] = useState(false);
  const [isEditingChild, setIsEditingChild] = useState(false);
  const [isAddingChild, setIsAddingChild] = useState(false);
  
  const navigate = useNavigate(); // Add navigate

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
      setIsLoadingTeam(true);
      try {
        const teamDetails = await getTeamById(selected.id);
        setSelectedTeam(teamDetails);

        // Update the URL parameter
        navigate(`/teams/${selected.id}`);
      } catch (error) {
        console.error("Failed to fetch team details:", error);
      } finally {
        setIsLoadingTeam(false);
      }
    }
  };

  const handleAddChild = () => {
    setIsAddingChild(true);
    setModalVisible(true);
  };

  const closeModal = () => {
    setModalVisible(false);
    setEditChildId(null);
    setEditFirstName("");
    setEditLastName("");
    setEditAge(null);
    setEditDateOfBirth("");
    setEditGender("");
    setIsAddingChild(false);
    setIsEditingChild(false);
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
    setEditGender(value.toString());
  };

  const handleEditChild = (childId: number) => {
    setIsEditingChild(true);
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

  const handleSaveChild = async () => {
    if (isEditingChild && editChildId !== null) {
      if (editAge !== null && editFirstName && editLastName) {
        const updatedChild = {
          childId: editChildId,
          isActive: true,
          age: editAge,
          dateOfBirth: editDateOfBirth || null,
          gender: editGender || null,
          firstName: editFirstName,
          lastName: editLastName,
        };

        try {
          await updateChild(updatedChild);
          const updatedTeam = await getTeamById(selectedTeam?.id!);
          setSelectedTeam(updatedTeam);
          closeModal();
        } catch (error) {
          console.error("Failed to update child:", error);
        }
      } else {
        console.error("Missing required fields for updating child");
      }
    } else if (isAddingChild) {
      if (editAge !== null && editFirstName && editLastName && selectedTeam) {
        const newChild = {
          teamId: selectedTeam.id,
          age: editAge,
          dateOfBirth: editDateOfBirth,
          gender: editGender,
          firstName: editFirstName,
          lastName: editLastName,
        };

        try {
          await createChild(newChild);
          const updatedTeam = await getTeamById(selectedTeam.id);
          setSelectedTeam(updatedTeam);
          closeModal();
        } catch (error) {
          console.error("Failed to create child:", error);
        }
      } else {
        console.error("Missing required fields for adding child");
      }
    }
  };

  return (
    <div className="p-8">
      {isLoading || (isLoadingTeam && <Loader loadingText={"Loading teams"} />)}
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
            <Modal
              onClose={closeModal}
              title={isEditingChild ? "Edit child" : "Add child"}
              acceptText={isEditingChild ? "Edit" : "Add"}
              onAccept={handleSaveChild}
            >
              <TextInput
                className="mb-2"
                label="First Name"
                value={editFirstName}
                onChange={handleFirstNameChange}
                required={true}
                errorMessage="Please enter your first name"
              />
              <TextInput
                className="mb-2"
                label="Last Name"
                value={editLastName}
                onChange={handleLastNameChange}
                required={true}
              />
              <TextInput
                className="mb-2"
                label="Age"
                value={editAge?.toString() || ""}
                onChange={handleAgeChange}
                required={true}
              />
              <TextInput
                className="mb-2"
                label="Date of Birth"
                value={editDateOfBirth}
                onChange={handleDateOfBirthChange}
                required={true}
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
              </SelectInput>
            </Modal>
          )}
        </>
      )}
    </div>
  );
};

export default TeamsPage;
