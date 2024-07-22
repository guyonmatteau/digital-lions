import React, { useState, useEffect } from "react";
import SelectInput from "@/components/SelectInput";
import CustomButton from "@/components/CustomButton";
import Modal from "@/components/Modal";
import TextInput from "@/components/TextInput";
import Loader from "@/components/Loader";
import Accordion from "@/components/Accordion";
import { Team } from "@/types/team.interface";
import { Child } from "@/types/child.interface";
import { Workshop } from "@/types/workshop.interface";

const WorkshopPage: React.FC = () => {
  const [programs, setPrograms] = useState([]);
  const [teams, setTeams] = useState<Team[]>([]);
  const [selectedProgramId, setSelectedProgramId] = useState<number | null>(null);
  const [selectedTeamId, setSelectedTeamId] = useState<number | null>(null);
  const [workshops, setWorkshops] = useState<Workshop[]>([]);
  const [modalVisible, setModalVisible] = useState(false);
  const [editWorkshopNumber, setEditWorkshopNumber] = useState<number | null>(null);
  const [editDate, setEditDate] = useState("");
  const [editAttendance, setEditAttendance] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isLoadingWorkshop, setIsLoadingWorkshop] = useState(false);

  useEffect(() => {
    const fetchPrograms = async () => {
      setIsLoading(true);
      try {
        const programsData = await fetch('/api/programs').then(res => res.json());
        setPrograms(programsData);
        setSelectedProgramId(programsData[0]?.id || null);
      } catch (error) {
        console.error("Failed to fetch programs:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchPrograms();
  }, []);

  useEffect(() => {
    const fetchTeams = async () => {
      if (!selectedProgramId) return;

      setIsLoading(true);
      try {
        const teamsData: Team[] = await fetch(`/api/programs/${selectedProgramId}/teams`).then(res => res.json());
        setTeams(teamsData);
        setSelectedTeamId(teamsData[0]?.id || null);
      } catch (error) {
        console.error("Failed to fetch teams:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchTeams();
  }, [selectedProgramId]);

  useEffect(() => {
    const fetchWorkshops = async () => {
      if (!selectedTeamId) return;

      setIsLoadingWorkshop(true);
      try {
        const workshopsData: {program_id: number, workshops: Workshop[]} = await fetch(`/api/teams/${selectedTeamId}/workshops`).then(res => res.json());
        setWorkshops(workshopsData.workshops);
      } catch (error) {
        console.error(`Failed to fetch workshops for team ${selectedTeamId}:`, error);
      } finally {
        setIsLoadingWorkshop(false);
      }
    };

    fetchWorkshops();
  }, [selectedTeamId]);

  const handleProgramChange = (value: string | number) => {
    setSelectedProgramId(typeof value === "string" ? parseInt(value, 10) : value);
    setSelectedTeamId(null);
    setWorkshops([]);
  };

  const handleTeamChange = (value: string | number) => {
    setSelectedTeamId(typeof value === "string" ? parseInt(value, 10) : value);
  };

  const handleAddWorkshop = (workshopNumber: number) => {
    const workshop = workshops.find(w => w.workshop_number === workshopNumber);
    if (workshop) {
      setEditWorkshopNumber(workshop.workshop_number);
      setEditDate(workshop.date || "");
      setEditAttendance(workshop.attendance);
      setModalVisible(true);
    }
  };

  const handleAttendanceChange = (childId: number, attendance: "present" | "absent") => {
    setEditAttendance(prevAttendance =>
      prevAttendance.map(child =>
        child.child_id === childId ? { ...child, attendance } : child
      )
    );
  };

  const handleSaveWorkshop = async () => {
    if (!selectedTeamId || editWorkshopNumber === null) return;

    const requestBody = {
      workshop_number: editWorkshopNumber,
      date: editDate,
      attendance: editAttendance
    };

    try {
      const response = await fetch(`/api/teams/${selectedTeamId}/workshops`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
      });

      if (!response.ok) {
        throw new Error(`Failed to save workshop: ${response.statusText}`);
      }

      const { id: workshopId } = await response.json();

      setWorkshops(prevWorkshops =>
        prevWorkshops.map(workshop =>
          workshop.workshop_number === editWorkshopNumber
            ? { ...workshop, workshop_id: workshopId, date: editDate, attendance: editAttendance }
            : workshop
        )
      );
      setModalVisible(false);
    } catch (error) {
      console.error("Failed to save workshop:", error);
    }
  };

  return (
    <div className="p-8">
      {(isLoading || isLoadingWorkshop) && <Loader loadingText="Loading..." />}
      {!isLoading && !isLoadingWorkshop && (
        <>
          <SelectInput
            className="mb-5"
            label="Select Program"
            value={selectedProgramId}
            onChange={handleProgramChange}
          >
            <option value="">Select a program</option>
            {programs.map((program) => (
              <option key={program.id} value={program.id}>
                {program.name}
              </option>
            ))}
          </SelectInput>
          {selectedProgramId && (
            <SelectInput
              className="mb-5"
              label="Select Team"
              value={selectedTeamId}
              onChange={handleTeamChange}
            >
              <option value="">Select a team</option>
              {teams.map((team) => (
                <option key={team.id} value={team.id}>
                  {team.name}
                </option>
              ))}
            </SelectInput>
          )}
          {selectedTeamId && workshops.map((workshop) => (
            <Accordion
              key={workshop.workshop_number}
              title={`Workshop ${workshop.workshop_number}`}
              className="mt-2"
            >
              {workshop.attendance.map((child) => (
                <div key={child.child_id} className="flex items-center justify-between mb-2">
                  <p>{`${child.first_name} ${child.last_name}`}</p>
                  <div>
                    <label className="mr-2">
                      <input
                        type="radio"
                        checked={child.attendance === "present"}
                        onChange={() => handleAttendanceChange(child.child_id, "present")}
                      />{" "}
                      Present
                    </label>
                    <label>
                      <input
                        type="radio"
                        checked={child.attendance === "absent"}
                        onChange={() => handleAttendanceChange(child.child_id, "absent")}
                      />{" "}
                      Absent
                    </label>
                  </div>
                </div>
              ))}
              <CustomButton
                label="Edit Attendance"
                variant="secondary"
                onClick={() => handleAddWorkshop(workshop.workshop_number)}
              />
            </Accordion>
          ))}
          {modalVisible && (
            <Modal onClose={() => setModalVisible(false)} title={`Edit Workshop ${editWorkshopNumber}`}>
              <TextInput
                className="mb-2"
                label="Date"
                value={editDate}
                onChange={setEditDate}
              />
              {editAttendance.map((child) => (
                <div key={child.child_id} className="flex items-center mb-2">
                  <p className="mr-2">{`${child.first_name} ${child.last_name}`}</p>
                  <label className="mr-2">
                    <input
                      type="radio"
                      checked={child.attendance === "present"}
                      onChange={() => handleAttendanceChange(child.child_id, "present")}
                    />{" "}
                    Present
                  </label>
                  <label>
                    <input
                      type="radio"
                      checked={child.attendance === "absent"}
                      onChange={() => handleAttendanceChange(child.child_id, "absent")}
                    />{" "}
                    Absent
                  </label>
                </div>
              ))}
              <CustomButton
                label="Save"
                variant="primary"
                onClick={handleSaveWorkshop}
                className="hover:bg-card-dark hover:text-white"
              />
            </Modal>
          )}
        </>
      )}
    </div>
  );
};

export default WorkshopPage;
