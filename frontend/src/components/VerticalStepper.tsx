import React, { useState } from 'react';
import { Child } from '@/types/child.interface';
import { Workshop } from '@/types/workshop.interface';

interface VerticalStepperProps {
  workshops: string[];
  current: number;
  children: Child[];
  onAttendanceChange: (childId: number, status: string) => void;
  onFetchWorkshops: (workshopId: number) => Promise<Workshop[]>;
}

const VerticalStepper: React.FC<VerticalStepperProps> = ({
  workshops,
  current,
  children,
  onAttendanceChange,
  onFetchWorkshops
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [workshopData, setWorkshopData] = useState<any[]>([]);

  const handleAccordionToggle = async () => {
    setIsOpen(!isOpen);

    if (!isOpen) {
      // Fetch workshop data when opening the accordion
      const workshopId = current + 1; // Assuming workshop IDs are 1-based and match the index
      try {
        const data = await onFetchWorkshops(workshopId);
        setWorkshopData(data);
      } catch (error) {
        console.error("Failed to fetch workshop data:", error);
      }
    }
  };

  return (
    <div className="w-full mx-auto">
      {workshops.map((workshop, index) => {
        const isCurrent = index === current;
        const isPrevious = index < current;
        const isNext = index > current;

        let stepClass = 'relative p-4 border-l-2 transition-colors duration-300 ease-in-out';
        if (isCurrent) {
          stepClass += ' border-blue-500 cursor-pointer';
        } else if (isPrevious) {
          stepClass += ' border-green-500';
        } else if (isNext) {
          stepClass += ' border-gray-300';
        }

        return (
          <div key={index} className={stepClass}>
            <div
              onClick={isCurrent ? handleAccordionToggle : undefined}
              className={`flex items-center cursor-pointer bg-card pb-2 pt-2 ${isOpen ? "rounded-t-lg " : "rounded-lg"}`}

            >
              <span
                className={`absolute -left-2.5 w-5 h-5 rounded-full flex items-center justify-center bg-white border-2 transition-colors duration-300 ease-in-out ${
                  isCurrent ? 'bg-blue-500 border-blue-500' : isPrevious ? 'bg-green-500 border-green-500' : 'bg-gray-300 border-gray-300'
                }`}
              >
                {isCurrent ? (
                  <span className="w-3 h-3 bg-white rounded-full"></span>
                ) : isPrevious ? (
                  <span className="w-3 h-3 bg-white rounded-full"></span>
                ) : (
                  <span className="w-3 h-3 bg-white rounded-full"></span>
                )}
              </span>
              <div className={`ml-8 ${isCurrent ? 'font-bold' : ''}`}>{workshop}</div>
            </div>
            {isCurrent && isOpen && (
              <div className={`p-4 rounded-b-lg ${isOpen ? "rounded-none" : "rounded-lg"} bg-card  transition-all duration-300 ease-in-out ${isOpen ? 'max-h-screen' : 'max-h-0 overflow-hidden'}`}>
                <h3 className="text-lg font-semibold">Attendance</h3>
                {children.map((child) => (
                  <div key={child.id} className="flex items-center my-2">
                    <span className="flex-1 min-w-0 mr-4">
                      {child.first_name} {child.last_name}
                    </span>
                    <div className="flex space-x-4">
                      <label className="flex items-center">
                        <input
                          type="radio"
                          name={`attendance-${child.id}`}
                          value="present"
                          checked={workshopData.find(att => att.child_id === child.id)?.attendance === 'present'}
                          onChange={() => onAttendanceChange(child.id, 'present')}
                        />
                        <span className="ml-2">Present</span>
                      </label>
                      <label className="flex items-center">
                        <input
                          type="radio"
                          name={`attendance-${child.id}`}
                          value="absent"
                          checked={workshopData.find(att => att.child_id === child.id)?.attendance === 'absent'}
                          onChange={() => onAttendanceChange(child.id, 'absent')}
                        />
                        <span className="ml-2">Absent</span>
                      </label>
                      <label className="flex items-center">
                        <input
                          type="radio"
                          name={`attendance-${child.id}`}
                          value="cancelled"
                          checked={workshopData.find(att => att.child_id === child.id)?.attendance === 'cancelled'}
                          onChange={() => onAttendanceChange(child.id, 'cancelled')}
                        />
                        <span className="ml-2">Cancelled</span>
                      </label>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
};

export default VerticalStepper;
