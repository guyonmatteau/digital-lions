// src/components/AttendancePage.tsx
import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import VerticalStepper from '@/components/VerticalStepper';
import SelectInput from '@/components/SelectInput';
import getTeams from '@/api/services/teams/getTeams';
import getTeamById from '@/api/services/teams/getTeamById';
import AddWorkshopToTeam from '@/api/services/workshops/AddWorkshopToTeam';
import getWorkshopsByTeam from '@/api/services/workshops/getWorkshopsByTeam';
import Layout from '@/components/Layout';
import { Team } from '@/types/team.interface';
import { TeamWithChildren } from '@/types/teamWithChildren.interface';

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
  const { teamId } = useParams<{ teamId: string }>();
  const [selectedTeam, setSelectedTeam] = useState<TeamWithChildren | null>(null);
  const [isLoadingTeam, setIsLoadingTeam] = useState(false);
  const [attendance, setAttendance] = useState<Record<number, string>>({});
  const [isLoading, setIsLoading] = useState(false);
  const [teams, setTeams] = useState<Team[]>([]);
  const navigate = useNavigate();
  const [selectedTeamWithAttendance, setSelectedTeamWithAttendance] = useState<any[]>([]);

  useEffect(() => {
    const fetchTeams = async () => {
      setIsLoading(true);
      try {
        const fetchedTeams = await getTeams();
        console.log('fetchedTeams:', fetchedTeams);
        setTeams(fetchedTeams);
      } catch (error) {
        console.error('Failed to fetch teams:', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchTeams();
  }, []);

  const handleTeamChange = async (value: string | number) => {
    const selectedId = typeof value === 'string' ? parseInt(value, 10) : value;
    const selected = teams.find((team) => team.id === selectedId);

    if (selected) {
      setIsLoadingTeam(true);
      try {
        const teamDetails = await getTeamById(selected.id);
        setSelectedTeam(teamDetails);
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
        date: new Date().toISOString(),
        workshop_number: selectedTeam.progress.workshop + 1, // Assuming this is the next workshop
        attendance: Object.entries(attendance).map(([childId, status]) => ({
          child_id: parseInt(childId, 10),
          attendance: status,
        })),
      };

      try {
        await AddWorkshopToTeam(selectedTeam.id, apiBody);
        alert('Attendance saved successfully!');
      } catch (error) {
        console.error('Failed to save attendance:', error);
      }
    }
  };

  const handleFetchWorkshops = async () => {
    try {
      const teamsDetailsWithAttendance = await getWorkshopsByTeam(selectedTeam?.id ?? 0);
      setSelectedTeamWithAttendance(teamsDetailsWithAttendance);
    } catch (error) {
      console.error("Failed to fetch workshop data:", error);
      return [];
    }
  };

  const workshops = [
    'Workshop 1',
    'Workshop 2',
    'Workshop 3',
    'Workshop 4',
    'Workshop 5',
    'Workshop 6',
    'Workshop 7',
    'Workshop 8',
    'Workshop 9',
    'Workshop 10',
    'Workshop 11',
    'Workshop 12',
  ];

  const currentWorkshopIndex = selectedTeam?.progress.workshop ?? 0;

  return (
    <Layout>
      <>
        <SelectInput
          className='mb-5'
          label={'Select team'}
          value={selectedTeam?.id || ''}
          onChange={handleTeamChange}
        >
          <option value=''>Select a team</option>
          {teams.map((team) => (
            <option key={team.id} value={team.id}>
              {team.name}
            </option>
          ))}
        </SelectInput>

        {selectedTeam && (
            <VerticalStepper
              workshops={workshops}
              current={currentWorkshopIndex}
              onAttendanceChange={handleAttendanceChange}
              onFetchWorkshops={handleFetchWorkshops}
              onSaveAttendance={handleSaveAttendance}
              selectedTeamWithAttendance={selectedTeamWithAttendance}
            >
              {selectedTeam.children}
            </VerticalStepper>
        )}
      </>
    </Layout>
  );
};

export default AttendancePage;
