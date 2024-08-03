import { Community } from "./community.interface";

interface Child {
  id: number;
  first_name: string;
  last_name: string;
}

interface Progress {
  current: number;
  total: number;
}

interface Program {
  id: number;
  name: string;
  progress: Progress;
}

export interface TeamWithChildren {
  is_active: boolean;
  last_updated_at: string;
  created_at: string;
  id: number;
  name: string;
  community: Community;
  children: Child[];
  program: Program;
}