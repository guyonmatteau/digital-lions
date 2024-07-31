import React, { useState, useEffect } from "react";
import { Child } from "@/types/child.interface";
import { Workshop } from "@/types/workshop.interface";
import CustomButton from "@/components/CustomButton";

interface VerticalStepperProps {
  workshops: string[];
  current: number;
  children: Child[];
  onAttendanceChange: (childId: number, status: string) => void;
  onFetchWorkshops: (workshopId: number) => void;
  onSaveAttendance: () => void;
  selectedTeamWithAttendance: Workshop[];
}

const VerticalStepper: React.FC<VerticalStepperProps> = ({
  workshops,
  current,
  children,
  onAttendanceChange,
  onFetchWorkshops,
  onSaveAttendance,
  selectedTeamWithAttendance,
}) => {
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  // Set the default open index
  useEffect(() => {
    setOpenIndex(current);
  }, [current]);

  // Get the workshop data for the current step
  const getWorkshopDataForCurrent = () => {
    return selectedTeamWithAttendance.find(
      (workshop) => workshop.workshop_number === current + 1
    );
  };

  const workshopData = getWorkshopDataForCurrent();
  const attendanceData = workshopData ? workshopData.attendance : [];

  const handleAccordionToggle = (index: number) => {
    setOpenIndex(openIndex === index ? null : index);
    if (openIndex !== index) {
      onFetchWorkshops(index + 1); // Assuming workshop IDs are 1-based and match the index
    }
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
              className={`bg-card flex items-center justify-between w-full p-5 font-medium text-white dark:text-gray-400 hover:bg-card-dark dark:hover:bg-gray-800 transition-colors cursor-pointer ${
                isOpen ? "rounded-t-lg" : "rounded-lg"
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
            </div>
            {isCurrent && isOpen && (
              <div
                className={`p-4 rounded-b-lg ${
                  isOpen ? "rounded-none" : "rounded-lg"
                } bg-card transition-all duration-300 ease-in-out ${
                  isOpen ? "max-h-screen" : "max-h-0 overflow-hidden"
                }`}
              >
                {children.length === 0 ? (
                  <h3 className="text-lg font-semibold">
                    No children in current team
                  </h3>
                ) : (
                  children.map((child) => {
                    // Find the attendance status for the current child
                    const childAttendance = attendanceData.find(
                      (attendance) => attendance.child_id === child.id
                    );
                    const attendanceStatus = childAttendance
                      ? childAttendance.attendance
                      : "absent"; // Default to "absent" if no data is found

                    return (
                      <div
                        key={child.id}
                        className="flex flex-col sm:flex-row items-center my-2"
                      >
                        <span className="flex-1 min-w-0 mb-2 sm:mb-0 sm:mr-4">
                          {child.first_name} {child.last_name}
                        </span>
                        <div className="flex space-x-4">
                          {["present", "absent", "cancelled"].map((status) => (
                            <label
                              key={status}
                              className="flex items-center cursor-pointer"
                            >
                              <input
                                type="radio"
                                name={`attendance-${child.id}`}
                                value={status}
                                checked={attendanceStatus === status}
                                onChange={() =>
                                  onAttendanceChange(child.id, status)
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
                {children.length > 0 && (
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
