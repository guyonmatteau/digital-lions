import React, { useState, useEffect } from "react";
import VerticalStepper from "@/components/VerticalStepper";
import getTeamById from "@/api/services/teams/getTeamById";
import addWorkshopToTeam from "@/api/services/workshops/addWorkshopToTeam";
import getWorkshopsByTeam from "@/api/services/workshops/getWorkshopsByTeam";
import Layout from "@/components/Layout";
import { TeamWithChildren } from "@/types/teamWithChildren.interface";
import { WorkshopInfo } from "@/types/workshopInfo.interface";
import SkeletonLoader from "@/components/SkeletonLoader";

import { useRouter } from "next/router";

interface AttendanceRecord {
  attendance: string;
  child_id: number;
}

interface Attendance {
  date: string;
  workshop_number: number;
  attendance: AttendanceRecord[];
}

const ProgramTrackerAttendancePage: React.FC = () => {
  const router = useRouter();
  const { communityId, teamId } = router.query;
  const [selectedTeam, setSelectedTeam] = useState<TeamWithChildren | null>(
    null
  );
  const [workshopDetails, setWorkshopDetails] = useState<WorkshopInfo[]>([]);
  const [attendance, setAttendance] = useState<Record<number, string>>({});
  const [communityName, setCommunityName] = useState<string | null>(null);
  const [teamName, setTeamName] = useState<string | null>(null);
  const [isLoadingTeam, setIsLoadingTeam] = useState(false);
  const [isSavingAttendance, setIsSavingAttendance] = useState(false);
  const [isSaved, setIsSaved] = useState(false);

  const breadcrumbs = [
    { label: "Program tracker", path: "/program-tracker" },
    {
      label: `${communityName}`,
      path: `/program-tracker/${communityId}/teams`,
    },
    {
      label: `${teamName || "Unknown Team"}`,
      path: `/program-tracker/${communityId}/teams/${teamId}`,
    },
  ];

  // Fetch team details when teamId changes
  useEffect(() => {
    if (teamId) {
      const fetchTeamById = async () => {
        setIsLoadingTeam(true);
        try {
          const numericTeamId = Number(teamId);
          if (isNaN(numericTeamId)) {
            throw new Error("Invalid team ID");
          }
          const teamDetails = await getTeamById(numericTeamId);
          setSelectedTeam(teamDetails); // Set the fetched team as selectedTeam
          setTeamName(teamDetails.name);
        } catch (error) {
          console.error("Failed to fetch team details:", error);
        } finally {
          setIsLoadingTeam(false);
        }
      };

      fetchTeamById();
    }
  }, [teamId]);

  useEffect(() => {
    // Retrieve and parse state from localStorage
    const storedState = localStorage.getItem("linkCardState");
    if (storedState) {
      const { communityName, teamName } = JSON.parse(storedState);
      setCommunityName(communityName);
      setTeamName(teamName);
    }
  }, []);

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
        console.log(error);
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
    <Layout breadcrumbs={breadcrumbs}>
      <>
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

export default ProgramTrackerAttendancePage;
