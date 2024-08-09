import React, { useState, useEffect } from "react";
import CustomButton from "@/components/CustomButton";
import { TeamWithChildren } from "@/types/teamWithChildren.interface";
import { WorkshopInfo } from "@/types/workshopInfo.interface";
import { AttendanceRecord } from "@/types/workshopAttendance.interface";
import { AttendanceStatus } from "@/types/attendanceStatus.enum";
import Badge from "@/components/Badge";

interface VerticalStepperProps {
  workshops: string[];
  current: number;
  onAttendanceChange: (childId: number, status: AttendanceStatus) => void;
  onFetchWorkshops: () => void;
  onSaveAttendance: () => void;
  selectedTeamWithAttendance: AttendanceRecord[];
  teamDetails: TeamWithChildren;
  workshopDetails: WorkshopInfo[];
  childs: any;
}

const VerticalStepper: React.FC<VerticalStepperProps> = ({
  workshops,
  current,
  onAttendanceChange,
  onFetchWorkshops,
  onSaveAttendance,
  selectedTeamWithAttendance,
  teamDetails,
  workshopDetails,
  childs,
}) => {
  const [openIndex, setOpenIndex] = useState<number | null>(null);
  const [attendanceData, setAttendanceData] = useState<AttendanceRecord[]>([]);

  console.log(workshopDetails);

  useEffect(() => {
    // Initialize attendanceData with default attendance if not already present
    const initializedAttendanceData = childs.map((child: any) => {
      const existingRecord = selectedTeamWithAttendance.find(
        (record) => record.child_id === child.id
      );
      return existingRecord || { child_id: child.id, attendance: "" }; // Default to empty string
    });
    setAttendanceData(initializedAttendanceData);
  }, [selectedTeamWithAttendance, childs]);

  const handleAttendanceChange = (
    childId: number,
    newAttendance: AttendanceStatus
  ) => {
    setAttendanceData((prevData) => {
      const updatedAttendanceData = prevData.map((entry) =>
        entry.child_id === childId
          ? { ...entry, attendance: newAttendance }
          : entry
      );
      console.log("updatedAttendanceData", updatedAttendanceData);
      // Add a new entry if not present
      if (!updatedAttendanceData.some((entry) => entry.child_id === childId)) {
        updatedAttendanceData.push({
          child_id: childId,
          attendance: newAttendance,
        });
      }
      return updatedAttendanceData;
    });
    console.log("attendanceData", attendanceData);
    onAttendanceChange(childId, newAttendance);
  };

  const handleAccordionToggle = (index: number) => {
    setOpenIndex(openIndex === index ? null : index);
    if (openIndex !== index) {
      onFetchWorkshops();
    }
  };

  const currentWorkshopAttendance = workshopDetails[current]?.attendance || {
    present: 0,
    total: 0,
  };

  return (
    <div className="w-full mx-auto">
      {workshops.map((workshop, index) => {
        const isCurrent = index === current;
        const isPrevious = index < current;
        const isNext = index > current;
        const isOpen = openIndex === index;

        let stepClass =
          "relative pl-4 pb-2 border-l-2 transition-colors duration-300 ease-in-out";
        if (isCurrent) {
          stepClass += " border-blue-500 cursor-pointer";
        } else if (isPrevious) {
          stepClass += " border-green-500";
        } else if (isNext) {
          stepClass += " border-gray-300";
        }

        return (
          <div key={index} className={stepClass}>
            <div
              onClick={
                isCurrent ? () => handleAccordionToggle(index) : undefined
              }
              className={`bg-card flex items-center justify-between w-full p-5 font-medium text-white  dark:bg-gray-900  transition-colors ${
                isOpen ? "rounded-t-lg" : "rounded-lg" 
              } ${
                isCurrent && "cursor-pointer hover:bg-card-dark dark:hover:bg-gray-800"
              }`}
            >
              <span
                className={`absolute -left-2.5 w-5 h-5 rounded-full flex items-center justify-center bg-white border-2 transition-colors duration-300 ease-in-out ${
                  isCurrent
                    ? "bg-blue-500 border-blue-500"
                    : isPrevious
                    ? "bg-green-500 border-green-500"
                    : "bg-gray-300 border-gray-300"
                }`}
              >
                <span className="w-3 h-3 bg-white rounded-full"></span>
              </span>
              <div className={`${isCurrent ? "font-bold" : ""}`}>
                {workshop}
              </div>
              <div
                className={`flex items-center space-x-2 ${
                  isCurrent ? "font-bold" : ""
                }`}
              >
                { isPrevious && workshopDetails[index]?.attendance && (
                  <div className="flex flex-col sm:flex-row gap-2">
                    <Badge variant="success">
                      Present: {workshopDetails[index].attendance.present || 0}
                    </Badge>
                    <Badge variant="warning">
                      Absent: {workshopDetails[index].attendance.absent || 0}
                    </Badge>
                    <Badge variant="danger">
                      Cancelled:{" "}
                      {workshopDetails[index].attendance.cancelled || 0}
                    </Badge>
                  </div>
                )}
              </div>

              {isCurrent && (
                <svg
                  data-accordion-icon
                  className={`w-3 h-3 ${
                    !isOpen ? "rotate-180" : ""
                  } transition-transform`}
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 10 6"
                >
                  <path
                    stroke="currentColor"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M9 5 5 1 1 5"
                  />
                </svg>
              )}
            </div>
            {isCurrent && isOpen && (
              <div
                className={`p-4 rounded-b-lg ${
                  isOpen ? "rounded-none" : "rounded-lg"
                } bg-card transition-all duration-300 ease-in-out dark:bg-gray-900 dark:text-white ${
                  isOpen ? "max-h-screen" : "max-h-0 overflow-hidden"
                }`}
              >
                {childs.length === 0 ? (
                  <h3 className="text-lg font-semibold">
                    No children in current workshop
                  </h3>
                ) : (
                  childs.map((entry: any) => {
                    const { id, first_name, last_name } = entry;
                    // Find the attendance status for the current child
                    const attendanceEntry = attendanceData.find(
                      (e) => e.child_id === id
                    );
                    const currentAttendance = attendanceEntry
                      ? attendanceEntry.attendance
                      : "";

                    return (
                      <div key={id} className="flex flex-col sm:flex-row my-2">
                        <span className="flex-1 min-w-0 mb-2 sm:mb-0 sm:mr-4">
                          {first_name} {last_name}
                        </span>
                        <div className="flex space-x-4">
                          {["present", "absent", "cancelled"].map((status) => (
                            <label
                              key={status}
                              className="flex items-center cursor-pointer"
                            >
                              <input
                                type="radio"
                                name={`attendance-${id}`}
                                value={status}
                                checked={currentAttendance === status}
                                onChange={() =>
                                  handleAttendanceChange(
                                    id,
                                    status as AttendanceStatus
                                  )
                                }
                              />
                              <span className="ml-2 capitalize">{status}</span>
                            </label>
                          ))}
                        </div>
                      </div>
                    );
                  })
                )}
                {attendanceData.length > 0 && (
                  <div className="flex items-center justify-end border-t mt-4 border-gray-200 rounded-b dark:border-gray-600">
                    <CustomButton
                      className="mt-4"
                      label="Save Attendance"
                      variant="secondary"
                      onClick={onSaveAttendance}
                    />
                  </div>
                )}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
};

export default VerticalStepper;
