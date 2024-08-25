import React, { useState, useEffect } from "react";
import VerticalStepper from "@/components/VerticalStepper";
import SelectInput from "@/components/SelectInput";
import getTeams from "@/api/services/teams/getTeams";
import getTeamById from "@/api/services/teams/getTeamById";
import addWorkshopToTeam from "@/api/services/workshops/addWorkshopToTeam";
import getWorkshopsByTeam from "@/api/services/workshops/getWorkshopsByTeam";
import getWorkshopById from "@/api/services/workshops/getWorkshopById";
import Layout from "@/components/Layout";
import { Team } from "@/types/team.interface";
import { TeamWithChildren } from "@/types/teamWithChildren.interface";
import { WorkshopInfo } from "@/types/workshopInfo.interface";
import { WorkshopAttendance } from "@/types/workshopAttendance.interface";
import Loader from "@/components/Loader";
import SkeletonLoader from "@/components/SkeletonLoader";

interface AttendanceRecord {
  attendance: string;
  child_id: number;
}

interface Attendance {
  date: string;
  workshop_number: number;
  attendance: AttendanceRecord[];
}

const AttendancePage: React.FC = () => {
  const [teams, setTeams] = useState<Team[]>([]);
  const [selectedTeam, setSelectedTeam] = useState<TeamWithChildren | null>(
    null
  );
  const [workshopDetails, setWorkshopDetails] = useState<WorkshopInfo[]>([]);
  const [attendance, setAttendance] = useState<Record<number, string>>({});
  const [isLoadingTeam, setIsLoadingTeam] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [isSavingAttendance, setIsSavingAttendance] = useState(false);
  const [isSaved, setIsSaved] = useState(false);

  useEffect(() => {
    const fetchTeams = async () => {
      setIsLoading(true);
      try {
        const fetchedTeams = await getTeams('active');
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
        const workshops = await getWorkshopsByTeam(selected.id);
        setSelectedTeam(teamDetails);
        setWorkshopDetails(workshops);
      } catch (error) {
        console.error("Failed to fetch team details:", error);
      } finally {
        setIsLoadingTeam(false);
      }
    }
  };

  const handleAttendanceChange = (childId: number, status: string) => {
    setAttendance((prev) => ({
      ...prev,
      [childId]: status,
    }));
  };

  const handleSaveAttendance = async () => {
    if (selectedTeam) {
      const apiBody: Attendance = {
        // if there is no workshpoDetails take the current Date
        date:
          workshopDetails.length === 0
            ? new Date().toISOString().split("T")[0]
            : workshopDetails[0].workshop.date.split("T")[0],
        workshop_number: selectedTeam.program.progress.current + 1,
        attendance: Object.entries(attendance).map(([childId, status]) => ({
          attendance: status,
          child_id: parseInt(childId, 10),
        })),
      };
      setIsSavingAttendance(true);
      setIsSaved(false);
      try {
        await addWorkshopToTeam(selectedTeam.id, apiBody);
        const teamDetails = await getTeamById(selectedTeam.id);
        const workshops = await getWorkshopsByTeam(selectedTeam.id);
        setSelectedTeam(teamDetails);
        setWorkshopDetails(workshops);
        setIsSaved(true);

        // const initialAttendance: Record<number, string> = {};
        // teamDetails.children.forEach((child) => {
        //   initialAttendance[child.id] = null; // or another default value
        // });
        // setAttendance(initialAttendance);
      } catch (error) {
      } finally {
        setIsSavingAttendance(false);
      }
    }
  };

  useEffect(() => {
    if (selectedTeam) {
      // Initialize attendance for the new team
      const initialAttendance: Record<number, string> = {};
      selectedTeam.children.forEach((child) => {
        initialAttendance[child.id] = "";
      });
      setAttendance(initialAttendance);
    }
  }, [selectedTeam]);

  const workshops = [
    "Workshop 1",
    "Workshop 2",
    "Workshop 3",
    "Workshop 4",
    "Workshop 5",
    "Workshop 6",
    "Workshop 7",
    "Workshop 8",
    "Workshop 9",
    "Workshop 10",
    "Workshop 11",
    "Workshop 12",
  ];

  const currentWorkshop = selectedTeam?.program.progress.current ?? 0;

  return (
    <Layout>
      {isLoading && <Loader loadingText="Loading teams" />}
      <>
        <SelectInput
          className="mb-5"
          label="Select team"
          value={selectedTeam?.id || ""}
          onChange={handleTeamChange}
        >
          <option value="">Select a team</option>
          {teams.map((team) => (
            <option key={team.id} value={team.id}>
              {team.name}
            </option>
          ))}
        </SelectInput>
        {isLoadingTeam ? (
          <div className=" w-full mx-auto ">
               {Array.from({ length: 12 }, (_, i) => (
        <SkeletonLoader
          key={i}
          type="stepper"
          index={i}
          totalItems={12} 
        />
      ))}
          </div>
        ) : (
          selectedTeam && (
            <VerticalStepper
              workshops={workshops}
              currentWorkshop={currentWorkshop}
              childs={selectedTeam.children}
              onAttendanceChange={handleAttendanceChange}
              onSaveAttendance={handleSaveAttendance}
              teamDetails={selectedTeam}
              workshopDetails={workshopDetails}
              isSavingAttendance={isSavingAttendance}
              isSaved={isSaved}
            />
          )
        )}
      </>
    </Layout>
  );
};

export default AttendancePage;
