export interface Attendance {
    child_id: number;
    first_name?: string;
    last_name?: string;
    attendance: "present" | "absent" | "cancelled";
  }
