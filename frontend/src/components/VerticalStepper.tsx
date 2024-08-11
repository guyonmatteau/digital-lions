import React, { useEffect, useState } from 'react';
import CustomButton from '@/components/CustomButton';
// import Badge from '@/components/Badge';
import { TeamWithChildren } from '@/types/teamWithChildren.interface';
import { WorkshopInfo } from '@/types/workshopInfo.interface';
import { AttendanceRecord } from '@/types/workshopAttendance.interface';
import { AttendanceStatus } from '@/types/attendanceStatus.enum';

interface VerticalStepperProps {
  workshops: string[];
  currentWorkshop: number;
  onAttendanceChange: (childId: number, status: AttendanceStatus) => void;
  onSaveAttendance: () => void;
  teamDetails: TeamWithChildren;
  workshopDetails: WorkshopInfo[];
  childs: any;
  animationDuration?: number;
  isSavingAttendance: boolean;

}

const VerticalStepper: React.FC<VerticalStepperProps> = ({
  workshops,
  currentWorkshop,
  onAttendanceChange,
  onSaveAttendance,
  workshopDetails,
  childs,
  animationDuration = 1,
  isSavingAttendance
}) => {
  const [checked, setChecked] = useState(0);
  const [openIndex, setOpenIndex] = useState<number | null>(null);
  const [attendanceData, setAttendanceData] = useState<AttendanceRecord[]>([]);
  
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
      if (!updatedAttendanceData.some((entry) => entry.child_id === childId)) {
        updatedAttendanceData.push({
          child_id: childId,
          attendance: newAttendance,
        });
      }
      return updatedAttendanceData;
    });
    onAttendanceChange(childId, newAttendance);
  };

  const handleAccordionToggle = (index: number) => {
    setOpenIndex(openIndex === index ? null : index);
  };
  const itemAnimationDuration = animationDuration / workshops.length;

  useEffect(() => {
    const createAnimation = () => {
      setChecked(0);
      for (let i = 0; i < currentWorkshop; i++) {
        setTimeout(() => {
          setChecked((prev) => Math.min(prev + 1, currentWorkshop)); 
        }, itemAnimationDuration * (i + 1) * 1200);
      }
    };

    createAnimation();
  }, [currentWorkshop, itemAnimationDuration]);


  useEffect(() => {
    if (checked === currentWorkshop) {
      setOpenIndex(currentWorkshop);
    }
  }, [checked, currentWorkshop]);

  return (
    <div className="w-full mx-auto">
      {workshops.map((workshop, index) => {
        const isCurrent = index === currentWorkshop;
        const isPrevious = index < currentWorkshop;
        const isNext = index > currentWorkshop;
        const isOpen = index === openIndex && isCurrent;

        let stepClass =
          "relative pl-4 pb-2";
        if (isCurrent) {
          stepClass += " border-blue-500 cursor-pointer";
        } else if (isPrevious) {
          stepClass += " border-green-500";
        } else {
          stepClass += " border-gray-300";
        }

        return (
          <div key={index} className={stepClass} >
            <div
              onClick={
                isCurrent ? () => handleAccordionToggle(index) : undefined
              }
              className={`bg-card flex items-center justify-between w-full p-5 font-medium text-white dark:bg-gray-900 transition-colors ${
                isCurrent ? "rounded-t-lg rounded-b-none" : "rounded-lg"
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
              {index < workshops.length - 1 && (
                <span
                className={`absolute left-[-1px] top-[2.6rem] bottom-[-25px] w-[2px] ${
                  index < checked
                    ? "bg-green-500"
                    : index === checked
                    ? "bg-blue-500"
                    : "bg-gray-300"
                } `}
                // style={{ height: lineHeight }}
                />
              )}

              <div className={`${isCurrent ? "font-bold" : ""}`}>
                {workshop}
              </div>
              {/* <div
                className={`flex items-center space-x-2 ${
                  isCurrent ? "font-bold" : ""
                }`}
              >
                {isPrevious && workshopDetails[index]?.attendance && (
                  <div className="flex flex-col sm:flex-row gap-2">
                    <Badge variant="success">
                      Present: {workshopDetails[index].attendance.present || 0}
                    </Badge>
                    <Badge variant="warning">
                      Absent: {workshopDetails[index].attendance.absent || 0}
                    </Badge>
                    <Badge variant="danger">
                      Cancelled: {workshopDetails[index].attendance.cancelled || 0}
                    </Badge>
                  </div>
                )}
              </div> */}
            </div>
            <div
              className={`card-content ${isOpen && isCurrent ? 'open' : 'closed'}`}
            >
              {isOpen && isCurrent && (
                <div className="p-4 rounded-b-lg bg-card transition-all duration-300 ease-in-out dark:bg-gray-900 dark:text-white">
                  {childs.length === 0 ? (
                    <h3 className="text-lg font-semibold">
                      No children in current workshop
                    </h3>
                  ) : (
                    childs.map((entry: any) => {
                      const { id, first_name, last_name } = entry;
                      const attendanceEntry = attendanceData.find(
                        (e) => e.child_id === id
                      );
                      const currentAttendance = attendanceEntry
                        ? attendanceEntry.attendance
                        : null;
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
                                  checked={currentAttendance === status && currentAttendance !== '' && currentAttendance !== null}
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
                  {(
                    <div className="flex items-center justify-end border-t mt-4 border-gray-200 rounded-b dark:border-gray-600">
                      <CustomButton
                        className="mt-4"
                        label="Save Attendance"
                        variant="secondary"
                        onClick={onSaveAttendance}
                        isBusy={isSavingAttendance}
                      />
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default VerticalStepper;
